import json
import math

def lambda_handler(event, context):
    query_params = event.get('queryStringParameters', {})
    d = 0.0

    a = float(query_params.get('a', 0))
    b = float(query_params.get('b', 0))
    c = float(query_params.get('c', 0))

    if a == 0 and b == 0 and c == 0:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'a': a,
                'b': b,
                'c': c,
                'error': 'Invalid input'
            })
        }
    
    if a == 0:
        return {
            'statusCode': 200,
            'body:': json.dumps(
                {
                    'a': a,
                    'b': b,
                    'c': c,
                    'error': 'Divide by zero'
                }
            )
        }
    
    d = b**2 - 4*a*c

    if d < 0:
        return {
            'statusCode': 200,
            'body': json.dumps({
                'a': a,
                'b': b,
                'c': c,
                'error': 'No real roots'
            })
        }
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'a': a,
                'b': b,
                'c': c,
                'x1': x1,
                'x2': x2
            })
        }
    
        