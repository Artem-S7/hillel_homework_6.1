from flask import Flask, render_template
app = Flask(__name__)
@app.get("/")
def home():
    return render_template("index.html")

@app.get("/cars")
def cars():
    return render_template("cars.html")

@app.get("/Auto")
def about():
    return "Сайт про вибір авто"

@app.get("/cars/Volvo_C30")
def volvo():
    return render_template("volvo.html")

@app.get("/cars/Audi_A8")
def audi():
    return render_template("audi.html")

@app.get("/cars/BMW_E90")
def bmw():
    return render_template("bmw.html")

app.run()
