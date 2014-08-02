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
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        web_view = QWebView(self)
        layout.addWidget(web_view)

        self.warehouse = WareHouse()
        web_view.page().mainFrame().addToJavaScriptWindowObject("warehouseObject", self.warehouse)

        pyDir = os.path.abspath(os.path.dirname(__file__))
        htmlUrl = QUrl.fromLocalFile(os.path.join(pyDir, "static/index.html"))
        web_view.setUrl(htmlUrl)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()