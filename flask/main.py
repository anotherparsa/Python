from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/about")
def aboutus_page():
    return render_template("aboutus.html")

@app.route("/data")
def passingdata_page():
    return render_template("data.html", name="Test")