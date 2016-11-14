#coding: utf-8

from MsgHandler import *
from ctypes import *
import struct

class BaseModule(Module):
    def procMsg(self, msg):
        print msg["data"]
        data_len = len('hello' + 4)
	buf = create_string_buffer(4)
        struct.pack_into('!I', buf, 0, data_len)
        msg["wbuf"] = buf + "hello"

        pass
        
         
