from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/weather')
def  get_weather():
    city = request.args.get('city')

    # Check empty strings:

    if not bool(city.strip()):
        city = "Kansas City"

    weather_data = get_current_weather(city)

    # City not found:

    vtitulo = f"No se encontró la Ciudad: {city}"
    vstatus = "?"
    vtemp = "?"
    vfeels = "?"

    if weather_data['cod'] == 200:
        vtitulo = weather_data["name"]
        vstatus = weather_data["weather"][0]["description"].capitalize()
        vtemp = f"{weather_data['main']['temp']:.1f}"
        vfeels = f"{weather_data['main']['feels_like']:.1f}"


    
    return render_template(
        "weather.html",
        title = vtitulo,
        status = vstatus,
        temp = vtemp,
        feels_like = vfeels
    )


    


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)