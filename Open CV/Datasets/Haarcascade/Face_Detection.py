import cv2

# Load Haar Cascade for face detection
face_Cascade = cv2.CascadeClassifier(r'Datasets\Haarcascade\haarcascade_frontalface_alt_tree.xml')

image_path = "Datasets\Haarcascade\VK.webp" 
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_Cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles and label
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)

# Show the result


img = cv2.resize(img, (1000, 600))

cv2.imshow("EE SAALA CUP NAMDU!", img)
cv2.waitKey(0)
cv2.destroyAllWindows()