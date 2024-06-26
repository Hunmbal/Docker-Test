import os 
import requests
from flask import Flask, request, render_template
from datetime import datetime

os.system("cls")
api_key = "a4d611d55373c1d9b2e482ea62c67a91"

app = Flask(__name__, static_url_path='/static')

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S').strftime(format)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('index.html', weather=weather_data)
    else:
        # Default city when the page is first loaded
        default_city = "Karachi"
        weather_data = get_weather(default_city)
        return render_template('index.html', weather=weather_data)

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&cnt={7*10}&appid={api_key}"
    temp = requests.get(url)
    data = temp.json()
    return data

if __name__ == "__main__":     
    city = "karachi"  
    weather_data = get_weather(city)
    print(weather_data, "\n")

    app.run(host='0.0.0.0', port=5000)
