#!/usr/bin/python3
"""
    THIS IS IS FOR INSERTING DATA INTO TABLES
    FEEL FREE TO MODIFY AND INSERT ANY DATA
    USE KWARGS ONLY AT THE MOMENT WHEN INSERTING
    EXAMPLE: new_user = User(**{att_name: att_value})
"""

import time  # Import the time module
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Service, Town, UserServiceAssoc # Add Town import

if __name__ == "__main__":
    start_time = time.time()  # Record start time

    # Create the engine
    engine = create_engine('postgresql://postgres:9150@localhost/postgres', echo=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Perform the query
    users = session.query(User).all()
    for user in users:
        rows = user.user_service_assoc
        if rows:
            print("User:")
            print(f"{user.first_name} -{user.email}- provides: ")
            for row in rows:
                print(f"{row.service.name} in {row.town.name}")

    # Close the session
    session.close()

    end_time = time.time()  # Record end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Script execution time: {elapsed_time} seconds")
