import json

'''
This lambda is used by API gateway and includes
HTTP status code and headers
'''
def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! through gh actions.You have hit from {}\n'.format(event['path'])
    }