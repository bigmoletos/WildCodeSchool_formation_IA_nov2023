from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # Remplacez 'your_api_key' par votre clé API OpenWeatherMap
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=your_api_key')
    data = response.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
