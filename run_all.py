import unittest
from Lib.HTMLTestRunnerCN import HTMLTestRunner
from run import *

#suite 可以各种组合定义
# suite = unittest.defaultTestLoader.discover("E:\Python\python_unittest\Test\CMS")#用例地址

list1 = makesuite_by_testlist('E:\Python\python_unittest\Test\CMS\\testlist.txt')
print(list1)
run(list1)


