# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAdm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QVBoxLayout, qApp
import pymssql

try:
    db = QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName("Driver={Sql Server};Server=localhost;Database=School;Uid=sa;Pwd=sa")
    db.open()
except Exception as e:
    print(e)

#判断数据库是否打开
if db.open():
   print('Opening Successfully')
else:
    print('Did not open')



class Ui_MainAdmWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(160, 10, 661, 561))
        self.tableView.setObjectName("tableView")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 360, 111, 151))
        self.groupBox.setObjectName("groupBox")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.buttonShow = QtWidgets.QPushButton(self.groupBox)
        self.buttonShow.setObjectName("buttonShow")
        self.buttonShow.clicked.connect(self.view_data)
        self.verticalLayout.addWidget(self.buttonShow)

        self.buttonAddOne = QtWidgets.QPushButton(self.groupBox)
        self.buttonAddOne.setObjectName("buttonAddOne")
        self.buttonAddOne.clicked.connect(self.add_row_data)
        self.verticalLayout.addWidget(self.buttonAddOne)

        self.buttonDelOne = QtWidgets.QPushButton(self.groupBox)
        self.buttonDelOne.setObjectName("buttonDelOne")
        self.buttonDelOne.clicked.connect(self.del_row_data)
        self.verticalLayout.addWidget(self.buttonDelOne)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 131, 22))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.comboBoxTables = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxTables.setObjectName("comboBoxTables")
        self.comboBoxTables.addItem("请选择")
        self.comboBoxTables.addItem("Courses")
        self.comboBoxTables.addItem("Choices")
        self.comboBoxTables.addItem("Students")
        self.comboBoxTables.addItem("Teachers")
        self.comboBoxTables.addItem("Admin")
        self.comboBoxTables.currentIndexChanged.connect(self.TableSelectionChange)


        self.horizontalLayout.addWidget(self.comboBoxTables)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.closeEvent)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.toAbout)

        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        global count2
        count2 = '请选择'

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "教务选课系统-管理员界面"))

        self.groupBox.setTitle(_translate("MainWindow", "操作"))
        self.buttonShow.setText(_translate("MainWindow", "显示"))
        self.buttonAddOne.setText(_translate("MainWindow", "添加一行"))
        self.buttonDelOne.setText(_translate("MainWindow", "删除一行"))

        self.label.setText(_translate("MainWindow", "表"))

        self.menuFile.setTitle(_translate("MainWindow", "操作"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))

    #选择指定表
    def TableSelectionChange(self):
        global count2
        count2 = self.comboBoxTables.currentText()


    #显示指定表
    def view_data(self):
        global count2
        #print('||'+count2)

        query = QSqlQuery()
        query.exec("Select name From syscolumns where id=Object_Id('"+count2+"')")
        i = 0
        tlname = []
        while query.next():
            #获取名称字段的值
            name = query.value("name")
            #表属性加入列表
            tlname.append(name)
            #print(tlname[i])
            i += 1

        #实例化一个可编辑数据模型
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)
        #设置数据模型的数据表
        print('已选:'+count2+'表')
        if count2 == '请选择':
            QMessageBox.warning(self, '警告', "请选择表")
        else:
            self.model.setTable(count2)
        #允许字段更改
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        #查询所有数据
        self.model.select()

    # 添加一行数据行
    def add_row_data(self):
        # 如果存在实例化的数据模型对象
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.create_db()

    # 删除一行数据
    def del_row_data(self):
        if self.model:
            self.model.removeRow(self.tableView.currentIndex().row())
        else:
            self.create_db()

    #关于窗口
    def toAbout(self):
        QMessageBox.about(self,"关于","嘻嘻")

    #退出警告
    def closeEvent(self, QCloseevent):
        reply = QMessageBox.question(self, '警告', "确认退出?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print('退出')
            sys.exit(app.exec_())
        else:
            print('取消退出')
            QCloseevent.ignore()


    def __init__(self):
        super(Ui_MainAdmWindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui_MainAdmWindow()
    main.show()
    sys.exit(app.exec_())


query = QSqlQuery()
query.exec("Select cname From courses,choices where courses.cid=choices.cid and day='1' and sect='1'")