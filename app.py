"""
    Flask application for Stock visualizations
"""
import sys

from flask import Flask, jsonify, render_template

import utils
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
    # Convert all the rows into a dictionary
    stock_dict = {"children": []}

    # iterate through all of thee rows in the dataframe
    for _, row in app.dataframe.iterrows():
        curr_stock = {}
        for col in app.dataframe.columns:
            curr_stock[col] = row[col]
        stock_dict["children"].append(curr_stock)

    return jsonify(stock_dict), 200


def main():
    """
        Main application handler
    """
    # in debug mode, use the cached dataframe
    if len(sys.argv) >= 2:
        app.dataframe = utils.load_dataframe("df.pickle")
        app.run(debug=True)
    else:
        app.dataframe = retrieve_stocks()
        utils.save_dataframe(app.dataframe, "df.pickle")
        app.run()


if __name__ == "__main__":
    main()
