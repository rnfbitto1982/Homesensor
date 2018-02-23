#!/user/bin/env python
import time

import sensors

class Sensor(object):
    """Homesensor is a security system for pyhton"""

    def __init__(self):
        super(Sensor, self).__init__()

    def create_sensor(self):
        self.mbs = sensors.mocksensors.MockBinarySensor("sensor1")
        self.mbs = sensors.mocksensors.MockNumericSensor("sensor2")
        pass

    def get_state(self):
        #Uptade sensors
        self.mbs.update_state()
        self.mbs.update_value()
        #get values from sensors
        value1 = self.mbs.get_state()
        value2 = self.mbs.get_value()
        return (value1, value2)

    def main():
        # crearsensores
        self.crate_sensors()
        while True:
            state = self.get_state()
        #   leersensores()
        #       if condiciones:
        #           notificar()
            print(state)
            time.sleep(1)
        pass

if __name__ == '__main__':
    sensor = Sensor()
    sensor.main()
