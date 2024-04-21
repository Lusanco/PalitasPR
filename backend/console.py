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
        arg_list = shlex.split(args)
        if arg_list:
            model_name = arg_list[0]
            # it use sign up function if model_name is User
            if model_name == 'User':
                data = dict(pair.split('=') for pair in arg_list[1:])
                db.sign_up(data)
            else:
                data = {model_name: dict(pair.split('=') for pair in arg_list[1:])}
                new_obj = db.new(data)
                if new_obj:
                    print(f"New {model_name} object created: {new_obj}")
                else:
                    print("Invalid input or model name.")
        else:
            print("Invalid input. Please provide a model name and key-value")

    def do_filter(self, args):
        """
        Filter objects based on criteria.
        Usage: filter <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: filter User name=Gardening town=New York
        """
        arg_list = args.split()
        if arg_list:
            model_name = arg_list[0]
            data = {model_name: dict(pair.split('=') for pair in arg_list[1:])}
            filtered_objs = db.filter(data)
            print(filtered_objs)
        else:
            print("Invalid input. Please provide a model name and key-value pairs.")

    def do_delete(self, args):
        """
        Delete objects based on criteria.
        Usage: delete <model_name> <key1>=<value1> <key2>=<value2> ...
        Example: delete Service name=Gardening
        """
        arg_list = args.split()
        if arg_list:
            model_name = arg_list[0]
            data = dict(pair.split('=') for pair in arg_list[1:])
            result = db.delete(model_name, **data)
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
        arg_list = args.split()
        if len(arg_list) == 2:
            email, pwd = arg_list
            db.login(email=email, pwd=pwd)
        else:
            print("Invalid input. Usage: login <email> <password>")

    def do_quit(self, args):
        """Quit the console"""
        return True

if __name__ == '__main__':
    DBConsole().cmdloop()