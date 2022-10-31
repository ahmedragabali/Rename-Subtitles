from fbs_runtime.application_context.PyQt5 import ApplicationContext
import sys
from RenameGUI import Rename

appctxt = ApplicationContext()
gui_main = Rename(appctxt)
gui_main.show()
sys.exit(appctxt.app.exec())