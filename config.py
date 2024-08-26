# config.py
import os
from dotenv import load_dotenv

# Charger les fichiers .env et .env.local
load_dotenv()
if os.path.exists('.env.local'):
    load_dotenv('.env.local')

# Définir TEMP_PATH
TEMP_PATH = os.getenv('TMP_PATH')

if TEMP_PATH is None:
    raise ValueError("La variable d'environnement 'TMP_PATH' n'est pas définie")
