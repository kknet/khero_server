# coding: utf-8

from os import *
from Log import *
from Net import *

class Server:
    def __init__(self):
        self._ip = "192.168.0.102"
        self._port = 8888
        self._timeout = 10
        self._net = Net(self._ip, self._port, self._timeout)

    def run(self):
        self._net.run()

if __name__ == "__main__":
    pidfile = "../proc/pid"
    if path.exists(pidfile):
        Log().e("pid文件已经存在，请检查程序是否已经运行")
        
    else:
        f = file(pidfile, 'w')
        f.write(str(getpid()))
        f.close()

        server = Server()
        server.run()

        if path.exists(pidfile):
            remove(pidfile)


