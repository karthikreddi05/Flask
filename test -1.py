from flask import Flask ,request
app = Flask(__name__)

@app.route('/add')
def addition ():
    return f"this is my test fun"

@app.route("/karthik")
def print_name():
    return f"JANGA KARTHIK REDDY"

@app.route("/user")
def print_user():
   data =  request.args.get('name')
   return f"{data}"


if __name__ == '__main__':
    app.run(host="0.0.0.0")

    