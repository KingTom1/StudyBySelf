# -*- coding: utf-8 -*-

import os

import requests

from bs4 import BeautifulSoup

import random

from faker import Factory

import queue

import threading

fake = Factory.create()

luoo_site = 'http://www.luoo.net/music/'

luoo_site_mp3 = 'http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio%s/%s.mp3'

proxy_ips = [

    '47.98.200.254'  # 这里配置可用的代理IP

]

headers = {

    'Connection': 'keep-alive',

    'User-Agent': fake.user_agent()

}


def random_proxies():
    ip_index = random.randint(0, len(proxy_ips) - 1)

    res = {'http': proxy_ips[ip_index]}

    return res


def fix_characters(s):
    for c in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
        s = s.replace(c, '')

    return s


class LuooSpider(threading.Thread):

    def __init__(self, url, vols, queue=None):

        threading.Thread.__init__(self)

        print
        '[luoo spider]'

        print
        '=' * 20

        self.url = url

        self.queue = queue

        self.vol = '1'

        self.vols = vols

    def run(self):

        for vol in self.vols:
            self.spider(vol)

        print
        '\ncrawl end\n\n'

    def spider(self, vol):

        url = luoo_site + vol

        print
        'crawling: ' + url + '\n'

        res = requests.get(url, proxies=random_proxies())

        soup = BeautifulSoup(res.content, 'html.parser')

        title = soup.find('span', attrs={'class': 'vol-title'}).text

        cover = soup.find('img', attrs={'class': 'vol-cover'})['src']

        desc = soup.find('div', attrs={'class': 'vol-desc'})

        track_names = soup.find_all('a', attrs={'class': 'trackname'})

        track_count = len(track_names)

        tracks = []

        for track in track_names:
            _id = str(int(track.text[:2])) if (int(vol) < 12) else track.text[:2]  # 12期前的音乐编号1~9是1位（如：1~9），之后的都是2位 1~9会在左边垫0（如：01~09）
            _name = fix_characters(track.text[4:])
            tracks.append({'id': _id, 'name': _name})
        phases = {

            'phase': vol,  # 期刊编号

            'title': title,  # 期刊标题

            'cover': cover,  # 期刊封面

            'desc': desc,  # 期刊描述

            'track_count': track_count,  # 节目数

            'tracks': tracks  # 节目清单(节目编号，节目名称)

        }

        self.queue.put(phases)


class LuooDownloader(threading.Thread):

    def __init__(self, url, dist, queue=None):

        threading.Thread.__init__(self)

        self.url = url

        self.queue = queue

        self.dist = dist

        self.__counter = 0

    def run(self):

        while True:

            if self.queue.get <= 0:

                pass

            else:

                phases = self.queue.get()

                self.download(phases)

    def download(self, phases):

        for track in phases['tracks']:

            file_url = self.url % (phases['phase'], track['id'])

            local_file_dict = '%s/%s' % (self.dist, phases['phase'])

            if not os.path.exists(local_file_dict):
                os.makedirs(local_file_dict)

            local_file = '%s/%s.%s.mp3' % (local_file_dict, track['id'], track['name'])

            if not os.path.isfile(local_file):

                print
                'downloading: ' + track['name']

                res = requests.get(file_url, proxies=random_proxies(), headers=headers)

                with open(local_file, 'wb') as f:

                    f.write(res.content)

                    f.close()

                print
                'done.\n'

            else:

                print
                'break: ' + track['name']


if __name__ == '__main__':

    spider_queue = queue.deque()
    luoo = LuooSpider(luoo_site, vols=['680', '721', '725', '720'], queue=spider_queue)

    luoo.setDaemon(True)

    luoo.start()

    downloader_count = 5

    for i in range(downloader_count):
        luoo_download = LuooDownloader(luoo_site_mp3, 'D:/luoo', queue=spider_queue)

        luoo_download.setDaemon(True)

        luoo_download.start()