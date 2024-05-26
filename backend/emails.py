#!/usr/bin/python3
'''
    Manage anything related to sending or receiving mails
'''
from os import getenv
from time import time
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.relationships import RelationshipProperty
from models import User, Service, Town, Review, Task
from base_model import BaseModel, Base
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
import aws_bucket


engine = create_engine('postgresql://demo_dev:demo_dev_pwd@demodb.ctossyay6vcz.us-east-2.rds.amazonaws.com/postgres')    

def send_confirm_email(email, first_name, token):
        '''
            Receives email, first name and token to send
            in the body of the email.
            Person receives a link to verify the email.
        '''
        from app import mail, app
        from flask_mail import Message
        from flask import url_for

        subject = "Welcome to PalitasPR"
        confirm_link = f"http://127.0.0.1:5000/api/verify_email/{token}"

        body = f"Hello,\n\nThank you for signing up {first_name}. Please click: {confirm_link} to verify your email."

        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.body = body
        print('TRYING EMAIL')
        try:
            mail.send(msg)
            print('Email sent')
            return "Email Sent Successfully"  # Add a return message for the user
        except Exception as e:
            print(f"Error sending email: {e}")
            return f"Error Sending Email: {e}"  # Inform user about the error

def confirm_email(token):
    '''
        Confirm token from email_confirm route.
        After user is confirmed, aws folders will be created for him.
        Return: <User id>
    '''
    Session = sessionmaker(bind=engine)
    session = Session()
    print(token)
    user = session.query(User).filter_by(verification_token = token).first()
    if user:
        response, status = aws_bucket.create_user_folder(user.id)
        if status == 201:
            # Eliminate the user token and validate him 'True'
            user.verification_token = None
            user.verified = True
        session.commit()
    else:
        return ({'error': 'No user with that token'}, 404) # No user with that token

    session.close()
    return (response, 200) # OK
