import cv2

image = cv2.imread('0ed58cccd51c4758e634d0b29e8cb0c2.jpg',cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(image,200,255)

cv2.imshow("Canny Edges",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()