#!/usr/bin/python3
"""
    THIS IS IS FOR INSERTING DATA INTO TABLES
    FEEL FREE TO MODIFY AND INSERT ANY DATA
    USE KWARGS ONLY AT THE MOMENT WHEN INSERTING
    EXAMPLE: new_user = User(**{att_name: att_value})
"""

#!/usr/bin/python3
"""
    THIS IS IS FOR INSERTING DATA INTO TABLES
    FEEL FREE TO MODIFY AND INSERT ANY DATA
    USE KWARGS ONLY AT THE MOMENT WHEN INSERTING
    EXAMPLE: new_user = User(**{att_name: att_value})
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import User, Service, Town, UserServicesAssociation # Add Town import

if __name__ == "__main__":
    # Create the engine
    engine = create_engine('postgresql://postgres:9150@localhost/postgres', echo=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the Town object for Ponce
    town = session.query(Town).filter_by(name="Ponce").first()

    # Retrieve the Service object for Gardening
    service = session.query(Service).filter_by(name="Gardening").first() # id 'dbc'

    user = session.query(User).filter_by(first_name="John", last_name="Doe").first() # jhon id is '0b', service '0f' barber of 

    new_assc = UserServicesAssociation(**{'user_id': user.id, 'service_id': service.id, 'town_id': town.id})

    session.add(new_assc)
    session.commit()

    # Close the session
    session.close()
