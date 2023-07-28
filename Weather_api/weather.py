import requests

api_key = "API KEY"
city = input("City name -: ")

# geolocater = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}")
try:
    user = int(input("For Celcius : Type 1,\nFor Fahrenheit : Type 2 = "))
    if user < 1 or user > 2:
        print("Please choose a valid option")
        exit()

    if user == 1:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}")
    elif user == 2:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}")

    data = weather_data.json()

    if weather_data.status_code == 200:
        #Print weather information Temp, Wind speed, cloud status
        print("\nCurrent Temp -: ", data['main']['temp'])
        print("Minimum Temp -: ", data['main']['temp_min'], " --- Maximum Temp : ", data['main']['temp_max'])
        print("Wind Speed -: ", data['wind']['speed'])
        print("Cloud Status -:", data['weather'][0]['description'])
    else:
        #print Error if occured
        print("Error:", data["message"])
except requests.exceptions.RequestException as e:
    print("An error occured :", str(e))
