__author__ = 'arthur'

from PyQt5.QtCore import *

class WareHouse(QObject):
    def __init__(self):
        super(QObject, self).__init__()

    @pyqtSlot(result=str)
    def some_string(self):
        return "hahahaha"

    @pyqtSlot(int, result=int)
    def compute(self, value):
        return value * 2

    @pyqtSlot(result=QVariant)
    def some_list(self):
        return QVariant([1,2,3])