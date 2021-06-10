from flask.json import jsonify
from functions import *
from flask import Flask, request
import sys

sys.stdout = sys.stderr

app = Flask(__name__)

@app.route("/evaluate")
def evaluate():

    ticker = request.args.get("ticker").upper()
    ror = int(request.args.get("ror"))
    print(ticker, ror)
    try:
        company_data =  get_data(Console(), ticker, ror)
    
    except Exception as ex:
        print("Error!")
        print(ex)
        return jsonify("response", "null")

    return company_data
    
@app.route("/")
def home():
    return "<h2>Welcome to the Stonks REST API</h2>"

if __name__ == "__main__":
    app.run(debug=True)