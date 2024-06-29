#!/usr/bin/python3
"""
Command line interface for the DB Operations
"""
import cmd
import shlex
import aws_bucket
import time
import random
import asyncio
from db.db_operations import DBOperations
from db.db_promotion import Db_promotion
from db.db_user import Db_user
from db.db_core import Db_core
from db.db_task import Db_task
from db.db_review import Db_review
from db.db_promo_towns import Db_promo_towns
from db.db_request_towns import Db_request_towns
from db.db_initial_contact import Db_initial_contact
from db.db_request import Db_request
from db_init import get_session

db_session = get_session()
db = DBOperations(db_session)
db_core = Db_core(db_session)
db_user = Db_user(db_session)
db_promo = Db_promotion(db_session)
db_task = Db_task(db_session)
db_review = Db_review(db_session)
db_promo_towns = Db_promo_towns(db_session)
db_request_towns = Db_request_towns(db_session)
db_initial_contact = Db_initial_contact(db_session)
db_request = Db_request(db_session)

class DBConsole(cmd.Cmd):
    """Simple command line interpreter for DB Operations"""
    prompt = '(console) '

    def do_new(self, args):
        """
        Add a new object to the database.
        Usage: new <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: new User first_name=John last_name=Doe email=john@example.com
        """
        arg_list = shlex.split(args)
        if arg_list:
            model_name = arg_list[0]
            if model_name == 'User':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                password = input("Enter password: ")
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': password
                }
                response = db_user.sign_up(data)
                print(response)
            else:
                data = {model_name: dict(pair.split('=') for pair in arg_list[1:])}
                new_obj = db.new(data)
                if new_obj:
                    print(f"New {model_name} object created: {new_obj}")
                else:
                    print("Invalid input or model name.")
        else:
            print("Invalid input. Please provide a model name.")

    def do_filter(self, args):
        """
        Filter objects based on criteria.
        Usage: filter <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: filter User name=Gardening town=New York
        """
        on = 1
        while on == 1:
            model_name = input("Enter <promotions> or <requests>: ")
            name = input("Enter service name: ")
            town = input("Enter town ID (or 'all' for all towns): ")
            
            if town.lower() == 'all':
                town_id = 'all'
            else:
                try:
                    town_id = int(town)
                except ValueError:
                    print("Invalid town ID. Please enter a valid number or 'all'.")
                    continue

            response, status_code = db_core.landing_searchBar(model=model_name, service=name, town_id=town_id)

            if status_code == 200:
                print(f'\nFound {response["total_count"]} results:\n')
                for result in response['results']:
                    print(result)
            else:
                print(f'Error: {response["error"]}')
            
            next_action = input('\n\nIf you don\'t want to filter again, press <q>: ')
            if next_action.lower() == 'q':
                on = 0

    def do_delete(self, args):
        """
        Delete objects based on criteria.
        Usage: delete <model_name> <model_id>
        Example: delete Promotion abc123
        """
        arg_list = shlex.split(args)
        if len(arg_list) == 2:
            model_name, model_id = arg_list
            user_id = input("Enter your user ID: ")

            response, status_code = db.delete_object(model_name, model_id, user_id)
            if 'error' in response:
                print(response['error'])
            else:
                print(response['message'])
        else:
            print("Invalid input. Usage: delete <model_name> <model_id>")

    def do_update(self, args):
        """
        Update an object in the database.
        Usage: update <model_name> <id>=<object_id> <key1>=<value1> <key2>=<value2> ...
        Example: update User id=abc123 first_name=Jane last_name=Smith
        """
        arg_list = args.split()
        if arg_list:
            model_name = arg_list[0]
            data = {model_name: dict(pair.split('=') for pair in arg_list[1:])}
            result = db.update(data)
            print(result)
        else:
            print("Invalid input. Please provide a model name, object ID, and key-value pairs.")

    def do_search(self, args):
        """
        Search for an object based on its class model and ID.
        Usage: search
        """
        class_name = input("Enter the class name: ")
        obj_id = input("Enter the object ID: ")

        obj = db.search(class_name, obj_id)
        if obj:
            obj_dict = obj.all_columns()
            print (obj_dict)
        else:
            print(f"No {class_name} object found with ID {obj_id}")

    def do_login(self, args):
        """
        Validate user login.
        Usage: login <email> <password>
        Example: login john@example.com mypassword
        """
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email and password:
            db_user.login(email=email, password=password)
        else:
            print("Invalid input. Usage: login <email> <password>")

    def do_aws(self, args):
        options = {
            '1': aws_bucket.get_picture,
            '2': aws_bucket.delete_picture,
            '3': 'q'
        }

        on = 1
        while on == 1:
            print('-AWS Testing-\n')
            intro = '\nChoose a method to test:\n'
            text1 = '1)-get_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict\n'
            text2 = '2)-delete_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict\n'
            option = input(f"{intro}{text1}{text2}3) quit\n choose option:")

            if option in options:
                response = options[option]
                if option != '3':
                    print(f"Doing {option}")
                    user_id = input("Enter User_id: ")
                    model = input("Select Promotion, Request, Review: ")
                    model_id = input("Enter Model_id: ")
                    pic_name = input("Enter Pic_name: ") 
                    result = options[option](user_id, model, model_id, pic_name)
                    print(result)

                    time.sleep(2)
                    response = input('\n\nIf you dont want to test aws again again press <q>: ')

                if response == 'q':
                    print('\n-Exiting AWS Testing, returning to console, BYE-\n\n')
                    on = 0
            else:
                print('\nChoose a valid option\n')
                time.sleep(1)

    def do_1000(self, args):
        '''
            Populate with a 1000 promos, request and also towns
            Must have user id and folders in aws
        '''
        service_names = {1: 'Nails', 2: 'Gardening', 3: 'Barber'}
        for i in range(500):
            model = 'Promotion'
            service_id = random.randint(1, 3)
            title = service_names[service_id]
            my_dict = {'user_id': '05e22474-4509-483e-aae0-2456003ff273',
            'title': f'{title}-{i}',
            'description': f'description {title} {i}',
            'service_id': service_id
            }
            response, status = db.new({model: my_dict})
            if status == 201:
                objDict = response['results']
                print(objDict)
                object_id = objDict['id']
                print(f'My object id is : {object_id}')
                for x in range(10):
                    response, status = db.new({'Promo_Towns': {'town_id': random.randint(1,10),'promo_id':object_id}})
                    if status != 201:
                        print(response)
                        return
            else:
                print(response)

        for i in range(500):
            model = 'Request'
            service_id = random.randint(1, 3)
            title = service_names[service_id]
            my_dict = {'user_id': '05e22474-4509-483e-aae0-2456003ff273',
            'title': f'{title}-{i}',
            'description': f'description {title} {i}',
            'service_id': service_id
            }
            response, status = db.new({model: my_dict})
            if status == 201:
                objDict = response['results']
                object_id = objDict['id']
                for x in range(10):
                    db.new({'Request_Towns': {'town_id': random.randint(1,10), 'request_id':object_id}})
            else:
                print(response)

    def do_userAws(self, args):
        '''
            Test for aws user folder creation (all folders promo, request, review, tasks, profile)
        '''
        user_id = input("Enter User_id: ")
        print('-----------------\n')
        response = aws_bucket.create_user_folder(user_id)
        print(response)
        print('-----------------\n')
    
    def do_deleteModel(self, args):
        '''
            delete a model folder (Promotion, Request, Task, Review)
        '''
        response2 = aws_bucket.delete_model_folder('007', 'Promotion', '005')

    def do_promo_reviews(self, args):
        """
        View all reviews for a specific promotion.
        Usage: promo_reviews <promo_id>
        Example: promo_reviews abc123
        """
        arg_list = shlex.split(args)
        if len(arg_list) == 1:
            promo_id = arg_list[0]
            reviews = db_promo.get_promo_reviews(promo_id)
            if reviews:
                print(f"Reviews for Promotion ID {promo_id}:")
                for review in reviews:
                    print(f"ReviewID: {review['id']}")
                    print(f"Description: {review['description']}")
                    print(f"Rating: {review['rating']}")
                    print(f"Pictures: {review['pictures']}")
                    print(f"Created At: {review['created_at']}")
                    print("-" * 20)
            else:
                print(f"No reviews found for Promotion ID {promo_id}")
        else:
            print("Invalid input. Usage: promo_reviews <promo_id>")

    def do_usersFolders(self, args):
        '''
            after resetting database, we can create all users folders
        '''
        response = db_user.create_folders_for_allUsers()
        print(response)
        db_session.close()

    def do_search_paginated(self, args):
        """
        Search for promotions or requests with pagination.
        Usage: search_paginated
        """
        on = 1
        while on == 1:
            model = input("Enter <promotions> or <requests>: ")
            service = input("Enter service name (or press Enter for all): ")
            town = input("Enter town name (or 'all'): ")
            page = int(input("Enter page number: "))
            limit = int(input("Enter number of items per page: "))

            response, status = db_core.landing_searchBar(model, service, town, page, limit)
            
            if status == 200:
                results = response['results']
                print(f"\nFound {response['total_count']} total results.")
                print(f"Showing page {response['page']} of {response['total_pages']}")
                print(f"Results for this page: {len(results)}")
                
                for item in results:
                    print(f"\nID: {item.get('promo_id') or item.get('request_id')}")
                    print(f"Title: {item['title']}")
                    print(f"Service: {item['service']}")
                    print(f"Description: {item['description']}")
                    print(f"Towns: {item['towns']}")
                    print("-" * 40)
            else:
                print(f"Error: {response.get('error', 'Unknown error')}")

            response = input('\nTo search again, press Enter. To quit, type "q": ')
            if response.lower() == 'q':
                on = 0

    def do_get_tasks(self, args):
        """
        Get tasks for a user.
        Usage: get_tasks
        """
        user_id = input("Enter user ID: ")
        tasks = db_task.get_tasks_by_userId(user_id)
        if tasks:
            for task in tasks:
                print()
                print(task.all_columns())
                print("-" * 40)
        else:
            print(f"No tasks found for user {user_id}")

    def do_get_review(self, args):
        """
        Get a review by task ID.
        Usage: get_review <task_id>
        """
        task_id = input("Enter task ID: ")
        review = db_review.get_review_by_TaskID(task_id)
        if review:
            print()
            print(review.all_columns())
            print("-" * 40)
        else:
            print(f"No review found for task {task_id}")

    def do_get_promo_towns(self, args):
        """
        Get towns for a promotion.
        Usage: get_promo_towns <promo_id>
        """
        promo_id = input("Enter promotion ID: ")
        towns = db_promo_towns.get_towns_for_promo(promo_id)
        if towns:
            print(f"Towns for promotion {promo_id}: {', '.join(towns)}")
        else:
            print(f"No towns found for promotion {promo_id}")

    def do_get_request_towns(self, args):
        """
        Get towns for a request.
        Usage: get_request_towns <request_id>
        """
        request_id = input("Enter request ID: ")
        towns = db_request_towns.get_towns_for_request(request_id)
        if towns:
            print(f"Towns for request {request_id}: {', '.join(towns)}")
        else:
            print

    def do_exit(self, line):
        print("Goodbye!")
        return True

if __name__ == '__main__':
    try:
        DBConsole().cmdloop()
    except KeyboardInterrupt:
        print("\nProcess interrupted. Goodbye!")