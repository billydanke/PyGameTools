import cv2 as cv

faceCascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
cameraReference = None

def getFacePosition():
    global faceCascade
    global cameraReference

    if(cameraReference == None):
        StartCamera()
    
    if not cameraReference.isOpened():
        print("Cannot open camera!")
        exit()

    ret,frame = cameraReference.read()

    if not ret:
        print("Unable to get frame from camera!")
        exit()

    #print(f"Frame size: ({frame.shape[0]},{frame.shape[1]})")
    srcGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(srcGray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    if len(faces) == 0:
        return None
    
    largestFace = max(faces, key=lambda rect: rect[2] * rect[3])

    return largestFace # Returns a Rect

def StartCamera():
    global cameraReference
    if(cameraReference == None):
        cameraReference = cv.VideoCapture(0)
        cameraReference.set(cv.CAP_PROP_FRAME_WIDTH,1920)
        cameraReference.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

def CloseCamera():
    global cameraReference
    if(cameraReference != None):
        cameraReference.release()