#!/usr/bin/python3
"""
SAERCH FILET USING QUERY
"""

import time  # Import the time module
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import User, Service, Town, UserServiceAssoc, BaseModel # Add Town import

if __name__ == "__main__":

    classes_dict = {'User': User, 'Service': Service}
    # Create the engine
    engine = create_engine('postgresql://postgres:9150@localhost/postgres', echo=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Dummy data
    data = {'Service': {'name': 'Auto Body Painting', 'town': 'All'}}
    town_name = "All"
    data_dict = data['Service']

    if 'town' in data_dict:
        town_name = data_dict['town']
    if 'name' in data_dict:
        service_name = data_dict['name']
    else:
        print('no service name provided') 
    print(town_name)
    service = session.query(Service).filter_by(name = service_name).first()
    my_service_id = service.id

    start_time = time.time()  # Start time measurement

    if town_name == 'All':
        print("Doing all")
        rows = session.query(UserServiceAssoc.user_id,User.first_name, User.last_name, func.array_agg(Town.name)) \
        .join(Town) \
        .join(User)\
        .filter(UserServiceAssoc.service_id == my_service_id) \
        .group_by(UserServiceAssoc.user_id, User.first_name, User.last_name) \
        .order_by(UserServiceAssoc.user_id) \
        .all()
    else:
        print("Doing Specific town")
        rows = session.query(UserServiceAssoc.user_id,User.first_name, User.last_name, func.array_agg(Town.name)) \
        .join(Town) \
        .join(User)\
        .filter((UserServiceAssoc.service_id == my_service_id) & (Town.name == town_name)) \
        .group_by(UserServiceAssoc.user_id, User.first_name, User.last_name) \
        .order_by(UserServiceAssoc.user_id) \
        .all()

    my_dict = {}

    for row in rows:
        user_id = row.user_id
        first_name = row.first_name
        last_name = row.last_name
        town_names = row[3]  # Assuming the array of town names is at index 3
        inner_dict = {
            'service': service_name,
            'first_name': first_name,
            'last_name': last_name,
            'towns': town_names
        }
        my_dict[user_id] = inner_dict

    print(f"MY DICTIONARY: {my_dict}")
    end_time = time.time()  # End time measurement
    elapsed_time = end_time - start_time  # Calculate elapsed time

    print("Query execution time:", elapsed_time, "seconds")

    session.close()
