from flask import Flask, jsonify, render_template
from stock_scraper import retrieve_stocks

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_stocks")
def get_stocks():
    return jsonify(retrieve_stocks()), 200


if __name__ == "__main__":
    app.run(debug=True)
