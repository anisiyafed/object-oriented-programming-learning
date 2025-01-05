from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, device_name):
        self.device_name = device_name
        self.status = "off"

    @abstractmethod
    def turn_on(self):
        ...

    @abstractmethod
    def turn_off(self):
        ...

    def get_status(self):
        return f"{self.device_name} is {self.status}."


class SmartLight(SmartDevice):
    def turn_on(self):
        self.status = "on"
        return f"{self.device_name} light is now ON."

    def turn_off(self):
        self.status = "off"
        return f"{self.device_name} light is now OFF."


class SmartThermostat(SmartDevice):
    def turn_on(self):
        self.status = "on"
        return f"{self.device_name} thermostat is now heating."

    def turn_off(self):
        self.status = "off"
        return f"{self.device_name} thermostat is now OFF."
