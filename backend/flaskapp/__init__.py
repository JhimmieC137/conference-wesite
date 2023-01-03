from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

def create_app(test_config=None):
    app = Flask(__name__)
    
    CORS(app, resources={r"/*":{'origins':"*"}})
    
    @app.route('/')
    def home():
        title = "Conference Website"  
        return jsonify({
            'Project': title,
            'message': 'success',
            'status': 200
        })
    
    return app
