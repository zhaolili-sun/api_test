"""
Log Level:
CRITICAL: 用于输出严重错误信息
ERROR: 用于输出错误信息
WARNING: 用于输出警示信息
INFO: 用于输出一些提升信息
DEBUG: 用于输出一些调试信息
优先级 CRITICAL > ERROR > WARNING > INFO > DEBUG
指定level = logging.DEBUG所有等级大于等于DEBUG的信息都会输出
若指定level = logging.ERROR WARNING,INFO,DEBUG小于设置级别的信息不会输出


日志格式:
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

Filename：指定路径的文件。这里使用了+—name—+是将log命名为当前py的文件名
Format：设置log的显示格式（即在文档中看到的格式）。分别是时间+当前文件名+log输出级别+输出的信息
Level：输出的log级别，优先级比设置的级别低的将不会被输出保存到log文档中
Filemode： log打开模式
•a：代表每次运行程序都继续写log。即不覆盖之前保存的log信息。
•w：代表每次运行程序都重新写log。即覆盖之前保存的log信息

"""
import logging
import os

#log日志配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s]~~%(levelname)s  [%(funcName)s: %(filename)s, %(lineno)d]   %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename='E:\Python\python_unittest\Log\log.txt',  # 日志输出文件
                    filemode='a')  # 追加模式

#项目路径
# prj_path = os.path.dirname(os.path.abspath('E:\Python\python and unittest\Lib'))  # 当前文件的绝对路径的上一级，__file__指当前文件
# # data_path = prj_path  # 数据目录，暂时在项目目录下
# test_path = prj_path  # 用例目录，暂时在项目目录下
# #
# log_file = os.path.join(prj_path, 'log.txt')  # 也可以每天生成新的日志文件
# report_file = os.path.join(prj_path, 'report.html')  # 也可以每次生成新的报告

testlist_file = os.path.join('E:\Python\python_unittest\Test\CMS','testlist.txt')
# 数据库配置cn环境
CMS_db_host = '40.125.165.3,16878,1433'   # 带端口sql server
CMS_db_user = 'sa'
CMS_db_passwd = 'Teld@teld.cn'
CMS_db = 'TELDCMS'


if __name__ == '__main__':
    print(testlist_file)