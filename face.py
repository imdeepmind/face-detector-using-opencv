#importing open cv
import cv2

# Importing the haar cascade files

# Visit https://github.com/opencv/opencv/tree/master/data/haarcascades for downloading own cascade files
haar_cascade_face = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
haar_cascade_eye = cv2.CascadeClassifier('cascade/data/haarcascade_eye.xml')

# Camera
camera = cv2.VideoCapture(0)

while True:
    # Reading frames from the camera
    ret, frame = camera.read()

    # Saving the gray version for the image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Searching my face
    myFace = haar_cascade_face.detectMultiScale(gray, 1.2, 5)

    # Loaping through the cordinates of my face
    for x,y,w,h in myFace: 
        # Color the box
        color = (0,255,0)
        stroke = 2

        # End points
        endX = x + w
        endY = y + h 

        # Drawing a rectangle around my face
        cv2.rectangle(frame, (x,y), (endX, endY), color, stroke)
        cv2.rectangle(gray, (x,y), (endX, endY), color, stroke)

        # Storing my face
        roi_gray = gray[x:endX, y:endY]
        roi_frame = frame[x:endX, y:endY]

        # Searching for my eyes
        myEye = haar_cascade_eye.detectMultiScale(roi_gray, 1.2, 5)

        # Looping through the cordinates 
        for ex, ey, eh, ew in myEye:
            endXeye = ex+ew
            endYeye = ey+eh

            # Drawing a rectangle around my eyes
            cv2.rectangle(roi_gray, (ex,ey), (endXeye,endYeye), color, stroke)
            cv2.rectangle(roi_frame, (ex,ey), (endXeye,endYeye), color, stroke)

    # This is for stopping the program based on a certain key
    if ret:
        cv2.imshow('frame',frame)
        cv2.imshow('gray',gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
# Releasing the camera
camera.release()

# Clossing all opencv windows
cv2.destroyAllWindows()

# Bye
