import json
import requests
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
x = input("Enter the city name for weather update's: " )

url = f"http://api.weatherapi.com/v1/current.json?key=dbbfae24ddef452fb3773647242908&q={x}"
r = requests.get(url)
dic = json.loads(r.text)
w = dic["current"]["temp_c"]
speaker.Speak(f"the current weather in {x} is {w} degree")

