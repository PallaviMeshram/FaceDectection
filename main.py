import cv2

cap = cv2.VideoCapture(0)
path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(path)

while True:
    ret, frame = cap.read()
    if ret:

        faces = face_cascade.detectMultiScale(frame, 1.3, 2)
        for face in faces[-1:]:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

        cv2.imshow("camera", frame)

        key_pressed = cv2.waitKey(1) & 0xff
        if key_pressed == ord('q'):
            break
cv2.destroyAllWindows()