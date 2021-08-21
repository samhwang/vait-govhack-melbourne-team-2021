try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType

mutation = ObjectType("Mutation")

@mutation.field("subscribe")
def Subscribe(obj, info, email):
    mail = email
    payload = {
        'success': True,
        'message': f"Email {mail} subscribed successful!"
    }
    return payload

