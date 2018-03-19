from nanpy import DHT
from time import sleep

dht = DHT(10, DHT.DHT11)

try:
    while True:
        print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
        #print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
        print("Humidity is %.2f %%" % dht.readHumidity())
        sleep(1)
except:
    print("Not Working")
