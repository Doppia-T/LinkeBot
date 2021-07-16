import sys
from datetime import datetime as time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QWidget

from linkebot.core import LinkeBot
from linkebot.handlers import get_linkedin_creds, get_targets


class LinkebotView(QWidget):
    def setupUi(self, MainWindow, controller):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setObjectName("emailLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.emailLabel)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setObjectName("email")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.email)
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
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logs = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.logs.setReadOnly(True)
        self.logs.setStyleSheet("")
        self.logs.setObjectName("logs")
        self.gridLayout_2.addWidget(self.logs, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.searchCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.searchCheck.setObjectName("searchCheck")
        self.searchCheck.setChecked(True)
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

        self.retranslateUi(MainWindow, controller)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @staticmethod
    def popup(type="Info", msg=None):
        msg_ = QMessageBox()
        msg_.setWindowTitle(f"{type}")
        msg_.setText(msg)
        msg_.exec_()

    def retranslateUi(self, MainWindow, controller):
        _translate = QtCore.QCoreApplication.translate

        _email, _password = get_linkedin_creds()
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.email.setText(_email)
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.password.setText(_password)

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
        self.searchCheck.setText(_translate("MainWindow", "Search Targets"))
        targets = get_targets()
        self.searchInput.setText(", ".join(targets))

        self.likeCheck.setText(_translate("MainWindow", "Like random posts"))
        self.commentCheck.setText(_translate("MainWindow", "Coment"))
        self.label_2.setText(_translate("MainWindow", "LINKEBOT"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.startBtn.clicked.connect(controller.start_scraper)
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.stopBtn.clicked.connect(controller.stop_task)
        self.label.setText(_translate("MainWindow", "Logs Output"))


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self.threadActive = True

    def stop(self) -> None:
        self.threadActive = False
        # self.wait()

    def run(self, username, password, targets):

        while self.threadActive:

            with LinkeBot(username=username, password=password) as linkebot:
                self.log.emit(f"{time.now()}: Logging in to linkedin.")
                logged_in = linkebot.login()
                if not logged_in:
                    self.log.emit(f"{time.now()}: Error during login.")
                    self.finished.emit()

                self.log.emit(f"{time.now()}: Login succesfull.")

                self.log.emit(f"{time.now()}: Getting the targets.")

                targets = get_targets()

                for target in targets:
                    self.log.emit(f"{time.now()}: Scraping target {target}.")

                    linkebot.search(target)

                self.log.emit(f"{time.now()}: Operation completed!")
                self.finished.emit()
                self.stop()

    # self.finished.emit()


class Controller:
    def __init__(self):
        self.view = None
        self.thread = None
        self.worker = None

    def start(self, view):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.view = view()
        self.view.setupUi(MainWindow, self)
        MainWindow.show()
        sys.exit(app.exec_())

    def cleanup(self):
        self.view.progressBar.setProperty("value", 0)

        self.view.logs.clear()

    def start_scraper(self):
        self.view.startBtn.setEnabled(False)
        self.cleanup()
        self.run_task()

    def reportProgress(self, progress):
        self.view.progressBar.setProperty("value", progress)

    def reportLogs(self, log):
        self.view.logs.append(log)

    def validate(self):

        if not self.view.email.text():
            self.view.popup(msg="email is rquried", type="Error")
            return False
        if not self.view.password.text():
            self.view.popup(msg="Password is rquried", type="Error")
            return False
        return True

    def stop_task(self):
        if self.thread:
            self.worker.stop()
            # self.thread.deleteLater()

        # self.handle_scraoer(state="STOP")

    def run_task(self):
        is_valid = self.validate()
        if is_valid:
            self.thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(
                lambda: self.worker.run(
                    self.view.email.text(), self.view.password.text(), []
                )
            )
            self.thread.started.connect(lambda: self.view.startBtn.setEnabled(False))
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.progress.connect(self.reportProgress)
            self.worker.log.connect(self.reportLogs)

            self.thread.start()
            self.thread.finished.connect(lambda: self.view.startBtn.setEnabled(True))
            self.thread.finished.connect(
                lambda: self.view.logs.append("Linkebot job completed.")
            )


if __name__ == "__main__":
    c = Controller()
    c.start(LinkebotView)
