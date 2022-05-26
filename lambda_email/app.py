import json
#import pandas
import datetime
import re
import numpy as np
# import requests


def validate(event, context):
    
    email_regex = re.compile('^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    matches1 = email_regex.match(event['email1']) != None
    matches2 = email_regex.match("a@b@c@--d@resultant.com") != None
    matches3 = email_regex.match(event['email3']) != None
    response = {
        'statusCode': 200,
        'body': json.dumps({ 'email-result1': matches1 , 'email-result2': matches2, 'email-result3': matches3})
    }

    return response

    #sam local invoke -e ./lambda_email/email_event.json EmailFunction