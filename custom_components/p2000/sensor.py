import logging


import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import (CONF_NAME)
import homeassistant.helpers.config_validation as cv
from .api import P2000Api

"""Start the logger"""
_LOGGER = logging.getLogger(__name__)
 
DEFAULT_NAME = "p2000"
CONF_GEMEENTEN = "gemeenten"
CONF_CAPCODES = "capcodes"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Optional(CONF_GEMEENTEN): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_CAPCODES): vol.All(cv.ensure_list, [cv.string])
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""

    name = config.get(CONF_NAME)

    filter = {
        "gemeenten": config.get(CONF_GEMEENTEN),
        "capcodes": config.get(CONF_CAPCODES)
    }

    _LOGGER.info(filter)

    api = P2000Api()

    add_entities([P2000Sensor(api, name, filter)])


class P2000Sensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, api, name, filter):
        """Initialize the sensor."""
        self.api = api
        self.attributes = {}
        self.filter = filter
        self._name = name
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the monitored installation."""
        attributes = self.attributes
        attributes['icon'] = 'mdi:fire-truck'
        return attributes

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        data = self.api.get_data(self.filter)

        if (data == None):
            return

        self.attributes = data
        self._state = data["id"]

