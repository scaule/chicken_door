from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
@app.route('/stop')
def stop():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    return 'Stop'
@app.route('/open')
def open():
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(40)
    GPIO.output(11, GPIO.LOW)
    return 'Open'
@app.route('/close')
def close():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(40)
    GPIO.output(12, GPIO.LOW)
    return 'close'
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    app.run(debug=True, port=80, host='0.0.0.0')
