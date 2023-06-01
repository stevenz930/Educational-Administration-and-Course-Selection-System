# -*- coding: utf-8 -*-
# python3.7 + sql server2012 + PyQt5+ eric6
# Form implementation generated from reading ui file 'C:\\Users\Administrator\Desktop\code\final\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTableView, QVBoxLayout, QTableWidgetItem
#import pymssql
import sys



class Ui_Update(object):
    def __init__(self):
        super(Ui_Update, self).__init__()
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        self.Ausername = 'sa'
        self.Apassword = 'sa'
        self.connect_to_sercer()

    def connect_to_sercer(self):
        try:
            db = QSqlDatabase.addDatabase("QODBC")
            db.setDatabaseName("Driver={Sql Server};Server='127.0.0.1';Database=cdb;Uid=self.Ausername;Pwd=self.Apassword")
            db.open()
            #self.conn = pymssql.connect(server='127.0.0.1', user=self.Ausername, password=self.Apassword,database='Personnel')
            #self.cursor = self.conn.cursor()
        except Exception:
            self.label_2.setText("网络错误！")

    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(471, 361)
        Update.setSizeGripEnabled(True)
        self.tableWidget = QtWidgets.QTableWidget(Update)
        self.tableWidget.setGeometry(QtCore.QRect(15, 161, 431, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Update)
        self.pushButton.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Update)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Update)
        self.label.setGeometry(QtCore.QRect(50, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Update)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Update)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Update)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Update)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Update)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Update)
        self.label_4.setGeometry(QtCore.QRect(380, 140, 54, 12))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Update)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Update)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Update)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(Update)
        self.label_6.setGeometry(QtCore.QRect(50, 100, 54, 12))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Update)
        self.pushButton_2.clicked.connect(Update.close)
        self.pushButton.clicked.connect(self.update1)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        _translate = QtCore.QCoreApplication.translate
        Update.setWindowTitle(_translate("Update", "Dialog"))
        self.pushButton.setText(_translate("Update", "Run"))
        self.pushButton_2.setText(_translate("Update", "Return"))
        self.label.setText(_translate("Update", "表名： "))
        self.label_2.setText(_translate("Update", "更新列："))
        self.label_3.setText(_translate("Update", "值："))
        self.label_5.setText(_translate("Update", "值："))
        self.label_6.setText(_translate("Update", "条件："))

    def update1(self):
        self.connect_to_sercer()
        table = self.lineEdit.text()
        title_em = ["EM_Id", "EM_name", "EM_age", "salary", "EntWorkDay", "OutWorkDay", "EM_leader"]
        title_DT_M = ["DEPT_id", "DEPT_name", "M_id", "M_name"]
        title_DT = ["DEPT_id", "DEPT_name", "DEPT_setdate", "DEPT_achi", "DEPT_Surplusfunds", "DEPT_target"]
        string = "update " + table + " set " + self.lineEdit_2.text() + " = " + self.lineEdit_3.text() + " where " + self.lineEdit_5.text() + " = " + self.lineEdit_4.text() + ";"
        print(string)
        self.cursor.execute(string)
        self.cursor.execute("select * from " + table)
        rows = self.cursor.fetchall()
        if (table == "employee"):
            self.tableWidget.setHorizontalHeaderLabels(title_em)
        elif (table == "department"):
            self.tableWidget.setHorizontalHeaderLabels(title_DT)
        elif (table == "manage"):
            self.tableWidget.setHorizontalHeaderLabels(title_DT_M)
        print(rows)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        # self.tableWidget.setHorizontalHeaderLabels(title_em)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                newItem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        self.conn.commit()
        self.conn.close()


class Ui_add(object):
    def __init__(self):
        super(Ui_add, self).__init__()
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        self.Ausername = ''
        self.Apassword = ''

    def connect_to_sercer(self):
        try:
            db = QSqlDatabase.addDatabase("QODBC")
            db.setDatabaseName(
                "Driver={Sql Server};Server='127.0.0.1';Database=cdb;Uid=self.Ausername;Pwd=self.Apassword")
            db.open()
        except Exception:
            self.label_2.setText("网络错误！")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(505, 398)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 101, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 70, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 70, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 160, 121, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 471, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add = QtWidgets.QLineEdit(Dialog)
        self.add.setGeometry(QtCore.QRect(20, 100, 461, 20))
        self.add.setObjectName("add")

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.run)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增或删除雇员"))
        self.pushButton.setText(_translate("Dialog", "Run"))
        self.pushButton_2.setText(_translate("Dialog", "Return"))
        self.radioButton_2.setText(_translate("Dialog", "新增"))
        self.radioButton_3.setText(_translate("Dialog", "删除"))
        self.add.setText(_translate("Dialog", "字符串请加‘’，列之间用逗号分开"))

    def run(self):
        self.connect_to_sercer()

        title_em = ["EM_Id", "EM_name", "EM_age", "salary", "EntWorkDay", "OutWorkDay", "EM_leader"]
        self.string = " "

        if (self.radioButton_2.isChecked and not (self.radioButton_3.isChecked())):
            self.string = self.string + "insert into employee values( " + self.add.text() + " );"
        elif (not (self.radioButton_2.isChecked()) and self.radioButton_3.isChecked()):
            self.string = self.string + "delete from employee where " + self.add.text() + ";"
        # self.cursor.execute("insert into employee values (10,'as',20,10000,'2019-01-01','2020-01-01','sas');")
        print(self.string)
        self.cursor.execute(self.string)
        # print(self.string)
        self.cursor.execute("select * from employee ;")
        rows = self.cursor.fetchall()
        print(rows)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels(title_em)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                newItem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        self.conn.commit()
        self.conn.close()


class Ui_Dialog(object):

    def __init__(self):
        super(Ui_Dialog, self).__init__()
        Dialog = QtWidgets.QDialog()
        self.PassWord = ''
        self.UserName = ''
        self.setupUi(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.logins = QtWidgets.QPushButton(Dialog)
        self.logins.setGeometry(QtCore.QRect(150, 190, 75, 23))
        self.logins.setObjectName("logins")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 230, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 113, 20))
        self.lineEdit.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 150, 181, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("")
        self.retranslateUi(Dialog)
        self.logins.clicked.connect(self.depend)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label_3.objectNameChanged.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.logins.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "退出"))
        self.label.setText(_translate("Dialog", "账号："))
        self.label_2.setText(_translate("Dialog", "密码："))
        # self.label_3.setText(_translate("Dialog", "TextLabel"))

    def depend(self):
        self.UserName = self.lineEdit.text()
        self.PassWord = self.password.text()
        try:
            db = QSqlDatabase.addDatabase("QODBC")
            db.setDatabaseName(
                "Driver={Sql Server};Server='127.0.0.1';Database=cdb;Uid=self.Ausername;Pwd=self.Apassword")
            db.open()
            conn = db.setDatabaseName(
                "Driver={Sql Server};Server='127.0.0.1';Database=cdb;Uid=self.Ausername;Pwd=self.Apassword")
            self.label_3.setText("Login Success!")
            self.label_3.setObjectName("a")
            conn.close
        except Exception:
            self.label_3.setText("账号或密码错误！")


class Ui_search():
    def __init__(self):
        super(Ui_search, self).__init__()
        Dialog = QtWidgets.QDialog()
        self.setupUi(Dialog)
        self.Susername = ''
        self.Spassword = ''

    def connect_to_sercer(self):
        try:
            db = QSqlDatabase.addDatabase("QODBC")
            db.setDatabaseName(
                "Driver={Sql Server};Server='127.0.0.1';Database=cdb;Uid=self.Ausername;Pwd=self.Apassword")
            db.open()
        except Exception:
            self.label_2.setText("网络错误！")

    def setupUi(self, search):
        search.setObjectName("search")
        search.resize(472, 354)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../picture/bitbug_favicon (4).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        search.setWindowIcon(icon)
        search.setSizeGripEnabled(True)
        self.pushButton = QtWidgets.QPushButton(search)
        self.pushButton.setGeometry(QtCore.QRect(360, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(search)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(search)
        self.label.setGeometry(QtCore.QRect(30, 10, 251, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(search)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.EM_Id = QtWidgets.QLineEdit(search)
        self.EM_Id.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.EM_Id.setObjectName("EM_Id")
        self.DE_M_Name = QtWidgets.QLineEdit(search)
        self.DE_M_Name.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.DE_M_Name.setObjectName("DE_M_Name")
        self.lineEdit_2 = QtWidgets.QLineEdit(search)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 130, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(search)
        self.label_2.setGeometry(QtCore.QRect(390, 150, 71, 20))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(search)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 451, 161))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Statistics = QtWidgets.QPushButton(search)
        self.Statistics.setGeometry(QtCore.QRect(360, 60, 75, 23))
        self.Statistics.setObjectName("Statistics")
        self.checkBox = QtWidgets.QCheckBox(search)
        self.checkBox.setGeometry(QtCore.QRect(60, 40, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(search)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 70, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(search)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 100, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(search)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 130, 111, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit.hide()
        self.EM_Id.hide()
        self.DE_M_Name.hide()
        self.lineEdit_2.hide()
        self.checkBox.clicked.connect(self.lineEdit.show)
        self.checkBox_2.clicked.connect(self.EM_Id.show)
        self.checkBox_3.clicked.connect(self.DE_M_Name.show)
        self.checkBox_4.clicked.connect(self.elsehide)
        self.pushButton_2.clicked.connect(self.serach)
        self.retranslateUi(search)
        self.pushButton.clicked.connect(search.close)
        self.Statistics.clicked.connect(self.all)
        QtCore.QMetaObject.connectSlotsByName(search)

    def elsehide(self):
        self.lineEdit_2.show()
        self.checkBox.setCheckable(False)
        self.checkBox_2.setCheckable(False)
        self.checkBox_3.setCheckable(False)
        self.checkBox.setChecked(0)
        self.checkBox_2.setChecked(0)
        self.checkBox_3.setChecked(0)
        if (self.checkBox_4.isclicked(0)):
            self.checkBox.setCheckable(True)
            self.checkBox_2.setCheckable(True)
            self.checkBox_3.setCheckable(True)

    def retranslateUi(self, search):
        _translate = QtCore.QCoreApplication.translate
        search.setWindowTitle(_translate("search", "search"))
        self.pushButton.setText(_translate("search", "return"))
        self.pushButton_2.setText(_translate("search", "Run"))
        self.checkBox.setText(_translate("search", "职员姓名"))
        self.label.setText(_translate("search", "查询选项(只选选项不输入则默认查询所有内容)"))
        self.checkBox_2.setText(_translate("search", "职员编号"))
        self.checkBox_3.setText(_translate("search", "部门经理"))
        self.checkBox_4.setText(_translate("search", "其他(仅单表)"))
        self.Statistics.setText(_translate("search", "Statistics"))

    def serach(self):
        self.connect_to_sercer()
        self.model = QStandardItemModel()
        title = []
        string2 = ''
        title_em = ["EM_Id", "EM_name", "EM_age", "salary", "EntWorkDay", "OutWorkDay", "EM_leader"]
        title_DT_M = ["DEPT_id", "DEPT_name", "M_name", "M_id"]
        title_DT = ["DEPT_id", "DEPT_name", "DEPT_setdate", "DEPT_achi", "DEPT_Surplusfunds", "DEPT_target"]
        string = "select * "
        table = "from "
        where = "where "
        if ((self.checkBox_2.isChecked() and self.checkBox_3.isChecked()) or (
                self.checkBox.isChecked() and self.checkBox_3.isChecked())):
            title.extend(title_DT_M)
            title.extend(title_em)
            table = table + " manage , employee "
            where = where + "M_name = '" + self.DE_M_Name.text() + "'"
            if (self.checkBox_2.isChecked()):
                where = where + " and EM_Id = '" + self.EM_Id.text() + "'"
            if (self.checkBox.isChecked()):
                where = where + " and EM_name = '" + self.lineEdit.text() + "'"
        elif (self.checkBox.isChecked() and self.checkBox_2.isChecked()):
            title.extend(title_em)
            where = where + "EM_name = '" + self.lineEdit.text() + "' and EM_Id = '" + self.EM_Id.text() + "'"
            table = table + 'employee '
        elif (self.checkBox_3.isChecked()):
            title.extend(title_DT_M)
            where = where + "manage.M_name = '" + self.DE_M_Name.text() + "'" + " and manage.M_name = employee.EM_leader;"
            table = table + "manage ,employee "
        elif (self.checkBox.isChecked()):
            title.extend(title_em)
            where = where + " EM_name = '" + self.lineEdit.text() + "'"
            table = table + "employee "
        elif (self.checkBox_2.isChecked()):
            title.extend(title_em)
            where = where + " EM_Id = '" + self.EM_Id.text() + "'"
            table = table + 'employee '
        elif (self.checkBox_4.isChecked()):
            table = table + 'employee '
            where = where + self.lineEdit_2.text()
        string = string + table + where
        print(self.checkBox.isChecked())
        print(string)
        self.cursor.execute(string)
        self.model.setHorizontalHeaderLabels(title)
        self.cursor.execute(string)
        rows = self.cursor.fetchall()
        print(rows)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        self.tableWidget.setHorizontalHeaderLabels(title)
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                newItem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        self.cursor.close
        self.conn.close

    def all(self):
        self.connect_to_sercer()
        self.cursor.execute("select avg(salary),count(*),avg(EM_age) from employee ;")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['平均工资', '员工人数', '平均年纪'])
        rows = self.cursor.fetchall()
        for i in range(len(rows)):
            for j in range(len(rows[0])):
                newItem = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, newItem)
        self.cursor.close
        self.conn.close


class Ui_MainWindow():
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.Dialog1 = QtWidgets.QDialog()
        self.ui1 = Ui_Dialog()
        self.ui1.__init__()
        self.ui1.setupUi(self.Dialog1)
        self.UsEr = ''
        self.PsWd = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 150, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 310, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 310, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(133, 61, 401, 41))
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 460, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.main_to_search)
        self.pushButton_2.clicked.connect(self.main_to_addanddelext)
        self.pushButton_4.clicked.connect(self.main_to_addanddelext)
        self.pushButton_3.clicked.connect(self.main_to_update)
        self.pushButton_5.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton_2.setText(_translate("MainWindow", "添加"))
        self.pushButton_3.setText(_translate("MainWindow", "修改"))
        self.pushButton_4.setText(_translate("MainWindow", "删除"))
        # self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("MainWindow", "退出"))

    def main_to_login(self):
        MainWindow.hide()
        self.Dialog1.show()
        self.Dialog1.exec_()
        MainWindow.show()
        self.UsEr = self.ui1.UserName
        self.PsWd = self.ui1.PassWord
        self.Welcome()

    def Welcome(self):
        self.label.setText("Welcome " + self.ui1.UserName + " !")

    def main_to_search(self):
        MainWindow.hide()
        self.Dialog2 = QtWidgets.QDialog()
        self.ui2 = Ui_search()
        self.ui2.__init__()
        self.ui2.Susername = self.UsEr
        self.ui2.Spassword = self.PsWd
        self.ui2.setupUi(self.Dialog2)
        self.Dialog2.show()
        self.Dialog2.exec_()
        MainWindow.show()

    def main_to_addanddelext(self):
        MainWindow.hide()
        self.Dialog3 = QtWidgets.QDialog()
        self.ui3 = Ui_add()
        self.ui3.__init__()
        self.ui3.Ausername = self.UsEr
        self.ui3.Apassword = self.PsWd
        self.ui3.setupUi(self.Dialog3)
        self.Dialog3.show()
        self.Dialog3.exec_()
        MainWindow.show()

    def main_to_update(self):
        MainWindow.hide()
        self.Dialog4 = QtWidgets.QDialog()
        self.ui4 = Ui_Update()
        self.ui4.__init__()
        self.ui4.Ausername = self.UsEr
        self.ui4.Apassword = self.PsWd
        self.ui4.setupUi(self.Dialog4)
        self.Dialog4.show()
        self.Dialog4.exec_()
        MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.main_to_login()
    sys.exit(app.exec_())