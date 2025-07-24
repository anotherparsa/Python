from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/about")
def aboutus_page():
    return render_template("aboutus.html")

kwargs = {
    "arg1" : "test1",
    "arg2" : "test2",
    "arg3" : "test3",
    "arg4" : "test4",
    "arg5" : "test5",
    "arg6" : "test6",
}

@app.route("/data")
def passingdata_page():
    return render_template("data.html", **kwargs)