import cv2
from networkx.algorithms.bipartite import color

face_Cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
eye_Cascade = cv2.CascadeClassifier(r'haarcascade_eye_tree_eyeglasses.xml')
smile_Cascade = cv2.CascadeClassifier(r'haarcascade_smile.xml')
left_eye_Cascade = cv2.CascadeClassifier(r'haarcascade_lefteye_2splits.xml')
right_eye_Cascade = cv2.CascadeClassifier(r'haarcascade_righteye_2splits.xml')


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    if ret is not True:
        print("Video Capture Failed Please Set Correctly Camera ")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face = face_Cascade.detectMultiScale(gray,1.1,5)

    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"Face Detected",(x-10,y-10),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,0,255),2)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]

        eyes = eye_Cascade.detectMultiScale(gray,1.1,5)
        if len(eyes) >=2:
           for(x,y,w,h) in eyes:
                cv2.circle(frame,(x+20,y+20),20,(0,0,255),1)

        smile = smile_Cascade.detectMultiScale(gray,1.1,50)

        if(len(smile)) > 0:
            cv2.putText(frame,"Smile Detected",(x-20,y-20),cv2.FONT_HERSHEY_DUPLEX,1.0,(0,0,255),2)




    cv2.imshow('Face Detect',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()