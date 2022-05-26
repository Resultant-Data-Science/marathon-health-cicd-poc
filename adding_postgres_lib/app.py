import json
import pandas
import datetime
import re
import psycopg2
# import requests


def validate(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "psycopg2 import successful",
 
        })
    }