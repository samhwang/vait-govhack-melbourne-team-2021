try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType

query = ObjectType("Query")


@query.field("hello")
def resolve_hello(obj, info):
    payload = {
        "success": True,
        "message": "Hello World"
    }
    return payload


publicSpace = ObjectType('PublicSpace')


@publicSpace.field('ratingByHr')
def resolve_rating_by_hr(obj, *_):
    return obj.get('ratingByHr')


@publicSpace.field('ratingByDay')
def resolve_rating_by_day(obj, *_):
    return obj.get('ratingByDay')


@query.field("publicSpaces")
def resolve_public_space(obj, info):
    try:
        # Get data and pass to payload
        public_spaces = [
            {
                'id': 1,
                'name': 'Deakin University',
                'type': 'Restricted public land',
                'LGA': 'BOROONDARA',
                'features': [
                    'hand sanitizer',
                    'library',
                    'campus'
                ],
                'size': 0.0166,
                'visitorCount': 40,
                'ratingByHr': [
                    {'hr': '06:00', 'rating': 5},
                    {'hr': '12:00', 'rating': 5},
                    {'hr': '18:00', 'rating': 4},
                ],
                'ratingByDay': [
                    {'day': '21/08/2021', 'rating': 3},
                    {'day': '22/08/2021', 'rating': 4},
                    {'day': '23/08/2021', 'rating': 3},
                    {'day': '24/08/2021', 'rating': 2},
                    {'day': '25/08/2021', 'rating': 4},
                    {'day': '26/08/2021', 'rating': 5},
                    {'day': '27/08/2021', 'rating': 5},
                ]
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
