#!/usr/bin/python3
"""
Command line interface for the DB Operations
"""
import cmd
import shlex
from db_operations import DBOperations
import aws_bucket
import time

db = DBOperations()

class DBConsole(cmd.Cmd):
    """Simple command line interpreter for DB Operations"""
    prompt = '(console) '

    def do_new(self, args):
        """
        Add a new object to the database.
        Usage: new <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: new User first_name=John last_name=Doe email=john@example.com
        """
        # arg_list = args.split()
        new_obj= None
        arg_list = shlex.split(args)
        if arg_list:
            model_name = arg_list[0]
            # it use sign up function if model_name is User
            if model_name == 'User':
                # Prompt for user input
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                password = input("Enter password: ")

                # Create a dictionary with the user data
                data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'password': password
                }
                response = db.sign_up(data)
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
            town = input("Enter town name(or all): ")

            
            filtered_objs = db.filter(model_name, name, town)
            print(f'\nFound {len(filtered_objs)} results:\n{filtered_objs}')
            response = input('\n\nIf you dont want to filter again press <q>: ')
            if response == 'q':
                on = 0


    def do_delete(self, args):
        """
        Delete objects based on criteria.
        Usage: delete <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: delete Service user_id=c0a5be5a-94bf-4ad8-95dc-1d6e54cb1aed name=Gardening
        """
        arg_list = shlex.split(args)
        if arg_list:
            model_name = arg_list[0]
            data = {model_name: dict(pair.split('=') for pair in arg_list[1:])}
            result = db.delete(data)
            if result:
                print("Delete successful.")
            else:
                print("Delete failed.")
        else:
            print("Invalid input. Please provide a model name and key-value pairs.")

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

    # def do_all(self, args):
    #     """
    #     Retrieve all objects in the database
    #     """
    #     class_name = input("Enter the class model: ")
    #     objs = db.search_all_objects(class_name)
    #     if objs:
    #         for obj in objs:
    #             print(obj.all_columns())
    #     else:
    #         print(f"No {class_name} objects found")

    def do_login(self, args):
        """
        Validate user login.
        Usage: login <email> <password>
        Example: login john@example.com mypassword
        """
        email = input("Enter email: ")
        password = input("Enter password: ")

        # Validate inputs and perform login
        if email and password:
            db.login(email=email, pwd=password)
        else:
            print("Invalid input. Usage: login <email> <password>")


    def do_quit(self, args):
        """Quit the console"""
        return True

    def do_aws(self, args):
        options = {
            '1': aws_bucket.get_picture,
            '2': aws_bucket.delete_picture,
            '3': 'q'
            }

        on = 1
        while on == 1:
            print('-AWS Testing-\n')  # Welcome

            # print was too long made text variables
            intro = '\nChoose a method to test:\n'
            text1 = '1)-get_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict\n'
            text2 = '2)-delete_picture(user_id: str, model: str, model_id: str, pic_name: str) -> dict\n'
            option = input(f"{intro}{text1}{text2}3) quit\n choose option:")

            if option in options:
                response = options[option] # By deafault option 3: quit
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
                print('\nChoose a valid option\n') # starts loop again
                time.sleep(1)
                

if __name__ == '__main__':
    DBConsole().cmdloop()
