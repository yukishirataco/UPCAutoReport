#-*- encoding:utf-8 -*-
import requests
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

def main_handler(event, context):
    mail_addr = '' # 发件邮箱
    mail_password = '' # 邮箱SMTP密码（也有可能是授权码，比如QQ)
    smtp_server = 'smtp.qq.com' # 邮箱SMTP地址
    recv_addr = '' # 收件邮箱地址
    payload_data = # Payload，请自行在浏览器的开发人员工具中获取，格式为形如{"sfzgsxsx": "0"}的内容
    now = datetime.now()
    payload_data['date'] = now.strftime("%Y%m%d")
    upcid = '' # 石大学号
    upcpassword = '' # 数字石大密码
    login_url = 'https://app.upc.edu.cn/uc/wap/login/check'
    save_url = 'https://app.upc.edu.cn/ncov/wap/default/save'
    report = requests.Session()
    login = report.post(login_url,data=dict(username=upcid,password=upcpassword))
    server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25,为了安全发送，可以使用587端口
    server.starttls()
    server.login(mail_addr, mail_password)
    if login.status_code == 200:
        ret = report.post(save_url,data=payload_data)
        msg = MIMEText(ret.json()['m'], 'plain', 'utf-8')
        server.sendmail(mail_addr, recv_addr, msg.as_string())
        server.quit()
        return (ret.json()['m'])
    else:
        msg = MIMEText("登录过程出现问题，请检查自己的数字石大账号密码是否输入正确。", 'plain', 'utf-8')
        server.sendmail(mail_addr, recv_addr, msg.as_string())
        server.quit()
        return "登录过程出现问题，请检查自己的数字石大账号密码是否输入正确。"
