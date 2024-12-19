import cv2
import serial
import time
cap=cv2.VideoCapture(3)
arduino=serial.Serial(port="/dev/ttyACM0", baudrate=9600,timeout=1)
time.sleep(2)

def arduino_conn(command):
    arduino.write(command.encode())
    print(f"Send command:",command)

glasses_casscade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

while True:
    ret,frame=cap.read()
    if not ret:
        break
    
    grey=cv2.cvtColor(frame,0)
    
    glasses=glasses_casscade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5,minSize=(50,50))
    
    
    for (x,y,w,h) in glasses:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,1,1),2)
        
        arduino_conn('MOVE')
        break
    
    cv2.imshow("Detected Object",frame)
    
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
arduino.close()
    




