#!/usr/bin/python3
'''
    Important READ:
    Working here, this file will manage all related S3 bucket
    operations to create folder, delete pictures from profile,
    read all pictures.
    To change user id go down at the end where the function is called
'''
import boto3
from botocore.exceptions import ClientError

# Specify your AWS credentials and region
aws_access_key_id = 'AKIA4MTWIBZ4HIVJ6NWI'
aws_secret_access_key = 'GTpG38b2yUeu+VkFew+nxScVY7IVfOjyK3p43k56'
region_name = 'us-east-2'

# Initialize the S3 client
s3_client = boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name)

def create_user_folder(user_id: str = None) -> None:
    '''
    Creates user's folder structure in an AWS S3 bucket when a user is added to the database.

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

    # user_folder will always have the '/' at the end
    user_folder = f'users/{user_id}/'
    profile_folder = f'{user_folder}profile/'
    promotions_folder = f'{user_folder}promotions/'
    requests_folder = f'{user_folder}requests/'
    tasks_folder = f'{user_folder}tasks/'
    reviews_folder = f'{user_folder}reviews/'

    # All folders to create
    folders = [user_folder,
               profile_folder,
               promotions_folder,
               requests_folder,
               tasks_folder,
               reviews_folder
               ]

    for folder in folders:
        try:

            # Attempt a head_object to check if it already exists
            s3_client.head_object(Bucket=bucket_name, Key=folder)
            print(f"Folder '{folder}' already exists.")

        except ClientError as e:

            if e.response['Error']['Code'] == "404":
                print(f'\n{folder} doesnt exist.\nCreating folder\n')

                # Put_object creates objects in the aws specified path
                response = s3_client.put_object(Bucket=bucket_name, Key=folder)

                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print(f"Folder '{folder}' created in bucket '{bucket_name}'.")
                else:
                    print(f"Failed to create {folder}")
                    return {'response': f'Failed To Create {folder}'}

    return profile_folder # Reurns the path of the profile folder

def get_picture(user_id: str, model: str, key: str) -> dict:
    """
    Retrieve an object (picture) from an AWS S3 bucket based on the specified user ID, model (folder),
    and key (object key/path).

    Parameters:
    - user_id (str): User identifier used to construct the folder path.
    - model (str): Model or folder name where the object is stored (e.g., 'Promotion').
    - key (str): Key or path of the object within the specified model's folder.

    Returns:
    - dict: A dictionary containing the response status or retrieved object details.

    Usage:
    Call this function with the user ID, model name, and key to retrieve an object from the S3 bucket.
    - Example: get_picture('101', 'Promotion', '001/Palitas_logo_pitch.png')
    """

    folders_dict = {
        'Promotion': f'user.{user_id}/promotions/{key}',
        'Request': f'user.{user_id}/requests/{key}',
        'Task': f'user.{user_id}/tasks/{key}',
        'Review': f'user.{user_id}/reviews/{key}'
        }
    if model in folders_dict:
        path = f'users/{folders_dict[model]}' # This pastes users/user.101/promotions/001/Palitas_logo_pitch.png
    else:
        return {'response': 'Model(Folder) does not not exist'}
    try:
        # Attempt to get the object
        response = s3_client.get_object(Bucket='palitas-pics', Key=path)
        
        return {'response': response}

    except ClientError as e:

        if e.response['Error']['Code'] == 'NoSuchKey':
            # Object does not exist, return an empty response
            return {'response': 'Picture not found'}
        else:
            # Other error occurred, raise or handle accordingly
            return {'response': e.response['Error']['Code']}

def create_model_folder(user_id: str, model: str, model_id: str) -> dict:
    '''
    Create a folder structure in an AWS S3 bucket based on a specified model Python class (Promotion, Request, Task, Review).

    Parameters:
    - user_id (str): The ID of the user associated with the model.
    - model (str): The type of model (e.g., 'Promotion', 'Request', 'Task', 'Review').
    - model_id (str): The ID of the specific model instance.

    Returns:
    - dict: A dictionary containing a response message indicating the outcome of the folder creation.

    Example Usage:
    - When a Promotion, Request, or Review is created in the database, this function is called to create corresponding folders in AWS S3.

    AWS S3 Folder Structure:
    - Root: users/<user_id>/
    - Subfolders:
      - promotions/<model_id>/
      - requests/<model_id>/
      - tasks/<model_id>/
      - reviews/<model_id>/

    '''
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
            folder_to_make = f'users/{user_id}/{models_dict[model]}/{model_id}/'

            # Attempt a head_object to check if user folder exists
            s3_client.head_object(Bucket='palitas-pics', Key=user_folder)
            print(f"Folder '{user_folder}' exists.")
            print(f'Making /{model}/{model_id}/ folder now')

        except ClientError as e:
            # User base folder for the model doesnt exist
            if e.response['Error']['Code'] == "404":
                print(f'\nRoot folder {user_folder} doesnt exist.\n')
                return {'response': f'Root Folder {user_folder} doesnt exist'}

        # Proceed to make model folder /model/<model_id/
        try:

            # STEP 2: Check if model folder /model/<model_id> exists
            s3_client.head_object(Bucket='palitas-pics', Key=folder_to_make)
            print(f"Folder '{folder_to_make}' exists. Do not overwrite.")
            return {'response': f'Folder {folder_to_make} exists. Do not overwrite.'}

        except ClientError as e:
            # Create folder since it doesnt exist
            if e.response['Error']['Code'] == "404":
                response = s3_client.put_object(Bucket='palitas-pics', Key=folder_to_make)

                # Check the response to determine the outcome
                if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                    print(f"Folder '{folder_to_make}' created successfully''.")
                    return {'response': 'ok'} # Folder created OK
                else:
                    print(f"Failed to create folder '{folder_to_make}")
                    return {'response': f'Failed to create folder {folder_to_make}'}

    else:
        print(f'{model} doesnt exist in: {models_dict}')
        return {'response': f'{model} doesnt exist in: {models_dict}'}
