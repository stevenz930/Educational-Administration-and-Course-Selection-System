import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_UILogin(QMainWindow):
    def setupUi(self, UILogin):
        print('1')


    def __init__(self):
        super(Ui_UILogin,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_UILogin()
    main.show()
    sys.exit(app.exec_())