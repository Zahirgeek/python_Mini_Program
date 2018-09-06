import smtplib
from email.mime.text import MIMEText

# 服务器
SMTPserver = "xxxx.163.com"
# 发送邮件的地址
sender = "xxxx@163.com"
# 授权密码(不等同于登录密码)
password = "xxxxxx"

# 发送的内容
message = ""
# 转为邮件文本
msg = MIMEText(message)
# 邮件主题
msg["Subject"] = "Null"
# 邮件的发送者
msg["From"] = sender

# 连接smtp服务器
mailServer = smtplib.SMTP(SMTPserver, 25)
# 登录
mailServer.login(sender, password)
# 发送邮件
mailServer.sendmail(sender, ["xxxxxx@qq.com"], msg.as_string())
# 退出服务器
mailServer.quit()
