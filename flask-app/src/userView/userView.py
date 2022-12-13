from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

userView = Blueprint('userView', __name__)

@userView.route('/userView', methods=['GET'])
def display_pictures():
    cursor = db.get_db().cursor()
    cursor.execute('select name, link, description from picture')
    # give app smith the data
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response