import socketio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11, 50)
servo.start(0)

sio = socketio.Client()

def scaleCoordinations(coordinates, dimensions):
    # Scale X
    factor = dimensions[0] / 180
    x = min(coordinates[0] / factor, 180)

    # Scale Y
    factor = dimensions[1] / 180
    y = min(coordinates[1] / factor, 180)

    return x, y

def rotate(x, y):
    servo.ChangeDutyCycle(2+(x/18))
    print(GPIO.output(11))


@sio.event
def receiveData(data):
    try:
        x, y = scaleCoordinations(data['Coordinates'], data['Dimensions'])
        rotate(x, y)
    except KeyboardInterrupt:
        servo.ChangeDutyCycle(7)
        time.sleep(0.5)
        servo.stop()
        GPIO.cleanup()

sio.connect('http://192.168.8.103:80/')