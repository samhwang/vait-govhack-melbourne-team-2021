try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType
import urllib3
import os
import boto3

mutation = ObjectType("Mutation")

def email_sender(recipient, subject):
    sender = 'samhwang21121994@yahoo.com.vn'
    client = boto3.client('ses')
    CHARSET = "UTF-8"

    s3_client = boto3.client('s3')
    email_template = s3_client.get_object(Bucket='vaitgovhackmelb', Key='index.htm')
    email_template = email_template['Body'].read().decode('utf-8')
    BODY_HTML = email_template

    response = client.send_email(
        Source=sender,
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
        'message': f"Email {email} subscribed successfully for suburb {suburb}!"
    }
    return payload
