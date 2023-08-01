#!/usr/bin/python3
"""Index view for the web service API and these are the importation of modules
    Create the route "/status" on the Blueprint object which is the path for blueprint
    stat blueprint that should return an object thru /stats
"""
from flask import jsonify
from api.v1.views import app_views  # Blueprint object
from models import storage
from models.engine.file_storage import classes


# Create the route "/status" on the Blueprint object which is the path for blueprint
@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify(status="OK")

# stat blueprint that should return an object thru /stats
@app_views.route('/stats')
def stats(cls=None):
    #Return number of objects by type

    objects = {}

    for key, value in classes.items():
        if key != 'BaseModel':
            # count objects by type from storage
            objects[key.lower()] = storage.count(value)
    return jsonify(objects)
