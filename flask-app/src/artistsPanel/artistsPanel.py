from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

artistsPanel = Blueprint('artistsPanel', __name__)

@artistsPanel.route('/artistsPanel', methods=['POST'])
def add_picture():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    name = request.form['name']
    link = request.form['link']
    description = request.form['description']
    query = "INSERT INTO picture (name, link, description) VALUES (\"{name}\", \"{link}\", \"{description}\")".format(name=name, link=link, description=description)
    cursor.execute(query)
    db.get_db().commit()
    return "Picture added successfully"

@artistsPanel.route('/artistsPanel/music', methods=['POST'])
def add_music():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    musicID = request.form['musicID']
    wavLink = request.form['wavLink']
    musicName= request.form['musicName']
    query = "INSERT into music (musicID, musicName, wavLink) VALUES (\"{musicID}\", \"{wavLink}\", \"{musicName}\")".format(musicID=musicID, wavLink=wavLink, musicName=musicName)
    cursor.execute(query)
    db.get_db().commit()
    return "music added successfully"

@artistsPanel.route('/artistsPanel/designs', methods=['POST'])
def add_design():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    designName = request.form['designName']
    designLink = request.form['designLink']
    query = "INSERT into donorDesigns (designName, designLink) VALUES (\"{designName}\", \"{designLink}\")".format(designName=designName, designLink=designLink)
    cursor.execute(query)
    db.get_db().commit()
    return "design added successfully"