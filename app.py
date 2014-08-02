__author__ = 'arthur'

import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *

from warehouse import WareHouse

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(300, 300, 1024, 800)
        self.setWindowTitle('WAREHOUSE')

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self. web_view = QWebView(self)
        layout.addWidget(self.web_view)

        pyDir = os.path.abspath(os.path.dirname(__file__))
        htmlUrl = QUrl.fromLocalFile(os.path.join(pyDir, "static/index.html"))
        self.web_view.setUrl(htmlUrl)

        self.web_view.urlChanged.connect(self.urlChanged)

    def urlChanged(self):
        self.warehouse = WareHouse()
        self.web_view.page().mainFrame().addToJavaScriptWindowObject("warehouseObject", self.warehouse)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
    