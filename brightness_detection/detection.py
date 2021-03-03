import cv2
import numpy
import matplotlib as plt
import PIL



if __name__ == "__main__":

    imgname = "matrix3.jpg"

    # img = cv2.imread(imgname, cv2.IMREAD_COLOR)
    img = cv2.imread(imgname, cv2.IMREAD_COLOR)
    print("Image shape:", img.shape)

    # resize image
    scale_percent = 45  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    print("Resized shape:", resized.shape)

    GBlur = cv2.GaussianBlur(resized, (3, 3), 0)
    canny = cv2.Canny(GBlur, 50, 150)
    imgHSV = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    print("HSV shape", imgHSV.shape)
    print("", imgHSV[100][200])

    cv2.imshow('img', resized)
    cv2.imshow('canny', canny)
    cv2.imshow('HSV', imgHSV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


