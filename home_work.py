from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    random_info = None

    if request.method == 'POST':
        random_info = get_random()
        print(random_info)
    return render_template('index.html', random_info=random_info)


def get_random():
    api_key = ''  # данный сайт работает без ключа
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
