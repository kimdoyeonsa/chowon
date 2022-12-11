import sys
from math import ceil

from PyQt5 import uic, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import sqlquery
from common import *


def prepareDatabase():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")
    db.open()

ui_file = common.resource_path("./select.ui")
class MainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(ui_file, self)
        self.page = 1
        self.perpage = 15

        self.q = QSqlQuery()
        self.buscar_nombre_lineEdit.returnPressed.connect(self.loaddata)


        self.totalblock=ceil(self.totalcount()/self.perpage)
        if self.totalblock==1:
            self.searchprev.setVisible(False)
            self.searchnext.setVisible(False)
        else:
            if self.page >= 1:
                self.searchnext.setVisible(False)
                self.searchprev.setVisible(True)
                self.searchprev.clicked.connect(self.decrement)
            else:
                self.searchnext.setVisible(True)
                self.searchprev.setVisible(False)
            if self.page<=self.totalblock:
                self.searchnext.setVisible(True)
                self.searchprev.setVisible(False)
                self.searchnext.clicked.connect(self.increment)
            else:
                self.searchnext.setVisible(False)
                self.searchprev.setVisible(True)


        self.loaddata()
    def nombretxtret(self):
        nombretxt=self.buscar_nombre_lineEdit.text()
        return nombretxt

    def comboboxret(self):
        if self.comboBoxSearch.currentText() == "이름":
            return "nombre"
        if self.comboBoxSearch.currentText() == "아파트동호수":
            return "dong_name"
        if self.comboBoxSearch.currentText() == "아이디":
            return "id"
        if self.comboBoxSearch.currentText() == "연락처":
            return "edad"

    def totalcount(self):
        self.q.exec(sqlquery.selectcount())
        count=0
        if self.q.next():
            count=self.q.value(0)
        return count
    def loaddata(self):
        self.buscar_Widget.setRowCount(0)
        self.buscar_Widget.setColumnCount(8)
        # rowp = 0
        # if self.page == 1:
        #     rowp = self.totalcount() - self.perpage
        # rowcount = self.totalcount() - ((self.page - 1) * self.perpage) - rowp
        self.buscar_Widget.setRowCount(15)
        self.buscar_Widget.setHorizontalHeaderLabels(
            ["id", "nombre","dong_name", "edad", "salario", "inPutOutput", "pay", "regdate"])
        self.q.exec(sqlquery.selectpage(self.comboboxret(),self.nombretxtret(),self.page,self.perpage))
        tablerow=0
        while(self.q.next()):
           self.buscar_Widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
           self.buscar_Widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(self.q.value(1))))
           self.buscar_Widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(self.q.value(2))))
           self.buscar_Widget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(self.q.value(3))))
           self.buscar_Widget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
           self.buscar_Widget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(self.q.value(5)))
           self.buscar_Widget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(self.q.value(6)))
           self.buscar_Widget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(self.q.value(7)))
           tablerow+=1
        self.buscar_Widget.resizeColumnsToContents()
    def decrement(self):
        self.page -= 1
        if self.page >= 1:
            self.searchprev.setVisible(True)
            self.labePlus.setText(str(self.page))
            self.loaddata()
        else:
            self.searchnext.setVisible(True)
            self.searchprev.setVisible(False)
    def increment(self):
        self.page+=1
        if(self.page<=self.totalblock):
            self.labePlus.setText(str(self.page))
            self.loaddata()

        else:
            self.searchnext.setVisible(False)
            self.searchprev.setVisible(True)


def start():
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    prepareDatabase()
    start()
