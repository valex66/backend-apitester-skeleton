import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 


@app.route('/associations', methods=["GET"])
def liste_assos():
    data=associations_df.to_dict()
    return jsonify(data)

@app.route('/associations/<int:id_asso>', methods=["GET"])
def detail_asso(id_asso):
    data=associations_df[associations_df["id"]==id_asso].to_dict()
    return jsonify(data)


@app.route('/events', methods=["GET"])
def liste_events():
    data=evenements_df.to_dict()
    return jsonify(data["nom"])

@app.route('/events/<int:id_event>', methods=["GET"])
def detail_event(id_event):
    data=evenements_df[evenements_df["id"]==id_event].to_dict()
    return jsonify(data)

@app.route('/associations/<int:id>/events', methods=['GET'])
def events_asso(id):
    data=evenements_df[evenements_df["association_id"]==id].to_dict()
    return jsonify(data)

@app.route('/associations/types', methods=['GET'])
def assos_par_type():
    data=associations_df["type"].to_dict()
    return jsonify(data)

@app.route('/associations/types/<type>', methods=['GET'])
def asso_par_type(type):
    data=associations_df[associations_df["type"]==type]["nom"].to_dict()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
