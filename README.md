#h3 Rotation Modul for python using opencv3 and numpy
#h5 Sample
```python
from cv2 import *
from rotate import *

source=imread("../test/img003.jpg");
rotX=10
rotY=10
rotZ=10
focalLength=500
distance=500
destination = rotateDeg(source,rotX,rotY,rotZ,focalLength,distance)
imshow("Sample", destination);
waitKey(0);
```
#h5 Commands
# returns radian from dregree
toRad(angle):
#returns the x rotation matrix
getRotXMat(angle=0):
#returns the y rotation matrix
getRotYMat(angle=0):
#returns the z rotation matrix
getRotZMat(angle=0):
#returns the transformation to the origin matrix
getToOriginMat(w,h):
#returns the transformation back to world coordinates matrix
getFromOriginMat(w,h,f=500):
#returns the distance matrix
getDistanceMat(distance=500):
#returns x rotated image
rotateX(img,angle, deg = 1):
#returns y rotated image
rotateY(img,angle, deg = 1):
#returns z rotated image
rotateZ(img,angle, deg = 1):
#returns radian rotated image
rotateRad(img,xRot,yRot,zRot,dist = 500,focal = 500):
#returns degree rotated image
rotateDeg(img,xRot,yRot,zRot,dist = 500,focal = 500):


#h5 Further Reads
+[C++ Code sample](http://stackoverflow.com/questions/6606891/opencv-virtually-camera-rotating-translating-for-birds-eye-view)
+[A Vision Based Top-View Transformation Model for a Vehicle Parking Assistant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3355419/)
+[A Simple Birds Eye View Transformation Technique](http://www.ijser.org/researchpaper%5CA-Simple-Birds-Eye-View-Transformation-Technique.pdf)
