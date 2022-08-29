import os
from io import BytesIO
import json
import requests
import numpy as np
from PIL import Image

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    PRIMEHUB_DEPLOYMENT_URL = os.getenv("PRIMEHUB_DEPLOYMENT_URL") 

    result = {}
    req = json.loads(req)
    
    if 'image_url' in req.keys():

        response = requests.get(req['image_url'])
        original = Image.open(BytesIO(response.content))
        img = np.asarray(original).astype(np.float32)
        img = np.reshape(img, (1, np.shape(img)[0], np.shape(img)[1])).tolist()

        payload = {"data": {}}
        payload['data']['ndarray'] = list(img)
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