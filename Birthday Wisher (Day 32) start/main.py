import smtplib
from email.mime.text import MIMEText
import datetime as dt
import random

smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = 'whd7327@naver.com'
password = input(f"{sendEmail} password: ")
recvEmail = 'whd4767@gmail.com'

now = dt.datetime.now()
weekend = now.weekday()
if weekend == 3:
  with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

  with smtplib.SMTP(smtpName, smtpPort) as connection:
    connection.starttls()
    connection.login(sendEmail, password)
    title="오늘의 명언"

    msg = MIMEText(quote)
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    msg['Subjetc'] = title

    connection.sendmail(sendEmail, recvEmail, msg.as_string())    









