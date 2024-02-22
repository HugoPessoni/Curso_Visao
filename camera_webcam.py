import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0) # trabalhando com WEBCAM

while True:
    #captura frame por frame
    ret, frame = video_capture.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # filtro cinza
    detections = face_detector.detectMultiScale(image_gray, minSize=(100, 100),minNeighbors=5)

    #desenha o retangulo 
    for (x, y, w, h) in detections:
        print(w, h)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #resultado
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #codificacao para parar o algoritmo
        break

video_capture.release() #libera memoria
cv2.destroyAllWindows() #fecha as janelas 