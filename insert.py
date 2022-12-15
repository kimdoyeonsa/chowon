import sys


from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

from common import *
import sqlquery


def prepareDatabase():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("data.db")
    db.open()
    q = QSqlQuery()
    if (q.exec(sqlquery.createtbl())):
        print("create table")
ui_file = common.resource_path("./insert.ui")
class MainWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(ui_file, self)
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

    def nextval(self):
        q = QSqlQuery()
        q.exec(sqlquery.selectmax())
        rec=q.record()
        numrows=0
        if q.next():
           numrows=q.value(0)
        return int(numrows)+1

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
            self.q.addBindValue(self.nextval())

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
