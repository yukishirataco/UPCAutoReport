# UPCAutoReport
基于腾讯云函数实现的中国石油大学（华东）疫情防控通自动填报与自动通过邮件告知 Python 实现。

本项目的思路来自： https://github.com/kngkngtian/AutoReport

## 需要的信息
1. 数字石大账号和密码
2. 获取一次填报后的信息

（以Firefox为例）

打开[https://app.upc.edu.cn/ncov/wap/default/index](疫情防控通)，F12 打开`开发人员工具 - 控制台`，输入 `vm.save()`，在`网络`选项卡内可以找到一个类型为POST的请求，找到里面的`请求`选项卡，展开`表单数据`这一项，并点击复制全部，将复制下来的内容留作备用。

3. 发送邮件通知用的发送、接收邮箱

请参考 [国内各大邮件平台SMTP服务器地址与端口大全](https://www.fujieace.com/jingyan/smtp.html) 配置 SMTP 服务器，QQ 邮箱之类的可能需要发送短信获取授权码以登录 SMTP 服务器。

然后请点击本项目页面右上角绿色的`↓ Code`图标，点击里面的[Download ZIP](https://github.com/npfjcg/UPCAutoReport/archive/main.zip)下载回本项目的代码，解压得到一个 index.py 文件

## 部署之前的准备

在完成上述步骤后，将准备好的各项内容填写入 index.py 中，完成之后打包成 zip。

## 在腾讯云部署
 打开[云函数](https://console.cloud.tencent.com/scf)，在左边的侧栏里进入`函数服务`，云环境为`Python 3.6`，然后将上一步中打包的zip文件上传。
 
 在`触发器配置`中，将`触发周期`设定为`自定义触发周期`，`Cron 表达式`建议填写为`5 0,8 * * *`即可。
 
 下一步点击`部署并测试`,观察返回结果。如果提示“操作成功”，或者“今天已经填报过了”那么说明填报是正常的。
 
