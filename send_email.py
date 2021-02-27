import smtplib
from email.mime.text import MIMEText
class send_email:
    def __init__(self,senderinfo,receiverinfo):
        with open(senderinfo,"r+",encoding='utf-8') as f:
            weichuli = f.readlines()
            chuli = []
            for zifu in weichuli:
                chuli.append(zifu.strip())
            self.mail_host = chuli[0]
            self.mail_user = chuli[1]
            self.mail_pass = chuli[2]
            self.sender = chuli[3]
        with open(receiverinfo,"r+",encoding='utf-8') as f:
            weichuli = f.readlines()
            chuli = []
            for zifu in weichuli:
                chuli.append(zifu.strip())
            self.receivers = chuli

    def send(self,title,contentaddr):
        with open(contentaddr,"r+",encoding='utf-8') as f:
            content = f.read()
        mail_host = self.mail_host
        mail_user = self.mail_user
        mail_pass = self.mail_pass
        sender = self.sender
        receivers = self.receivers
        # 邮件内容设置
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = title
        message['From'] = sender
        message['To'] = receivers[0]
        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.ehlo(mail_host)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                sender, receivers, message.as_string())
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)