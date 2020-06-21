"""
用例编写
新建一个test_开头（必须）的.py文件，如test_user_login.py
导入unittest
编写一个Test开头（必须）的类，并继承unittest.TestCase，做为测试类
在类中编写一个test_开头（必须）的方法，作为用例
"""
import unittest
import requests
import ast
from Lib.read_excel import *
from Lib.db_execute import *
from Lib.log import *


class TestBanner(unittest.TestCase): #类名必须以Test开头，必须继承unittest.TestCase类
    @classmethod
    def setUpClass(self):  # 整个测试类只执行一次
        #cls.data_list 同 self.data_list 都是该类的公共属性
        self.data_list1 = excel_to_list("E:\Python\python_unittest\TestData\CMS\\test_AddOrUpdateBlockInfo_data.xlsx","TestAddOrUpdateBlockInfo")  # 读取该测试类所有用例数据
        self.data_list2 = excel_to_list("E:\Python\python_unittest\TestData\CMS\\test_UpdateBlockInfoStatus_data.xlsx","TestUpdateBlockInfoStatus")  # 读取该测试类所有用例数据

        self.g = globals()
    #类中的方法，必须有一个额外的第一个参数self,self是类的一个实例
    def test_AddOrUpdateBlockInfo(self):
        case_data = get_test_data(self.data_list1, 'test_AddOrUpdateBlockInfo')  # 从数据列表中查找到该用例数据
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')  # 从字典中取数据，excel中的标题也必须是小写url
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        #从excel读取出来的数据是字符串格式的，转换成字典
        params = ast.literal_eval(data)
        ret = requests.post(url=url,params=params)  # 表单请求，数据转为字典格式
        # print(ret.url)  #请求链接
        # result是返回的实体信息
        result = ret.text
        data_dict = json.loads(result)
        #把data_dict添加到全局变量
        self.g["A"] = data_dict
        # print(data_dict)
        # print(self.data["A"])
    def test_UpdateBlockInfoStatus(self):
        case_data = get_test_data(self.data_list2, 'test_UpdateBlockInfoStatus')
        if not case_data:  # 有可能为None
            print("用例数据不存在")
        url = case_data.get('url')
        data = case_data.get('data')
        param = ast.literal_eval(data)
        data = param['filter']
        data_dict = ast.literal_eval(data)
        data_dict['Id'] = self.g["A"]
        # print(data_dict)
        value = str(data_dict)
        # print(value)
        params = {'filter':value,'token':'A01eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiJhYWRjNzM0My02NWJjLTQxOGUtODY1ZS1jN2MzMzIyZDBkYWQiLCJzZXNzaW9uX2lkIjoiMjQzOTM0MWNhMzI0NGNjMjg5YjU1N2U5OTUxOTJjNWZSRFMxIiwidG9rZW5faWQiOiIxNzE1NGJhZTYzODg0M2ExYjQ4NGFjY2MyZTg2NmIxMCIsInJlZnJlc2h0b2tlbl9pZCI6ImUwZTQ3NmI2ZjQ3YTQ5ZDNhN2Y0MzliNzk3NTJhZWE3IiwidmFsaWRhdGVfdHlwZSI6MSwic2NvcGUiOiIqIiwic291cmNlIjoiQSIsImNsaWVudF9pcCI6IjIyMy43OS4zNy44NCIsImV4cCI6MTU5MjU3Mjg1OS4wLCJjcmVhdGVfZnJvbSI6Im1haW4iLCJyZHNfZmxhZyI6MX0.G1cKGSKxi5J9kz0Ga1ktld3OtzVesQ9a4-DiGOzFkqA'}
        print(params)
        res = requests.post(url=url,params=params)
        print(res.text)
        log = Logger(level="debug").logger
        log.debug("测试用例：{}".format('test_AddOrUpdateBlockInfo'))
        log.debug("url：{}".format(url))
        log.debug("请求参数：{}".format(params))
        log.debug("期望结果：{}".format('1'))
        log.debug("实际结果：{}".format(res.text))
if __name__ == '__main__':
    unittest.main(verbosity=2)


"""
verbosity可以设置测试结果显示级别
0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共100个 失败20 成功80
1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
并且 你在命令行里加入不同的参数可以起到一样的效果
"""



