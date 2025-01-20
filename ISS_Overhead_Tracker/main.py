import requests
import  datetime as dt
import smtplib

MY_LATITUDE = 20.593683
MY_LONGITUDE = 78.962883
MY_EMAIL = "Your_mail-id"
PASSWORD = "App Password"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_longitude_condition = iss_longitude-5 < iss_longitude < iss_longitude + 5
iss_latitude_condition = iss_latitude-5 < iss_latitude < iss_latitude + 5

def is_it_dark():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0
    }
    response_1 = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response_1.raise_for_status()
    data_1 = response_1.json()
    sunrise = int(data_1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_1["results"]["sunset"].split("T")[1].split(":")[0])

    now =  dt.datetime.now()
    hour = now.hour
    if (hour <= sunrise) or (hour >= sunset):
        return True
    else:
        return False


if (iss_longitude_condition and iss_latitude_condition) and is_it_dark():
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=MY_EMAIL,password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:Look Overhead\n\n Get out and look overhead to see ISS Space Shuttle.")
    connection.close()

