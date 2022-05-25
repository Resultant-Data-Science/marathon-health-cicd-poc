import json
import pandas
import datetime
import re
import psycopg2
# import requests


def validate(event, context):
    
    response = {
        'statusCode': 200,
        'body': json.dumps({"psycopg2 import successful"})
    }

    return response