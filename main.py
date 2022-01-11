import requests
import datetime


APP_ID = "fed47a41"
API_KEY = "1e925ea8ec6291357705c9fe207d53e2"

querytext = input("tell me what exersices you did?  ")

data1 = {
    "query": querytext,
    "gender": "male",
    "weight_kg": 59,
    "height_cm": 169.10,
    "age": 19
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(
    url="https://trackapi.nutritionix.com/v2/natural/exercise", json=data1, headers=headers)
result = response.json()


today_date = datetime.datetime.now().date().strftime("%d/%m/%Y")
time = datetime.datetime.now().time().strftime("%I:%M:%S")
exercise = result["exercises"][0]["user_input"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]


sheety_url = "https://api.sheety.co/4e8d84ce270d0f5fea637f8ade3fd0cf/miloWorkout/workouts"

for exercisee in result["exercises"]:
    data_to_add = {
        "workout":
            {
                "date": today_date,
                "time": time,
                "exercise": exercise,
                "duration": duration,
                "calories": calories
            }

    }

headers2 = {
    "Content-Type": "application/json"
}
response2 = requests.post(url=sheety_url, json=data_to_add, headers=headers2)
print(response2.text)
