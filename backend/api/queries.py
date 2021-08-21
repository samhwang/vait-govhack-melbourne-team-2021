try:
    import unzip_requirements
except ImportError:
    pass

from ariadne import ObjectType


# PSA: DONT READ FROM HERE ONWARDS - LAST MINUTE CODING WARNING
import boto3
import pandas as pd
import io
import random


def get_random_features():
    features = ['Furniture/seating',
                'Shops/cafe/kiosk',
                'Market/stall',
                'Stage/event space',
                'Community building',
                'Shade structure',
                'Playspace',
                'Sportfield/court',
                'Toilets/amenities',
                'Drinking water',
                'Way-finding signage',
                'Public or community art',
                'Educational program/space',
                'Meeting room/space',
                'Public transport options',
                'Welcome desk/information pod',
                'Heritage elements',
                'Trees/plants',
                'Beach/foreshore',
                'Wetlands/river/water',
                'Animals/wildlife']

    return random.choices(features, k=random.choice(range(0, len(features))))


def get_visitor_count():
    return random.choice(range(0, 20))


def get_rating_by_hour():
    return [
        {'hr': '06:00', 'rating': random.choice(range(0, 5))},
        {'hr': '12:00', 'rating': random.choice(range(0, 5))},
        {'hr': '18:00', 'rating': random.choice(range(0, 5))},
    ]


def get_rating_by_day():
    return [
        {'day': '21/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '22/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '23/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '24/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '25/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '26/08/2021', 'rating': random.choice(range(0, 5))},
        {'day': '27/08/2021', 'rating': random.choice(range(0, 5))},
    ]


def add_random_data(obj):
    for item in obj:
        item['features'] = get_random_features()
        item['visitorCount'] = get_visitor_count()
        item['ratingByHr'] = get_rating_by_hour()
        item['ratingByDay'] = get_rating_by_day()


def s3_get_file():
    s3_client = boto3.client('s3')

    data_object = s3_client.get_object(
        Bucket='vaitgovhackmelb', Key='data.csv')

    df = pd.read_csv(io.BytesIO(data_object['Body'].read()), nrows=50)

    return df


# Where the fun begins
data = s3_get_file().to_dict('records')
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
def resolve_public_space(*_, limit=10):
    if limit > 50:
        payload = {
            "success": False,
            "errors": ["Maximum records allowed to query reached."],
            "public_spaces": [],
        }
        return payload

    try:
        # Get data and pass to payload
        public_spaces = data[:limit]
        payload = {
            "success": True,
            "public_spaces": public_spaces
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)],
            "public_spaces": [],
        }
    return payload
