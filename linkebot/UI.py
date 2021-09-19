import sys
from datetime import datetime as time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget

from .core import LinkeBot
from .handlers import get_linkedin_creds, get_targets


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
        # self.stopBtn.setStyleSheet("background: rgb(0, 0, 0); color: white;")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 887, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetup_creds = QtWidgets.QAction(MainWindow)
        self.actionSetup_creds.setObjectName("actionSetup_creds")
        self.actionSetup_comments = QtWidgets.QAction(MainWindow)
        self.actionSetup_comments.setObjectName("actionSetup_comments")
        self.menuFile.addAction(self.actionSetup_creds)
        self.menuFile.addAction(self.actionSetup_comments)
        self.menubar.addAction(self.menuFile.menuAction())

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
        self.MainWindow = MainWindow

        self._email, self._password = get_linkedin_creds()
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.emailLabel.setText(_translate("MainWindow", "✉️ Email"))
        self.email.setText(self._email)
        self.passwordLabel.setText(_translate("MainWindow", "🔐 Password"))
        self.password.setText(self._password)

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
        self.stopBtn.clicked.connect(lambda x: controller.stop_task(initial=True))
        self.label.setText(_translate("MainWindow", "Logs Output"))
        self.menuFile.setTitle(_translate("MainWindow", "Settings"))
        self.actionSetup_creds.setText(_translate("MainWindow", "Load Config"))
        self.actionSetup_creds.triggered.connect(
            lambda: self.showDialog(controller, "creds Name", setting_type="CONFIG")
        )
        self.actionSetup_comments.setText(_translate("MainWindow", "Load Comments"))
        self.actionSetup_comments.triggered.connect(
            lambda: self.showDialog(controller, "comments", setting_type="COMMENTS")
        )

    def showDialog(self, controller, form_label=None, setting_type=None):
        fname = QFileDialog.getOpenFileName(
            self, "Open file", "c:\\", "Yaml files (*.yaml *.yml)"
        )
        if fname[0]:
            if setting_type == "CONFIG":
                self._email, self._password = get_linkedin_creds(config_path=fname[0])
                self.email.setText(self._email)
                self.password.setText(self._password)
            if setting_type == "COMMENTS":
                self.commentInput.setText(fname[0])


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    log = pyqtSignal(str)
    success = pyqtSignal(bool)
    result = pyqtSignal(object)


class Worker(QRunnable):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__()

        self.signals = WorkerSignals()
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.targets = kwargs["targets"]
        self.to_search = kwargs["to_search"]
        self.to_like = kwargs["to_like"]
        self.to_comment = kwargs["to_comment"]
        self.threadActive = True

        self.bot = LinkeBot(username=self.username, password=self.password)

    def stop(self) -> None:
        if self.threadActive:
            self.threadActive = False
            self.bot.terminate()
            self.signals.log.emit(f"{time.now()}: Stopping...")

    # @pyqtSlot()
    def run(self):
        try:
            self.signals.log.emit(f"{time.now()}: Starting....")
            linkebot = self.bot
            self.signals.progress.emit(3)
            self.signals.log.emit(f"{time.now()}: Logging in to linkedin.")
            logged_in = linkebot.login()
            if not logged_in:
                self.signals.log.emit(f"{time.now()}: Error during login.")
                self.signals.finished.emit()
                return
            self.signals.progress.emit(10)

            self.signals.log.emit(f"{time.now()}: Login succesfull.")

            if self.to_search:
                targets = self.targets
                self.signals.log.emit(f"{time.now()}: Getting the targets.")
                if not isinstance(targets, list):
                    targets = [targets]

                linkebot.search(targets, self.signals.progress)
                if self.to_like:
                    linkebot.like_random_posts(targets)
            self.signals.progress.emit(100)

            self.signals.log.emit(f"{time.now()}: Operation completed!")
            self.signals.finished.emit()
        except Exception:
            self.signals.log.emit(f"{time.now()}: Stopped!")
            self.signals.finished.emit()


class Controller:
    def __init__(self):
        self.view = None
        self.threadpool = None
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

    def enableButton(self):
        self.view.startBtn.setEnabled(True)

    def stop_task(self, initial=False):
        if self.threadpool:
            if not initial:
                self.view.startBtn.setEnabled(True)
            self.worker.stop()
            self.threadpool.clear()
            # self.event_stop.set()

    def run_task(self):
        is_valid = self.validate()
        if is_valid:
            self.threadpool = QThreadPool()
            self.threadpool.setMaxThreadCount(1)
            print(
                "Multithreading with maximum %d threads"
                % self.threadpool.maxThreadCount()
            )
            self.worker = Worker(
                username=self.view.email.text(),
                password=self.view.password.text(),
                targets=self.view.searchInput.text().split(","),
                to_search=self.view.searchCheck.isChecked(),
                to_like=self.view.likeCheck.isChecked(),
                to_comment=self.view.commentCheck.isChecked(),
            )

            self.worker.signals.progress.connect(self.reportProgress)
            self.worker.signals.log.connect(self.reportLogs)
            self.worker.signals.finished.connect(self.stop_task)
            self.threadpool.start(self.worker)


if __name__ == "__main__":
    c = Controller()
    c.start(LinkebotView)
