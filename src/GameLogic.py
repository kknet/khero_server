# coding: utf-8

from Singleton import *
from Log import *
from MapCell import *

@singleton
class GameLogic:
    def __init__(self):
        self._landManager = LandManager()
        self._roleManager = RoleManager()

    def step(self, delta):
        pass

