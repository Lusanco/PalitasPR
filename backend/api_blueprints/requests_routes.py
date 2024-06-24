from flask import Blueprint, jsonify, make_response, g
from db.db_promotion import Db_promotion
import asyncio
from db.db_operations import DBOperations
from db.db_user import Db_user
import aws_bucket

request_bp = Blueprint('request', __name__)


@request_bp.route("/request/<id>", methods=["GET"])
def show_request(id):
    request = DBOperations(g.db_session).search('Request', id)
    if request:
        request_dict = {}
        request_dict.update(request.all_columns())
        request_dict['first_name'] = request.user.first_name
        request_dict['last_name'] = request.user.last_name
        profile = Db_user(g.db_session).get_profile_by_userId(request.user.id)
        request_dict['profile_id'] = profile.id
        picNames = request_dict['pictures']
        request_id = request_dict['id']
        user_id = request_dict['user_id']
        urls = []
        # Get all pic names
        if request_dict['pictures']:
            pic_list = picNames.split('|')

            async def handler_getPictures(pic_list, user_id, request_id):
                tasks = []

                for pic in pic_list:
                    task = asyncio.create_task(aws_bucket.get_picture_async(user_id, 'Request', request_id, pic))
                    tasks.append(task)
                awsResults = await asyncio.gather(*tasks)
                urls = [response[0]['results'] for response in awsResults if response[1] == 200]
                if not urls:
                    urls = []
                return urls

            urls = asyncio.run(handler_getPictures(pic_list, user_id, request_id))

        if len(urls) == 0:
            urls == None 

        request_dict['pictures'] = urls
        return make_response(jsonify({'results': request_dict}), 200)
    else:
        return make_response(jsonify({"error": f"No Request object found with ID {id}"}), 404)
