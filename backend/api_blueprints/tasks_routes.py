from flask import Blueprint, jsonify, request, make_response, session, g
from db.db_operations import DBOperations
from flask_login import login_required, current_user
from db.db_task import Db_task
from db.db_promotion import Db_promotion
from db.db_request import Db_request
task_bp = Blueprint('tasks', __name__)

@task_bp.before_request
def keep_session_alive():
    session.modified = True

@task_bp.route("/", methods=["GET", "POST", "PUT"])
@login_required
def get_tasks():
    '''
        Get all Tasks(contracts) of a user
    '''
    #---------------------------- GET --------------------------------------------------------------
    if request.method == 'GET':
        tasks_list = []
        provider_tasks = []
        receiver_tasks = []

        tasks = Db_task(g.db_session).get_tasks_by_userId(current_user.id)
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
    # ----------------------------------------------------------------------------------------
    # ---------------------PUT-------------------------------------------------------------------
    if request.method == 'PUT':
        # CANNOT change to 'pending' via this route, pending is when the task is created

        data = request.get_json()
        # data = {'id':'<task_id>', 'status': 'open'}
        # data2 = {'id':'<task_id>', 'status': 'closed'}
        task_dict = data

        task = DBOperations(g.db_session).search('Task', '<task_id')
        if not task:
            return 'No task object found', 404
        if task.status == 'closed' or task.status == 'rejected':
            return 'cannot modify task', 400

        # Manage new status and old status errors
        old_task_status = task.status
        if 'status' in data:
            if old_task_status != 'pending' and data['status'] == 'pending':
                return 'Cant revert status back to pending', 400
            if old_task_status == data['status']:
                return 'Old status and new status are the same', 400

        # Find contact from where task originated
        initial_contact = DBOperations(g.db_session).search('Initial_Contact', task.initial_contact_id)
        if not initial_contact:
            return 'No initial_contact_found', 404
        
        response, status = DBOperations(g.db_session).update({'Task': task_dict})
        if status != 200:
            g.db_session.rollback()
            return response, status

        # Change read columns for initial_contact if  task status change
        if 'status' in data:
            new_status = data['status']

            # Notify contact_receiver(promo owner)
            if old_task_status == 'pending' and new_status == 'open':
                read_recipient = 'receiver_read'

            # Notify sender, the task was marked as closed
            elif old_task_status == 'open' and new_status == 'closed':
                read_recipient = 'sender_read'

            response, status = DBOperations(g.db_session).update('Initial_Contact', {'id': initial_contact.id, read_recipient: False})
            if status != 200:
                g.db_session.rollback()
                return make_response(jsonify({'error': 'Could not change read values for initial contact'}), 500)

        g.db_session.commit()    
        return make_response(jsonify({'results': 'ok'}), 200)
    #-------------------------------------------------------------------------------------------
    # ----------------------POST--------------------------------------------------------------
    if request.method == 'POST':
        data = request.get_json()
        # data = {
        #     'initial_contact_id': '65fb8bf8-3495-44ab-a806-cbecd3953c9a',
        #     'terms': 'Montar Equipo|Sesion de 3 horas',
        #     'price': 200
        #     }
        keys = [
            'initial_contact_id',
            'terms',
            'price'
            ]
        models = {
            'Promotion': 'promo_id',
            'Request': 'request_id'
            }

        # Error handlers
        if 'status' in data:
            return make_response(jsonify({'error': 'status cannot be used'}), 400)
        for key in keys:
            if key not in data:
                return make_response(jsonify({'error': f'Missing key: {key}'}), 400)

        # Get all info needed from the initial contact to create the task
        initial_contact = DBOperations(g.db_session).search('Initial_Contact', data['initial_contact_id'])
        if not initial_contact:
            return make_response(jsonify({'error': f"No such intial_contact {data['initial_contact_id']}"}), 400)

        if initial_contact.promo_id:
            model_type = 'Promotion'
            model_id = initial_contact.promo_id
        else:
            model_type = 'Request'
            model_id = initial_contact.request_id

        promo_or_request = DBOperations(g.db_session).search(model_type, model_id)
        if not promo_or_request:
            return make_response(jsonify({'error': f'No such {model_type}'}), 400)

        # Values for the task object assigned here below
        # If promotion, the contact was made by user that saw the Promotion(sender of initial_contact)
        #If Request, the contact was made by the user that saw the Request(sender of initial_contact)
        service_id = promo_or_request.service_id
        description = data['terms']
        initial_contact_id = data['initial_contact_id']
        price = data['price']

        if model_type == 'Promotion':
            service_providerID = promo_or_request.user_id
            service_receiverID = initial_contact.sender_id
        else:
            service_providerID = initial_contact.sender_id
            service_receiverID = promo_or_request.user_id
        
        dict_for_task = {
            'provider_id': service_providerID,
            'receiver_id': service_receiverID,
            'service_id': service_id,
            'description': description,
            'initial_contact_id': initial_contact_id,
            'price': price,
            models[model_type]: model_id
        }

        response, status = DBOperations(g.db_session).new({'Task': dict_for_task})
        if status != 201:
            return make_response(jsonify(response), status)
        g.db_session.commit()
        return make_response(jsonify({'results': 'ok'}), 201)
