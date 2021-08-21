import random
import pandas as pd
import boto3
import io


def get_random_features():
    import random
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

    df = pd.read_csv(io.BytesIO(data_object['Body'].read()))

    return df
