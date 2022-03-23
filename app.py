from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    global ch
    if request.method == "POST":
        ch = request.form["choice"]
        if ch == '1':
            return redirect("/weights")
        elif ch == '2':
            return redirect("/distance")
        elif ch == '3':
            return redirect("/temperature")
    else:
        return render_template('index.html')


@app.route('/weights', methods=['POST','GET'])
def weight():
    return render_template('weights.html')

@app.route('/distance', methods=['POST','GET'])
def distance():
    return render_template('distance.html')

@app.route('/temperature', methods=['POST','GET'])
def temperature():
    return render_template('temperature.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == "POST":

        if ch == '1':
            weight_pounds = request.form["user-weight"]
            weight_pounds = float(weight_pounds)
            weight_kg = weight_pounds * 0.45359237
            return render_template('result.html',weight_kg=weight_kg,weight_pounds=weight_pounds,ch=ch)

        elif ch == '2':
            distance_miles = request.form["user-distance"]
            distance_miles = float(distance_miles)
            distance_km = distance_miles * 1.609344
            return render_template('result.html',distance_km=distance_km,distance_miles=distance_miles,ch=ch)

        elif ch == '3':
            temperature_fahrenheit = request.form["user-temperature"]
            temperature_fahrenheit = float(temperature_fahrenheit)
            temperature_celsius = (temperature_fahrenheit - 32) * (5/9)
            return render_template('result.html',temperature_celsius=temperature_celsius,temperature_fahrenheit=temperature_fahrenheit,ch=ch)
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)
