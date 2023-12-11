from PyQt5 import QtCore, QtGui, QtWidgets
from controllers import post
from models import Entrega

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 260, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 130, 461, 25))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(260, 180, 461, 25))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(260, 260, 251, 25))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(260, 220, 461, 25))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.get_data())
        self.pushButton.setGeometry(QtCore.QRect(260, 340, 281, 101))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nome do Cliente"))
        self.label_2.setText(_translate("MainWindow", "Rua"))
        self.label_3.setText(_translate("MainWindow", "Bairro"))
        self.label_4.setText(_translate("MainWindow", "Telefone"))
        self.pushButton.setText(_translate("MainWindow", "Enviar Entrega"))

    def get_data(self):
        try:
            entrega_i = Entrega()  # Criar uma nova instância de Entrega
            entrega_i.nome_cliente = self.plainTextEdit.toPlainText()
            entrega_i.logradouro = self.plainTextEdit_2.toPlainText()
            entrega_i.bairro = self.plainTextEdit_4.toPlainText()
            entrega_i.telefone = self.plainTextEdit_3.toPlainText()
            post(entrega_i)  # Chamar a função post com a instância de Entrega como argumento
            self.plainTextEdit.clear()
            self.plainTextEdit_2.clear()
            self.plainTextEdit_3.clear()
            self.plainTextEdit_4.clear()
        except Exception as e:
            print(f"Erro ao processar os dados: {e}")
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
