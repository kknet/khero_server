#coding: utf-8
from Singleton import *
from Role import *


@singleton
class GameDB:
    SAVE_NUM_PER_SECOND = 1
    def __init__(self):
        self._connected = False
        self._roleListToSave = []
        self._landListToSave = []
        self._time = 0


    def conn(self):
        pass


    def disconn(self):
        pass


    def execute(self, sql):
        pass


    def getRoleListByUserID(self, userId):
        pass

    def getRoleInfo(self, roleId):
        pass


    def setRoleInfo(self, role):
        pass

    def updateDBRoleInfo(self, role):
        pass

    def getLandInfo(self, landId):
        pass

    def updateDBLandInfo(self, land):
        

    def setLandInfo(self, land):
        pass


    def step(self, delta):
        self._time += delta
        num = int(self._time * SAVE_NUM_PER_SECOND)
        self._time -= num * 1.0 /SAVE_NUM_PER_SECOND
        while num > 0:
            if len(self._roleListToSave) > 0:
                role = self._roleListToSave.pop()
                self.updateDBRoleInfo(role)
            if len(self._landListToSave) > 0:
                land = self._landListToSave.pop()
                self.updateDBLandInfo(land)



