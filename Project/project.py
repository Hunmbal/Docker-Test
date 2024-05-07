import os 
import requests
from flask import Flask, request, render_template

os.system("cls")
api_key = "a4d611d55373c1d9b2e482ea62c67a91"

app = Flask(__name__, static_url_path='/static')

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
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    temp = requests.get(url)
    data = temp.json()
    return data

if __name__ == "__main__":
    app.run(debug=True)
