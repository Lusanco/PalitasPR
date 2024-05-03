#!/usr/bin/python3
"""
Command line interface for the DB Operations
"""
import cmd
import shlex
from db_operations import DBOperations

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
                new_obj = db.sign_up(data)
                if new_obj:
                    print(f"\nNew {model_name} object created: '{first_name} {last_name}' with email: '{email}'.\n")
            
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
        model_name = input("Enter model name: ")
        name = input("Enter service name: ")
        town = input("Enter town name(or all): ")

        # Constructing the filter criteria
        data = {model_name: {"name": name, "town": town}}
        
        filtered_objs = db.filter(data)
        print(f'Found {len(filtered_objs)} results:\n{filtered_objs}')
        

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

if __name__ == '__main__':
    DBConsole().cmdloop()
