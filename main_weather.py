from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template('index_w.html', weather=weather)

def get_weather(city):
    api_key = '521b46d6f22cc23ecaf9b62c7a103938'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or 'main' not in data:
        return "Нет информации о погоде в вашем городе"
    return data

if __name__ == "__main__":
    app.run(debug=True)

