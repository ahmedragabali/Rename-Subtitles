from PyQt5.QtCore import QObject, pyqtSlot
from os import listdir, rename
from os.path import join
import re


class Worker(QObject):
    def __init__(self, qt, signal_to_emit, parent=None):
        super().__init__(parent)
        self.signal_to_emit = signal_to_emit
        self.qt = qt

    def AppendToLogs(self, txt):
        self.signal_to_emit.emit(txt)

    @pyqtSlot()
    def rename_Button_Clicked(self):
        self.AppendToLogs(
            "---------------------------------------------------------------")
        self.qt.path.setEnabled(False)
        self.qt.rename_button.setEnabled(False)
        try:
            mypath = self.qt.path.text()
            files = listdir(mypath)

            SRTs = [s for s in files if s.find('srt') > 0]
            Videos = [m for m in files if (
                m.find('.mp4') > 0 or m.find('.m4v') > 0
                or m.find('.mkv') > 0)]
            self.AppendToLogs(
                f"Found {len(Videos)} Video file and {len(SRTs)} SRT file")
            if len(SRTs) == len(Videos):
                for SRT in SRTs:
                    old_name = join(mypath, SRT)
                    temp = re.compile(r'S[0-9]{2}E[0-9]{2}')

                    res = temp.search(SRT.upper())
                    if res is None:
                        self.AppendToLogs("Error in SRT: {}".format(SRT))
                        continue
                    for Video in Videos:
                        if Video.upper().find(res.group(0)) > 0:
                            found = Video
                            break
                    new_srt = found[0:found.rfind('.m')] + '.srt'
                    new_name = join(mypath, new_srt)
                    rename(old_name, new_name)
                    self.AppendToLogs(res.group(0) + " Done.")
                self.AppendToLogs("All Done.")
            else:
                self.AppendToLogs('Number of files are different')
        except Exception as e:
            self.AppendToLogs(str(e), exc_info=True)

        self.qt.path.setEnabled(True)
        self.qt.rename_button.setEnabled(True)
