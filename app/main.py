'''
 http://localhost:8000/city-info?city=toronto

 uvicorn app.main:app --reload --host 0.0.0.0
'''

import fastapi
from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi import FastAPI, Query
import json
import requests

app = FastAPI()
# url = 'http://api.openweathermap.org/data/2.5/weather'
# appid = '6317f054c6846e41d98c8c381da7c082'

def get_city_temperature(city: str):
    url = "http://api.openweathermap.org/data/2.5/weather"
    headers = {
        "Accepts": "application/json"
    }
    params = {
        "appid": "7032b4df7d4397a6667526b5523ee7bb",
        "units": "metric",
        "q": city
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        city_name = data['name']
        temperature = data["main"]["temp"]
        status = response.status_code
        return f"City: {city_name}, temperature: {temperature} C°, Status: {status}"
    except requests.RequestException as e:
        print(f"Request Error: {e}")
        return None

@app.get("/city-info", summary="Get city info", tags=["city"])
async def get_city_info(city: str):
    if not city:
        raise HTTPException(status_code=400, detail=f"City param no specified")
    return get_city_temperature(city)


# url = ''
# response = response.get(url)
# print(response)
#
# if response.status_code == 200:
#     data_json = response.json()
#     for
