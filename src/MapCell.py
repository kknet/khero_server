# coding: utf-8

from Material import *
from ResourceContainer import *
from Log import *
from Singleton import *


@singleton
class LandManager:
    def __init__(self):
        self._landWidth = 100
        self._landHeight = 100
        self._landList = []
        for i in range(self._landWidth):
            tmp = []
            for j in range(self._landHeight):
                tmp.append(PlainMapCell())
            self._landList.append(tmp)

    def getLandByXY(self, x, y):
        if x >= 0 and x < len(self._landList) and y >= 0 and y < len(self._landList[x]):
            return self._landList[x][y]
        else:
            return None


class MapCell:
    # 地图块类型
    MAP_TYPE_PLAIN = 1		#平原
    MAP_TYPE_HILL = 2		#丘陵
    MAP_TYPE_MOUNTAIN = 3	#山脉
    MAP_TYPE_BASIN = 4		#盆地

    
    def __init__(self, mapType):
        self._x = 0
        self._y = 0
        self._mapType = mapType
        self._owner = None
        self._price = 0
        self._canSell = True
   
    def getOwner(self):
        return _owner

 
    def setPrice(self, price):
        if price >= 0:
            self._price = price

    def getPrice(self):
        return self._price

    def canSell(self):
        return self._canSell

    def onSale(self):
        self._canSell = True

    def stopSelling(self):
        self._canSell = False


    def sellTo(self, owner):
        if self._canSell is False:
            return False
        if owner.consumeMoney(self._price) is True:
            self._owner = owner
            self._owner.obtainLand(self)
            return True
        else:
            return False
            

class PlainMapCell(MapCell):
    def __init__(self):
        MapCell.__init__(self, MapCell.MAP_TYPE_PLAIN)

class HillMapCell(MapCell):
    def __init__(self):
        MapCell.__init__(self, MapCell.MAP_TYPE_HILL)

class MountainMapCell(MapCell):
    def __init__(self):
        MapCell.__init__(self, MapCell.MAP_TYPE_MOUNTAIN)

class BasinMapCell(MapCell):
    def __init__(self):
        MapCell.__init__(self, MapCell.MAP_TYPE_BASIN)



