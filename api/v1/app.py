#!/usr/bin/python3
"""the importation of modules for app.py for easy connectivity
    set strict slashes on routes
     Define a method to handle teardown_appcontext that calls storage.close()
     404 Responds handler for unavailable resources
"""
from flask import Flask, make_response, jsonify
from flask_cors import CORS

import os
from models import storage
from api.v1.views import app_views  # Blueprint

app = Flask(__name__)
# set strict slashes on routes
app.url_map.strict_slashes = False

# Register the blueprint app_views to the Flask instance app
app.register_blueprint(app_views)

# Set up CORS for app
CORS(app, resources={'/*': {'origins': '0.0.0.0'}})

# Define a method to handle teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def close_storage(error=None):
    # Called when application context is torn down
        storage.close()


@app.errorhandler(404)  # 404 Responds handler for unavailable resources
def not_found(error):
    #Return a not found repond error
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    # Run the Flask server
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
