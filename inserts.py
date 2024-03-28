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

    # Perform the query
    results = session.query(User.first_name.label('person'),
                            Service.name.label('service'),
                            Town.name.label('town')) \
                    .join(UserServicesAssociation, User.id == UserServicesAssociation.user_id) \
                    .join(Service, Service.id == UserServicesAssociation.service_id) \
                    .join(Town, Town.id == UserServicesAssociation.town_id) \
                    .filter(Town.name.in_(['Ponce', 'Salinas'])) \
                    .all()

    # Process the results
    for result in results:
        print(f"Person: {result.person} service: {result.service} Town: {result.town}")

    # Close the session
    session.close()
