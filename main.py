from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23
    return {"Station": station,
            "Date": date,
            "Temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
