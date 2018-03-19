from nanpy import (ArduinoApi,SerialManager)
from nanpy.arduinotree import ArduinoTree
from time import sleep


try:
    connection = SerialManager()
    a = ArduinoApi(connection=connection)
    print("Connection Established")
    
except:
    print("Connection Not Established")

ldrPin = a.pinMode(5, a.INPUT)


try:
    while True:
        val = a.digitalRead(ldrPin)
        print(val)
        sleep(1)
except:
    print("Not Working")

