try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType

mutation = ObjectType("Mutation")

@mutation.field("subscribe")
def Subscribe(obj, info, email, suburb):
    payload = {
        'success': True,
        'message': f"Email {email} subscribed successful for suburb {suburb}!"
    }
    return payload

