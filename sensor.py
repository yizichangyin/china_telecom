
from homeassistant.helpers.entity import Entity

class MySensor(Entity):
    @property
    def name(self):
        return "My Custom Sensor"

    @property
    def state(self):
        return "Hello World"
