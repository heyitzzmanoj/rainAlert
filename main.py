import requests 
import json 
from twilio.rest import Client 
api_key = "4bb4a24a19f52fa8260f57705b94a1d2"  
api_end_point = "https://api.openweathermap.org/data/2.5/forecast"  
account_sid = "AC7c040d63a5405bab54dc99209945d44a" 
auth_token ="3c825e290978532ca2c2e8336ae99b3e"
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
    client  = Client(account_sid,auth_token)
    message = client.messages.create(
            body = "Bring an umbrella",
            from_= "+19126164076",
            to  = "+917568836319"
    ) 
else: 
    client  = Client(account_sid,auth_token)
    message = client.messages.create(
            body = "Clear",
            from_= "+19126164076",
            to  = "+917568836319"
    )

