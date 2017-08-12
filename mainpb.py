# -*- coding: utf-8 -*-

import json
import traceback

from gzip import GzipFile
from base64 import b64decode, b64encode

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler, Application, asynchronous
from tornado.ioloop import IOLoop

from utils import Debug

from SyncMessage_pb2 import MessageLogin,MessageGenerateExistedClients,MessageLogout  #导入自定义的protobuf文件 这里要根据自己的项目自己生成
class ClientManager(object):
	#初始化
	def __init__(self):
		self.__clients = {} #玩家列表

	def add_client(self, name, client): #加入一个玩家
		self.__clients[name] = client 

	def remove_client(self, name):		#移除一个玩家
		if name in self.__clients:
			del self.__clients[name]

	def send_message_to_all_except_one(self, excepted_name, message): #发送消息给除了自己以外的所有人
		for k, v in self.__clients.items():
			if k != excepted_name:
				v.write_message(message, binary = True)

	def send_message_to_sender(self, excepted_name, message):  # 发送消息给发送者
		for k, v in self.__clients.items():
			if k == excepted_name:
				v.write_message(message, binary = True)

	def get_client_list(self):  #获取玩家列表
		return self.__clients.keys()

class MainHandler(WebSocketHandler):
	__client_manager = ClientManager()

	#def check_origin(self, origin):
	#	return True

	def open(self):
		Debug.log('get a new connection')
		self.set_nodelay(True)
		self.__name = ''

	def on_message(self, message):
		
		try:
			if message[1] == 0x00: # 0x00代表登陆（0x00是自己定义，可以随意修改成自己的标头）
				login = MessageLogin()  #初始化 登陆的protobuf  
				login.ParseFromString(bytes(message[4:])) #去掉前四位标头  去后面的protobuf数据  并反序列序列化
				self.__name = login.account
				MainHandler.__client_manager.add_client(self.__name, self) #将新登陆玩家 加入到 玩家列表中

				Debug.log('All Clienk ' + str(MainHandler.__client_manager.get_client_list()))

				resp = MessageGenerateExistedClients()  # 初始化 已注册的protobuf
				resp.clients.extend(MainHandler.__client_manager.get_client_list())  # 将已登陆的玩家列表 转成protobuf 数据
				self.write_message(b'\x00\x22\x00\x00' + resp.SerializeToString(), binary = True)	#将protobuf数据序列化 传给 新登陆的玩家（前端用词数据生成其玩家的模型）
				Debug.log('get login req from ' + self.__name)
			MainHandler.__client_manager.send_message_to_all_except_one(self.__name, message) #将自己的登陆信息 传给除自己以外的其他人
		except Exception as e:
			traceback.print_exc()

	def on_close(self): #玩家退出时执行的回调
		rep = MessageLogout()
		rep.account = self.__name
		MainHandler.__client_manager.send_message_to_all_except_one(self.__name, b'\x00\x01\x00\x00' + rep.SerializeToString())

		MainHandler.__client_manager.remove_client(self.__name)
		Debug.log('removed: ' + self.__name)
		Debug.log('remain clients: ' + str(MainHandler.__client_manager.get_client_list()))
		self.close()

if __name__ == '__main__':
	Application([
		('/', MainHandler),
	]).listen(10040) #绑定的服务器端口

	IOLoop.instance().start()
