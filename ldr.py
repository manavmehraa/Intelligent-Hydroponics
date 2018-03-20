from nanpy import (ArduinoApi,SerialManager)
from nanpy.arduinotree import ArduinoTree
from time import sleep


try:
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    print("Connection Established")
    
except:
    print("Connection Not Established")

ldrPin = a.pin.get('A1")


try:
    while True:
        val = ldrPin.read_analog_value()
        print(val)
        sleep(1)
except:
    print("Not Working")

