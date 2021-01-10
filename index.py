#-*- encoding:utf-8 -*-
import requests
import smtplib
from email.mime.text import MIMEText

def main_handler(event, context):
    mail_addr = ''
    mail_password = ''
    smtp_server = 'smtp.qq.com'
    recv_addr = ''
    # Payload，请自行在浏览器的开发人员工具中获取
    payload_data = { 
    }
    upcid = ''
    upcpassword = ''
    login_url = 'https://app.upc.edu.cn/uc/wap/login/check'
    save_url = 'https://app.upc.edu.cn/ncov/wap/default/save'

    report = requests.Session()
    login = report.post(login_url,data=dict(username=upcid,password=upcpassword))
    if login.status_code == 200:
        ret = report.post(save_url,data=payload_data)
        msg = MIMEText(ret.json()['m'], 'plain', 'utf-8')
        server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
        server.starttls()
        server.login(mail_addr, mail_password)
        server.sendmail(mail_addr, recv_addr, msg.as_string())
        server.quit()
        return (ret.json()['m'])
    else:
        return "登录过程出现问题，请检查自己的数字石大账号密码是否输入正确。"
main_handler(0,0)
