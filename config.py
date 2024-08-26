# config.py
import os
from dotenv import load_dotenv

# Charger les fichiers .env et .env.local
if os.path.exists('.env.local'):
    load_dotenv('.env.local')
else:
    load_dotenv('.env')

# Définir TEMP_PATH
TEMP_PATH = os.getenv('TMP_PATH')
ALLOWED_EXTENSIONS = os.getenv('ALLOWED_EXTENSIONS')
ALLOWED_IPS = os.getenv('ALLOWED_IPS').split(',')
IP_RESTRICTION = os.getenv('IP_RESTRICTION').lower()

if TEMP_PATH is None:
    raise ValueError("La variable d'environnement 'TMP_PATH' n'est pas définie")
