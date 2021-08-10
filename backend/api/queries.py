# Resolve Hello query
def resolve_hello(obj, info):
    payload = {
        "success": True,
        "message": "Hello World"
    }
    return payload
