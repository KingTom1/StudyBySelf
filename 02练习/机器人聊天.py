# coding:utf-8
from time import sleep
import requests
s = input("请主人输入话题：")
while True:
	resp=requests.post("http://www.tuling123.com/openapi/api",data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
	resp = resp.json()
	sleep(1)
	print('小鱼：', resp['text'])
	s = resp['text']
	resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
	# resp = requests.post("http://www.tuling123.com/openapi/api",data={"key": "4fede3c4384846b9a7d0456a5e1e2943", "info": s, })
	resp.encoding = 'utf8'
	resp = resp.json()
	sleep(1)
	print('菲菲：', resp['content'])
	# print('菲菲：', resp['text'])
