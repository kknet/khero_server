#coding:utf-8

from Timer import *

import time
import sys

class TS(TimerTask):
    def __init__(self):
        self._time = time.time()
    def onTimer(self):
        self._ctime = time.time()
        dt = self._ctime - self._time
        print "定时器触发,用时",dt

def run(scale):
    s = 0
    os = -1
    t1 = time.time()
    while True:
        t2 = time.time()
        dt = (t2 - t1) * scale
        t1 = t2
        s += dt
        if int(s) is not os:
            os = int(s)
            print "Tick " + str(os) + "s"
        TM().step(dt)


def init(second):
    ts = TS()
    t = Timer(second, ts)
    t.start()


if __name__ == '__main__':
    s = sys.argv[1]
    t = sys.argv[2]
    scale = int(s)
    init(float(t))
    run(scale)

