# app.py
from flask import Flask
# Importer et enregistrer les blueprints
from routes import main as main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
