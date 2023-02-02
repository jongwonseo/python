import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = 'whd7327@naver.com'
password = input(f"{sendEmail} password: ")
recvEmail = 'whd4767@gmail.com'

title="체험판"
content='되나 안되나...'

msg = MIMEText(content)
msg['From'] = sendEmail
msg['To'] = recvEmail
msg['Subjetc'] = title

s = smtplib.SMTP(smtpName, smtpPort)
s.starttls()
s.login(sendEmail, password)
s.sendmail(sendEmail, recvEmail, msg.as_string())
s.close()
