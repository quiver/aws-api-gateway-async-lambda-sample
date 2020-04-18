import time

def func(event, context):
    time.sleep(3)
    return {'statusCode': 200,
            'body': 'ok'}

