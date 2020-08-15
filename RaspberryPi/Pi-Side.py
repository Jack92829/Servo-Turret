import socketio
import RPi.GPIO as GPIO
import time
import signal

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
servoY = GPIO.PWM(11, 50)
servoX = GPIO.PWM(12, 50)
servoX.start(0)
servoY.start(0)
sio = socketio.Client()

print('Ready')

def KeyboardInterruptHandle(signal, frame):
    servoX.ChangeDutyCycle(7)
    servoY.ChangeDutyCycle(7)
    time.sleep(2)
    servoX.stop()
    servoY.stop()
    GPIO.cleanup()
    exit()

def scaleCoordinations(coordinates, dimensions):
    # Scale X
    factor = dimensions[0] / 180
    x = min(coordinates[0] / factor, 180)

    # Scale Y
    factor = dimensions[1] / 180
    y = min(coordinates[1] / factor, 180)

    return x, y

def rotate(x, y):
    servoX.ChangeDutyCycle(2+(x/18))
    servoY.ChangeDutyCycle(2+(y/18))

@sio.event
def receiveData(data):
    x, y = scaleCoordinations(data['Coordinates'], data['Dimensions'])
    print(x, y)
    rotate(x, y)

signal.signal(signal.SIGINT, KeyboardInterruptHandle)
sio.connect('http://ip here')
