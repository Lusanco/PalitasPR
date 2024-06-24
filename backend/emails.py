'''
    Manage anything related to sending or receiving mails
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User
import aws_bucket
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DB_URL")
engine = create_engine(db_url)



def load_html_template(template_path):
    with open(template_path, 'r') as file:
        return file.read()


def send_confirm_email(email, first_name, token):
    '''
        Receives email, first name and token to send
        in the body of the email.
        Person receives a link to verify the email.
    '''
    from flask_mail import Message
    from app import mail, app

    subject = "Welcome to PalitasPR"
    confirm_link = f"http://127.0.0.1:5000/api/user/verify_email/{token}"

    # Load the HTML template
    html_template = load_html_template(
        'backend/email_template/email_template.html')

    # Inject dynamic content into the HTML template
    html_content = html_template.replace(
        '{{first_name}}', first_name).replace('{{confirm_link}}', confirm_link)

    msg = Message(
        subject, sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.html = html_content  # Set the HTML content of the email

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
    user = session.query(User).filter_by(verification_token=token).first()
    if user:
        response, status = aws_bucket.create_user_folder(user.id)
        if status == 201:
            # Eliminate the user token and validate him 'True'
            user.verification_token = None
            user.verified = True
        session.commit()
    else:
        # No user with that token
        return ({'error': 'No user with that token'}, 404)

    session.close()
    return (response, 200)  # OK