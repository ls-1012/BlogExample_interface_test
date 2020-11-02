from utils.parse_datafile import *
from utils.report import html_report
import time
from utils.emails import *
from utils.operator_Excel import *
import traceback
from utils.Log import *
from conf.ProjVar import *

# global_vars={}
funcall_cost=0
total_test_case = 0#记录总共测试用例数
success_test_case = 0#记录成功用例数
failed_test_case = 0#记录失败用例数

my_log = MyLog()
log = my_log.get_logger()

test_results=[]
# 获取TXT数据格式
"""
test_cases=get_testdata(test_data_file)
for i in test_cases:
    name,value,method,assert_value,extract_rule=i.strip().split('||')
    print(name,value,method,assert_value,extract_rule)
"""
# 获取Excel中数据格式
wb = OPExcel(excel_data_file)
wb.set_sheet_by_sheetname("测试数据")
excelContent = wb.getExcelContent()
print("excelContent:",excelContent)
for i in range(1,len(excelContent)):
    caseid, name, value, method, assert_value, regx,is_run = excelContent[i][:7]
    print("读取到的参数：",caseid, name, value, method, assert_value, regx,is_run)
    if is_run.lower() !='y':continue
    res=None
    try:
        # 提取url
        url=parse_name(name)
        #提取参数
        data=parse_value(value)

        # 统计执行结果
        now = time.time()
        log.debug("method:%s, url:%s, data:%s"%(method, url, data))
        res = send_request(method, url, data)
        log.debug("res:%s"% res)
        funcall_cost = time.time() - now

        flag = "pass"
        # 断言执行结果
        asser_result(res, assert_value)

        # 提取依赖参数
        if regx != str(None):
            log.info("提取前的参数，正则---> %s, 带提取内容--->%s"%(regx,res))
            extract_value_by_rule(res, regx)
        # print("funcall_cost:",funcall_cost)
    except AssertionError:
        log.error("assertion failed....正则---> %s, 带提取内容--->%s"%(regx,res))
        failed_test_case += 1
        flag='fail'
    except Exception:
        log.error(traceback.print_exc())
        traceback.print_exc()
        failed_test_case += 1
        flag='fail'
    else:
        log.info("执行成功！！！")
        success_test_case += 1


    wb.writeContent(i+1,actual_data,res)
    wb.writeContent(i+1, is_passed, flag)

    #获取需要写入报告的字段的数据
    test_results.append((url, data, res, funcall_cost, assert_value, flag))



# print(test_results)
# 将数据写入HTML模板中
html=html_report(*test_results)
# print(html)
# 创建生成的报告的文件名
report_path=os.path.dirname(os.path.realpath(__file__))
reportFileName = "TestReport.html"
html_path=os.path.join(report_path,'report',reportFileName)
if os.path.exists(html_path):
    import shutil
    reportFileNameBK="Report{}.html".format(time.strftime("%Y%m%d%H%M%S"))
    shutil.move(html_path,os.path.join(report_path,'report',reportFileNameBK))
    del shutil

# 将HTML内容写入文件中
with open(html_path,"wb")as f:
    f.write(html.encode("utf-8"))

print("执行成功的用例%s条,执行失败的用例%s条"%(success_test_case,failed_test_case))

#发送HTML格式的报告
send_email(html_path)

log.info("email is sent successfully!")











