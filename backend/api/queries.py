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
        public_spaces = data
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
