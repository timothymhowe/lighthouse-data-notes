# import flask and jsonify
from flask import Flask, jsonify, request

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
api = Api(app)


class RawFeats :
    def __init__(self, feats) :
        self.feats = feats

    def fit(self, X, y = None) :
        pass

    def transform(self, X, y = None) :
        return X[self.feats]

    def fit_transform(self, X, y = None) :
        self.fit(X)
        return self.transform(X)


model = pickle.load(open("model.pickle", "rb"))


class Scoring(Resource) :
    def post(self) :
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index = json_data.keys()).transpose()

        # getting predictions from the model
        # it is much simpler because we used pipelines during dev
        res = model.predict_proba(df)

        # we cannot send nump array as a results
        return res.tolist()


api.add_resource(Scoring, '/scoring')

if __name__ == '__main__' :
    app.run(debug = True, host = '0.0.0.0', port = 5000)
