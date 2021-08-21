import urllib3
import json
import os
import datetime
import boto3
import sys


from ariadne import ObjectType

try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType

mutation = ObjectType("Mutation")

s3_client = boto3.client('s3')

email_template = s3_client.get_object(Bucket='vaitgovhackmelb', Key='index.htm')
email_template = email_template['Body'].read()

BODY_HTML = email_template

def email_sender(recipient, subject):
    sender = os.environ['sender']
    client = boto3.client('ses')
    CHARSET = "UTF-8"
    BODY_HTML = f.read()
    response = client.send_email(
        Source='samhwang21121994@yahoo.com.vn',
        Destination={
            'ToAddresses': recipient.split(',')
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                }
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': subject,
            },
        },
    )


@mutation.field("subscribe")
def Subscribe(obj, info, email, suburb):
    subject = 'Thanks for subscribed!'
    email_sender(recipient=email, subject=subject)
    payload = {
        'success': True,
        'message': f"Email {email} subscribed successful for suburb {suburb}!"
    }
    return payload
