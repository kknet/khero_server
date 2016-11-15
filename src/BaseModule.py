# coding: utf-8

from socket import *
from select import *
from MsgHandler import *
from ctypes import *
import struct

import sys
sys.path.append('../src/msg')
from message_pb2 import *

from Log import *


class BaseModule(Module):
    def procMsg(self, user_data):
        if user_data["msg_id"] == Login_Request:
            self.onLoginRequest(user_data)

    # 响应登录消息
    def onLoginRequest(self, user_data):
        req = Request()
        req.ParseFromString(user_data["msg_data"])
        if req.HasField('login'):
            Log().d('OnLoginRequest(' + req.login.username +"," + req.login.password + ")")
            res = Response()
            res.result = True
            res.last_response = True
            res.login.token = 1234
            res_str = res.SerializeToString()
            self.sendMsg(user_data, Login_Response, res_str)


    # 发送串行化后的数据
    def sendMsg(self, user_data, msgId, serializeData):
        data_len = len(serializeData) + 8
        buf = create_string_buffer(8)
        struct.pack_into('!I', buf, 0, msgId)
        struct.pack_into('!I', buf, 4, data_len)
        user_data["wbuf"] += (buf.raw + serializeData)
        user_data["epl"].modify(user_data["fd"], EPOLLOUT)
        
        
