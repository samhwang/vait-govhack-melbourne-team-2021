try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType

query = ObjectType("Query")

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
                    {'hr': '06:00', 'rating': 3},
                    {'hr': '12:00', 'rating': 5},
                    {'hr': '18:00', 'rating': 4},
                ],
                'ratingByDay': [
                    {'day': '21/08/2021', 'rating': 5},
                    {'day': '22/08/2021', 'rating': 5},
                    {'day': '23/08/2021', 'rating': 1},
                    {'day': '24/08/2021', 'rating': 3},
                    {'day': '25/08/2021', 'rating': 4},
                    {'day': '26/08/2021', 'rating': 2},
                    {'day': '27/08/2021', 'rating': 5},
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
                    {'hr': '06:00', 'rating': 4},
                    {'hr': '12:00', 'rating': 5},
                    {'hr': '18:00', 'rating': 2},
                ],
                'ratingByDay': [
                    {'day': '21/08/2021', 'rating': 5},
                    {'day': '22/08/2021', 'rating': 5},
                    {'day': '23/08/2021', 'rating': 3},
                    {'day': '24/08/2021', 'rating': 2},
                    {'day': '25/08/2021', 'rating': 4},
                    {'day': '26/08/2021', 'rating': 3},
                    {'day': '27/08/2021', 'rating': 5},
                ]
            },
            {
                'id': 3,
                'name': 'Deakin University',
                'location': '221 Burwood Hwy, Burwood VIC 3125',
                'suburb': 'Burwood',
                'features': [
                    'hand sanitizer',
                    'library',
                    'campus'
                ],
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
