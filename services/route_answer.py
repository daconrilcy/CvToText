from flask import jsonify, url_for


class RouteAnswer:
    def __init__(self, status=True, message='', status_code=200):
        self.status = status
        self.message = message
        self.status_code = status_code
        self.answer = {'status': self.status, 'message': self.message}

    def get_answer(self):
        return jsonify(self.answer), self.status_code


class ErrorAnswer(RouteAnswer):
    def __init__(self, message, status_code=400):
        super().__init__(False, message, status_code)


class SuccessAnswer(RouteAnswer):
    def __init__(self, message='Operation successful', status_code=200, **kwargs):
        super().__init__(True, message, status_code)
        self.answer.update(kwargs)


class FunctionAnswer(RouteAnswer):
    def __init__(self, base_name, task_id=None, message='', task_function=None, status=True, status_code=200):
        super().__init__(status=status, message=message, status_code=status_code)
        self.task_function = task_function
        self.base_name = base_name
        self.task_id = task_id
        self.answer.update({'result_url': get_url(self.base_name, self.task_id, 'result')})

    def update_answer_with_task(self, extra_data):
        self.answer.update(extra_data)


class StartAnswer(FunctionAnswer):
    def __init__(self, task_id, base_name):
        super().__init__(task_id=task_id, base_name=base_name, message='Task started')
        self.update_answer_with_task({'status_url': get_url(self.base_name, self.task_id)})


class StatusAnswer(FunctionAnswer):
    def __init__(self, task_id, task_function, base_name):
        super().__init__(task_id=task_id, base_name=base_name, message='Task status', task_function=task_function)
        self.state = task_function.AsyncResult(task_id)
        self.update_answer_with_task({'state': self.state.state, 'info': self.state.info})


class ResultAnswer(FunctionAnswer):
    def __init__(self, task_id, task_function, base_name):
        super().__init__(task_id=task_id, base_name=base_name, message='Task result', task_function=task_function)
        result = self.get_task_result(task_function, task_id)
        self.answer.update({'status_url': get_url(self.base_name, self.task_id), 'result': result})

    def get_task_result(self, task_function, task_id):
        async_result = task_function.AsyncResult(task_id)
        if async_result.ready():
            return async_result.get()
        else:
            self.status = False
            self.status_code = 202
            return 'Task not ready'


def get_url(base_name, task_id, type_url='status'):
    return url_for(f'main.{base_name}_task_{type_url}', task_id=task_id, _external=True)
