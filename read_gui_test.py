import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.gui_readtxt import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # sys.stdout = EmittingStr(textWritten=self.outputWritten)
        # sys.stderr = EmittingStr(textWritten=self.outputWritten)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = MyWindow()
    mainForm.show()
    sys.exit(app.exec_())
