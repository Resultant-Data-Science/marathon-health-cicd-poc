import json
import pandas
import datetime
import re
# import psycopg2
# import requests


def validate(event, context):
    
    email_regex = re.compile('^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    matches1 = email_regex.match("a@b@c@--d@resultantcom") != None
    matches2 = email_regex.match("a@b@c@--d@resultant.com") != None
    matches3 = email_regex.match("xyz@resultant.com") != None
    a = np.array([1, 2, 3])
    print(a)
    response = {
        'statusCode': 200,
        'body': json.dumps({ 'result1': matches1 , 'result2': matches2, 'result3': matches3})
    }

    return response