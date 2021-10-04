import datetime as dt
import pandas
import random
import smtplib
today_month = dt.datetime.now().month
today_date = dt.datetime.now().day
today_tuple = (today_month,today_date)

#reading from csv file
df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month,data_row.day):data_row for (index, data_row) in df.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    person_name = birthday_person["name"]
    email_to_send = birthday_person["email"]

    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        letter_content = file.read()
        letter_to_mail = letter_content.replace("[NAME]",person_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="ssg137173@gmail.com",password="Randomtester@1234")
        connection.sendmail(from_addr="ssg137173@gmail.com",
                            to_addrs=email_to_send,
                            msg=f"Subject:Birthday Wish\n\n{letter_to_mail}")








