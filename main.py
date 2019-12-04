#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("./") 

import cv2
from module.cloud_vision import text_detect

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
      print('capture done\n\n')
      cv2.imwrite("img/capture_%03d.png"%(save_count),frame)
      cv2.imwrite("img/cap.png",frame)
      save_count += 1
      
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
      print('\n')

      detect_result = text_detect()
      if not detect_result :
        print("")
      else:
        detect_num = int(len(detect_result['responses'][0]['textAnnotations']))-1
        print( "%02d words detected" % detect_num )

        success_num_list = [1, 5]
        if detect_num in success_num_list:
          print("Game Clear!!! %02d is success number!" % detect_num ) 
        else:
          print("Not Clear...")
      
      print('\n')
      print('--- Game end ---')
      print('--- Game end ---')
      print('--- Game end ---')

      print('\n' + "-" * 50 + '\n')

    # record_fps毎にひたすら画像を保存する
    if flg_record and frame_cnt % record_fps == 0:
      cv2.imwrite("record/capture_%03d.png"%(save_count),frame)
      print ("capture frame %s"%(save_count))
      save_count += 1

  # 終了処理(キャプチャを解放する)
  cap.release()
  cv2.destroyAllWindows()

capture_camera()

