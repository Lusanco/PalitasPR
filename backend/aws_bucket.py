#!/usr/bin/python3
'''
    All related S3 AWS Bucket operations.
    C.R.U.D operations.

'''
import boto3
from botocore.exceptions import ClientError
from typing import Tuple, Dict

# Specify your AWS credentials and region
aws_access_key_id = 'AKIA4MTWIBZ4HIVJ6NWI'
aws_secret_access_key = 'GTpG38b2yUeu+VkFew+nxScVY7IVfOjyK3p43k56'
region_name = 'us-east-2'

# Initialize the S3 client
s3_client = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name)

def create_user_folder(user_id: str = None) -> Tuple[Dict[str, str], int]:
    '''
    Creates user's folder structure in an AWS S3 bucket when a user is verified.

    Parameters:
    - user_id (str): The ID of the user for whom the folder structure will be created.

    Returns:
    - str: The path of the profile folder created for the user column profile_pic(for now testing)

    Example:
    - When a new user is added to the database, this function is called to create the necessary folder structure in AWS S3.

    AWS S3 Folder Structure:
    - Root: users/<user_id>/
    - Subfolders:
      - profile/
      - promotions/
      - requests/
      - tasks/
      - reviews/

    Note:
    - Folders in AWS S3 must end with '/'.

    '''
    bucket_name = 'palitas-pics' # Root for all folders

    if user_id is None:
        return ({'error': 'no user id provided'}, 400) # OK

    # user_folder will always have the '/' at the end
    user_folder = f'users/{user_id}/'
    profile_folder = f'{user_folder}profile/'
    promotions_folder = f'{user_folder}promotions/'
    requests_folder = f'{user_folder}requests/'
    tasks_folder = f'{user_folder}tasks/'
    reviews_folder = f'{user_folder}reviews/'
    gallery_folder = f'{user_folder}gallery/'

    # All folders to create
    folders = [user_folder,
               profile_folder,
               promotions_folder,
               requests_folder,
               tasks_folder,
               reviews_folder,
               gallery_folder
               ]

    for folder in folders:
        try:

            # Attempt a head_object to check if folder doesnt exist
            s3_client.head_object(Bucket=bucket_name, Key=folder)
            print(f"Folder '{folder}' already exists.")
            return ({'error':f'Folder {folder} already exists'}, 400)

        except ClientError as e:
            # Proceed to create folders
            if e.response['Error']['Code'] == "404":
                print(f'\nCreating folder: {folder}\n')

                # Create folder
                response = s3_client.put_object(Bucket=bucket_name, Key=folder)

                if response['ResponseMetadata']['HTTPStatusCode'] != 200:
                    print(f"Failed to create {folder}")
                    return ({'error': f'AWS Failed To Create  {folder}'}, 500)

    return ({'results': 'Created AWS folders'}, 201) # OK


def create_model_folder(user_id: str, model: str, model_id: str):
    '''
    Create a folder in AWS S3 bucket based on a specified model Python class (Promotion, Request, Task, Review)
    This is for making the folder of a new <Promotion> or <Request> as an example...
    After this folder is created we can put the pictures inside

    Example folder for new Promotion;
    users/007/promotion/<model_id/

    Example Usage:
     - Example: delete_picture('101', 'Promotion', '001')
    '''
    print(f'\n\nInside createfolder: user_id:{user_id}, model:{model}, model_id:{model_id}\n\n')
    models_dict = {
        'Promotion': 'promotions',
        'Request': 'requests',
        'Task': 'tasks',
        'Reviews': 'reviews'
        }
    if model in models_dict:
        try:

            # STEP 1: Check if user root folder exists <user_id>/model/
            user_folder = f'users/{user_id}/{models_dict[model]}/'
            if model != 'Gallery' and model != 'Profile':
                folder_to_make = f'users/{user_id}/{models_dict[model]}/{model_id}/'
            else:
                folder_to_make = f'users/{user_id}/{models_dict[model]}/'

            # Attempt a head_object to check if user folder exists
            s3_client.head_object(Bucket='palitas-pics', Key=user_folder)
            print(f"User Root Folder '{user_folder}' exists.")
            if model != 'Gallery' and model != 'Profile':
                print(f'Making /{models_dict[model]}/{model_id}/\n')
            else:
                print(f'Making /{models_dict[model]}/\n')

        except ClientError as e:
            # User base folder for the model doesnt exist
            if e.response['Error']['Code'] == "404":
                print(f'\nRoot folder {user_folder} doesnt exist.\n')
                return ({'error': f'Root Folder {user_folder} doesnt exist'}, 404)

        # Proceed to make model folder /model/<model_id/
        try:

            # STEP 2: Check if model folder /model/<model_id> exists
            s3_client.head_object(Bucket='palitas-pics', Key=folder_to_make)
            print(f"Folder '{folder_to_make}' exists. Do not overwrite.")
            return ({'error': f'Folder {folder_to_make} exists. Do not overwrite.'}, 400)

        except ClientError as e:
            # Create folder since it doesnt exist
            if e.response['Error']['Code'] == "404":
                response = s3_client.put_object(Bucket='palitas-pics', Key=folder_to_make)

                # Check the response to determine the outcome
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print(f"Folder '{folder_to_make}' created successfully''.")
                    return ({'results': 'ok'}, 201) # Folder created OK
                else:
                    print(f"Failed to create folder '{folder_to_make}")
                    return ({'error': f'Failed to create folder {folder_to_make}'}, 500)

    else:
        print(f'{model} doesnt exist in: {models_dict}')
        return ({'error': f'{model} doesnt exist in: {models_dict}'}, 400)


def get_picture(user_id: str, model: str, model_id: str, pic_name: str):
    """
    Retrieve a picture from an AWS S3 bucket.
    and pic_name (object pic_name/path).

    Usage:
    Call this function with the user ID, model name, model_id, and pic_name to retrieve a picture from the S3 bucket.
    - Example: get_picture('101', 'Promotion', '001', 'Palitas_logo_pitch.png')
    """

    models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}',
        'Gallery': f'{user_id}/gallery/{pic_name}',
        'Profile': f'{user_id}/profile/{pic_name}',
        }
    if model in models_dict:
        path = f'users/{models_dict[model]}' # This pastes users/101/promotions/001/Palitas_logo_pitch.png
    else:
        return ({'response': 'Model(Folder) does not not exist'}, 400)
    try:
        # Attempt to get the object
        response = s3_client.get_object(Bucket='palitas-pics', Key=path)
        
        return ({'results': response}, 200)

    except ClientError as e:

        if e.response['Error']['Code'] == 'NoSuchKey':
            # Object does not exist, return an empty response
            return ({'error': 'Picture not found'}, 400)
        else:
            # Other error occurred, raise or handle accordingly
            return ({'error': 'Internal error aws'}, 500)


def delete_picture(user_id: str, model: str, model_id: str, pic_name: str):
        """
        Delete a picture from an AWS S3 bucket based on the specified user ID, model,model_id and pic_name.

        Usage:
        Call this function with the user ID, model name, and pic_name to delete an object from the S3 bucket.
        - Example: delete_picture('101', 'Promotion', '001/Palitas_logo_pitch.png')
        """

        # Define the models and their respective paths
        models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}',
        'Profile': f'{user_id}/profile/{pic_name}',
        'Gallery': f'{user_id}/gallery/{pic_name}' 
        }

        if model in models_dict:
            path = f'users/{models_dict[model]}'  # Construct the full path of the picture
        else:
            return {'response': 'Model (Folder) does not exist'}

        # Check if object exists
        try:
            s3_client.head_object(Bucket='palitas-pics', Key=path)
            print(f'Object found {path}')

        except ClientError as e: # Not found object

            if e.response['Error']['Code'] == "404":
                return {'response': f'No object found {path}'}


        try:
            # Attempt to delete the object from the S3 bucket
            print(f'\nPAth to delete object from: {path}\n')
            response = s3_client.delete_object(Bucket='palitas-pics', Key=path)
            return {'response': 'ok'}

        except ClientError as e:
            # Handle the specific error codes
            if e.response['Error']['Code'] == 'NoSuchKey':
                return {'response': 'Object not found'}
            else:
                return {'response': e.response['Error']['Code']}

def put_picture(user_id: str, model: str, model_id: str, pic_name: str, content: bytes):
        """
        Put a picture from AWS S3 bucket based on the specified user ID, model, model_id and pic_name, pic <bytes>

        Usage:
        Call this function with the user ID, model name, and pic_name to delete an object from the S3 bucket.
        - Example: delete_picture('101', 'Promotion', '001/Palitas_logo_pitch.png', <bytes>)
        """

        # Define the models and their respective paths
        models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}',
        'Gallery': f'{user_id}/gallery/{pic_name}',
        'Profile': f'{user_id}/profile/{pic_name}'
        }
        # Oonstruct path of picture
        if model in models_dict:
            path = f'users/{models_dict[model]}'  # Construct the full path of the object
        else:
            return ({'error': 'Model (Folder) does not exist'}, 400)

        # Check if picture doesnt exist already, we will not overwrtie pictures yet...
        try:
            s3_client.head_object(Bucket='palitas-pics', Key=path)
            print(f'Object -{path}- already exists')
            return ({'response': f'Object {path} already exists'}, 400)

        except ClientError as e: # 
            if e.response['Error']['Code'] == "404":
                try:
                    # Put picture
                    response = s3_client.put_object(Bucket='palitas-pics', Key=path, Body=content)
                    return ({'response': 'ok'}, 200)

                except ClientError as e:
                    # Handle the specific error codes
                    if e.response['Error']['Code'] == 'NoSuchKey':
                        return ({'response': 'Object not found'}, 404)
                    else:
                        return ({'error': 'AWS error'}, 500)
