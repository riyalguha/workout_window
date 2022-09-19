
import requests
from datetime import datetime
import os

api_id="834999d2"

api_key="68a903f9eed8d233a358597e74ad0b32"
headers={
    "x-app-id" : api_id,
    "x-app-key" : api_key,
    # "x-remote-user-id" : "0",
}
exercise_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
query=input("Enter your exercise : ")
gender=input("Enter your gender ")
weight=int(input("Enter your weight in kgs "))
height=int(input("Enter your height in cms "))
age=int(input("Enter your age "))
query_params={
    "query" : query,
    "gender" : gender,
    "weight_kg" : weight,
    "height_cm" : height,
    "age" : age,
}
response=requests.post(url=exercise_endpoint,json=query_params,headers=headers)
exercise = response.json()['exercises'][0]['name']
duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']
print(response.json()['exercises'][0]['nf_calories'])

time=datetime.now()
formatted_date = time.strftime("%d/%m/%Y")
time_time=time.strftime("%H:%M:%S")
print(formatted_date)
print(time_time)

sheety_api="https://api.sheety.co/96fcde2a65620f8a931d0d1433a21af1/workoutsProj/workouts"
spreadsheet_data = {
    "workout" : {
        "date" : formatted_date,
        "time" : time_time,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories,
    }
}
header = {
    "Authorization" : "Basic cml5YWxfZ3VoYTp2aXZla25hZ2Fy"
}
sheety_response=requests.post(url=sheety_api,json=spreadsheet_data,headers=header)
print(sheety_response.status_code)
