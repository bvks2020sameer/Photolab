import cv2
import cvlib

image = cv2.imread('/home/viraj/people.extra_extension.py.extra_extension/viraj_sharma.jpg')

def blur_faces(image):
 faces, confidences = cvlib.detect_face(image)

 for face in faces:
  x, y, w, h = face
  
  cropped_face = image[y:h, x:w]

  blurred_face = cv2.GaussianBlur(cropped_face, (7, 7), 0)

  image[y:h, x:w] = blurred_face

 return image

