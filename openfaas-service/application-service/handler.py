import os
import json
import requests

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    PRIMEHUB_DEPLOYMENT_URL = os.getenv("PRIMEHUB_DEPLOYMENT_URL") 

    result = {}
    req = json.loads(req)
    
    if 'data' not in req.keys():
        result['result'] = "Error"
        result['content'] = "Did not find the data key value."
    else:
        payload = {"data": {}}
        payload['data']['ndarray'] = req['data']['ndarray']
        r = requests.post(PRIMEHUB_DEPLOYMENT_URL, json = payload)
        result['status_code'] = r.status_code
        if r.status_code == 200:
            content = r.json()
            result['result'] = content['data']['ndarray'][0]
            if 'input' in req.keys():
                if req['input'] == result['result'].index(max(result['result'])):
                    result['verify'] = 1
                else:
                    result['verify'] = 0
    return result