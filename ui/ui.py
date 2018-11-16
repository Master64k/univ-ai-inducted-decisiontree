# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created: Fri Nov 16 00:50:40 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 372)
        Dialog.setMinimumSize(QtCore.QSize(500, 372))
        Dialog.setMaximumSize(QtCore.QSize(500, 372))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/fa.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 111))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-image:url(\':/logo/logo.png\');\n"
"\n"
"}")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 120, 481, 232))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 16, 461, 81))
        self.label.setObjectName("label")
        self.credit_history = QtGui.QComboBox(self.groupBox)
        self.credit_history.setGeometry(QtCore.QRect(110, 109, 101, 22))
        self.credit_history.setObjectName("credit_history")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 112, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 143, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 172, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 202, 41, 16))
        self.label_5.setObjectName("label_5")
        self.debt = QtGui.QComboBox(self.groupBox)
        self.debt.setGeometry(QtCore.QRect(110, 140, 101, 22))
        self.debt.setObjectName("debt")
        self.guarantees = QtGui.QComboBox(self.groupBox)
        self.guarantees.setGeometry(QtCore.QRect(110, 170, 101, 22))
        self.guarantees.setObjectName("guarantees")
        self.earnings = QtGui.QComboBox(self.groupBox)
        self.earnings.setGeometry(QtCore.QRect(110, 200, 101, 22))
        self.earnings.setObjectName("earnings")
        self.simulate = QtGui.QPushButton(self.groupBox)
        self.simulate.setGeometry(QtCore.QRect(317, 200, 75, 23))
        self.simulate.setObjectName("simulate")
        self.quit = QtGui.QPushButton(self.groupBox)
        self.quit.setGeometry(QtCore.QRect(398, 200, 75, 23))
        self.quit.setObjectName("quit")
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(320, 110, 41, 16))
        self.label_7.setObjectName("label_7")
        self.risk_level = QtGui.QLabel(self.groupBox)
        self.risk_level.setGeometry(QtCore.QRect(360, 109, 61, 16))
        self.risk_level.setObjectName("risk_level")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 352, 501, 20))
        self.label_6.setStyleSheet("QLabel::#label6\n"
"{\n"
"    text-align:center;\n"
"}")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FinanciAnalyzer", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Análise", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Bem vindo ao FinanciAnalyzer.\n"
"\n"
"Selecione abaixo as informações relativas as condições financeiras do cliente e depois clique em\n"
"\'simular\' para obter o resultado.\n"
"\n"
"Todas as categorias de informação são obrigatórias.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Histórico de crédito:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Endividamento:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Garantias:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Renda:", None, QtGui.QApplication.UnicodeUTF8))
        self.simulate.setText(QtGui.QApplication.translate("Dialog", "Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.quit.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Risco:</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.risk_level.setText(QtGui.QApplication.translate("Dialog", "--", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"center\">© 2018 - Master64k</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import ui.img_rc
