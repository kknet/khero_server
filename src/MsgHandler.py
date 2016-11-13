#coding: utf-8

from Singleton import *


class Module:
    def __init__(self):
        self.moduleId = 0

    def procMsg(msg):
        return 


@singleton
class MsgHandler:
    def __init__(self):
	self.modules = {0 : Module()}

    def registerModule(module):
        self.modules[module.moduleId] = module

    def handleMsg(self, msg):
        module = self.modules[msg.id & 0xFFFF0000]
        if module is not None:
            module.procMsg(msg)
