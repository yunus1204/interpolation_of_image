import cv2
img=cv2.imread("C:\\Users\\welco\\OneDrive\\Desktop\\New folder\\img.jpg")
cv2.imshow("orginal",)
(h,w)=img.shape[:2]
res=cv2.resize(img,(int (h/2),int(w/2)),interpolation=cv2.INTER_NEAREST)

cv2.imshow("image",res)
cv2.waitKey(0)
cv2.destroyAllwindows()
