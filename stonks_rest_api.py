from functions import *
from flask import Flask

app = Flask(__name__)

@app.route("/<ticker>")
def evaluate(ticker):

    ticker = ticker.upper()
    try:
        company_data =  get_data(Console(), ticker, 10)
    
    except:
        company_data = null

    return company_data
    
@app.route("/")
def home():
    return "<h2>Welcome to the Stonks REST API</h2>"

if __name__ == "__main__":
    app.run(debug=True)