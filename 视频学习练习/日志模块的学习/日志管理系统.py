# 将本文开始的代码封装在一个类中
import logging
#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():

    def __init__(self, logname, loglevel, logger):

        format_dict = {
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        }
        ''' 指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中'''
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = list(format_dict)[int(loglevel)]
        print(formatter)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger

# 再通过以下方式调用，便是一个简单的日志系统了
logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
