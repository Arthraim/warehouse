__author__ = 'arthur'

from PyQt5.QtCore import *

from models import *

class WareHouse(QObject):
    def __init__(self):
        super(QObject, self).__init__()

    @pyqtSlot(result=QVariant)
    def all_cargo(self):
        return QVariant(map(lambda x: x.javascriptify(), Cargo.select()))