from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        temperature = int(request.form["temperature"])

        if temperature >= 35:
            result = "Sunny ☀️"
        elif temperature >= 25:
            result = "Partly Cloudy ⛅"
        elif temperature >= 15:
            result = "Cloudy ☁️"
        else:
            result = "Rainy 🌧️"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
