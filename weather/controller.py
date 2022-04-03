from utils import app
from flask import request,render_template
import requests


@app.route("/weather")
def weather():
    return render_template('weather.html')


@app.route("/get_weather", methods=["POST"])
def get_weather():
    if request.method == 'POST':
        lat = request.form['lat']
        lon = request.form['lon']
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b4f6f5bf33ff9a68b09e7c324196b9fc'

        r = requests.get(url).json()

        return render_template('success2.html',data=r)