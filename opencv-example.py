import cv2
import imutils
#image = cv2.imread('input_image.jpg')
#0 dile webcam ashbe
cap = cv2.VideoCapture('test_video.mp4')

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=800)
    #cv2.imshow('Application', frame)

    text = "This is my custom texts"
    cv2.putText(frame, text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

    cv2.rectangle(frame, (50,50), (500, 500), (0, 0, 255), 2)

    #cv2.imwrite('output_image.jpg', frame)

    cv2.imshow('Application', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
