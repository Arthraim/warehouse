__author__ = 'arthur'

from PyQt5.QtCore import *

from models import *

class WareHouse(QObject):
    def __init__(self):
        super(QObject, self).__init__()

    @pyqtSlot(result=QVariant)
    def all_cargo(self):
        l = list()
        for cargo in Cargo.select():
            print cargo.name
            l.append(cargo.javascriptify())
            print cargo.javascriptify()
        return QVariant(l)