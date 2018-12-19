import cv2
import numpy as np

def get_location(img,template):
    result = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.35
    # print(result.shape)
    location = np.where(result >= threshold)
    print(location)
    return location


def get_roi(location,h,w):

    roi=[]
    for i in range(len(location[0])):
        x = location[0][i]
        y = location[1][i]
        roi.append(img[x:x+h,y:y+w])
    return roi


def highlight_and_show(roi,location,img,h,w):

    mask = np.zeros(img.shape, dtype = "uint8")
    img = cv2.addWeighted(img, 0.25, mask, 0.75, 0) # Darkens the image

    for i in range(len(location[0])):
        x = location[0][i]
        y = location[1][i]
        img[x:x+h,y:y+w] = roi[i]

    cv2.imshow('Found',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread("puzzle.jpg")
template_original = cv2.imread("waldo.jpg")
template = cv2.resize(template_original,(15,40))
h,w,c = template.shape

loc = get_location(img,template)
roi = get_roi(loc,h,w)
highlight_and_show(roi,loc,img,h,w)
