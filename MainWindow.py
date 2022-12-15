import sys
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
ins_file = common.resource_path("./insert.ui")
class insertWindow(QDialog):
    insert_finish_signal = pyqtSignal()  ##### 추가
    def __init__(self,):
        QDialog.__init__(self)

    def show_dialog(self,id):
        uic.loadUi(ins_file, self)
        self.id=id
        print(self.id)
        self.show()
        self.selectid(self.id)
        # self.salario_lineEdit.setReadOnly(True)
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
        self.q = QSqlQuery()
        self.aregar_Button.clicked.connect(self.onAgregar)
    def checked(self):
        arr=[]
        items=""
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
        if self.dry_checkBox.isChecked()==True:
            self.dry = "드라이"
            arr.append(self.dry)
        #     self.salario_lineEdit.insert(self.dry)
        if self.repair_checkBox.isChecked()==True:
            self.repair = "수선"
            arr.append(self.repair)
            # self.salario_lineEdit.insert(self.repair)
        if self.iron_checkBox.isChecked() == True:
            self.iron = "아이롱"
            arr.append(self.iron)
            # self.salario_lineEdit.insert(self.iron)
        if self.outdoor_checkBox.isChecked() == True:
           self.outdoor="잠바"
           arr.append(self.outdoor)
            # self.salario_lineEdit.append(f'{self.outdoor}')
        if self.long_checkBox.isChecked() == True:
            self.long = "롱패딩"
            arr.append(self.long)
            # self.salario_lineEdit.append(f'{self.long}')
        if self.cote_checkBox.isChecked() == True:
            self.cote = "코트"
            arr.append(self.cote)
            # self.salario_lineEdit.append(f'{self.cote}')
        if self.sweater_checkBox.isChecked() == True:
            self.sweater = "스웨터"
            arr.append(self.sweater)
            # self.salario_lineEdit.append(f'{self.sweater}')
        if self.pent_checkBox.isChecked() == True:
            self.pent = "바지"
            arr.append(self.pent)
            # self.salario_lineEdit.append(f'{self.pent}')
        if self.cloth_checkBox.isChecked() == True:
            self.cloth = "상의"
            arr.append(self.cloth)
            # self.salario_lineEdit.append(f'{self.cloth}')
        if self.set_checkBox.isChecked() == True:
            self.set = "한벌"
            arr.append(self.set)
            # self.salario_lineEdit.append(f'{self.set}')
        if self.ycloth_checkBox.isChecked() == True:
            self.ycloth = "Y셔츠"
            arr.append(self.ycloth)
        for item in arr:
            items+=item+" "
            self.salario_lineEdit.setText(items)

            # self.salario_lineEdit.append(f'{self.ycloth}')

        # self.salario_lineEdit.insert(f'{self.dry}{self.repair}{self.iron}{self.outdoor}{self.long}{self.cote}{self.sweater}{self.pent}{self.cloth}{self.set}{self.ycloth}')
    def selectid(self,id):
        return id

    def onAgregar(self):
        dong_name = self.dong_name_combo.currentText()
        nombre = self.nombre_lineEdit.text()
        edad = self.edad_lineEdit.text()
        salario = self.salario_lineEdit.text()
        inPutOutput = self.inPutOutput.currentText()
        pay = self.pay_comboBox.currentText()
        if dong_name == "이름/아파트명":
            QMessageBox.warning(self, "Error", "이름/아파트명을 넣으세요")

        if nombre == "":
            QMessageBox.warning(self, "Error", "이름을 넣으세요")

        if edad == "":
            QMessageBox.warning(self, "Error", "연락처를 넣으세요")

        if salario == "":
            QMessageBox.warning(self, "Error", "작업을 넣으세요")

        else:

            edad = str(edad)

            self.q.prepare(sqlquery.insert())
            self.q.addBindValue(self.id)

            self.q.bindValue(1, nombre)

            self.q.bindValue(2, dong_name)

            self.q.bindValue(3, edad)

            self.q.bindValue(4, salario)

            self.q.bindValue(5, inPutOutput)

            self.q.bindValue(6, pay)

            if(self.q.exec()==True):

                if (QMessageBox.question(self, "OK", "등록할까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
                    #self.dong_name_combo.clear()
                    #self.inPutOutput.clear()
                    self.nombre_lineEdit.clear()
                    self.edad_lineEdit.clear()
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
                    QMessageBox.about(self,"등록완료","등록완료 하였습니다.")

        self.close()
        self.insert_finish_signal.emit()

    def msgexec(self):
        return QMessageBox.exec()

edit_file = common.resource_path("./update_edit.ui")
class updateMainWindow(QDialog):
    edit_finish_signal = pyqtSignal() ##### 추가
    def __init__(self,):
        QDialog.__init__(self)
        ####### __init__()에 있는 문장들을 아래 show_dialog() 함수로 다 옮김

    def show_dialog(self, id): ######## 추가
        uic.loadUi(edit_file, self)
        self.q = QSqlQuery()
        self.id=id
        self.selectid(self.id)
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
        #     self.salario_lineEdit.insert(self.dry)
        if self.repair_checkBox.isChecked():
            self.repair = "수선"
            arr.append(self.repair)
            # self.salario_lineEdit.insert(self.repair)
        if self.iron_checkBox.isChecked() == True:
            self.iron = "아이롱"
            arr.append(self.iron)
            # self.salario_lineEdit.insert(self.iron)
        if self.outdoor_checkBox.isChecked() == True:
            self.outdoor = "잠바"
            arr.append(self.outdoor)
            # self.salario_lineEdit.append(f'{self.outdoor}')
        if self.long_checkBox.isChecked() == True:
            self.long = "롱패딩"
            arr.append(self.long)
            # self.salario_lineEdit.append(f'{self.long}')
        if self.cote_checkBox.isChecked() == True:
            self.cote = "코트"
            arr.append(self.cote)
            # self.salario_lineEdit.append(f'{self.cote}')
        if self.sweater_checkBox.isChecked() == True:
            self.sweater = "스웨터"
            arr.append(self.sweater)
            # self.salario_lineEdit.append(f'{self.sweater}')
        if self.pent_checkBox.isChecked() == True:
            self.pent = "바지"
            arr.append(self.pent)
            # self.salario_lineEdit.append(f'{self.pent}')
        if self.cloth_checkBox.isChecked() == True:
            self.cloth = "상의"
            arr.append(self.cloth)
            # self.salario_lineEdit.append(f'{self.cloth}')
        if self.set_checkBox.isChecked() == True:
            self.set = "한벌"
            arr.append(self.set)
            # self.salario_lineEdit.append(f'{self.set}')
        if self.ycloth_checkBox.isChecked() == True:
            self.ycloth = "Y셔츠"
            arr.append(self.ycloth)
        for item in arr:
            items += item + " "
            self.salario_lineEdit.setText(items)


    def selectid(self,id):
       self.q.prepare(sqlquery.selectid())
       self.q.addBindValue(id)
       self.q.exec()
       if self.q.next():
            self.nombre_lineEdit.setText(self.q.value(1))
            self.edad_lineEdit.setText(str(self.q.value(3)))

    def updatebtn(self):
        print(self.id)
        dong_name = self.dong_name_combo.currentText()
        nombre = self.nombre_lineEdit.text()
        edad = self.edad_lineEdit.text()
        salario = self.salario_lineEdit.text()
        inPutOutput = self.inPutOutput.currentText()
        pay = self.pay_comboBox.currentText()
        if dong_name == "이름/아파트명":
            QMessageBox.warning(self, "Error", "이름/아파트명을 넣으세요")

        if nombre == "":
            QMessageBox.warning(self, "Error", "이름을 넣으세요")

        if edad == "":
            QMessageBox.warning(self, "Error", "연락처를 넣으세요")

        if salario == "":
            QMessageBox.warning(self, "Error", "작업을 넣으세요")

        else:

            edad = str(edad)

            self.q.prepare(sqlquery.update())

            self.q.bindValue(0,nombre)

            self.q.bindValue(1,dong_name)

            self.q.bindValue(2,edad)

            self.q.bindValue(3,salario)

            self.q.bindValue(4,inPutOutput)

            self.q.bindValue(5,pay)

            self.q.bindValue(6,str(self.id))
            if (self.q.exec() == True):

                if (QMessageBox.question(self, "OK", "수정할까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
                    # self.dong_name_combo.clear()
                    # self.inPutOutput.clear()
                    self.nombre_lineEdit.clear()
                    self.edad_lineEdit.clear()
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
                    QMessageBox.about(self, "수정완료", "수정완료 하였습니다.")
        self.close()
        # main = MainWindow() ##### 삭제
        # main.loaddata() ##### 삭제
        self.edit_finish_signal.emit()  ##### 추가

    def msgexec(self):
           return QMessageBox.exec()

ui_file = common.resource_path("./MainWindow.ui")

class MainWindow(QDialog):
    signal = pyqtSignal(int)
    id_signal = pyqtSignal(str)
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(ui_file, self)

        self.q = QSqlQuery()
        self.insertwindow = insertWindow()  ##### 추가
        self.signal.connect(self.insertwindow.show_dialog)  ##### 추가
        self.insertwindow.insert_finish_signal.connect(self.loaddata)  ##### 추가
        self.updatemain = updateMainWindow()  ##### 추가
        self.id_signal.connect(self.updatemain.show_dialog)  ##### 추가
        self.updatemain.edit_finish_signal.connect(self.loaddata)  ##### 추가
        self.select_lineEdit.returnPressed.connect(self.loaddata)
        self.deletebtn.clicked.connect(self.btnDel)
        self.updatebtn.clicked.connect(self.btnupd)
        self.insertbtn.clicked.connect(self.btnins)
        self.buttonUpdate.clicked.connect(self.regorderupdate)
        self.buttonDelAll.clicked.connect(self.btnDelAll)
        self.page = 1
        self.perpage = 15
        self.totalblock=ceil(self.totalcount()/self.perpage)
        self.pagebtn()
        self.loaddata()
    def pagebtn(self):
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
        self.pagebtn()
        self.select_Widget.setRowCount(0)
        self.select_Widget.setColumnCount(8)
        # rowp = 0
        # if self.page == 1:
        #     rowp = self.totalcount() - self.perpage
        # rowcount = self.totalcount() - ((self.page - 1) * self.perpage) - rowp
        self.select_Widget.setRowCount(15)
        self.select_Widget.setHorizontalHeaderLabels(
            ["id", "nombre","dong_name", "edad", "salario", "inPutOutput", "pay", "regdate"])
        self.q.exec(sqlquery.selectpage(self.comboboxret(),self.nombretxtret(),self.page,self.perpage,"asc"))
        tablerow=0
        while(self.q.next()):
           self.select_Widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
           self.select_Widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(self.q.value(1))))
           self.select_Widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(self.q.value(2))))
           self.select_Widget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(self.q.value(3))))
           self.select_Widget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
           self.select_Widget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(self.q.value(5)))
           self.select_Widget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(self.q.value(6)))
           self.select_Widget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(self.q.value(7)))
           tablerow+=1
        self.select_Widget.resizeColumnsToContents()
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

    def btnDel(self):
         try:
             crow = self.select_Widget.currentRow() #현재의 row를 가져옮.
             id = self.select_Widget.item(crow, 0).text()#item에서 row,column값의 텍스트를 가져옮
             if QMessageBox.question(self, "Elminar", "지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                 self.q.prepare(sqlquery.delete())
                 self.q.bindValue(0,str(id))
                 if self.q.exec()==True:
                     QMessageBox.warning(self,"Elminar","지웠습니다")
                 self.loaddata()
         except:
             print("")

    def regorderupdate(self):
        self.select_Widget.setRowCount(0)
        self.select_Widget.setColumnCount(8)
        self.select_Widget.setRowCount(15)
        self.select_Widget.setHorizontalHeaderLabels(
            ["id", "nombre", "dong_name", "edad", "salario", "inPutOutput", "pay", "regdate"])
        self.q.exec(sqlquery.selectpage(self.comboboxret(), self.nombretxtret(), self.page, self.perpage, "desc"))
        tablerow = 0
        while (self.q.next()):
            self.select_Widget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(self.q.value(0))))
            self.select_Widget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(self.q.value(1))))
            self.select_Widget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(self.q.value(2))))
            self.select_Widget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(self.q.value(3))))
            self.select_Widget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(self.q.value(4)))
            self.select_Widget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(self.q.value(5)))
            self.select_Widget.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(self.q.value(6)))
            self.select_Widget.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(self.q.value(7)))
            tablerow += 1
        self.select_Widget.resizeColumnsToContents()

    def btnDelAll(self):
        if QMessageBox.question(self, "Elminar", "다 지울까요?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.q.exec(sqlquery.deleteall())
            self.loaddata()
    def btnupd(self):
        try:
            crow = self.select_Widget.currentRow()  # 현재의 row를 가져옮.
            id = self.select_Widget.item(crow, 0).text()  # item에서 row,column값의 텍스트를 가져옮
            self.id_signal.emit(id)
        except:
            print()

    def maxval(self):
        q = QSqlQuery()
        q.exec(sqlquery.selectmax())
        numrows = 0
        if q.next():
            numrows = q.value(0)
        return numrows
    def btnins(self):
        try:
            nextval=int(self.maxval())+1
            self.signal.emit(nextval)
        except:
            print()

def start():
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    prepareDatabase()
    start()
