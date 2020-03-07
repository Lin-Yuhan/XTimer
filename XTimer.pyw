import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from pygame import mixer
from PyQt5.QtCore import QTimer, QTimerEvent, Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QFormLayout, QLineEdit, QMainWindow
from PyQt5.QtGui import QIcon

mixer.init()
mixer.music.load('canon in d.mp3')


class XTimer(QLabel):
    """docstring for XTimer"""
    def __init__(self):
        super().__init__()
        self.sec = 0
        self.timer_open = True
        self.notJustStart = False
        self.qssStyle = '''
        QWidget{
            background-color:white;
        }
        QLabel#time_L{
            font:bold 60px;
            font-family:微软雅黑;
            color:#FFA07A;
        }
        QLabel#tSet_L{
            font-size:12px;
            font-family:微软雅黑;
        }

        QPushButton{
            border-style:none;
            padding:10px;

            background-color:#FFE4B5;
            color:black;
            font-family:微软雅黑;
            font-size:12px;
        }
        QPushButton:hover{
            border-style:none;
            padding:10px;

            background-color:#FF8C69;
            color:black;
            font-family:微软雅黑;
            font-size:12px;
        }
        QPushButton:disabled{
            border-style:none;
            padding:10px;

            background-color:#EEEED1;
            color:black;
            font-family:微软雅黑;
            font-size:12px;
        }

        QLineEdit{
            background-color:#EDEDED;
            color:black;
            border-style:none;
            padding:8px;
            font-family:微软雅黑;
        }
        QLineEdit:focus{
            background-color:#D3D3D3;
            color:;
            border-style:none;
            padding:8px;
            font-family:微软雅黑;
        }
        
        '''
        self.setWindowTitle('XTimer')
        self.resize(220, 250)
        self.setWindowIcon(QIcon('./icon.png'))

        self.tSet_label = QLabel(self)
        self.tSet_label.setText(u'时间(min):')
        self.tSet_label.setObjectName('tSet_L')

        self.t_label = QLabel(self)
        self.t_label.setText('0:0')
        self.t_label.setAlignment(Qt.AlignCenter)
        self.t_label.setObjectName('time_L')

        self.time_id = self.startTimer(1000)
        self.setStyleSheet(self.qssStyle)

        self.stop_button = QPushButton(u'停止')
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.resize(self.stop_button.sizeHint())

        self.start_button = QPushButton(u'开始')
        self.start_button.clicked.connect(self.start_timer)
        self.start_button.resize(self.start_button.sizeHint())
        self.start_button.setEnabled(False)

        self.set_button = QPushButton(u'设置时间')
        self.set_button.clicked.connect(self.set_timer)
        self.set_button.resize(self.set_button.sizeHint())
        self.set_button.setEnabled(False)

        self.time_edit = QLineEdit('')

        self.layout=QFormLayout()
        self.layout.addRow(self.t_label, )
        self.layout.addRow(self.start_button, )
        self.layout.addRow(self.stop_button, )
        self.layout.addRow(self.tSet_label, self.time_edit)
        self.layout.addRow(self.set_button, )
        self.setLayout(self.layout)

    def timerEvent(self, a0:QTimerEvent):
        self.t_label.setText(str(self.sec//60)+':'+str(self.sec%60))
        if self.sec == 0:
            self.stop_timer()
            if self.notJustStart:
                mixer.music.play()
        else:
            self.sec -= 1

    def stop_timer(self):
        self.stop_button.setEnabled(False)
        if self.timer_open:
            self.killTimer(self.time_id)
            self.timer_open = False
            self.start_button.setEnabled(True)
            self.set_button.setEnabled(True)

    def start_timer(self):
        self.stop_button.setEnabled(True)
        self.start_button.setEnabled(False)
        if self.timer_open == False:
            self.timer_open = True
            self.time_id = self.startTimer(1000)

    def set_timer(self):
        if self.time_edit.text() != '':
            try:
                self.sec = 60*int(self.time_edit.text())
            except ValueError:
                self.sec = 0
            self.notJustStart = True
        else:
            self.sec = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xt = XTimer()
    xt.show()
    sys.exit(app.exec_())
