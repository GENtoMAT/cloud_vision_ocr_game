#!/usr/bin/env python
# -*- coding: utf-8 -*-


from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
API_KEY=""
FILE_NAME="img/cap.png"

def text_detect(imgname=FILE_NAME):
  api_key=API_KEY

  img_requests = []
  with open(imgname, 'rb') as f:
    ctxt = b64encode(f.read()).decode()
    img_requests.append({
                          'image': {'content': ctxt},
                          'features': [{
                            #'type': 'LABEL_DETECTION',
                            'type': 'TEXT_DETECTION',
                            #'maxResults': 5
                          }]
                        })

  response = requests.post(ENDPOINT_URL,
                           data=json.dumps({"requests": img_requests}).encode(),
                           params={'key': api_key},
                           headers={'Content-Type': 'application/json'})

  res = response.json()
  if "responses" in res:
    if "textAnnotations" in res['responses'][0]:
      print('text found')
      for text in res['responses'][0]['textAnnotations']:
        print(text["description"])

      #print(res['responses'][0]['textAnnotations'][0]['description'])
      return res
    else:
      print('no text found')
      return False

if __name__ == '__main__':
  text_detect()
