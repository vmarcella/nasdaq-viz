import pandas as pd
import requests


def retrieve_stocks():
    """
        Retrieve the stocks from the nasdaq

        Returns a dataframe
    """
    request = requests.get(
        "http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download"
    )
    # convert the csv file into a list of lines
    processed_text = request.text.split("\n")

    dataframe_rows = []

    # convert each line into an element inside of the list
    for line in processed_text[1:]:
        row = line.split(",")[:-1]
        dataframe_rows.append(row)

    # Use all rows besides the last one (Garbage)
    dataframe = pd.DataFrame(dataframe_rows[:-1])

    # set columns using the first element in the processed csv
    # besides the last index in the list (Garbage)
    columns = processed_text[:1][0].rstrip().split(",")[:-1]
    dataframe.columns = columns

    # Convert all the rows into a dictionary
    stock_dict = {"stocks": []}
    for _, row in dataframe.iterrows():
        stock_dict["stocks"].append({col: row[col] for col in dataframe.columns})

    return dataframe
