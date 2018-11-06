import logging
#
# logging.basicConfig(level=logging.DEBUG)
# logging.info('hello!')

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

# critical > error > warning > info > debug,notset日志级别
handler=logging.FileHandler("TNLOG-error.log")

def log(level):
    logger = logging.getLogger()
    #不能重复创建handler,否则会重复写入同样的记录?
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical\n")

if __name__ == "__main__":
    log(logging.NOTSET)
    log(logging.DEBUG)
    log(logging.INFO)
    log(logging.WARNING)
    log(logging.ERROR)
    log(logging.CRITICAL)