import uuid
from werkzeug.utils import secure_filename


def get_secure_filename(filename):
    # Sécuriser le nom de fichier pour éviter des problèmes potentiels
    filename = secure_filename(filename)
    new_file_name = filename.replace(' ', '_')
    uniq_file_name = f"{uuid.uuid4()}_{new_file_name}"
    return uniq_file_name