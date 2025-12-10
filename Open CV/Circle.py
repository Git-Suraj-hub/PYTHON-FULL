import cv2

image = cv2.imread('0ed58cccd51c4758e634d0b29e8cb0c2.jpg')

circle = cv2.circle(image,[390,180],120,[0,0,255],5)

cv2.imshow('circle',circle)
cv2.waitKey(0)
cv2.destroyAllWindows()