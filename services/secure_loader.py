import os
from services.secure import is_allowed_file, get_secure_filename
from config import TEMP_PATH
from services.route_answer import ErrorAnswer, SuccessAnswer

def secure_file_loader(request):
    if 'file' not in request.files:
        return ErrorAnswer('No file part')
    file = request.files['file']

    if not file or file.filename == '':
        return ErrorAnswer('No file part')

    if not is_allowed_file(file.filename):
        return ErrorAnswer('File type not allowed')

    filename = str(get_secure_filename(file.filename))
    file_path = os.path.join(str(TEMP_PATH), filename)
    file.save(file_path)

    return SuccessAnswer(message='File loaded', file_path=file_path, filename=filename)
