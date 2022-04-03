from utils import app


@app.route("/weather")
def weather():
    pass

@app.route("/get_weather", methods=["POST"])
def get_weather():
    pass