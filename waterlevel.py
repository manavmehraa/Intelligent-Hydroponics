from nanpy import SerialManager
from nanpy.arduinotree import ArduinoTree
from time import sleep



try:
    connection = SerialManager()
    a = ArduinoTree(connection=connection)
    print("Connection Established")
except:
    print("Connection Not Established")
    

waterPin = a.pin.get('A0')

try:
    while True:
        value = waterPin.read_analog_value()
        print(value)
        sleep(1)
except:
    print("Not Working")
    

