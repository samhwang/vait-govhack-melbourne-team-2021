try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType


# PSA: DONT READ FROM HERE ONWARDS - LAST MINUTE CODING WARNING
import boto3
import pandas as pd
import io

from utils import add_random_data, s3_get_file

# Where the fun begins
data = s3_get_file()
add_random_data(data)

###################################


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
<<<<<<< HEAD
        public_spaces = data
=======
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
>>>>>>> 015de0573aab8216f1347fb19508949fa725c92e
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
