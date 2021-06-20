import csv
import pandas as pd
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)



@app.route('/')
def main():
    return render_template("welcome.html")


@app.route('/main', methods=['POST'])
def main_in():
    return render_template("index.html")

@app.route('/index', methods=['POST'])
def get_data():
    global first_name
    global last_name
    global age
    global passenger
    first_name = request.form.get("first")
    last_name = request.form.get("last")
    age = request.form.get("age", type=int)
    passenger = request.form.get("passenger", type=int)
    a = 17

    if request.method == 'POST':
        if request.form['first'] == '' or request.form['last'] == '' or request.form['age'] == '' or request.form['passenger'] == '':
            error = 'Please enter information to continue !!'
            return render_template('index.html', error=error)
        if (age > a):
            with open('data.txt','a')as info:
                info.write("\n")
                info.write("First Name - Last Name - Age -  Passengers ")
                info.write("\n")
                info.write(first_name)
                info.write("\n")
                info.write(last_name)
                info.write("\n")
                info.write(str(age))
                info.write("\n")
                info.write(str(passenger))
                info.write("\n")
                info.write("-----------------------------------------------------")
                return "<h1>If your information is correct click SUBMIT button and get your DREAM VACATION LOCATION </h1>"+ "<br> First Name : " + first_name + "<br> Last Name : " + last_name + "<br> Age : " + str(age) + "<br> Number of passengers : " + str(passenger)  + render_template('button.html')
        else:
            return "<h1>You have to be older than 18. </h1>"


@app.route('/locationGet5', methods=['POST','GET'])
def get_location():
    file = "bookDATA.csv"
    with open(file) as csvfile:
        results = []
        reader = csv.DictReader(csvfile)
        location = request.form.get("location")
        for row in reader:
            if location == row['Location']:
                results.append(dict(row))
    return render_template('priceData.html', results=results)


@app.route('/locationGet', methods=['POST','GET'])
def get_hotel():
    location = request.form.get("location")
    if (location == 'safari'):
        return redirect(url_for('safari'))
    if (location == 'beach'):
        return redirect(url_for('beach'))
    if (location == 'forest'):
        return redirect(url_for('forest'))
    if (location == 'mountain'):
        return redirect(url_for('mountain'))
    return render_template("locationGet.html")

@app.route('/beach', methods=['POST','GET'])
def beach():
    file = "bookDATA.csv"
    with open(file) as csvfile:
        results = []
        reader = csv.DictReader(csvfile)
        location = ("beach")
        for row in reader:
            if location == row['Location']:
                results.append(dict(row))

    file1 = "bookDATA.csv"
    with open(file1) as csvfile1:
        hotel = request.form.get("hotel")
        hotels = []
        reader1 = csv.DictReader(csvfile1)
        for row in reader1:
            if hotel == row['Hotel']:
                hotels.append(dict(row))

    return render_template('beach.html', results=results, hotels=hotels)

@app.route('/safari', methods=['POST','GET'])
def safari():
    file = "bookDATA.csv"
    with open(file) as csvfile:
        results = []
        reader = csv.DictReader(csvfile)
        location = ("safari")
        for row in reader:
            if location == row['Location']:
                results.append(dict(row))

    file1 = "bookDATA.csv"
    with open(file1) as csvfile1:
        hotel = request.form.get("hotel")
        hotels = []
        reader1 = csv.DictReader(csvfile1)
        for row in reader1:
            if hotel == row['Hotel']:
                hotels.append(dict(row))

    return render_template('safari.html', results=results, hotels=hotels)

@app.route('/forest', methods=['POST','GET'])
def forest():
    file = "bookDATA.csv"
    with open(file) as csvfile:
        results = []
        reader = csv.DictReader(csvfile)
        location = ("forest")
        for row in reader:
            if location == row['Location']:
                results.append(dict(row))

    file1 = "bookDATA.csv"
    with open(file1) as csvfile1:
        hotel = request.form.get("hotel")
        hotels = []
        reader1 = csv.DictReader(csvfile1)
        for row in reader1:
            if hotel == row['Hotel']:
                hotels.append(dict(row))

    return render_template('forest.html', results = results,  hotels=hotels)

@app.route('/mountain', methods=['POST','GET'])
def mountain():
    file = "bookDATA.csv"
    with open(file) as csvfile:
        results = []
        reader = csv.DictReader(csvfile)
        location = ("mountain")
        for row in reader:
            if location == row['Location']:
                results.append(dict(row))

    file1 = "bookDATA.csv"
    with open(file1) as csvfile1:
        hotel = request.form.get("hotel")
        hotels = []
        reader1 = csv.DictReader(csvfile1)
        for row in reader1:
            if hotel == row['Hotel']:
                hotels.append(dict(row))

    return render_template('mountain.html', results=results, hotels=hotels)

#login part
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again.'
        else:
            return redirect(url_for('admin'))
    return render_template('login.html', error=error) + "<br>"

#admin part when you log in
@app.route('/admin', methods=['POST', 'GET'])
def admin():
    a = pd.read_csv("bookDATA.csv")
    a.to_html()
    html_file = a.to_html()
    if request.method == 'POST':
        with open('bookDATA.csv', 'a') as file:
            hotel = request.form.get("hotel")
            location = request.form.get("location")
            price = request.form.get("price", type=int)
            writer = csv.writer(file)
            writer.writerow([hotel, location, price])

    #loading text file for admin
    b = pd.read_csv("data.txt")
    b.to_html()
    html_file2 = b.to_html()

    c = pd.read_csv("dataBooking.txt")
    c.to_html()
    html_file3 = c.to_html()

    return  render_template("admin.html") + "<h1>THIS IS OUR DATA</h1>" + html_file + "<br><h1>ALL USERS</h1>" + html_file2 + "<br><h1>USERS THAT BOOKED </h1>" + html_file3 + render_template("admin_back.html")


@app.route('/book', methods=['POST', 'GET'])
def book():
    global first_name
    global last_name
    global age
    global passenger
    firstName = first_name
    lastName = last_name
    age_age = age
    passengerr = passenger

    with open('dataBooking.txt', 'a')as info:
        info.write("\n")
        info.write("First Name - Last Name - Age - Passengers ")
        info.write("\n")
        info.write(firstName)
        info.write("\n")
        info.write(lastName)
        info.write("\n")
        info.write(str(age_age))
        info.write("\n")
        info.write(str(passengerr))
        info.write("\n")
        info.write("-----------------------------------------------------")

    return render_template('book.html', firstName=firstName, lastName=lastName)



if __name__ == '__main__':
    app.run()