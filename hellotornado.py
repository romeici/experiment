#!/usr/bin/env python3  
# -*- coding:utf-8 -*-  
#  
#   Authhor :Eric.Tang  
#   Email   :jeepxiaozi66@gmail.com  
#   Date    :13/06/02 22:17:57  
#   Desc    :hello,world of tornado  
#  
  
import tornado.ioloop  
import tornado.web  
  
class MainHandler(tornado.web.RequestHandler):  
	def get(self):  
		self.write("Hello, world")  
  
application = tornado.web.Application([  
	(r"/",MainHandler),  
])  
  
if __name__=="__main__":  
	application.listen(8888)  
	tornado.ioloop.IOLoop.instance().start()  