import requests 
import json
import os 
from twilio.rest import Client 
import smtplib
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key = os.getenv("API_KEY") 
my_number = os.getenv("MY_NUMBER") 
api_end_point= os.getenv("API_END")
my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
to_email = os.getenv("TO_EMAIL")
#api_key = "4bb4a24a19f52fa8260f57705b94a1d2"  
#api_end_point = "https://api.openweathermap.org/data/2.5/forecast"  
#account_sid = "AC7c040d63a5405bab54dc99209945d44a" 
#auth_token ="3c825e290978532ca2c2e8336ae99b3e" 
def mail_sent(m):
    my_email = "sutharm965.com@gmail.com"
    password = "wnvwcgemqyebaseq"
    
    
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="sutharmanoj275@gmail.com",msg=m) 
    connection.close() 
    
def msg_sent(m):
    client  = Client(account_sid,auth_token)
    message = client.messages.create(
            body = m,
            from_= "+19126164076",
            to  = "+917568836319"
    )

def create_forcast():
    weather_paramerte ={
        "lat":24.5777364,
        "lon":73.711837,
        "appid": api_key,
        "cnt":4
        
    }
    response = requests.get(url=api_end_point,params=weather_paramerte)
    data = response.json()
    with open("5_day_forcast.json","w") as file:
        json.dump(data,file,indent=4)  
create_forcast()
with open("5_day_forcast.json") as file:
    data = json.load(file)["list"] 

rain = False
for hour in data:
    if (hour["weather"][0]["id"]) < 700:
        rain = True 
if rain:
    m=f"""Subject: Rain Alert

      Bring an Umbrella"""
    try:
        msg_sent("Bring an umbrella") 
    except:
        mail_sent(m) 
    
else: 
    m=f"""Subject: Rain Alert

      All clear"""         
    try:
        msg_sent("Clear") 
    except:
        mail_sent(m)  
        
