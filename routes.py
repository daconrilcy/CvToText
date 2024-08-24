from flask import jsonify, request, url_for, Blueprint
from services.secure_filename import get_secure_filename
from tasks import ocr_document, test_task_sleep
import os

# Créer un blueprint pour les routes principales
main = Blueprint('main', __name__)


@main.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello World'}), 200

@main.route('/api/test_task', methods=['GET'])
def test_task():
    task = test_task_sleep.delay()
    return jsonify({'task_id': task.id}), 200


@main.route('/api/get_text/<task_id>', methods=['GET'])
def get_text(task_id):
    result_text = ocr_document.AsyncResult(task_id)
    if result_text.ready():
        return jsonify({'result_text': result_text.get()}), 200
    else:
        return jsonify({'error': 'Task not ready'}), 202


@main.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = get_secure_filename(file.filename)
    file_path = os.path.join('C:\\', 'dev', 'py', 'pdfToText', 'tmp', filename)
    file.save(file_path)
    task = ocr_document.delay(filename, file_path)

    return jsonify({'task_id': task.id,
                    'status_url': url_for('main.task_status', task_id=task.id, _external=True),
                    'result_url': url_for('main.task_status', task_id=task.id, _external=True)
                    })


@main.route('/api/status/<task_id>')
def task_status(task_id):
    task = ocr_document.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': task.info,  # Le texte OCRisé une fois prêt
        }
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # Exception raised
        }
    return jsonify(response)
