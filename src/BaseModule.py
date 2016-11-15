#coding: utf-8

from socket import *
from select import *
from MsgHandler import *
from ctypes import *
import struct

import sys
sys.path.append('../src/msg')
from message_pb2 import *

class BaseModule(Module):
    def procMsg(self, msg):
        print msg["data"]
        if msg["id"] == Login_Request:
            self.onLoginRequest(msg)

    # 响应登录消息
    def onLoginRequest(self, msg):
        req = Request()
        req.ParseFromString(msg["data"])
        if req.HasField('login'):
            Log().d("用户登录(用户名：" + req.login.username + "  密码：" + req.login.password+")")
            res = Response()
            res.result = True
            res.last_response = True
            res.login.token = "1234"
            res_str = res.SerializeToString()
            self.sendMsg(msg, Msg.Login_Response, res_str)


    # 发送串行化后的数据
    def sendMsg(self, msg, msgId, serializeData):
        data_len = len(serializeData) + 8
        buf = create_string_buffer(8)
        struct.pack_into('!I', buf, 0, msgId)
        struct.pack_into('!I', buf, 4, data_len)
        msg["wbuf"] += (buf.raw + serializeData)
        msg["epl"].modify(msg["fd"], EPOLLOUT)
        
        
