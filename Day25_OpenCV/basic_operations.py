import cv2

image = cv2.imread(r'D:\Fendy\BahasaPemrograman\python\opencv\Day25_OpenCV\img.jpg')

resize_image = cv2.resize(image, (500, 500))
# (h, w) = resize_image.shape[:2]
# center = (w//2), (h//2)
#
# rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)
# rotated_image = cv2.warpAffine(resize_image, rotation_matrix, (w, h))
#
# cv2.imshow('image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# CROP IMAGE
# crop_image = resize_image[100:300, 100:300]
#
# cv2.imshow('image', crop_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# CONVERSI WARNA
# gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)
# hsv_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2HSV)
# cv2.imshow('gray_image', gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#FLIP IMAGE
# flip_hor = cv2.flip(resize_image, 1)
# flip_ver = cv2.flip(resize_image, 0)
# flip_both = cv2.flip(resize_image, -1)
#
# cv2.imshow('Hor', flip_hor)
# cv2.imshow('Ver', flip_ver)
# cv2.imshow('Both', flip_both)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#PIXEL MANIPULATION

pixel = resize_image[100:120, 100:120] = [0, 0, 255]
print(pixel)

cv2.imshow('image', resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('gray_image.png', gray_image)
