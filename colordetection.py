import numpy as np
import cv2
cap = cv2.VideoCapture(r'E:/test.mp4')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(r'E:/6.avi', fourcc, 25, size)
while(1):
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.convertScaleAbs(frame)
    params = cv2.SimpleBlobDetector_Params()
    params.blobColor = 0
    params.filterByColor = True
    params.minArea = 0
    params.filterByArea = False
    params.minThreshold = 120;
    params.maxThreshold = 255;
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3:
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(frame)
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    if ret == True:
        video.write(im_with_keypoints)
        cv2.imshow('frame', im_with_keypoints)
    else:
        cap.release()
        break
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break