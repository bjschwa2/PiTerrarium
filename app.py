

'''
PiTerrarrium interface for controlling rasberry pi GPIO header
author: Bradley Schwarz

'''

import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
        17 : {'name' : 'AC 1 Sprinklers', 'state' : GPIO.LOW},
        23 : {'name' : 'AC 2 Lights', 'state' : GPIO.LOW},
        18 : {'name' : 'AC 3 Heater', 'state' : GPIO.LOW},
        22 : {'name' : 'AC 4', 'state' : GPIO.LOW},
        27 : {'name' : 'AC 5', 'state' : GPIO.LOW},
        4  : {'name' : 'AC 6', 'state' : GPIO.LOW},
        14 : {'name' : '5v 1', 'state' : GPIO.LOW},
        15 : {'name' : '5v 1Fan', 'state': GPIO.LOW},
        24 : {'name' : 'Input 1 Temp1', 'state': GPIO.LOW},
        10 : {'name' : 'Input 2 Humidity', 'state': GPIO.LOW},
        9  : {'name' : 'Input 3 Temp2', 'state': GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)


