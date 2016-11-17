#coding: utf-8


import time

from Singleton import *
from Log import *
from abc import *


@singleton
class TM:
    def __init__(self):
        self._runningTimers = []
        self._unusedTimers = []
        self._cancelTimers = []

    def step(self, delta):
        # 移除代取消的定时器
        for timer in self._cancelTimers:
            self._cancelTimers.remove(timer)
        # 正在运行中的定时器
        for timer in self._runningTimers:
            timer.step(delta)
        # 完成不再使用的定时器
        for timer in self._unusedTimers:
            self._unusedTimers.remove(timer)

    def addTimer(self, timer):
        if timer._leftTime < 0:
            return
        if timer._timerTask is None:
            return
        if timer._isComplete is True:
            return
        self._runningTimers.append(timer)


    def delTimer(self, timer):
        self._unusedTimers.append(timer)

    def cancelTimer(self, timer):
        self._cancelTimers.append(timer)

    def clearTimer(self):
        self._runningTimers = []


# 定时器任务抽象类
class TimerTask(object):
    __metaclass__ = ABCMeta

    # 定时器回调函数
    @abstractmethod
    def onTimer(self):
        pass


# 定时器类
class Timer:
    # 构造时传入时间和回调类
    def __init__(self, leftTime = 0, timerTask = None):
        self._leftTime = leftTime
        self._timerTask = timerTask
        self._isPause = False
        self._isComplete = False

    def start(self):
        TM().addTimer(self)

    def step(self, delta):
        if self._isPause == False:
            self._leftTime -= delta
            if self._leftTime <= 0:
                if self._timerTask is not None and self._isComplete is False:
                    self._timerTask.onTimer()
                self._isComplete = True
		TM().delTimer(self)
     
    def pause(self):
        if self._isPause == False:
            self._isPause = True

    def resume(self):
        if self._isPause == True:
            self._isPause = False

    def cancel(self):
        if self._isComplete is False:
            TM().cancelTimer(self)

    def isComplete(self):
        return self._isComplete

