import cv2

# image = cv2.imread(r'D:\Fendy\BahasaPemrograman\python\opencv\Day25_OpenCV/img.jpg')
#
# if image is None:
#     print('no image')
# else:
#     resize_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)
#     cv2.imshow('image', resize_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# video_capture = cv2.VideoCapture(r'D:\Fendy\BahasaPemrograman\python\opencv\Day25_OpenCV\video.mp4')
# while True:
#     ret, frame = video_capture.read()
#     if not ret :
#         break
#     resized = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
#     rotate_image = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)
#
#     cv2.imshow('Video', rotate_image)
#     cv2.waitKey(33)
#
#     if cv2.waitKey(33) & 0xFF == ord('q'):
#         break
#
# video_capture.release()
# cv2.destroyAllWindows()

camera = cv2.VideoCapture(0)
while True:
    ret, frame1 = camera.read()
    if not ret:
        break

    cv2.imshow('frame1', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
