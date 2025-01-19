import random
import pandas
import datetime as dt
import smtplib

num = random.randint(1,3)

birthdays = pandas.read_csv("birthdays.csv")
birth_days_list = list(birthdays["day"])
birth_months_list = list(birthdays["month"])
current_date_time = dt.datetime.now()
current_day = current_date_time.day
current_month = current_date_time.month

if current_month in birth_months_list and current_day in birth_days_list:
    with open(f"./letter_templates/letter_{num}.txt") as sample_letter:
        letter = sample_letter.read()
        birthday_day = birthdays[(birthdays["month"]==current_month) & (birthdays["day"]==current_day)]
        named_letter = letter.replace("[NAME]",f"{birthday_day["name"][0]}")
        birthday_email = birthday_day["email"][0]

    my_email = "senders_email@gmail.com"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password="app_password")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday\n\n{named_letter}"
        )





