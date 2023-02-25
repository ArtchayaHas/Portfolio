import cv2
import numpy as np
import os


path = 'C:/Users/squid/PycharmProjects/FeatureDetection/ImageQuery/'
orb = cv2.ORB_create(nfeatures = 1000)

images = []
className = []

myList = os.listdir(path)

for name in myList:
    image = cv2.imread(f'{path}{name}', 0)
    images.append(image)
    className.append(os.path.splitext(name)[0])

price = [65, 50, 60, 63, 45, 40, 45]
count = [0, 0, 0, 0, 0, 0, 0]

GamePrice = dict(zip(className, price))
GameCount = dict(zip(className, count))


def findDes(images):
    desList = []
    for img in images:
        kp, des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

def findID(img, desList):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher()

    matchlist = []
    finalVal = -1
    try:
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.75 * n.distance:
                    good.append([m])
            matchlist.append(len(good))
    except:
        pass
    #print(matchlist)
    if len(matchlist) != 0:
        if max(matchlist) > 30:
            finalVal = np.argmax(matchlist)

    return finalVal


desList = findDes(images)

cap = cv2.VideoCapture(0)

# font
font = cv2.FONT_HERSHEY_SIMPLEX

# fontScale
fontScale = 0.8

# Red color in BGR
color = (0, 0, 255)

# Line thickness of 2 px
thickness = 2

Total = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        id = findID(frame, desList)
        key = className[id]
        img_name = f'{className[id]}.jpg'

        cv2.imwrite(img_name, frame)
        print(f'{className[id]} {GamePrice[key]} usd')

        img2 = cv2.imread(img_name)
        imgOriginal = img2.copy()


        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        if id != -1:
            cv2.putText(imgOriginal, className[id], (50, 50), font, fontScale,
                        color, thickness, cv2.LINE_AA, False)

        cv2.imshow('img2', imgOriginal)

        # #Calculate total price
        if key in GameCount.keys():
            GameCount[key] += 1
            Total += GamePrice[key] * GameCount[key]
        else:
            break

        try:
            os.remove(img_name)
        except:
            pass

cap.release()
cv2.destroyAllWindows()

print(f'Total: {Total} usd')














