#!/usr/bin/python3
'''
    All related S3 AWS Bucket operations.
    C.R.U.D operations.

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


def create_model_folder(user_id: str, model: str, model_id: str) -> dict:
    '''
    Create a folder structure in an AWS S3 bucket based on a specified model Python class (Promotion, Request, Task, Review).

    Parameters:
    - user_id: The ID of the user associated with the model.
    - model: The type of model (e.g., 'Promotion', 'Request', 'Task', 'Review').
    - model_id: The ID of the specific model instance.

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
            print(f"User Root Folder '{user_folder}' exists.")
            print(f'Making /{models_dict[model]}/{model_id}/ folder now')

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


def get_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict:
    """
    Retrieve an object (picture) from an AWS S3 bucket based on the specified user ID, model (Promotion, Request, Task, Review),
    and pic_name (object pic_name/path).

    Parameters:
    - user_id: User identifier used to construct the folder path.
    - model: Model or folder name where the object is stored (e.g., 'Promotion').
    - model_id: Model or folder name where the object is stored (e.g., 'Promotion').
    - pic_name: pic_name or path of the object within the specified model's folder.

    Returns:
    - dict: A dictionary containing the response status or retrieved object details.

    Usage:
    Call this function with the user ID, model name, and pic_name to retrieve an object from the S3 bucket.
    - Example: get_picture('101', 'Promotion', '001', 'Palitas_logo_pitch.png')
    """

    models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}'
        }
    if model in models_dict:
        path = f'users/{models_dict[model]}' # This pastes users/101/promotions/001/Palitas_logo_pitch.png
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


def delete_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict:
        """
        Delete a picture from an AWS S3 bucket based on the specified user ID, model,model_id and pic_name.

        Parameters:
        - user_id: User identifier used to construct the folder path.
        - model: Model or folder name where the object is stored (example: 'Promotion' = /promotions/).
        - model_id: Model or folder name where the object is stored (e.g., 'Promotion').
        - pic_name: pic_name or path of the object within the specified model's folder (promotions/<pic_name>)

        Returns:
        - dict: A dictionary containing the response status of the delete operation.

        Usage:
        Call this function with the user ID, model name, and pic_name to delete an object from the S3 bucket.
        - Example: delete_picture('101', 'Promotion', '001/Palitas_logo_pitch.png')
        """

        # Define the models and their respective paths
        models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}'
        }
    
        if model in models_dict:
            path = f'users/{models_dict[model]}'  # Construct the full path of the object
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

def put_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict:
        """
        Delete a picture from an AWS S3 bucket based on the specified user ID, model, model_id and pic_name.

        Parameters:
        - user_id: User identifier used to construct the folder path.
        - model: Model or folder name where the object is stored (example: 'Promotion' = /promotions/).
        - model_id: Model or folder name where the object is stored (e.g., 'Promotion').
        - pic_name: pic_name or path of the object within the specified model's folder (promotions/<pic_name>)

        Returns:
        - dict: A dictionary containing the response status of the delete operation.

        Usage:
        Call this function with the user ID, model name, and pic_name to delete an object from the S3 bucket.
        - Example: delete_picture('101', 'Promotion', '001/Palitas_logo_pitch.png')
        """

        # Define the models and their respective paths
        models_dict = {
        'Promotion': f'{user_id}/promotions/{model_id}/{pic_name}',
        'Request': f'{user_id}/requests/{model_id}/{pic_name}',
        'Task': f'{user_id}/tasks/{model_id}/{pic_name}',
        'Review': f'{user_id}/reviews/{model_id}/{pic_name}'
        }
        # Check if the specified model is valid
        if model in models_dict:
            path = f'users/{models_dict[model]}'  # Construct the full path of the object
        else:
            return {'response': 'Model (Folder) does not exist'}

        # Check if object exists
        try:
            s3_client.head_object(Bucket='palitas-pics', Key=path)
            print(f'Object -{path}- already exists')
            return {'response': f'Object {path} already exists'}

        except ClientError as e: # Not found object, proceed to put

            if e.response['Error']['Code'] == "404":
                try:
                    # Attempt to put object
                    print(f'\nPAth to put object: {path}\n')
                    response = s3_client.put_object(Bucket='palitas-pics', Key=path)
                    return {'response': 'ok'}

                except ClientError as e:
                    # Handle the specific error codes
                    if e.response['Error']['Code'] == 'NoSuchKey':
                        return {'response': 'Object not found'}
                    else:
                        return {'response': e.response['Error']['Code']}
