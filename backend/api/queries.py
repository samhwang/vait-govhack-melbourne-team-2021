# Resolve Hello query
def resolve_hello(obj, info):
    payload = {
        "success": True,
        "message": "Hello World"
    }
    return payload

def resolve_public_space(obj, info):
    try:
        # Get data and pass to payload
        public_spaces = [
            {
                'id': 1,
                'name': 'Doveton Aveue',
                'location': '69/124 Doveton',
                'suburb': 'Doveton',
                'features': [
                    'voicd',
                    'dishwasher'
                ],
                'visitorCount': 5
            },
            {
                'id': 2,
                'name': '4 Cavill ct',
                'location': '69/124 Cavil ct',
                'suburb': 'Doveton',
                'features': [
                    'dishwasher'
                ],
                'visitorCount': 4
            }
        ]
        payload = {
            "success": True,
            "public_spaces": public_spaces
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)],
        }
    return payload