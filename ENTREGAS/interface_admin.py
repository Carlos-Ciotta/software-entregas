from PyQt5 import QtCore, QtGui, QtWidgets
from controllers import get_all


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 901)
        MainWindow.setMinimumSize(QtCore.QSize(1123, 901))
        MainWindow.setMaximumSize(QtCore.QSize(1123, 901))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 1091, 721))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.close())
        self.pushButton_sair.setGeometry(QtCore.QRect(960, 810, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        #populate
        self.populate_table()
        self.pushButton_sair.setFont(font)
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.pushButton_atualizar = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.populate_table())
        self.pushButton_atualizar.setGeometry(QtCore.QRect(960, 760, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_atualizar.setFont(font)
        self.pushButton_atualizar.setObjectName("pushButton_atualizar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 770, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.plainTextEdit_id = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_id.setGeometry(QtCore.QRect(60, 770, 104, 25))
        self.plainTextEdit_id.setObjectName("plainTextEdit_id")
        self.pushButton_status = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.get_data())
        self.pushButton_status.setGeometry(QtCore.QRect(20, 812, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_status.setFont(font)
        self.pushButton_status.setObjectName("pushButton_status")
        self.pushButton_excluir = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.popup())
        self.pushButton_excluir.setGeometry(QtCore.QRect(260, 810, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_excluir.setFont(font)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 770, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        self.menuInserir = QtWidgets.QMenu(self.menubar)
        self.menuInserir.setObjectName("menuInserir")
        MainWindow.setMenuBar(self.menubar)
        self.actionInserir_entregas = QtWidgets.QAction(MainWindow)
        self.actionInserir_entregas.triggered.connect(lambda: self.interface_inserir_entregas())
        self.actionInserir_entregas.setObjectName("actionInserir_entregas")
        self.menuInserir.addAction(self.actionInserir_entregas)
        self.menubar.addAction(self.menuInserir.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Cliente"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Rua"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Bairro"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Telefone"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.pushButton_atualizar.setText(_translate("MainWindow", "Atualizar"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.pushButton_status.setText(_translate("MainWindow", "Alterar"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Selecionar Status"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Aguardando"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Em andamento"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Entregue"))
        self.menuInserir.setTitle(_translate("MainWindow", "Inserir"))
        self.actionInserir_entregas.setText(_translate("MainWindow", "Inserir Nova Entrega"))

    def populate_table(self):
        try:
            dados = get_all()
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(len(dados))
            for row, item in enumerate(dados):
                for column, data in enumerate(item):
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            print(f"Erro {e}")

    def get_data(self):
        id = self.plainTextEdit_id.toPlainText()
        status = self.comboBox.currentText()
        self.plainTextEdit_id.clear()
        self.comboBox.setCurrentIndex(0)

        return id, status
    
    def close():
        MainWindow.close()
    
    def popup(self):
        from popup_excluir_entrega import Ui_Form
        self.form = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self.form.show()

    def interface_inserir_entregas(self):
        from interface_insere_entrega import Ui_MainWindow
        self.form = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.form)
        self.form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
