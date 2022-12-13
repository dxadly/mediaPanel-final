from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

musicView = Blueprint('musicView', __name__)

# Get all music from the DB
@musicView.route('/musicView', methods=['GET'])
def get_music():
    cursor = db.get_db().cursor()
    cursor.execute('select musicID, musicName, wavLink from music')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
