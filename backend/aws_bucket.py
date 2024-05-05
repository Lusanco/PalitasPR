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
        TESTING WILLL ONLY RETURN PROFILE PATH
        Creates user's folder, ideally when user is added to database.
        Returns folders to store the paths on the database.
        Makes the folders in aws for:
        1) users/user.id/
        2) users/user.id/reviews/
        3) users/user.id/profile/
        4) users/user.id/tasks/

        Folders in aws need to finish with the '/'
    '''
    bucket_name = 'palitas-pics' # Root for all folders

    # user_folder will always have the '/' at the end
    user_folder = f'users/user.{user_id}/'
    reviews_folder = f'{user_folder}reviews/'
    profile_folder = f'{user_folder}profile/'
    tasks_folder = f'{user_folder}tasks/'

    folders = [user_folder, reviews_folder, profile_folder, tasks_folder]

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
                    print(f"Folder '{user_folder}' created in bucket '{bucket_name}'.")
                else:
                    print(f"Failed to create {user_folder}")
                    return
    return profile_folder
# def delete_object(user_id: str = None, object_path: str = None) -> None:
#     '''
#         Delete objects from a specified user.
#         Example: User 004 wants to delete his picture in folder /profile/pic.01
#     '''
#     bucket_name = 'palitas-pics'
<<<<<<< HEAD

#     user_folder = f'users/user.{user_id}/'
#     reviews_folder = f'{user_folder}reviews/'
#     profile_folder = f'{user_folder}profile/'
#     tasks_folder = f'{user_folder}tasks/'

#     try:

#             # Attempt a head_object to check if it already exists
#             s3_client.head_object(Bucket=bucket_name, Key=folder)
#             print(f"Folder '{folder}' already exists.")

#         except ClientError as e:

#             if e.response['Error']['Code'] == "404":
#                 print(f'\n{folder} doesnt exist.\nCreating folder\n')

#                 # Put_object creates objects in the aws specified path
#                 response = s3_client.put_object(Bucket=bucket_name, Key=folder)

=======

#     user_folder = f'users/user.{user_id}/'
#     reviews_folder = f'{user_folder}reviews/'
#     profile_folder = f'{user_folder}profile/'
#     tasks_folder = f'{user_folder}tasks/'

#     try:

#             # Attempt a head_object to check if it already exists
#             s3_client.head_object(Bucket=bucket_name, Key=folder)
#             print(f"Folder '{folder}' already exists.")

#         except ClientError as e:

#             if e.response['Error']['Code'] == "404":
#                 print(f'\n{folder} doesnt exist.\nCreating folder\n')

#                 # Put_object creates objects in the aws specified path
#                 response = s3_client.put_object(Bucket=bucket_name, Key=folder)
>>>>>>> development/backend
