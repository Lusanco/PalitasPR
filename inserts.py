#!/usr/bin/python3
"""
    THIS IS IS FOR INSERTING DATA INTO TABLES
    FEEL FREE TO MODIFY AND INSERT ANY DATA
    USE KWARGS ONLY AT THE MOMENT WHEN INSERTING
    EXAMPLE: new_user = User(**{att_name: att_value})
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import User, Service  # Change to absolute import

if __name__ == "__main__":
    # Create the engine
    engine = create_engine('postgresql://postgres:9150@localhost/postgres', echo=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # INSERT into table ONLY KWARGS
    new_user = User(**{'first_name': "Juan", 'last_name': "Melendez"})

    # appending 'Nails' service to user, user can have more than one service
    service = session.query(Service).filter_by(name="Gardening").first()
    new_user.services.append(service)
    
    session.add(new_user)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
