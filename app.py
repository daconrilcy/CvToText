# app.py
from flask import Flask
from flask_jwt_extended import JWTManager

from config import JWT_SECRET
# Importer et enregistrer les blueprints
from routes import main as main_blueprint

app = Flask(__name__)
# Clé secrète utilisée pour signer le JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET
app.config['JWT_IDENTITY_CLAIM'] = 'identity'

# Initialiser JWT
jwt = JWTManager(app)


app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
