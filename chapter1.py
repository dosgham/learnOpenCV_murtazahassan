import cv2
'''
print("Package Imported")
img = cv2.imread("Resources/lenna.jpg")
cv2.imshow('Output',img)
cv2.waitKey(100)
'''


cap = cv2.VideoCapture(0)
cap.set(10,100)
while True:
    success,img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



'''
img = cv2.imread('Resources/lenna.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)


cv2.imshow('Gray Image',imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Canny Image',imgCanny)
cv2.waitKey(0)
'''


