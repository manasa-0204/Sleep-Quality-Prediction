
from flask import Flask, render_template, request

from sleep import predict_sleep, accuracy

app = Flask(__name__)

# Home page
@app.route("/")
def home():

    return render_template(
        "index.html",
        accuracy=round(accuracy * 100, 2)
    )


# Prediction page
@app.route("/predict", methods=["POST"])
def predict():

    sleep = request.form["sleep"]
    screen = request.form["screen"]
    caffeine = request.form["caffeine"]
    stress = request.form["stress"]

    # Predict sleep quality
    result = predict_sleep(
        sleep,
        screen,
        caffeine,
        stress
    )

    return render_template(
        "index.html",
        prediction=result,
        accuracy=round(accuracy * 100, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
