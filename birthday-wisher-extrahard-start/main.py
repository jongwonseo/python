from datetime import *
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText
 
today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")

# 키가 튜플?
birthdays_dict = {(data_row["month"], data_row['day']):data_row for index, data_row in data.iterrows()}

if today_tuple in birthdays_dict:
  birthpay_person = birthdays_dict[today_tuple]
  file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
  
  with open(file_path) as letter_file:
    contents = letter_file.read()
    contents = contents.replace("[NAME]", birthpay_person['name'])
  
  smtpName = "smtp.naver.com"
  smtpPort = 587

  sendEmail = 'whd7327@naver.com'
  password = input(f"{sendEmail} password: ")
  recvEmail = 'whd4767@gmail.com'
  
  with smtplib.SMTP(smtpName, smtpPort) as connection:
    connection.starttls()
    connection.login(sendEmail, password)
    title=f"{birthpay_person['name']} birthday!!!"

    msg = MIMEText(contents)
    msg['From'] = sendEmail
    msg['To'] = recvEmail
    msg['Subjetc'] = title

    connection.sendmail(sendEmail, recvEmail, msg.as_string())    
  