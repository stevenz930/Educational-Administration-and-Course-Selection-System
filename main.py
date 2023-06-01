from PyQt5.QtCore import QCoreApplication

from mainAdm import Ui_MainAdmWindow
from mainStu import Ui_MainStuWindow
from mainTea import *
from login_1 import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class MainTeaWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.UI = Ui_MainTeaWindow()
    self.UI.setupUi(self)

class MainStuWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.UI = Ui_MainStuWindow()
    self.UI.setupUi(self)

class MainAdmWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.UI = Ui_MainAdmWindow()
    self.UI.setupUi(self)

class LoginWindow(QDialog):
  def __init__(self):
    QDialog.__init__(self)
    self.UI=Ui_Dialog()
    self.UI.setupUi(self)


if __name__=='__main__':
  app=QApplication(sys.argv)
  MainTeaWin = MainTeaWindow()
  MainStuWin = MainStuWindow()
  MainAdmWin = MainAdmWindow()
  LoginWin = LoginWindow()

  #self.actionLogin = QtWidgets.QAction(MainWindow)
  #self.actionLogin.setObjectName("actionLogin")
  LoginWin.show()
  #按钮事件
  btnTea=LoginWin.UI.buttonLoginTea
  btnStu=LoginWin.UI.buttonLoginStu
  btnAdm=LoginWin.UI.buttonLoginAdm
  btnTea.clicked.connect(MainTeaWin.show)
  btnStu.clicked.connect(MainStuWin.show)
  btnAdm.clicked.connect(MainAdmWin.show)

  #显示登录窗口

  sys.exit(app.exec_())
