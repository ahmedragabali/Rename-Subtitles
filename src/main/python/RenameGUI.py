from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSignal, QThread, pyqtSlot, QCoreApplication
from PyQt5.uic import loadUi
from worker import Worker


class Rename(QMainWindow):
    add_text = pyqtSignal(str)

    def __init__(self, appctxt: ApplicationContext = None):
        QMainWindow.__init__(self)
        if appctxt:
            loadUi(appctxt.get_resource("rename.ui"), self)
        else:
            loadUi(r"src/main/resources/base/rename.ui", self)
        self.setWindowTitle("Rename Subtitles")
        self._translate = QCoreApplication.translate

        self.Logs_Box.appendPlainText(
            'Please enter the path of the season folder')

        self.worker = Worker(self, self.add_text)
        self.thread = QThread(self)
        self.worker.moveToThread(self.thread)
        self.thread.start()
        self.rename_button.clicked.connect(self.worker.rename_Button_Clicked)
        self.add_text.connect(self.display_changes)

    @pyqtSlot(str)
    def display_changes(self, text):
        self.Logs_Box.appendPlainText(text)

    @pyqtSlot()
    def on_browse_button_clicked(self):
        dirname = QFileDialog.getExistingDirectory(
            self, options=QFileDialog.ShowDirsOnly)
        self.path.setText(dirname)
