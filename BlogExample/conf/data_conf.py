
import os
# 填写要测试的服务器的地址和端口
ip=''
port=''
# filepath='username.txt'
# test_data_file='../../data/test_data.py'

# 工程根目录
proj_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取日志配置文件路径
log_conf_file=os.path.join(proj_path,"conf","log.conf")

# 获取TXT文件格式的测试数据
test_data_file=os.path.join(proj_path,"data","test_data.txt")
# 获取Excel文件格式的测试数据
excel_data_file=os.path.join(proj_path,"data","testdata.xlsx")
filepath=os.path.join(proj_path,"data","username.txt")

email='xxx@qq.com'

#需要增加的接口地址维护在这里
register= "http://%s:%s/register/"%(ip,port)
login="http://%s:%s/login/"%(ip,port)
create="http://%s:%s/create/"%(ip,port)
getBlogsOfUser="http://%s:%s/getBlogsOfUser/"%(ip,port)
update="http://%s:%s/update/"%(ip,port)
getBlogContent="http://%s:%s/getBlogContent/"%(ip,port)
getBlogsContent="http://%s:%s/getBlogsContent/articleIds="%(ip,port)
delete="http://%s:%s/delete/"%(ip,port)