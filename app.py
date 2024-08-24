from flask import Flask, url_for, jsonify, request
# Importer et enregistrer les blueprints
from routes import main as main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)
