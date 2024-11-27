import fastapi
from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi import FastAPI

import json
import requests

app = FastAPI()
@app.get('/')
def hello_world():
    return{'Hello': 'World'}
# uvicorn app.main:app --reload --host


#
# BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
#
# response = requests.get(BASE_URL)
# print(response)
#
# if response.status_code == 200:
#     data_json = response.json()
#     weather_data = {}
#     for item in data_json:
#
# else:
#     print(f'Error {response.status_code}')
#
#
#

# 6317f054c6846e41d98c8c381da7c082