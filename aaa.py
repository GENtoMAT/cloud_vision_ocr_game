import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('camera capture', frame)

    k = cv2.waitKey(1)
    if k ==27:
        break
    elif k==ord("a"):
        print("pushed 'a'")

cap.release()
cv2.destroyAllWindows()


#flameに入ってくる、映像のデータ
#


