# import xlrd,os
# # os.path.join()函数连接两个或更多的路径名
# data_path = os.path.join('E:\Python\\test01\TestData\CMS', 'test_GetSolutionByWherePage_data.xlsx')
# print(data_path)
# wb = xlrd.open_workbook('test_GetSolutionByWherePage_data.xlsx')  # 打开excel
# sh = wb.sheet_by_name('TestGetSolutionByWherePage')  # 按工作簿名定位工作表
# print(sh.nrows)  # 有效数据行数
# print(sh.ncols)  # 有效数据列数
# print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
# print(sh.row_values(0))  # 输出第1行的所有值（列表格式）
#
# # 将数据和标题组装成字典，使数据更清晰
# print(dict(zip(sh.row_values(0), sh.row_values(1))))
#
# # 遍历excel,打印所有的数据
# for i in range(sh.nrows):
#     print(sh.row_values(i))

import xlrd
import os
"""
获取某条用例的数据，需要3个参数，excel数据文件名（data_file），工作簿名（sheet），用例名（case_name）
如果我们只封装一个函数，每次调用（每条用例）都要打开一次excel并遍历一次，这样效率比较低。
我们可以拆分成两个函数，一个函数excel_to_list(data_file, sheet)，一次获取一个工作表的所有数据，
另一个函数get_test_data(data_list, case_name)从所有数据中去查找到该条用例的数据
"""


def excel_to_list(data_file, sheet):
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            return case_data
            # 如果查询不到会返回None

if __name__ == '__main__':   # 测试一下自己的代码
    data_list = excel_to_list("E:\Python\python_unittest\TestData\CMS\\test_GetSolutionByWherePage_data.xlsx", "TestGetSolutionByWherePage")  # 读取excel，TestGetSolutionByWherePage工作簿的所有数据
    print(data_list)
    case_data = get_test_data(data_list, 'test_Get_SolutionByWherePage')  # 查找用例'test_Get_SolutionByWherePage'的数据
    print(case_data)