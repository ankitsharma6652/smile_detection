import cv2
#Load the Cascade
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml') 
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#To capture the video
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
#use video file as input--> cap=cv2.VideoCapture('filename.mp4)
def detect(gray,frame):
    #Face Detection
    faces=face_cascade.detectMultiScale(gray,1.3,4)
    for x,y,w,h in faces:
        #For creating rectangle around face
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
        #Simply cropping both original image and grayscale image for better result
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        #Detecting smile
        smiles=smile_cascade.detectMultiScale(roi_gray,1.8,20)
        #Creating rectangle for smiling face
        for sx,sy,sw,sh in smiles:
                cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
        return frame
while True:
    #Reading image
    _,frame=cap.read()
    #converting to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame) #Function call
    #Display
    cv2.imshow('Detecting smile',canvas)
    #Stop if escape key is pressed
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
#Releasing cap object
cap.release()
cv2.destroyAllWindows()