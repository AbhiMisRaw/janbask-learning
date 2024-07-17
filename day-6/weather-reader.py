import requests, json

api_key = "e872111c7a7e434ea5b125702241607"

city = input("Enter the City : ")

url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

res = requests.get(url).json()

print(res)
