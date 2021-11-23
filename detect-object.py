import cv2, random

# cap is video capture object
cap = cv2.VideoCapture(0)

while True:
    check, frame1 = cap.read()
    check, frame2 = cap.read()
    status = 0
    diff = cv2.absdiff(frame1, frame2)

    # making feed gray
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)

    # adding blur in feed
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # adding threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # dilate feed
    dilate = cv2.dilate(thresh, None, iterations=3)

    # adding contours
    contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for ct in contours:
        if cv2.contourArea(ct) < 2000:
            continue
        status = 1
        x, y, w, h = cv2.boundingRect(ct)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)
        path = "C:/py/APPS/sapp2/data"
        counter = random.randint(0, 500)
        status = status + 1
        name = 'intruder' + str(counter) + '.jpg'
        print(name)
        cv2.imwrite('C:/py/APPS/sapp2/folder/data/'+name, frame1)

    cv2.imshow("Live", frame1)
    if cv2.waitKey(1) == ord('q'):
        break
    print(status)

cap.release()
cv2.destroyAllWindows()
