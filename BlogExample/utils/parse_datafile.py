#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         parse_datafile.py
# Author:       ls
# Date:         2020/09/16 14:28
#-------------------------------------------------------------------------------

import requests
import re
from utils.get_username import *
from conf.data_conf import *
from utils.operator_Excel import OPExcel
from utils.Log import *

global_vars={}
patt01=re.compile(r"\${(\w+)}")
patt02=re.compile(r"%{(\w+)}")
pattm5=re.compile(r"\$md5{(\w+)}")

my_log = MyLog()
log = my_log.get_logger()
# total_test_case = 0#记录总共测试用例数
# success_test_case = 0#记录成功用例数
# failed_test_case = 0#记录失败用例数

# # 统计耗时
# def count_time(func):
#     def inner(*args,**kwargs):
#         global funcall_cost
#         now = time.time()
#         data=func(*args,**kwargs)
#         funcall_cost = time.time()-now
#         return data
#     return inner
#
#
# #统计执行结果
# def count_excute_res(func):
#     def inner(*args,**kwargs):
#         global failed_test_case
#         global success_test_case
#         data=""
#         try:
#             data=func(*args,**kwargs)
#         except AssertionError:
#             failed_test_case += 1
#         except:
#             failed_test_case += 1
#         else:
#             success_test_case += 1
#         return data
#     return inner


# 解析请求所需的参数，一行参数以元组形式展示，所有的参数保存到列表中
def get_testdata(filepath):
    print(filepath)

    with open(filepath)as f:
        # 拿到文件中的所有测试数据，list中每一个数据以\n结尾
        data=f.readlines()
    return data
# def get_testXXX():
#     # test_cases=list(map(lambda x:x.strip(),data))
#     test_results=[]
#     for i  in data:
#         #此处对应文件中每行数据的接口名、参数、请求方法、断言属性，
#         name, value, method, assert_value, extract_rule = i.strip().split('||')
#         # print(name, value, method, assert_value, extract_rule)
#         # 提取url
#         url = parse_name(name)
#         # 提取参数
#         data = parse_value(value)
#         print(url, data)
#
#
#         test_results.append((url,data,method,assert_value,extract_rule))
#
#
#     return test_results

# 发送接口请求
def send_request(method,url,data=None):
    res=None
    if method=='get':
        if data is None:
            res = requests.get(url + data)
            return res.text
        res=requests.get(url+data)
    elif method =='post':
        res=requests.post(url,data)
    elif method =='put':
        res=requests.put(url,data)

    return res.text

# 匹配接口对应的URL
def parse_name(name):
    if name is not None:
        # print(name)
        url=eval(name)
        return url
    return None

# 对参数进行处理：${}---执行表达式,%{}----全局变量中查到对应的值
def parse_value(value):
    
    if '$' in value:
        # 匹配用户名，并替换为正确的用户名
        if patt01.search(value):
            rand=patt01.search(value).group(1)
            randnum=eval(rand)
            value=patt01.sub(randnum(filepath),value)

        # 匹配密码，并替换为正确的密码
        if pattm5.search(value):
            param=get_pwd(pattm5.search(value).group(1))
            print("$param:",param)
            value=pattm5.sub(param,value)
            print("$value:",value)

    # 匹配成功，并在全局变量中查找对应key的value，替换
    elif '%' in value:        
        while patt02.search(value):   
            param=patt02.search(value).group(1)
            if global_vars.get(param,None):
                value=patt02.sub(global_vars[param],value,1)
                continue
            return "数据替换失败。。。"
    return value

# 根据正则表达式提取要匹配的值，保存到全局变量中
def extract_value_by_rule(res,rule):
    global global_vars
    if rule != str(None):
        keyword,regx=rule.split("----")
        log.info("拆后的正则表达式为-- %s" % regx)
        log.info("提取前全局变量global_vars 的值--->(%s)" % global_vars)
        if re.search(regx,res) :
            global_vars[keyword] = re.search(regx, res).group(1)
        else:
            log.error('正则表达式提取失败：%s'%regx)
        log.info("提取后全局变量global_vars 的值-->(%s)" % global_vars)



# 断言结果
def asser_result(res,keywords):
    try:
        
        assert keywords in res
        print("接口断言成功♪(^∇^*)")

    except AssertionError:
        print("断言失败~~")
        raise AssertionError
    except:
        print("未知异常！！！")
        raise


if __name__=="__main__":
    pass
