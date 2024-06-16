from flask import Blueprint, jsonify, request, make_response, session
from db.db_user import Db_user
from db.db_operations import DBOperations
import emails
from flask_login import login_user, logout_user, login_required, current_user
from db.db_promotion import Db_promotion
from db.db_task import Db_task

task_bp = Blueprint('tasks', __name__)

@task_bp.before_request
def keep_session_alive():
    session.modified = True

@task_bp.route("/", methods=["GET"])
@login_required
def get_tasks():
    '''
        Get all Tasks(contracts) of a user
    '''
    tasks_list = []
    provider_tasks = []
    receiver_tasks = []

    tasks = Db_task().get_tasks_by_userId(current_user.id)
    if not tasks:
        return make_response(jsonify({"results": tasks_list}), 200)
    else:
        for task in tasks:
            task_dict = {}
            task_dict.update(task.all_columns())

            if task.receiver_id == current_user.id:
                receiver_tasks.append(task_dict)
            else:
                provider_tasks.append(task_dict)

    tasks_list.append(provider_tasks)
    tasks_list.append(receiver_tasks)
    return make_response(jsonify({"results": tasks_list}), 200)
