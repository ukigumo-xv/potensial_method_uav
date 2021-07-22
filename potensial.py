# 
import sys
from PyQt5 import QtWidgets as qt

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

if __name__ == '__main__':
    main()
