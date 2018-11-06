#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-11-29 16:32:33
# Project: ZenTalk_Download

from pyspider.libs.base_handler import *
import re
import time

class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.wdjurl = 'http://www.wandoujia.com/apps/com.asus.cnzentalk'
        self.baiduurl = 'http://shouji.baidu.com/software/11306355.html'
        self.yingyongbaourl = 'http://sj.qq.com/myapp/detail.htm?apkName=com.asus.cnzentalk'
        self.tool = Tool()
        self.time = self.tool.getCurrentIntTime()

    FILE_NAME = 'zentalk_download.txt'

    #@every(minutes=24 * 60) # 每天执行一次
    @every(minutes=1)  # 每1min执行一次
    def on_start(self):
        self.crawl(self.wdjurl, callback=self.index_wdjpage, fetch_type='js')
        self.crawl(self.baiduurl, callback=self.index_baidupage, fetch_type='js')
        self.crawl(self.yingyongbaourl, callback=self.index_yingyongbaopage, fetch_type='js')

    @config(age=60)  # 有效期1min
    @config(priority=3)
    def index_wdjpage(self, response):
        raw_download = response.doc('[itemprop="interactionCount"]').text()
        download = self.tool.getCount(raw_download)

        # write to file
        self.writeToFile(download, '豌豆荚')

    @config(age=60) # 有效期1min
    @config(priority=2)
    def index_baidupage(self, response):
        raw_download = response.doc('.yui3-g .download-num').text()
        download = self.tool.getCount(re.split(':', raw_download)[1])

        # write to file
        self.writeToFile(download, '百度手机助手')

    @config(age=60)  # 有效期1min
    @config(priority=1)
    def index_yingyongbaopage(self, response):
        raw_download = response.doc('.det-ins-num').text()[:-2]
        download = self.tool.getCount(raw_download)

        # write to file
        self.writeToFile(download, '应用宝' )

    def writeToFile(self, download, platform, append=True):
        if append :
            f = open(self.FILE_NAME, 'a')
            f.write(platform + ": " + str(download) + '\n')
        else:
            f = open(self.FILE_NAME, 'w')
            f.write("\n------ time: " + self.tool.getCurrentTime() + "," + str(self.tool.getCurrentIntTime()) + " ------------------\n")
            f.write(platform + ": " + str(download) + '\n')
        f.close()

# 工具类
class Tool:
    # 将超链接广告剔除
    removeADLink = re.compile('<div class="link_layer.*?</div>')
    # 去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeADLink, "", x)
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        # strip()将前后多余内容删除
        return x.strip()

    # it support convert string include unit to count
    # such as 6000,60.2万,1亿
    def getCount(self, x):
        x = self.replace(x)
        if (self.isFloat(x) or str.isdigit(str(x))):
            return x
        else:
            num = re.findall("\d+\.?\d*", x)[0]
            unit = re.sub(num, "", x)
            unit_number = 1
            if (unit == "万"):
                unit_number = 10000
            elif (unit == "亿"):
                unit_number =100000000
            return float(num) * unit_number

    def isFloat(self, number):
        try:
            num = float(number)
            return True
        except ValueError:
            return False

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 获取当前时间 unix 时间戳
    def getCurrentIntTime(self):
        return (int)(time.mktime(time.localtime(time.time())))