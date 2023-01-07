import sys
import time
from math import ceil

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

import sqlquery
from common import *


def prepareDatabase():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")
    db.open()
    q = QSqlQuery()
    q.exec(sqlquery.createtbl())
    q.exec(sqlquery.sal_createtbl())
    # q.exec(sqlquery.sal_foriegn())
    q.exec(sqlquery.pragma_on())
edit_file = common.resource_path("./edit.ui")
class editWindow(QDialog):
    edit_finish_signal = pyqtSignal()
    def __init__(self,):
        QDialog.__init__(self)

    def show_dialog(self,id,page,sel):
        uic.loadUi(edit_file, self)
        self.label_text=['등록','수정']
        self.q = QSqlQuery()
        self.id=id
        self.page=page
        self.sel=sel
        print(self.id)
        self.show()
        self.selectid()
        self.aregar_Button.clicked.connect(self.onAgregar)
        self.aregar_Button.setText(self.label_text[sel])

    def selectid(self):
        self.q.prepare(sqlquery.selectid())
        self.q.addBindValue(self.id)
        self.q.exec()
        if self.q.next():
            self.nombre_lineEdit.setText(self.q.value(1))
            self.edad_lineEdit.setText(str(self.q.value(3)))

    def onAgregar(self):
        try:
            dong_name = self.dong_name_combo.currentText()
            nombre = self.nombre_lineEdit.text()
            edad = self.edad_lineEdit.text()

            if dong_name == "이름/아파트명":
                QMessageBox.warning(self, "Error", "이름/아파트명을 넣으세요")

            if nombre == "":
                QMessageBox.warning(self, "Error", "이름을 넣으세요")

            else:
                if self.sel==0:
                    edad = str(edad)
                    self.q.prepare(sqlquery.insert())
                    self.q.addBindValue(self.id)
                    self.q.bindValue(1, nombre)
                    self.q.bindValue(2, dong_name)
                    self.q.bindValue(3, edad)
                else:
                    self.q.prepare(sqlquery.update())
                    self.q.bindValue(0, nombre)
                    self.q.bindValue(1, dong_name)
                    self.q.bindValue(2, edad)
                    self.q.bindValue(3, str(self.id))
                if(self.q.exec()==True):
                    if (QMessageBox.question(self, "OK", self.label_text[self.sel]+"할까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
                        #self.dong_name_combo.clear()
                        #self.inPutOutput.clear()
                        self.nombre_lineEdit.clear()
                        self.edad_lineEdit.clear()
                        QMessageBox.about(self,self.label_text[self.sel]+"완료",self.label_text[self.sel]+"완료 하였습니다.")
                self.close()
            self.edit_finish_signal.emit()
        except:
            pass

    def msgexec(self):
        return QMessageBox.exec()

sal_file = common.resource_path("./sal_update.ui")
class saledit_MainWindow(QDialog):
    saledit_finish_signal = pyqtSignal()
    saladd_finish_signal = pyqtSignal() #1
    def __init__(self,):
        QDialog.__init__(self)
    def show_dialog(self,id,sel):
        uic.loadUi(sal_file, self)
        self.q = QSqlQuery()
        self.id=id
        print(self.id)
        self.sel=sel
        self.label_text = ['등록', '수정']
        self.aregar_Button.clicked.connect(self.updatebtn)
        self.show()
        self.salario_lineEdit.setReadOnly(True)
        self.dry_checkBox.stateChanged.connect(self.checked)
        self.repair_checkBox.stateChanged.connect(self.checked)
        self.iron_checkBox.stateChanged.connect(self.checked)
        self.outdoor_checkBox.stateChanged.connect(self.checked)
        self.long_checkBox.stateChanged.connect(self.checked)
        self.cote_checkBox.stateChanged.connect(self.checked)
        self.sweater_checkBox.stateChanged.connect(self.checked)
        self.pent_checkBox.stateChanged.connect(self.checked)
        self.cloth_checkBox.stateChanged.connect(self.checked)
        self.set_checkBox.stateChanged.connect(self.checked)
        self.ycloth_checkBox.stateChanged.connect(self.checked)
        self.label.setText('작업'+self.label_text[self.sel])
        self.aregar_Button.setText(self.label_text[self.sel])
    def checked(self):
        arr = []
        items = ""
        self.dry = ""
        self.repair = ""
        self.iron = ""
        self.outdoor = ""
        self.long = ""
        self.cote = ""
        self.sweater = ""
        self.pent = ""
        self.cloth = ""
        self.set = ""
        self.ycloth = ""
        if self.dry_checkBox.isChecked():
            self.dry = "드라이"
            arr.append(self.dry)
        if self.repair_checkBox.isChecked():
            self.repair = "수선"
            arr.append(self.repair)
        if self.iron_checkBox.isChecked() == True:
            self.iron = "아이롱"
            arr.append(self.iron)
        if self.outdoor_checkBox.isChecked() == True:
            self.outdoor = "잠바"
            arr.append(self.outdoor)
        if self.long_checkBox.isChecked() == True:
            self.long = "롱패딩"
            arr.append(self.long)
        if self.cote_checkBox.isChecked() == True:
            self.cote = "코트"
            arr.append(self.cote)
        if self.sweater_checkBox.isChecked() == True:
            self.sweater = "스웨터"
            arr.append(self.sweater)
        if self.pent_checkBox.isChecked() == True:
            self.pent = "바지"
            arr.append(self.pent)
        if self.cloth_checkBox.isChecked() == True:
            self.cloth = "상의"
            arr.append(self.cloth)
        if self.set_checkBox.isChecked() == True:
            self.set = "한벌"
            arr.append(self.set)
        if self.ycloth_checkBox.isChecked() == True:
            self.ycloth = "Y셔츠"
            arr.append(self.ycloth)
        for item in arr:
            items += item +" "
            self.salario_lineEdit.setText(items)


    def selectid(self):
       self.q.prepare(sqlquery.selectid())
       self.q.addBindValue(self.id)
       self.q.exec()
       if self.q.next():
            self.salario_lineEdit.setText(self.q.value(4))

    def updatebtn(self):
        salario = self.salario_lineEdit.text()
        inPutOutput = self.inPutOutput.currentText()
        pay = self.pay_comboBox.currentText()
        if salario == "":
            QMessageBox.warning(self, "Error", "작업을 넣으세요")

        else:
            if self.sel == 0:
                self.q.prepare(sqlquery.sal_insert())
                self.q.bindValue(0,str(maxval("sal_emple")))
                self.q.bindValue(1,int(self.id))
                self.q.bindValue(2,salario)
                self.q.bindValue(3, inPutOutput)
                self.q.bindValue(4,pay)
            else:
                self.q.prepare(sqlquery.sal_update())
                self.q.bindValue(0, salario)
                self.q.bindValue(1, inPutOutput)
                self.q.bindValue(2, pay)
                self.q.bindValue(3,str(self.id))
            if (self.q.exec() == True):
                if (QMessageBox.question(self, "OK", '작업을 '+self.label_text[self.sel]+" 할까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
                    self.salario_lineEdit.clear()
                    self.dry_checkBox.setChecked(False)
                    self.repair_checkBox.setChecked(False)
                    self.iron_checkBox.setChecked(False)
                    self.outdoor_checkBox.setChecked(False)
                    self.long_checkBox.setChecked(False)
                    self.cote_checkBox.setChecked(False)
                    self.sweater_checkBox.setChecked(False)
                    self.pent_checkBox.setChecked(False)
                    self.cloth_checkBox.setChecked(False)
                    self.set_checkBox.setChecked(False)
                    self.ycloth_checkBox.setChecked(False)
                    self.saladd_finish_signal.emit() #1
                    QMessageBox.about(self, self.label_text[self.sel]+"완료", self.label_text[self.sel]+"완료 하였습니다.")
        self.close()
        self.saledit_finish_signal.emit()
    def msgexec(self):
           return QMessageBox.exec()
sel_file = common.resource_path("./seltbl.ui")
class seltblWindow(QDialog):
    sel_finish_signal = pyqtSignal()
    sal_ins_signal = pyqtSignal(str, int)
    sal_upd_signal = pyqtSignal(str, int)
    saladd_btn_signal=pyqtSignal() #1
    saldel_btn_signal=pyqtSignal() #1
    def __init__(self, ):
        QDialog.__init__(self)
    def show_dialog(self, id):
        uic.loadUi(sel_file, self)
        self.q = QSqlQuery()
        self.id = id
        self.page = 1
        self.perpage = 10
        self.pagebtn()
        self.selectuser()
        self.salins_Window = saledit_MainWindow()
        self.sal_ins_signal.connect(self.salins_Window.show_dialog)
        self.salins_Window.saledit_finish_signal.connect(self.selectuser)
        self.salupd_Window = saledit_MainWindow()
        self.sal_upd_signal.connect(self.salupd_Window.show_dialog)
        self.salupd_Window.saledit_finish_signal.connect(self.selectuser)
        self.salins_Window.saladd_finish_signal.connect(self.sal_add_signal_func) #1
        self.salupd_Window.saladd_finish_signal.connect(self.sal_add_signal_func) #1
        self.btnadd.clicked.connect(self.sal_addbtn)
        self.btnupd.clicked.connect(self.sal_updbtn)
        self.btndel.clicked.connect(self.sal_btnDel)
        self.searchprev.clicked.connect(self.sal_decrement)
        self.searchnext.clicked.connect(self.sal_increment)
        self.sel_finish_signal.emit()
        self.show()
    #1
    def sal_add_signal_func(self):
        self.saladd_btn_signal.emit()
    def show_init(self):
        self.totalblock = ceil(self.totalcount() / self.perpage)
    def totalcount(self):
        self.q.prepare(sqlquery.sal_emple_count())
        self.q.addBindValue(self.id)
        self.q.exec()
        count = 0
        if self.q.next():
            count = self.q.value(0)
        return count
    def pagebtn(self):
        self.show_init()
        if self.page == 1:
            self.searchprev.setVisible(False)
            self.searchnext.setVisible(False)
        if self.page > 1:
            self.searchprev.setVisible(True)
            self.searchnext.setVisible(False)
            if self.page != self.totalblock:
                self.searchnext.setVisible(True)
            else:
                self.searchnext.setVisible(False)
        else:
            self.searchprev.setVisible(False)
            self.searchnext.setVisible(True)
    def selectuser(self):
        self.sel_tableWidget.setRowCount(0)
        self.sel_tableWidget.setColumnCount(6)
        self.sel_tableWidget.setRowCount(self.perpage)
        self.sel_tableWidget.setHorizontalHeaderLabels(
            ["id","작업", "입/출고", "선/후불", "작업등록일","작업마감일"])
        self.pagebtn()
        self.q.prepare(sqlquery.sal_emple_i_w_p(self.page,self.perpage))
        self.q.addBindValue(self.id)
        self.q.exec()
        tablerow = 0
        while (self.q.next()):
            self.sel_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
            self.sel_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.q.value(1)))
            self.sel_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.q.value(2)))
            self.sel_tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(self.q.value(3)))
            self.sel_tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
            self.sel_tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(self.q.value(5)))

            tablerow += 1
        self.sel_tableWidget.resizeColumnsToContents()

    def sal_decrement(self):
        self.page -= 1
        if self.page >= 1:
            self.searchprev.setVisible(True)
            self.labePlus.setText(str(self.page))
            self.selectuser()
        else:
            self.searchnext.setVisible(True)
            self.searchprev.setVisible(False)
    def sal_increment(self):
        self.page += 1
        if (self.page <= self.totalblock):
            self.labePlus.setText(str(self.page))
            self.searchnext.setVisible(True)
            self.selectuser()
        else:
            self.searchnext.setVisible(False)
            self.searchprev.setVisible(True)
    def sal_addbtn(self):
        try:
            self.sal_ins_signal.emit(self.id,0)
        except:
            print()
    def sal_updbtn(self):
        try:
            crow = self.sel_tableWidget.currentRow()
            sal_id = self.sel_tableWidget.item(crow, 0).text()
            self.sal_upd_signal.emit(sal_id, 1)
        except:
            print()
    def sal_btnDel(self):
        try:
            if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self.q.prepare(sqlquery.sal_delete())
                crow = self.sel_tableWidget.currentRow()
                sal_id = self.sel_tableWidget.item(crow, 0).text()
                self.q.bindValue(0, sal_id)
                if self.q.exec() == True:
                    QMessageBox.warning(self, "Elminar", "지웠습니다")
                    self.selectuser()
                    self.sel_finish_signal.emit()
                    self.saldel_btn_signal.emit()

        except:
            QMessageBox.warning(self, "Elminar", "선택이 되어있지 않습니다.")
read_file = common.resource_path("./read.ui")
class readMainWindow(QDialog):
    saled_signal = pyqtSignal(str, int)
    ed_signal = pyqtSignal(str,int,int)
    id_signal = pyqtSignal(str)
    sel_signal = pyqtSignal(str)
    read_finish_signal = pyqtSignal()
    def __init__(self,):
        QDialog.__init__(self)
    def show_dialog(self, id,page):
        uic.loadUi(read_file, self)
        self.q = QSqlQuery()
        self.id=id
        print(self.id)
        self.page=page
        self.updatemain = editWindow()
        self.ed_signal.connect(self.updatemain.show_dialog)
        self.closebtn.clicked.connect(self.close_btn)
        self.selmain=seltblWindow() #1
        self.selmain.saldel_btn_signal.connect(self.sal_select) #1
        self.selmain.saladd_btn_signal.connect(self.sal_select) #1
        self.sel_signal.connect(self.selmain.show_dialog)
        self.selbtn.clicked.connect(self.selectbtn)
        self.deletebtn.clicked.connect(self.btnDel)
        self.user_updatebtn.clicked.connect(self.btnupd)
        self.updatemain.edit_finish_signal.connect(self.selectid)
        self.selectid()
        self.sal_select()
        self.show()
    def selectid(self):
       self.q.prepare(sqlquery.selectid())
       self.q.addBindValue(self.id)
       self.q.exec()
       if self.q.next():
            self.nombre_lineEdit.setText(self.q.value(1))
            self.dong_name_lineEdit.setText(self.q.value(2))
            self.edad_lineEdit.setText(str(self.q.value(3)))
            self.regdate_lineEdit.setText(str(self.q.value(4)))
       self.read_finish_signal.emit()
    def totalcount(self):
        self.q.prepare(sqlquery.sal_emple_count())
        self.q.bindValue(0,self.id)
        self.q.exec()
        count=0
        if self.q.next():
            count=self.q.value(0)
        return count
    def sal_select(self):
        self.salsel_tableWidget.setRowCount(0)
        self.salsel_tableWidget.setColumnCount(5)
        self.salsel_tableWidget.setRowCount(self.totalcount())
        self.salsel_tableWidget.setHorizontalHeaderLabels(
            ["id", "작업", "입/출고", "선/후불","작업마감일"])
        self.q.prepare(sqlquery.sal_emple_i_w())
        self.q.bindValue(0,self.id)
        self.q.exec()
        tablerow = 0
        while (self.q.next()):
            self.salsel_tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
            self.salsel_tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(self.q.value(1)))
            self.salsel_tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(self.q.value(2)))
            self.salsel_tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(self.q.value(3)))
            self.salsel_tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(5)))
            tablerow += 1
        self.salsel_tableWidget.resizeColumnsToContents()

    def close_btn(self):
        self.close()
    def btnupd(self):
        try:
           self.ed_signal.emit(self.id,self.page,1)
        except:
            QMessageBox.warning(self, "update", "선택이 되어있지 않습니다.")

    def btnDel(self):
         try:
             if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                 self.q.prepare(sqlquery.delete())
                 self.q.bindValue(0,str(self.id))
                 if self.q.exec()==True:
                     QMessageBox.warning(self,"Elminar","지웠습니다")
                     self.read_finish_signal.emit()
                     self.close()
         except:
             QMessageBox.warning(self, "Elminar", "선택이 되어있지 않습니다.")

    def selectbtn(self):
        self.sel_signal.emit(self.id)

ui_file = common.resource_path("./MainWindow.ui")

class MainWindow(QDialog):
    signal = pyqtSignal(int,int,int)
    read_signal = pyqtSignal(str,int)
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(ui_file, self)
        self.q = QSqlQuery()
        self.read_dialog = readMainWindow()
        self.read_signal.connect(self.read_dialog.show_dialog)
        self.read_dialog.read_finish_signal.connect(self.loaddata)
        self.read_dialog.id_signal.connect(self.loaddata)
        self.insertWindow = editWindow()
        self.signal.connect(self.insertWindow.show_dialog)
        self.insertWindow.edit_finish_signal.connect(self.loaddata)
        self.select_lineEdit.returnPressed.connect(self.loaddata)
        self.select_Widget.clicked.connect(self.read)
        self.insertbtn.clicked.connect(self.btnins)
        self.buttonDelAll.clicked.connect(self.btnDelAll)
        self.page = 1
        self.perpage = 10
        self.orderby="asc"
        self.buttonUpdate.clicked.connect(self.regorderupdate)
        self.pagebtn()
        self.loaddata()
        self.searchprev.clicked.connect(self.decrement)
        self.searchnext.clicked.connect(self.increment)

    def show_init(self):
        self.totalblock=ceil(self.totalcount()/self.perpage)
    def pagebtn(self):
        self.show_init()
        print(self.page, self.totalblock)
        if self.page==1:
            self.searchprev.setVisible(False)
            self.searchnext.setVisible(False)
        if self.page > 1:
            self.searchprev.setVisible(True)
            self.searchnext.setVisible(False)
            if self.page != self.totalblock:
                self.searchnext.setVisible(True)
            else:
                self.searchnext.setVisible(False)
        else:
            self.searchprev.setVisible(False)
            self.searchnext.setVisible(True)


    def regorderupdate(self):
        if self.buttonUpdate.isChecked():
            self.orderby="desc"
            self.buttonUpdate.setText("지난등록순")
            self.loaddata()
        else:
            self.orderby = "asc"
            self.buttonUpdate.setText("최신등록순")
            self.loaddata()
    def nombretxtret(self):
        nombretxt=self.select_lineEdit.text()
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
    #검색 페이징
    def loaddata(self):
        self.select_Widget.setRowCount(0)
        self.select_Widget.setColumnCount(5)
        self.select_Widget.setRowCount(self.perpage)
        self.select_Widget.setHorizontalHeaderLabels(
            ["id", "이름","동/호수", "연락처", "등록일"])
        self.pagebtn()
        self.q.exec(sqlquery.selectpage(self.comboboxret(),self.nombretxtret(),self.page,self.perpage,self.orderby))
        tablerow=0
        while(self.q.next()):
           self.select_Widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
           self.select_Widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(self.q.value(1))))
           self.select_Widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(self.q.value(2))))
           self.select_Widget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(self.q.value(3))))
           self.select_Widget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
           tablerow+=1
        self.select_Widget.resizeColumnsToContents()
    def decrement(self):
        try:
            self.page-=1
            if self.page >= 1:
                self.searchprev.setVisible(True)
                self.labePlus.setText(str(self.page))
                self.loaddata()
            else:
                self.searchnext.setVisible(True)
                self.searchprev.setVisible(False)
        except:
            print()
    def increment(self):
        try:
            self.page+=1
            if(self.page<=self.totalblock):
                self.labePlus.setText(str(self.page))
                self.searchnext.setVisible(True)
                self.loaddata()
            else:
                self.searchnext.setVisible(False)
                self.searchprev.setVisible(True)
        except:
            print()

    def read(self):
        try:
            crow = self.select_Widget.currentRow()  # 현재의 row를 가져옮.
            id = self.select_Widget.item(crow, 0).text()  # item에서 row,col
            self.read_signal.emit(id,self.page)
        except:
            QMessageBox.warning(self, "update", "선택이 되어있지 않습니다.")

    def btnDelAll(self):
        if QMessageBox.question(self, "Elminar", "다 지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.q.exec(sqlquery.deleteall())
            self.loaddata()
    def btnins(self):
        try:
            nextval=int(maxval("empleado"))
            self.signal.emit(nextval,self.page,0)
        except:
            print()
def maxval(tbl):
    q = QSqlQuery()
    q.exec(sqlquery.selectmax(tbl))
    numrows = 0
    if q.next():
        numrows = q.value(0)
    return int(numrows+1)
def start():
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    prepareDatabase()
    start()