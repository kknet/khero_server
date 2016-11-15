#coding: utf-8

from message_pb2 import *
from socket import *
from ctypes import *
import struct

sock = socket(AF_INET, SOCK_STREAM, 0)
sock.connect(("192.168.0.102", 8888))

req = Request()
req.login.username = "kongyatong"
req.login.password = "password"
req_data = req.SerializeToString()
datalen = len(req_data) + 8
print datalen
msgid = Login_Request
buf = create_string_buffer(8)
print msgid
struct.pack_into('!I', buf, 0, msgid)
struct.pack_into('!I', buf, 4, datalen)

send_data = buf.raw + req_data
sock.send(send_data)

data = sock.recv(1024)
print data
