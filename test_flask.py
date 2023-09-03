from flask import Flask, request
app=Flask(__name__)

@app.route("/")   #decorator
def welcome():
    return "Welcome All"

@app.route("/addition")   #decorator
def add():
    a=request.args.get("num1")
    b=request.args.get("num2")
    return([int(a)+int(b)])


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)