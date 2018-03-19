from nanpy import (ArduinoApi, SerialManager)
from nanpy.arduinotree import ArduinoTree
from nanpy import DHT
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
dht = DHT(10, DHT.DHT11)


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

def temp():
    print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
    #print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
    print("Humidity is %.2f %%" % dht.readHumidity())
    sleep(1)
    
    

try:
    while True:
        print("Water Level = ", water())
        relay()
        temp()
except:
    print("Not Working")
