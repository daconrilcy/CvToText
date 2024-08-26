from flask import jsonify, request, Blueprint
from services.route_answer import StartAnswer, StatusAnswer, ResultAnswer, ErrorAnswer
from services.secure import is_client_allowed
from services.secure_loader import secure_file_loader
from tasks import ocr_document, test_task_sleep

main = Blueprint('main', __name__)
maincoreurl = '/api'

@main.before_request
def before_request():
    if not is_client_allowed(request):
        return ErrorAnswer('Not allowed').get_answer()

def create_task_route(task_func, base_name):
    task = task_func.delay()
    return StartAnswer(task.id, base_name).get_answer()

def create_status_route(task_id, task_func, base_name):
    return StatusAnswer(task_id=task_id, task_function=task_func, base_name=base_name).get_answer()

def create_result_route(task_id, task_func, base_name):
    return ResultAnswer(task_id=task_id, task_function=task_func, base_name=base_name).get_answer()

@main.route(f'{maincoreurl}/test/connexion', methods=['GET'])
def test():
    return jsonify({'message': 'Hello World'}), 200

@main.route(f'{maincoreurl}/test/task', methods=['GET'])
def test_task():
    return create_task_route(test_task_sleep, 'test')

@main.route(f'{maincoreurl}/test/task/status/<task_id>', methods=['GET'])
def test_task_status(task_id):
    return create_status_route(task_id, test_task_sleep, 'test')

@main.route(f'{maincoreurl}/test/task/result/<task_id>', methods=['GET'])
def test_task_result(task_id):
    return create_result_route(task_id, test_task_sleep, 'test')

@main.route(f'{maincoreurl}/ocr/upload', methods=['POST'])
def upload_file():
    file_loader = secure_file_loader(request)
    if not file_loader.status:
        return file_loader.get_answer()

    task = ocr_document.delay(file_loader.filename, file_loader.file_path)
    return StartAnswer(task.id, 'ocr').get_answer()

@main.route(f'{maincoreurl}/ocr/status/<task_id>')
def ocr_task_status(task_id):
    return create_status_route(task_id, ocr_document, 'ocr')

@main.route(f'{maincoreurl}/ocr/result/<task_id>')
def ocr_task_result(task_id):
    return create_result_route(task_id, ocr_document, 'ocr')
