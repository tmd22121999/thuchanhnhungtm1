#import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
ledRed = 13 
ledYellow= 19
ledGreen= 26
ledRedSts = 0
ledYellowSts = 0
ledGreenSts = 0
"""
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledYellow,GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYellow, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)
"""
@app.route('/')
def index():
 #ledRedSts = GPIO.input(ledRed)
 #ledYellowSts = GPIO.input(ledYellow)
 #ledGreenSts = GPIO.input(ledGreen)
 templateData = { 'ledRed' : ledRedSts, 'ledYellow' :
ledYellowSts, 'ledGreen' : ledGreenSts }
 return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
 global ledRedSts , ledYellowSts, ledGreenSts
 if deviceName == "ledRed":
  if action == "on":
   ledRedSts = 1
  if action == "off":
   ledRedSts = 0
  actuator = ledRed
 if deviceName == "ledYellow":
  if action == "on":
   ledYellowSts = 1
  if action == "off":
   ledYellowSts = 0
  actuator = ledYellow
 if deviceName == "ledGreen":
  if action == "on":
   ledGreenSts = 1
  if action == "off":
   ledGreenSts = 0
  actuator = ledGreen
 """
 if action == "on":
  GPIO.output(actuator, GPIO.HIGH)
 if action == "off":
  GPIO.output(actuator, GPIO.LOW)
 ledRedSts = GPIO.input(ledRed)
 ledYellowSts = GPIO.input(ledYellow)
 ledGreenSts = GPIO.input(ledGreen)
 """

 templateData = { 'ledRed' : ledRedSts, 'ledYellow' : ledYellowSts,
'ledGreen' : ledGreenSts }
 return render_template('index.html', **templateData )
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')

