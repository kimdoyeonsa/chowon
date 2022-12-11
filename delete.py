import sys
from math import ceil

from PyQt5 import uic, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *



import sqlquery
from common import common


def prepareDatabase():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")
    db.open()
ui_file = common.resource_path("./delete.ui")

class MainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(ui_file, self)
        self.page=1
        self.perpage=15
        # 삭제
        # self.eliminarModelq = QSqlQueryModel(self)
        # self.eliminarModelq.setQuery(sqlquery.selectpage(self.page, self.perpage))
        # self.eliminar_tableView.setModel(self.eliminarModelq)
        # self.eliminarModel = QSqlTableModel(self)
        # self.eliminarModel.setTable("empleado")
        # self.eliminarModel.select()
        # self.eliminar_tableView.setEditTriggers(QTableView.NoEditTriggers)
        # self.eliminar_tableView.setSelectionBehavior(QTableView.SelectRows)
        # self.eliminar_tableView.setModel(self.eliminarModelq)
        self.eliminar_Widget.clicked.connect(self.btnDel)
        # self.labePlus.setText(str(self.page))
        self.buttonDelAll.clicked.connect(self.btnDelAll)
        self.eliminar_lineEdit.returnPressed.connect(self.loaddata)
        self.q = QSqlQuery()
        self.totalblock = ceil(self.totalcount() / self.perpage)
        if self.totalblock == 1:
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
            if self.page <= self.totalblock:
                self.searchnext.setVisible(True)
                self.searchprev.setVisible(False)
                self.searchnext.clicked.connect(self.increment)
            else:
                self.searchnext.setVisible(False)
                self.searchprev.setVisible(True)

        self.loaddata()

    def nombretxtret(self):
        nombretxt = self.eliminar_lineEdit.text()
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

        count = 0
        if self.q.next():
            count = self.q.value(0)
        return count

    def loaddata(self):
        self.eliminar_Widget.setRowCount(0)
        self.eliminar_Widget.setColumnCount(8)
        # rowp = 0
        # if self.page == 1:
        #     rowp = self.totalcount() - self.perpage
        # rowcount = self.totalcount() - ((self.page - 1) * self.perpage) - rowp
        self.eliminar_Widget.setRowCount(15)
        self.eliminar_Widget.setHorizontalHeaderLabels(
            ["id", "nombre","dong_name", "edad", "salario", "inPutOutput", "pay", "regdate"])
        self.q.exec(sqlquery.selectpage(self.comboboxret(), self.nombretxtret(), self.page, self.perpage))
        tablerow = 0
        while (self.q.next()):
            self.eliminar_Widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
            self.eliminar_Widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(self.q.value(1))))
            self.eliminar_Widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(self.q.value(2))))
            self.eliminar_Widget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(self.q.value(3))))
            self.eliminar_Widget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
            self.eliminar_Widget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(self.q.value(5)))
            self.eliminar_Widget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(self.q.value(6)))
            self.eliminar_Widget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(self.q.value(7)))
            tablerow += 1
        self.eliminar_Widget.resizeColumnsToContents()
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
        self.page += 1
        if (self.page <= self.totalblock):
            self.labePlus.setText(str(self.page))
            self.loaddata()

        else:
            self.searchnext.setVisible(False)
            self.searchprev.setVisible(True)
    def btnDelAll(self):
        if QMessageBox.question(self, "Elminar", "다 지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.q.exec(sqlquery.deleteall())
            self.loaddata()
    def btnDel(self):
        try:
            crow = self.eliminar_Widget.currentRow()
            id = self.eliminar_Widget.item(crow, 0).text()
            if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self.q.prepare(sqlquery.delete())
                self.q.bindValue(0,str(id))
                if self.q.exec()==True:
                    QMessageBox.warning(self,"Elminar","지웠습니다")
                self.loaddata()
        except:
            print("")
    # 수정


        # self.modificarQuery.select()
     # self.buttonUpdate.clicked.connect(self.buttonUpdate)
        # self.buttonUpdate.clicked.connect(self.btnUpdate)


        # self.modificar_tableView.clicked.connect(self.onUpdata)

        #self.modificar_tableView.setModel(self.modificarModel)
        # self.modificar_tableView.setModel(self.modificarQuery)
        # self.eliminar_lineEdit.textEdited.connect(self.onEliminarSerch)
        # self.eliminarModelcnt=QSqlQueryModel(self)
        # self.eliminarModelcnt.setQuery(sqlquery.selectall())
        # self.totalblock=ceil(self.eliminarModelcnt.rowCount()/self.perpage)
        # if (self.page >= 1):
        #     self.searchprev.clicked.connect(self.decrement)
        #     self.searchprev.setVisible(False)
        # else:
        #     pass
        # self.searchnext.clicked.connect(self.increment)

        # if(self.page>=1):
        #     self.searchprev.setVisible(True)
        #     self.searchprev.clicked.connect(self.decrement)
        # else:
        #     self.searchprev.setVisible(False)
        # if(self.page<totalblock):
        #     self.searchnext.setVisible(True)
        #     self.searchnext.clicked.connect(self.increment)
        # else:
        #     self.searchnext.setVisible(False)
        #
        # self.eliminar_tableView.clicked.connect(self.onEliminar)

        # self.modificarModel.beforeUpdate.connect(self.onModificarModel_beforeUpdate)

    # def onUpdata(self):
    #     self.modificarModel = QSqlTableModel(self)
    #     self.modificarModel.select()
    #     self.modificarModel.setTable("empleado")

    # def btnUpdate(self):
    #     self.modificarQuery = QSqlQueryModel(self)
    #     self.modificarQuery.setQuery("select * from empleado order by id desc")
    #     self.modificar_tableView.setModel(self.modificarQuery)

    # def btnDelAll(self):
    #     if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
    #         self.eliminarModelq = QSqlQueryModel(self)
    #         self.eliminarModelq.setQuery(sqlquery.delete())
    #         self.eliminar_tableView.setModel(self.eliminarModelq)
    #         self.eliminarModelq.setQuery(sqlquery.selectpage(self.page, self.perpage))
    #         self.eliminar_tableView.setModel(self.eliminarModelq)
    #
    #
    # def refreshTables(self):
    #    self.eliminarModelq.setQuery(sqlquery.selectpage(self.page, self.perpage))

        # self.modificarQuery.setQuery("select * from empleado order by id desc limit 15")


    # def onModificar(self):
    #     self.refreshTables()
    #
    # def onEliminar(self, idx):
    #     self.refreshTables()
    #     self.eliminar_tableView.setEditTriggers(QTableView.NoEditTriggers)
    #     self.eliminar_tableView.setSelectionBehavior(QTableView.SelectRows)
    #     # self.eliminar_tableView.setModel(self.eliminarModel)

    #
    #     if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
    #         self.eliminarModelcnt = QSqlQueryModel(self)
    #         self.eliminarModelcnt.setQuery(sqlquery.selectall())
    #         row = (((self.page-1)*self.perpage)+idx.row())-1
    #         print(row)
    #         if self.eliminarModel.removeRow(row):
    #             self.eliminarModelq.setQuery(sqlquery.selectall())
    #             self.eliminarModel.select()
    #             self.eliminar_tableView.setModel(self.eliminarModelq)
    #             self.eliminarModelq.setQuery(sqlquery.selectpage(self.page,self.perpage))
    # def decrement(self):
    #     print(self.eliminarModelcnt.rowCount())
    #     self.page -= 1
    #     if self.page>=1:
    #         self.searchnext.setVisible(True)
    #         self.labePlus.setText(str(self.page))
    #         self.eliminarModelq.setQuery(sqlquery.selectpage(self.page, self.perpage))
    #     else:
    #         self.searchprev.setVisible(False)
    #         self.searchnext.setVisible(True)
    #
    # def increment(self):
    #     print(self.eliminarModelcnt.rowCount())
    #     self.page += 1
    #     if(self.page<=self.totalblock):
    #         self.searchprev.setVisible(True)
    #         self.labePlus.setText(str(self.page))
    #         self.eliminarModelq.setQuery(sqlquery.selectpage(self.page, self.perpage))
    #     else:
    #         self.searchprev.setVisible(True)
    #         self.searchnext.setVisible(False)
    # def onEliminarSerch(self, txt):
    #     if self.comboBoxSearch.currentText() == "이름/아파트동호수":
    #         self.eliminarModelq.setQuery(sqlquery.search("nombre", txt))
    #     if self.comboBoxSearch.currentText() == "아이디":
    #         self.eliminarModelq.setQuery(sqlquery.search("id", txt))
    #     if self.comboBoxSearch.currentText() == "연락처":
    #         self.eliminarModelq.setQuery(sqlquery.search("edad", txt))
    #


    def msgexec(self):
        return QMessageBox.exec()

def start():
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    prepareDatabase()
    start()
