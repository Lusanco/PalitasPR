#!/usr/bin/python3
"""
    ALLOWS OPERATIONS FOR FRONT END DEVS
    THIS FILE WILL BRIDGE OUR CLASSES AND FLASK
    USING LOCAL POSTGRES DB NEED TO CHAMGE TO AWS

"""
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from unidecode import unidecode
from aws_bucket import create_model_folder
from db_init import get_session
from aws_bucket import delete_model_folder
from models import (
    User,
    Service,
    Town,
    Promo_Towns,
    Review,
    Task,
    Promotion,
    Request,
    Request_Towns,
    Promotion,
    Profile,
) 


class DBOperations:

    classes_dict = {
                'User': User,
                'Service': Service,
                'Town': Town,
                'Promo_Towns': Promo_Towns,
                'Request_Towns': Request_Towns,
                'Review': Review,
                'Task': Task,
                'Promotion': Promotion,
                'Request': Request,
                'Profile': Profile
                }

    def __init__(self):
        self.session = get_session()

    def new(self, front_data):
        """
        Create a new instance of a model and save it to the database.

        Args:
            front_data (dict): A dictionary containing the model name as key and its attributes as value.

        Returns:
            dict: A dictionary with the created object if successful, or an error message.

        Example:
            front_data = {'User': {'name': 'John Doe', 'email': 'john@example.com', 'password': '12345'}}
        """
        if front_data is None:
            return None

        model_name, inner_dict = list(front_data.items())[0]
        model_class = self.classes_dict.get(model_name)

        if not model_class:
            return {'error': 'Not valid class'}, 400
        
        new_object = model_class(**inner_dict)
        self.session.add(new_object)

        try:
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            print(e)
            return ({"Error": "Error"}, 500)

        # check if object needs aws folder
        aws_folders = {Promotion: "Promotion", Request: "Request", Review: "Review"}
        if model_class in aws_folders:
            response = create_model_folder(
                new_object.user_id, aws_folders[model_class], new_object.id
            )
            if response[1] != 201:
                self.session.rollback()
                return response

        return ({'results': new_object}, 201)

    def update(self, data):
        """
        Update an object in the database based on the provided data.

        usage: data = {
                "User": {
                    "id": 123,
                    "name": "New Name",
                    "email": "newemail@hotmail.com"
                }
            }
        """
        class_name = list(data.keys())[0]
        if class_name in self.classes_dict:
            update_dict = {}
            update_dict.update(data[class_name])

            obj_id = update_dict.pop("id", None)

            if obj_id:
                model_class = self.classes_dict[class_name]
                obj = self.session.query(model_class).filter_by(id=obj_id).first()

                if obj:
                    for key, value in update_dict.items():
                        if hasattr(model_class, key):
                            setattr(obj, key, value)
                        else:
                            print(f"Attribute '{key}' not found in {class_name} model.")

                    self.session.commit()
                    print(f"{class_name} object with ID {obj_id} updated successfully.")
                else:
                    print(f"{class_name} object with ID {obj_id} not found.")
            else:
                return ({"message": "Object ID not provided."}, 400)
        else:
            return ({"message": "Class not found"}, 400)
        return ({"message": "ok"}, 200)


    # def confirm_password(self, user_obj, password):
    #     """
    #     Confirm the password for the given user object.
    #     """

    #     hashed_password = user_obj.password.encode("utf-8")

    #     if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
    #         return True
    #     else:
    #         return False

    def search(self, class_name, obj_id):
        """
        Search for an object based on its class model and ID.

        usage: class_name="User", obj_id=001
        """
        if class_name in self.classes_dict:
            model_class = self.classes_dict[class_name]
            obj = self.session.query(model_class).filter_by(id=obj_id).first()
            if obj:
                return obj
            else:
                return None
        else:
            return None


    def delete_object(self, model, model_id, user_id):
            """
            Delete a promotion, request, or picture associated with the user.
            """
            allowed_models = ['Promotion', 'Request', 'Profile']
            if model not in allowed_models:
                return {'error': 'Invalid model'}, 400

            # if model == 'Profile':
            #     # Handle deletion of the user's profile
            #     profile_obj = self.session.query(Profile).filter_by(id=user_id).first()
            #     if not profile_obj:
            #         return {'error': f'No profile found for user {user_id}'}, 404

            #     try:
            #         self.session.delete(profile_obj)
            #         self.session.commit()
            #     except SQLAlchemyError as e:
            #         self.session.rollback()
            #         return {'error': str(e)}, 500

            #     try:
            #         # Delete user's profile folder from AWS S3
            #         delete_model_folder(user_id, 'Profile', user_id)
            #     except Exception as e:
            #         return {'error': str(e)}, 500

            #     return {'message': 'Profile deleted successfully'}, 200

            model_class = self.classes_dict.get(model)
            if not model_class:
                return {'error': f'No model found with name {model}'}, 400

            obj = self.session.query(model_class).filter_by(id=model_id, user_id=user_id).first()
            if not obj:
                return {'error': f'No {model} found with ID {model_id} for user {user_id}'}, 404

            try:
                self.session.delete(obj)
                self.session.commit()
            except SQLAlchemyError as e:
                self.session.rollback()
                return {'error': str(e)}, 500

            if model in ['Promotion', 'Request', 'Profile']:
                try:
                    delete_model_folder(user_id, model, model_id)
                except Exception as e:
                    return {'error': str(e)}, 500

            return {'message': f'{model} with ID {model_id} deleted successfully'}, 200


    # async def reset_password(self, data):
    #     """
    #     Reset password for a user.
    #     """
    #     session = get_session()
    #     email = data.get('email')
    #     try:
    #         valid = validate_email(email)
    #         email = valid.email
    #     except EmailNotValidError:
    #         return {"error": "Invalid email"}

    #     user = session.query(User).filter_by(email=email).first()
    #     if not user:
    #         return {"error": "User not found"}

    #     hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    #     user.pwd = hashed
    #     session.add(user)

    #     try:
    #         session.commit()
    #     except SQLAlchemyError as e:
    #         session.rollback()
    #         print(e)
    #         return {"error": "Password reset failed"}, 500

    #     asyncio.create_task(send_confirm_email(user.email, "Your password has been reset"))
    #     return {"result": "Password reset successfully"}, 200


    # async def my_reviews(self, user_id):
    #     """
    #     Retrieve reviews for a user.
    #     """
    #     session = get_session()
    #     rows = session.query(
    #         Review.id,
    #         Review.comment,
    #         Review.rating,
    #         Review.created_at,
    #         Service.name,
    #     ).select_from(Review).join(Service, Review.service_id == Service.id).filter(
    #         Review.user_id == user_id
    #     ).order_by(Review.created_at).all()

    #     return [{"id": row.id, "comment": row.comment, "rating": row.rating, "created_at": row.created_at, "service": row.name} for row in rows]