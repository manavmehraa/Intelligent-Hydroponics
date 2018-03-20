from nanpy import (ArduinoApi,SerialManager)
from time import sleep


relayPin = 5

try:
    connection = SerialManager()
    a = ArduinoApi(connection=connection)
    print("Connection Established")
except:
    print("No Connection Established")


a.pinMode(relayPin , a.OUTPUT)

try:
    while True:
        a.digitalWrite(relayPin, a.LOW)
        sleep(2)
        a.digitalWrite(relayPin, a.HIGH)
        sleep(2)
except:
    print("Not Working")
    


