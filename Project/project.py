import os
import requests
from flask import Flask
from flask import render_template


os.system("cls")
api_key = "a4d611d55373c1d9b2e482ea62c67a91"

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html', weather=weather_data)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    #print(url)
    temp = requests.get(url)
    data = temp.json()
    return data


if __name__ == "__main__":     
    city = "karachi"  
    weather_data = get_weather(city)
    print(weather_data, "\n")

    app.run(debug=True)


