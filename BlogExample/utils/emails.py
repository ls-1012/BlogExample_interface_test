#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         emails.py
# Author:       ls
# Date:         2020/09/18 16:29
#-------------------------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.encoders import encode_base64

def send_email(filepath):
    smtpip="smtp.qq.com"
    smtpport=25
    # 此处填写发送人的账号信息
    user=''
    passwd=''
    # 此处填写发送者和接收者的邮件账号
    from_addr=''
    to_addrs=['']

    # 发送附件

    msg = MIMEMultipart()
    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(filepath, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('application', 'octet-stream')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment',filename='接口测试报告.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

        msg.attach(MIMEText("Python 测试报告结果,请看附件","html","utf-8"))

    # 创建连接smtp服务器的对象
    smtpobj=smtplib.SMTP()
    # smtpobj.set_debuglevel(1)
    smtpobj.connect(smtpip,smtpport)
    smtpobj.login(user,passwd)
    # 发送邮件需要发件人，收件人，发送邮件的内容
    # msg部分是邮件发送的内容，其中邮件内容分纯文本MIMEText类型，带附件MIMEMultipart，

    msg['From']=from_addr
    msg['To']="xxx@qq.com"
    msg['Subject']=Header("Python.接口测试报告",'utf-8')
    # print(from_addr)
    # print(to_addrs)
    # print(msg)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())

    print("发送成功")