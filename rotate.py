import numpy as np
import cv2 as cv
# returns radian from dregree
def toRad(angle):
    return angle * np.pi/180;
#returns the x rotation matrix
def getRotXMat(angle=0):
    return np.array([[1,0,0,0],
        [0,np.cos(angle),-np.sin(angle),0],
        [0,np.sin(angle),np.cos(angle),0],
        [0,0,0,1]]);
#returns the y rotation matrix
def getRotYMat(angle=0):
    return np.array([[np.cos(angle),0,-np.sin(angle),0],
        [0,1,0,0],
        [np.sin(angle),0,np.cos(angle),0],
        [0,0,0,1]]);
#returns the z rotation matrix
def getRotZMat(angle=0):
    return np.array([[np.cos(angle),-np.sin(angle),0,0],
        [np.sin(angle),np.cos(angle),0,0],
        [0,0,1,0],
        [0,0,0,1]]);
#returns the transformation to the origin matrix
def getToOriginMat(w,h):
    return np.array([[1, 0, -w/2],
        [0, 1, -h/2],
        [0, 0, 0],
        [0, 0, 1]])
#returns the transformation back to world coordinates matrix
def getFromOriginMat(w,h,f=500):
    return np.array([[f, 0, w/2, 0],
        [0, f, h/2, 0],
        [0, 0,   1, 0]]);
#returns the distance matrix
def getDistanceMat(distance=500):
    return np.array([[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, distance],
        [0, 0, 0, 1]]);
#returns x rotated image
def rotateX(img,angle, deg = 1,focal = 500, dist = 500):
    if deg:
        angle = toRad(angle)
    h,w,depth = img.shape
    transMat = np.dot(getFromOriginMat(w,h,focal),np.dot(getDistanceMat(dist), np.dot(getRotXMat(angle), getToOriginMat(w,h))))
    return cv.warpPerspective(img, transMat, (w,h), cv.INTER_CUBIC | cv.WARP_INVERSE_MAP);
#returns y rotated image
def rotateY(img,angle,deg = 1,focal = 500, dist = 500):
    if deg:
        angle = toRad(angle)
    print(angle)
    h,w,depth = img.shape
    transMat = np.dot(getFromOriginMat(w,h,focal), np.dot(getDistanceMat(dist), np.dot(getRotYMat(angle), getToOriginMat(w,h))))
    return cv.warpPerspective(img, transMat, (w,h), cv.INTER_CUBIC | cv.WARP_INVERSE_MAP);
#returns z rotated image
def rotateZ(img,angle,deg = 1,focal = 500, dist = 500):
    if deg:
        angle = toRad(angle)
    h,w,depth = img.shape
    transMat = np.dot(getFromOriginMat(w,h,focal), np.dot(getDistanceMat(dist), np.dot(getRotZMat(angle), getToOriginMat(w,h))))
    return cv.warpPerspective(img, transMat, (w,h), cv.INTER_CUBIC | cv.WARP_INVERSE_MAP);
#returns radian rotated image
def rotateRad(img,xRot,yRot,zRot,dist = 500,focal = 500):
    h,w,depth = img.shape
    rotMat = np.dot(np.dot(getRotXMat(xRot),getRotYMat(yRot)),getRotZMat(zRot))
    transMat = np.dot(getFromOriginMat(w,h,focal), np.dot(getDistanceMat(500), np.dot(rotMat, getToOriginMat(w,h))))
    return cv.warpPerspective(img, transMat, (w,h), cv.INTER_CUBIC | cv.WARP_INVERSE_MAP);
#returns degree rotated image
def rotateDeg(img,xRot,yRot,zRot,dist = 500,focal = 500):
    xRot = toRad(xRot)
    yRot = toRad(yRot)
    zRot = toRad(zRot)
    return rotateRad(img,xRot,yRot,zRot,dist,focal)