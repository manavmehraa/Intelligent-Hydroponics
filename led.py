from nanpy import (ArduinoApi,SerialManager)
from time import sleep


ledPin = 13

try:
    connection = SerialManager()
    a = ArduinoApi(connection=connection)
    print("Connection Established")
except:
    print("No Connection Established")


a.pinMode(ledPin , a.OUTPUT)

try:
    while True:
        a.digitalWrite(ledPin, a.LOW)
        sleep(1)
        a.digitalWrite(ledPin, a.HIGH)
        sleep(1)
except:
    print("Not Working")
    
