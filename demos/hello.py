from flask import Flask

app = Flask("Hello World")


@app.route("/")
def start():
    return "Start ist hier"

@app.route("/hello")
@app.route("/hello/<name>")
def greeting(name="World"):
    return "Hello " + name + "!"



if __name__ == "__main__":
    app.run(debug=True, port=5000)
