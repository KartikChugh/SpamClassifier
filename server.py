from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('models/saved/model.joblib')

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def classify():
    if request.method == "POST":
        message = request.form['submission']
        return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)