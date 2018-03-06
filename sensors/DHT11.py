from .numeric import NumericSensor

import Adafruit_DHT


class DHT11sensor(NumericSensor)

    def __init__(self, name):
        super(DHT11sensor, self).__init__(name)

        sensor = Adafruit_DHT.DHT11

        gpio = 17

        temperature = Adafruit_DHT.read_retry(sensor, gpio)

        if temperature is not None
          print('Temp={0:0.1f}*C '.format(temperature))
        else:
          print('Failed to get reading. Try again!')
