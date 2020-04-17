import time

def f_sync(event, context):
    time.sleep(3)
    return {'statusCode': 200,
            'body': 'sync'}


def f_async(event, context):
    time.sleep(3)
    return {'statusCode': 200,
            'body': 'async'}
