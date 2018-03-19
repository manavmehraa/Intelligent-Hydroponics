from nanpy import (ArduinoApi, SerialManager)
from nanpy.arduinotree import ArduinoTree
from nanpy import DHT
import requests
import json
from time import sleep

firebase_url = 'https://hydro-2018.firebaseio.com/'

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
    temp = dht.readTemperature(False)
    #print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
    #print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
    #print("Humidity is %.2f %%" % dht.readHumidity())
    sleep(1)
    return temp
    
def humidity():
    hum = dht.readHumidity()
    sleep(1)
    return hum

def firebase():
    data = {'water':water(), 'temp':temp(), 'humidity':humidity()}
    requests.post(firebase_url + '/value.json', data=json.dumps(data))
    
 
try:
    while True:
        water()
        temp()
        humidity()
        firebase()
        #print("Water Level = ", water())
        #val =water()
        #relay()
        #print("Temperature = ", temp())
        #temp=temp()
        #print("Humidity = ", humidity())
        #hum = humidity()
        #data = {'Waterlevel':val, 'temperature':temp, 'Humidity':hum}
        #request.post(firebase_url + '/' + '/value.json', data=json.dumps(data))
except:
    print("Not Working")