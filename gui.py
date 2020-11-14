from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,QPrintPreviewDialog
from PyQt5.QtGui import QFont,QTextDocument,QTextCursor

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.initUi(self)

    def initUi(self, MainPlat):
        MainPlat.setObjectName("MainWindow")
        MainPlat.resize(750, 450)
        self.centralWidget = QtWidgets.QWidget(MainPlat)
        self.centralWidget.setObjectName("centralWidget")
        self.setWindowTitle("地铁网络仿真平台")

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        
        # 文本框
        self.label = QLabel()
        self.label.setFont(QFont("宋体", 12, QFont.Bold))
        self.label.setText("待显示文本")
        self.setCentralWidget(self.label)
        # 打开文件 button
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("打开")
        MainPlat.setCentralWidget(self.centralWidget)
        QtCore.QMetaObject.connectSlotsByName(MainPlat)

        self.pushButton.clicked.connect(self.openfile)
        self.printAction2 = QAction(self.tr("打印有预留"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '')

    def on_printAction2_triggered(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertText(self.label.text())
        document.print(printer)

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", 'You typed:' + textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        """打印完毕之后清空文本框"""
        self.textbox.setText('')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
