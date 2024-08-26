import uuid
from werkzeug.utils import secure_filename
from config import ALLOWED_EXTENSIONS, ALLOWED_IPS, IP_RESTRICTION


def get_secure_filename(filename):
    # Sécuriser le nom de fichier pour éviter des problèmes potentiels
    filename = secure_filename(filename)
    new_file_name = filename.replace(' ', '_')
    uniq_file_name = f"{uuid.uuid4()}_{new_file_name}"
    return uniq_file_name


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def is_allowed_ip(ip):
    return ip in ALLOWED_IPS

def is_ip_restricted():
    return IP_RESTRICTION == 'true'

def is_client_allowed(request):
    print(request.remote_addr)
    if is_ip_restricted():
        return is_allowed_ip(request.remote_addr)
    else:
        return True