from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index_w.html', weather=weather, news=news)


def get_weather(city):
    api_key = '521b46d6f22cc23ecaf9b62c7a103938'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or 'main' not in data:
        return "Нет информации о погоде в вашем городе"
    return data


def get_news():
    api_key = '12475b48ce2946b7ba29b28a3f560a05'
    url = f"https://newsapi.org/v2/everything?q=keyword&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])


if __name__ == "__main__":
    app.run(debug=True)

