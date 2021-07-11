from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel
        )
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel
        )
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 826, 115))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.logs = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.logs.setEnabled(False)
        self.logs.setGeometry(QtCore.QRect(0, 0, 821, 211))
        self.logs.setStyleSheet("")
        self.logs.setObjectName("logs")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.searchCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.searchCheck.setObjectName("searchCheck")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.searchCheck
        )
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setObjectName("searchInput")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.searchInput
        )
        self.likeCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.likeCheck.setObjectName("likeCheck")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.likeCheck)
        self.commentCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.commentCheck.setObjectName("commentCheck")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.commentCheck
        )
        self.commentInput = QtWidgets.QLineEdit(self.centralwidget)
        self.commentInput.setObjectName("commentInput")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.commentInput
        )
        self.gridLayout.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet('font: 20pt "Consolas"; text-align: center; ')
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setAutoFillBackground(False)
        self.stopBtn.setStyleSheet("background: rgb(170, 0, 0); color: white;")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.logs.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.searchCheck.setText(_translate("MainWindow", "Search"))
        self.likeCheck.setText(_translate("MainWindow", "Like random posts"))
        self.commentCheck.setText(_translate("MainWindow", "Coment"))
        self.label_2.setText(_translate("MainWindow", "LINKEBOT"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Logs Output"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
