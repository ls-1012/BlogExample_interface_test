#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         ProjVar.py
# Author:       ls
# Date:         2020/10/12 21:16
#-------------------------------------------------------------------------------
import os

"""将Excel中的列设置为常量"""


# excel 纵坐标从0开始,横坐标从1开始
caseid=0
url=1
request_data=2
method=3
assert_value=4
extrac_regx=5
is_run=6
actual_data = 7
is_passed=8


# 获取case标题
# def get_caseid():
#     return Global_var.caseid

# # 获取url
# def get_url():
#     return Global_var.url
#
# # 获取url
# def get_method():
#     return Global_var.method
# # # 获取header
# # def get_is_header():
# #     return Global_var.header
#
# # # 获取是否执行
# # def get_is_run():
# #     return Global_var.is_run
#
# # 获取assert_value
# def get_assert_value():
#     return Global_var.assert_value
#
# # 获取extrac_regx
# def get_extrac_regx():
#     return Global_var.extrac_regx
#
# # 获取请求数据
# def get_request_data():
#     return Global_var.request_data
#
# # 获取预期结果
# def get_except_data():
#     return Global_var.expect_data
#
# # 获取实际结果
# def get_actual_data():
#     return Global_var.actual_data
#
# # # 获取执行时间
# # def get_excute_time():
# #     return Global_var.excute_time