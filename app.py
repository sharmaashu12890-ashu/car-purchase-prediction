from flask import Flask, request, render_template, redirect, url_for
import pickle
from sklearn.linear_model import LogisticRegression


app = Flask (__name__)


with open ("model.pkl", "rb") as file:
    model = pickle.load(file)


print("Model Loaded SucessFully")
print(model)


@app.route("/")
def home():
    return render_template("index.html", prediction = None)

@app.route("/predict", methods = ["POST"])
def predict():

        Age = float(request.form["Age"])
        EstimatedSalary = float(request.form["EstimatedSalary"])

        prediction = model.predict([[Age, EstimatedSalary]])

        if prediction[0] == 1:
            result = "Person will purchase the car"

        else:
            result = ("Person will not purchase the car")


        return render_template("index.html", prediction=result)


if __name__ == ("__main__"):
    app.run(debug=True)