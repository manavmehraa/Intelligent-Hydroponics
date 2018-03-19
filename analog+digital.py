from nanpy import (ArduinoApi, SerialManager)
from nanpy.arduinotree import ArduinoTree
from time import sleep

try:
    connection=SerialManager()
    a = ArduinoApi(connection=connection)
    b = ArduinoTree(connection=connection)
    print("Working")
except:
    print("Not Working")
    
relayPin = 5
a.pinMode(relayPin, a.OUTPUT)
waterPin = b.pin.get('A0')


def water():
    val = waterPin.read_analog_value()
    return val

def relay():
        a.digitalWrite(relayPin, a.HIGH)
        #print("Relay On")
        sleep(1)
        a.digitalWrite(relayPin, a.LOW)
        sleep(1)
        #print("Relay Off")
    

try:
    while True:
        print("Water Level = ", water())
        relay()
except:
    print("Not Working")
