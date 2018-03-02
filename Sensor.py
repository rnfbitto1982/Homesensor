import time
import pprint as pp
import notifications
import sensors
import random

class Guardian(object):
    """Homesensor is a security system for python"""
    def __init__(self):
        super(Guardian, self).__init__()
        self.binary_sensors_names = [
            "bsensors1", "bsensors2", "bsensors3"
        ]
        self.numeric_sensors_names = [
            "nsensors1", "nsensors2", "nsensors3"
        ]
        self.numeric_sensors = []
        self.binary_sensors = []
        self.sensors = {}
        self.sensors["binary"] = {}
        self.sensors["numeric"] {}

        # self.notify = notifications.MockNotification()
        self.notify = notifications.TelegramNotification()
        self.already_n = []

    def create_sensors(self):
        for name in self.numeric_sensors_names:
            self.numeric_sensors_append(
                sensor.mocksensors.MockNumericSensor(name)
            )
        for name in self.binary_sensors_names:
            self.binary_sensors.append(
                sensors.mocksensors.MockNumericSensor(name)
            )
        pass

    def get_state(self):
        # update sensors
        for sensor in self.binary_sensors:
            sensor.update_state()
            self.sensor["binary"][sensor.name] =  sensor.get_state()

        for sensor in self.numeric_sensors:
            sensors.update_value()
            self.sensor["numeric"][sensor.name] =  sensor.get_value()
        return sensors

    def main(self):
        #crearsensores
        self.create_sensors()
        while True:
            state = self.get_state()

            for ns in self.sensors["numeric"]:
                if self.sensors["numeric"][ns] >15.0 \
                    and ns not in self.already_n:
                    self.notify.notify(ns)
                    self.already_n.append(ns)
            time.sleep(0.2)
        pass


if __name__ == '__main__':
    random.speed(1)
    sensor = Sensor()
    sensor.main()
