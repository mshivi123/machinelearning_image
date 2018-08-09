import cv2
myimage=cv2.imread(r"C:\Users\hp\Desktop\photos\shivi.jpg",cv2.IMREAD_COLOR)
print(myimage.ndim)
myimage1=myimage[:,0]
print(myimage1.ndim)
frow=myimage[:1]
print(myimage)
print(frow)
myimage2=cv2.imread(r"C:\Users\hp\Desktop\photos\shivi.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("mywindow",myimage2)
p=cv2.waitKey(0)&0xff
if p==ord('q'):
    cv2.destroyAllWindows()
    

