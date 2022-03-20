# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from main import encryption, decryption


client_path = Path(__file__)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(str((client_path / '../resources/logo.png').resolve())))
        MainWindow.resize(700, 550)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.enc_txt = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.enc_txt.setMaximumSize(QtCore.QSize(337, 16777215))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        self.enc_txt.setFont(font)
        self.enc_txt.setObjectName("enc_txt")
        self.horizontalLayout.addWidget(self.enc_txt)
        self.dec_txt = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.dec_txt.setMaximumSize(QtCore.QSize(336, 16777215))
        self.dec_txt.setObjectName("dec_txt")
        self.horizontalLayout.addWidget(self.dec_txt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet("color: rgb(78, 154, 6)")
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.status_line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.status_line.setStyleSheet("color: rgb(78, 154, 6);")
        self.status_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.status_line.setLineWidth(1)
        self.status_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.status_line.setObjectName("status_line")
        self.verticalLayout.addWidget(self.status_line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.enc_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.enc_btn.setStyleSheet("")
        self.enc_btn.setDefault(True)
        self.enc_btn.setObjectName("enc_btn")
        self.horizontalLayout_2.addWidget(self.enc_btn)
        self.dec_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dec_btn.setObjectName("dec_btn")
        self.horizontalLayout_2.addWidget(self.dec_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.info_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setItalic(True)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet("padding: 5px;\n"
"color: rgb(136, 138, 133);")
        self.info_label.setAlignment(QtCore.Qt.AlignCenter)
        self.info_label.setObjectName("info_label")
        self.verticalLayout.addWidget(self.info_label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Buttons backend
        self.enc_btn.clicked.connect(self.enc)
        self.dec_btn.clicked.connect(self.dec)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encriptación SAJI"))
        self.enc_txt.setPlaceholderText(_translate("MainWindow", "Escribe aquí un texto para encriptar o espera a que se muestre un texto decriptado..."))
        self.dec_txt.setPlaceholderText(_translate("MainWindow", "Escribe aquí un texto para decriptar o espera a que se muestre un texto encriptado..."))
        self.status_label.setText(_translate("MainWindow", ":) No hay ningún fallo. Te avisaremos si algo no funciona correctamente"))
        self.enc_btn.setText(_translate("MainWindow", "Encripta el texto"))
        self.dec_btn.setText(_translate("MainWindow", "Decripta el texto"))
        self.info_label.setText(_translate("MainWindow", "Programado y diseñado por ErtonDev [Python 3.6 / Qt / PyQt5]"))

    # My functions
    def enc(self):
        enc_content = encryption(self.enc_txt.toPlainText())
        if enc_content != "":
            # status
            self.change_status(False)
            # and calls functions from main
            encrypted = encryption(enc_content)
            # shows results in the opposite textedit
            self.dec_txt.setText(encrypted)
        else:
            # status
            self.change_status(True)
            # and does nothing

    def dec(self):
        dec_content = decryption(self.dec_txt.toPlainText())
        if dec_content != "":
            # status
            self.change_status(False)
            # and calls functions from main
            decrypted = decryption(dec_content)
            # shows results in the opposite textedit
            self.enc_txt.setText(decrypted)
        else:
            # status
            self.change_status(True)
            # and does nothing

    def change_status(self, status):
        # If something goes wrong or starts working after doing anything the status bar must tell the user about it
        if status is True:
            self.status_label.setText(":( Algo ha fallado. Asegurate de introducir texto en el espacio adecuado.")
            self.status_label.setStyleSheet("color: rgb(204, 0, 0);")
            self.status_line.setStyleSheet("color: rgb(204, 0, 0);")
        else:
            self.status_label.setText(":) No hay ningún fallo. Te avisaremos si algo no funciona correctamente.")
            self.status_label.setStyleSheet("color: rgb(78, 154, 6);")
            self.status_line.setStyleSheet("color: rgb(78, 154, 6);")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())