from PyQt5 import QtCore, QtGui, QtWidgets
from interface_admin import Ui_MainWindow
from controllers import delete_by_id, get_by_id
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_nome_cliente = QtWidgets.QLabel(Form)
        self.label_nome_cliente.setGeometry(QtCore.QRect(20, 90, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nome_cliente.setFont(font)
        self.label_nome_cliente.setObjectName("label_nome_cliente")
        self.label_endereco = QtWidgets.QLabel(Form)
        self.label_endereco.setGeometry(QtCore.QRect(20, 120, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_endereco.setFont(font)
        self.label_endereco.setObjectName("label_endereco")
        self.label_telefone = QtWidgets.QLabel(Form)
        self.label_telefone.setGeometry(QtCore.QRect(20, 150, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_telefone.setFont(font)
        self.label_telefone.setObjectName("label_telefone")
        self.label_status = QtWidgets.QLabel(Form)
        self.label_status.setGeometry(QtCore.QRect(20, 180, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")
        self.pushButton_sim = QtWidgets.QPushButton(Form, clicked = lambda: self.delete())
        self.pushButton_sim.setGeometry(QtCore.QRect(50, 240, 111, 31))
        self.pushButton_sim.setObjectName("pushButton_sim")
        self.pushButton_nao = QtWidgets.QPushButton(Form)
        self.pushButton_nao.setGeometry(QtCore.QRect(214, 240, 111, 31))
        self.pushButton_nao.setObjectName("pushButton_nao")
        ####inclui valores
        self.altera_label()
        ########
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Você tem certeza que quer excluir:"))
        self.label_nome_cliente.setText(_translate("Form", "Nome do Cliente"))
        self.label_endereco.setText(_translate("Form", "Endereço"))
        self.label_telefone.setText(_translate("Form", "Telefone"))
        self.label_status.setText(_translate("Form", "Status"))
        self.pushButton_sim.setText(_translate("Form", "Sim"))
        self.pushButton_nao.setText(_translate("Form", "Não"))

    def delete(self):
        id = Ui_MainWindow.get_id
        delete_by_id(id)

    def altera_label(self):
        response = Ui_MainWindow.get_id
        self.label_nome_cliente.setText(response)
        #self.label_endereco.setText(array[2])
        #self.label_status.setText(array[3])
        #self.label_telefone.setText(array[1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
