import cv2 
#Load the cascade
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml') 
#Load the image
img=cv2.imread(r'filename.jpg')
# Detecting smile
smiles=smile_cascade.detectMultiScale(img,1.8,20)
#creating Rectangle
for sx,sy,sw,sh in smiles:
    cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2) 
#Display
cv2.imshow('Detected Smile',img)
#Press any key to escape
cv2.waitKey()