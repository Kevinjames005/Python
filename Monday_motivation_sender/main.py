import smtplib
import datetime as dt
import random

with open(file="quotes.txt",mode="r") as file:
    quotes = file.readlines()
    stripped_quotes = [line.strip("\n") for line in quotes]


now = dt.datetime.now()
if now.weekday()==1:

    my_email = "senders_email@gmail.com"

    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email,password="app_password")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="receivers_email",
        msg=f"Subject:Hello\n\n{random.choice(stripped_quotes)}."
    )
    connection.close()


