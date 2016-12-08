#coding:utf-8

from Material import *

class ResourceContainer:
    def __init__(self):
        self._stone = Stone()
        self._wood = Wood()
        self._coal = Coal()
        self._iron = Iron()

    def getStone(self):
        return self._stone

    def getWood(self):
        return self._wood

    def getCoal(self):
        return self._coal

    def getIron(self):
        return self._iron

