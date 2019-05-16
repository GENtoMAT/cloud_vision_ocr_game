#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./") 

import cv2
from test_cloud_vision import text_detect

from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
API_KEY="AIzaSyBagnOBM5TyRIWlp9nFXgiZf1lz-mT7NNk"
FILE_NAME="img/cap.png"

def capture_camera(mirror=False, size=None):
    """Capture video from camera"""
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    save_count = 1
    flg_record = False
    frame_cnt = 0
    record_fps = 10

    while True:
        ret, frame = cap.read()
        frame_cnt += 1

        # フレームをリサイズ
        if size is not None and len(size) == 2:
          frame = cv2.resize(frame, size)

        # フレームを表示する
        cv2.namedWindow("camera capture", cv2.WINDOW_NORMAL)
        resized_frame = cv2.resize(frame,(int(1920/3), int(1080/3)))
        cv2.imshow('camera capture', resized_frame)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27:
            break
        elif k == ord("c"): # 1frameキャプチャをOCR
          print('capture done, OCR start...\n\n')
          cv2.imwrite("img/capture_%03d.png"%(save_count),frame)
          cv2.imwrite("img/cap.png",frame)
          text_detect()
          save_count += 1
          print('\n' + "-" * 50)
        elif k == ord("r"): # 連番画像保存スタート
          print('start record')
          flg_record = True
        elif k == ord("s"): # 連番画像ストップ　
          print('stop record')
          flg_record = False
        elif k == ord("d"): # 最新の保存済みの画像をOCR
          print('--- Game start ---')
          print('--- Game start ---')
          print('--- Game start ---')

          detect_result = text_detect()
          #f = open("output.json", "w")
          #json.dump(detect_result, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
          #print(detect_result['responses'][0]['textAnnotations'][0]['description'])
          # if "responses" in detect_result :
          #   print("ok") 
          #print(len(detect_result['responses'][0]['textAnnotations']))
          detect_num = len(detect_result['responses'][0]['textAnnotations'])
          if detect_num == 5:
            print("Game Clear!!!　　やっぱ、５チャンだね！！！")
          else:
            print( "%02d個　detect　されちゃったよ" % detect_num )
          print(detect_result['responses'][0]['textAnnotations'][0]['description'])


          print('--- Game end ---')
          print('--- Game end ---')
          print('--- Game end ---')
        # record_fps毎にひたすら画像を保存する
        if flg_record and frame_cnt % record_fps == 0:
          cv2.imwrite("record/capture_%03d.png"%(save_count),frame)
          print ("capture frame %s"%(save_count))
          save_count += 1

    # 終了処理(キャプチャを解放する)
    cap.release()
    cv2.destroyAllWindows()

# def text_detect(imgname=FILE_NAME):
#   api_key=API_KEY
#   img_requests = []
#   with open(imgname, 'rb') as f:
#     ctxt = b64encode(f.read()).decode()
#     img_requests.append({
#                           'image': {'content': ctxt},
#                           'features': [{
#                             #'type': 'LABEL_DETECTION',
#                             'type': 'TEXT_DETECTION',
#                             'maxResults': 5
#                           }]
#                         })
#   response = requests.post(ENDPOINT_URL,
#                            data=json.dumps({"requests": img_requests}).encode(),
#                            params={'key': api_key},
#                            headers={'Content-Type': 'application/json'})
#   res = response.json()
#   if "responses" in res:
#     if "textAnnotations" in res['responses'][0]:
#       #print(res['responses'][0]['textAnnotations'][0]['description'])
#       return res
#     else:
#       print('no text found')
#       print("no data")
# if __name__ == '__main__':
#   text_detect()


capture_camera()

