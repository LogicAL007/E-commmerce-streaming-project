import linecache
import json
import requests
import logging
import numpy as np
from numpy import add
import pandas as pd

df = pd.read_csv ('/mnt/c/Users/ayomi/OneDrive/Documents/GitHub/E-commmerce-streaming-project/data.csv', encoding= 'ISO-8859-1') 
# write a data validation code

def convert_csv_to_txt(df):
    df['json'] = df.to_json(orient='records', lines=True).splitlines()
    dfjson = df['json']
    np.savetxt(r'./output.txt', dfjson.values, fmt='%s')
    return

def request_post(file_path: str, start: int = 1, end: int = 10) -> None:
    '''
    Sends POST requests to a specified URL with JSON data read from a file.

    :param file_path: The path to the file from which to read the JSON strings.
    :param start: The starting line number in the file to read from. Defaults to 1.
    :param end: The ending line number in the file to read up to. Defaults to 10.

    :return: None
    '''
    i = start
    while i <= end:
        line = linecache.getline(file_path, i)
        if line.strip():
            myjson = json.loads(line)
            response = requests.post('http://localhost:80/invoiceitem', json=myjson)
            logging.info(response.json())
        i += 1

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    convert_csv_to_txt(df)
    request_post('./output.txt')
