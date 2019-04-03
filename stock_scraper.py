import pandas as pd
import requests


def retrieve_stocks():
    """
        Retrieve the stocks from the nasdaq
    """
    request = requests.get(
        "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"
    )
    print(request.text)
    dataframe = pd.DataFrame(
        (line.split(",")[:-1] for line in request.text.split("\n")[1:])
    )
    dataframe.columns = request.text.split("\r")[:1][0].split(",")[:-1]

    return dataframe.to_json()
