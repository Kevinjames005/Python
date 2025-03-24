from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import smtplib

load_dotenv()

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

connection = requests.get(url="https://appbrewery.github.io/instant_pot/",headers=header)
data = connection.text

html_data = BeautifulSoup(data,"html.parser")
prize_tag = html_data.find(class_="a-offscreen")
prize_with_dollar = prize_tag.text.split("$")
prize_digits = float(prize_with_dollar[1])


if prize_digits < 100:
# Email details
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = os.getenv('sender_email')
    password = os.getenv('password')
    receiver_email = os.getenv('receiver_email')

    # Raw message
    msg = """\
    From: kevinjames00547@gmail.com
    To: letsmaktheway2fut@gmail.com
    Subject:"Price Drop Alert!"
    body:
    Hey there!

    Good news! The item you were interested in just dropped in price.

    Grab it before the price goes back up!

    Regards,
    Your Price Tracker Bot
    """

    # Send the email
    server = smtplib.SMTP(smtp_server, port)
    try:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)  # Send the email
        print("Email sent successfully!")
    finally:
        server.quit()


