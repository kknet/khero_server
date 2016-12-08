#coding: utf-8

from Material import *
from ResourceContainer import *
from Log import *
from Singleton import *
from Timer import *

@singleton
class RoleManager:
    def __init__(self):
        self._roleList = {}

    def getRole(self, roleId):
        if self._roleList.contains(roleId):
            return self._roleList[roleId]

    def addRole(self, role):
        if self._roleList.contains(role.roleId):
            return False
        else:
            self._roleList[role.roleId] = role
            return True
    def delRole(self, roleId):
        if self._roleList.contains(roleId):
            self._roleList.delitem(roleId)




class Role:
    MALE = 1
    FEMALE = 2
    MAX_LOST_HEART_BEAT = 3
    HEART_BEAT_TIME = 60
    def __init__(self):
        self._age = 0
        self._gender = self.__class__.MALE
        self._resourceContainer = ResourceContainer()
        self._money = 0
        self._landList = []
        self._online = False
        self._lostHeartBeatCount = 0
        self._userData = None


    class HeartBeatTask(TimerTask):
        def __init__(self, outClass):
            self._outClass = outClass
       
        def onTimer(self):
            self._outClass._lostHeartBeatCount ++
            if self._outClass._lostHeatBeatCount < Role.MAX_LOST_HEART_BEAT:
                self._outClass.heartBeat()
            else:
                RoleManager().kickRole(self._outClass)

    def heartBeat(self):
        heartBeatTask = self.HeartBeatTask()
        timer = Timer(Role.HEART_BEAT_TIME, heartBeatTask)
        timer.start()        


    def getAge(self):
        return self._age

    def setAge(self, age):
        if age > 0:
            self._age = age


    def getGender(self):
        return self._gender

    def setGender(self, gender):
        if gender is self.__class__.MALE:
            self._gender = self.__class__.MALE
        elif gender is self.__class__.FEMALE:
            self._gender = self.__class__.FEMALE
        else:
            Log().e("性别设置错误")

    def getResContainer(self):
        return self._resourceContainer

    def setMoney(self, money):
        self._money = money

    def getMoney(self):
        return self._money

    def consumeMoney(self, money):
        if money <= self._money:
            self._money -= money
            return True
        else:
            return False

    def earnMoney(self, money):
        if money >= 0:
            self._money += money

    def obtainLand(self, mapcell):
        self._landList.append(mapcell)

    def setUserData(self, userdata):
        self._userData = userdata
