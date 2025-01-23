from twilio.rest import Client
import requests
import datetime as dt
import random

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = ""
account_sid = ''
auth_token = ''

date_now = dt.datetime.now()
today_date = str(date_now.date())
date_today_list = today_date.split("-")
date_yesterday= int(date_today_list[2]) - 1
date_yesterday_string = str(date_yesterday)
date_yesterday_full = f"{date_today_list[0]}-{date_today_list[1]}-{date_yesterday_string}"
date_before_yesterday = int(date_today_list[2]) - 2
date_before_yesterday_string = str(date_before_yesterday)
date_before_yesterday_full = f"{date_today_list[0]}-{date_today_list[1]}-{date_before_yesterday_string}"


parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":ALPHA_API_KEY
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query",params=parameters)
stock_data = response.json()
yesterday_close_value = stock_data["Time Series (Daily)"][f"{date_yesterday_full}"]["4. close"]
print(yesterday_close_value)
before_yesterday_close_value = yesterday_close_value = stock_data["Time Series (Daily)"][f"{date_before_yesterday_full}"]["4. close"]
print(before_yesterday_close_value)

change_amount = float(yesterday_close_value) - float(before_yesterday_close_value)
percentage_of_change = float(change_amount/float(before_yesterday_close_value)*100)
print(round(percentage_of_change,2))

if percentage_of_change > 0:
    message=f"⬆️{round(percentage_of_change,2)}"
else :
    message = f"⬇️{round(percentage_of_change,2)}"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percentage_of_change<=-2 or percentage_of_change <= 2:
    NEWS_API_KEY = ""
    news_parameters = {
        "q":COMPANY_NAME,
        "from":date_before_yesterday_full,
        "language":"en",
        "apiKey":NEWS_API_KEY
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything",params=news_parameters)
    news_data  = news_response.json()
    i = random.randint(0,2)
    news_title = news_data["articles"][i]["title"]
    news_description = news_data["articles"][i]["description"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='',
        body=f'\nTSLA:{message}\n'
             f'Title:{news_title}\n'
             f'Brief:{news_description}',
        to=''
    )
    print(message.status)
