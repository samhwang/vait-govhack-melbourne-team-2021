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
                'name': 'Doveton Aveue',
                'location': '69/124 Doveton',
                'suburb': 'Doveton',
                'features': [
                    'voicd',
                    'dishwasher'
                ],
                'visitorCount': 5,
                'ratingByHr': [
                    {'hr': '00:00', 'rating': 0}
                ],
                'ratingByDay': [
                    {'day': '21/08/2021', 'rating': 0}
                ]
            },
            {
                'id': 2,
                'name': '4 Cavill ct',
                'location': '69/124 Cavil ct',
                'suburb': 'Doveton',
                'features': [
                    'dishwasher'
                ],
                'visitorCount': 4,
                'ratingByHr': [
                    {'hr': '00:00', 'rating': 0}
                ],
                'ratingByDay': [
                    {'day': '21/08/2021', 'rating': 0}
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
