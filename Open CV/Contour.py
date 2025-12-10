import cv2


# Read the image
image = cv2.imread('OIP.webp')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

counter,hierachy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)



cv2.drawContours(image,counter,-1,(0,255,0),1)


# Show results
cv2.imshow('Grayscale', gray)
cv2.imshow('Threshold', thresh)
cv2.imshow('Counter Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
