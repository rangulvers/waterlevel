import pandas as pd

from flask import Flask, json

api = Flask(__name__)


def read_waterlevel():
    df = pd.read_csv("waterlevel.csv")
    return df.to_json(orient="split")


@api.route('/level', methods=['GET'])
def get_waterlevel():
    data = read_waterlevel()
    d = json.loads(data)
    return json.dumps(d)


if __name__ == '__main__':
    api.run()
