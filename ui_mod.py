# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Med.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 754)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_5.addWidget(self.textEdit)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.groupBox_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox_2.setMinimum(10)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setSingleStep(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.spinBox.setMaximum(20)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.groupBox_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.groupBox_3)
        self.commandLinkButton.setEnabled(True)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout_2.addWidget(self.commandLinkButton)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.groupBox_3)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.verticalLayout_6.addLayout(self.formLayout_3)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtWidgets.QTableView(self.groupBox_6)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupBox_6)
        self.verticalLayout_6.addLayout(self.formLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MedSpider+"))
        MainWindow.setWindowIcon(QIcon('logo.ico'))
        self.groupBox.setTitle(_translate("MainWindow", "研究内容"))
        self.groupBox_2.setTitle(_translate("MainWindow", "AI模型设置"))
        self.checkBox_2.setText(_translate("MainWindow", "使用AI协助"))
        self.label.setText(_translate("MainWindow", "模型选择:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "GPT3.5Turbo"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Kimi"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GPT4"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Gemini"))
        self.comboBox.setItemText(4, _translate("MainWindow", "GLM4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "自定义模型"))
        self.label_2.setText(_translate("MainWindow", "模型代理:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "不使用代理"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Great API"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "自定义代理"))
        self.label_4.setText(_translate("MainWindow", "APIKey"))
        self.lineEdit_2.setText(_translate("MainWindow", "sk-********"))
        self.label_6.setText(_translate("MainWindow", "自定义模型："))
        self.lineEdit_4.setText(_translate("MainWindow", "gpt-3.5-turbo"))
        self.label_3.setText(_translate("MainWindow", "代理地址:"))
        self.lineEdit.setText(_translate("MainWindow", "https://api.surger.xyz/v1"))
        self.groupBox_4.setTitle(_translate("MainWindow", "搜索设置"))
        self.label_7.setText(_translate("MainWindow", "年内的文献"))
        self.label_8.setText(_translate("MainWindow", "保存文献数量"))
        self.pushButton.setText(_translate("MainWindow", "运行搜索"))
        self.pushButton_2.setText(_translate("MainWindow", "下载文献"))
        self.groupBox_3.setTitle(_translate("MainWindow", "网络设置"))
        self.checkBox.setText(_translate("MainWindow", "使用随机代理池"))
        self.label_5.setText(_translate("MainWindow", "配置个人代理:"))
        self.lineEdit_3.setText(_translate("MainWindow", "coming soon"))
        self.commandLinkButton.setText(_translate("MainWindow", "MedSpider Created By BecomingW"))
        self.groupBox_5.setTitle(_translate("MainWindow", "日志"))
        self.groupBox_6.setTitle(_translate("MainWindow", "表格预览"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
