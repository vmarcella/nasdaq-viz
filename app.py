"""
    Flask application for Stock visualizations
"""
from flask import Flask, jsonify, render_template

from stock_scraper import retrieve_stocks

app = Flask(__name__)


@app.route("/")
def index():
    """
        Get the index page
    """
    return render_template("index.html")


@app.route("/get_stocks")
def get_stocks():
    """
        Get the stock data
    """
    dataframe = retrieve_stocks()
    # Convert all the rows into a dictionary
    stock_dict = {"stocks": []}

    # iterate through all of thee rows in the dataframe
    for _, row in dataframe.iterrows():
        curr_stock = {}
        for col in dataframe.columns:
            curr_stock[col] = row[col]
        stock_dict["stocks"].append(curr_stock)

    return jsonify(stock_dict), 200


if __name__ == "__main__":
    app.run(debug=True)
