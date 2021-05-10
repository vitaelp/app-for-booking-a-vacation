from flask import Flask, render_template, request
import pandas as pd
import xlrd
import openpyxl


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/index', methods=['POST'])
def get_data():


    first_name = request.form.get("first")
    last_name = request.form.get("last")
    age = request.form.get("age", type=int)
    night = request.form.get("night", type=int)
    passenger = request.form.get("passenger", type=int)
    a = 18


    if age > a:
        with open('data.txt', 'a')as info:
            info.write("\n")
            info.write("First Name - Last Name - Budget - Age - Nights - Passengers ")
            info.write("\n")
            info.write(first_name)
            info.write("\n")
            info.write(last_name)
            info.write("\n")
            info.write(str(age))
            info.write("\n")
            info.write(str(night))
            info.write("\n")
            info.write(str(passenger))
            info.write("\n")
            info.write("-----------------------------------------------------")

        return """<h1>If your information is correct click SUBMIT button and get your DREAM VACATION LOCATION </h1>"""+ "<br> First Name : " + first_name + "<br> Last Name : " + last_name + "<br> Age : " + str(age) + "<br> Number of passengers : " + str(passenger) + "<br> Number of nights : " + str(night) + render_template('button.html')
    else:
        return """<h1>You have to be older than 18. </h1>"""


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    dictionary = pd.read_excel('book.xlsx', index_col=0).to_dict() #radimo dictionary
    return dictionary


@app.route('/locationPrice', methods=['POST', 'GET'])
def locationPrice():
    return render_template('priceData.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)