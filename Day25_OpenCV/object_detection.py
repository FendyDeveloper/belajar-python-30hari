import cv2
import cv2.data

#threshold
# image = cv2.imread('img4.jpg', 0)
#
# resize_image = cv2.resize(image, (500, 500))
# # gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
#
#
# cv2.imshow('thresh', thresh)
# # cv2.imshow('grayimage', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #Canny CV2
# canny = cv2.Canny(resize_image, 100, 200)
# cv2.imshow('canny', canny)

#CV2 find Contour
#
# _, thresh = cv2.threshold(resize_image, 127, 255, cv2.THRESH_BINARY)
# contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
# # Ubah warna ke BGR
# image_with_contours = cv2.cvtColor(resize_image, cv2.COLOR_GRAY2BGR)
# cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)
# cv2.imshow('image', image_with_contours)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# CascadeClassFier
# cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
# face_cascade = cv2.CascadeClassifier(cascade_path)


# image = cv2.imread(r'img4.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_car.xml')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Ini adalah calon calon mahasiswa ITS", (x-50,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()




