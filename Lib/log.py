# from config import *
# import json
#
# def log_case_info(case_name, url, data, expect_res, res_text):
#     if isinstance(data,dict):
#         data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
#     logging.info("测试用例：{}".format(case_name))
#     logging.info("url：{}".format(url))
#     logging.info("请求参数：{}".format(data))
#     logging.info("期望结果：{}".format(expect_res))
#     logging.info("实际结果：{}".format(res_text))


import logging
from logging import handlers
import json
class Logger(object):
    # 日志级别关系映射
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    def __init__(self, filename="E:\Python\python_unittest\Log\Log.txt", level="debug", when="D", backupCount=3,
                 fmt='[%(asctime)s]~~%(levelname)s [%(funcName)s: %(filename)s, %(lineno)d]   %(message)s'):
        # 设置日志输出格式
        format_str = logging.Formatter(fmt)
        # 设置日志在控制台输出
        streamHandler = logging.StreamHandler()
        # 设置控制台中输出日志格式
        streamHandler.setFormatter(format_str)
        # 设置日志输出到文件（指定间隔时间自动生成文件的处理器  --按日生成）
        # filename：日志文件名，interval：时间间隔，when：间隔的时间单位， backupCount：备份文件个数，若超过这个数就会自动删除
        fileHandler = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backupCount,
                                                        encoding="utf-8")
        # 设置日志文件中的输出格式
        fileHandler.setFormatter(format_str)
        # 设置日志输出文件
        self.logger = logging.getLogger(filename)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 将输出对象添加到logger中
        self.logger.addHandler(streamHandler)
        self.logger.addHandler(fileHandler)


#
# if __name__ == '__main__':
#     log = Logger(level="debug").logger
#     log.debug("ceshi")



