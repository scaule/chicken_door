from flask import Flask
import RPi.GPIO as GPIO
import time
import datetime

#File to write status log 
FILE_NAME = "poule.txt"

#TIME TO OPEN OR CLOSE DOOR 
SLEEP_TIME = 40

app = Flask(__name__)
def writeStatus (status) :
    statusFile = open (FILE_NAME, 'a' )
    statusFile.write(status +' | '+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

def readLastStatus () :
    fileHandle = open (FILE_NAME, 'r' )
    lineList = fileHandle.readlines()
    fileHandle.close()
    return lineList[-1].split("|")[0].strip()

@app.route('/open')
def openDoor():
    if readLastStatus() == 'open':
        return 'Already open'
    writeStatus('open')    
    GPIO.output(12, GPIO.LOW)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(SLEEP_TIME)
    GPIO.output(11, GPIO.LOW)
    return 'Open'

@app.route('/close')
def closeDoor():
    print readLastStatus()
    if readLastStatus() == 'close':
        return 'Already close'
    writeStatus('close')
    GPIO.output(11, GPIO.LOW)
    GPIO.output(12, GPIO.HIGH)
    time.sleep(SLEEP_TIME)
    GPIO.output(12, GPIO.LOW)
    return 'Close'

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    app.run(debug=True, port=8033, host='0.0.0.0')

