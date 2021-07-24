# 
#
# [reference]
# - https://neko-py.com/python-configparser
# - http://www.yamamo10.jp/yamamoto/comp/Python/library/configparser/index.php#APPLI:NUM
#
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import configparser

def show_message():
    messagebox = qt.QMessageBox(qt.QMessageBox.Information,
                                        'Title - Hello',
                                        'Hello, Qt for Python!',
                                        qt.QMessageBox.Close
                                        )
    messagebox.exec_()

def main():
    # アプリケーション作成、Qt初期化のために最初にインスタンス化する
    app = qt.QApplication(sys.argv)

    # ボタン作成
    button = qt.QPushButton('click me!')
    button.resize(100, 40)
    button.show()

    # ボタンクリック時のシグナルに、メッセージ表示のスロット(関数)を結びつける
    button.clicked.connect(show_message)

    # アプリケーションを起動する
    sys.exit(app.exec_())

class MainWindow(QWidget):
    def __init__(self, map, parent=None):
        super(MainWindow, self).__init__(parent) # 初期化
        self.x = map['x']
        self.y = map['y']
        self.mesh = map['mesh']
        print('self.x = ', self.x*10)
        self.initUI() # UIの初期化

    @property
    def MAPW(self):
        return self.x*self.mesh

    @property
    def MAPH(self):
        return self.y*self.mesh


    def initUI(self): # UIの初期化をするメソッド
        # self.resize(400, 300) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.resize(self.MAPW, self.MAPH) # ウィンドウの大きさの設定(横幅, 縦幅)
        self.move(400, 300) # ウィンドウを表示する場所の設定(横, 縦)
        self.setWindowTitle('PyQt5 sample GUI') # ウィンドウのタイトルの設定
        #self.setWindowIcon(QIcon('xxxx.jpg')) # ウィンドウ右上のアイコンの設定
        btn = QPushButton('Hello World PyQt5', self) # ボタンウィジェット作成
        btn.resize(btn.sizeHint()) # ボタンのサイズの自動設定
        btn.move(100, 50) # ボタンの位置設定(ボタンの左上の座標)

if __name__ == '__main__':
    # read config file
    print('Read config file...')
    config = configparser.RawConfigParser()
    config.read('config.ini')
    
    # map config
    map = {}
    map['x'] = config.getint('mapconfig', 'MAPX')   # width
    map['y'] = config.getint('mapconfig', 'MAPY')   # height
    map['mesh'] = config.getint('mapconfig', 'MAPMESH')
    print('[MAPCONFIG]')
    print(map)

    # UAV ocnfig
    uav = {}
    uav['N']        = config.get('uavconfig', 'uavN')
    uav['iniPos']   = config.get('uavconfig', 'uavIniPos')
    print('[UAV config]')
    print(uav)

    app = QApplication(sys.argv) #PyQtで必ず呼び出す必要のあるオブジェクト
    main_window = MainWindow(map) #ウィンドウクラスのオブジェクト生成
    main_window.show() #ウィンドウの表示
    sys.exit(app.exec_()) #プログラム終了

    # main()
