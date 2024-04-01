#!/usr/bin/python3
"""
Update data from a user
"""

import time  # Import the time module
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Service, Town, UserServiceAssoc, BaseModel # Add Town import

if __name__ == "__main__":
    start_time = time.time()  # Record start time
    classes_dict = {'User': User, 'Service': Service}
    # Create the engine
    engine = create_engine('postgresql://postgres:9150@localhost/postgres', echo=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Simulate front end data
    data = {'User': {'id': '6864b3ff-2b3d-4e7e-8410-f6755b44f9eb', 'last_name': 'Snow'}}
    
    class_name = list(data.keys())[0] # First key class name
    if class_name in classes_dict:
        update_dict = {}
        update_dict.update(data[class_name])

        # User id from dict of front data
        if 'id' in update_dict:
            user_id = update_dict['id']
            update_dict.pop('id')
        else:
            print("Id not found")

        # Perform the query
        user = session.query(classes_dict[class_name]).filter_by(id=user_id).first()

        user_columns = user.all_columns()
        user_columns.update(update_dict)

        for key, value in user_columns.items():
            setattr(user, key, value)

        # Commit the changes to the database
        session.commit()
        print(user_columns)
        # Close the session
    else:
        print("Class Not Found")
    session.close()

    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Script execution time: {elapsed_time} seconds")
