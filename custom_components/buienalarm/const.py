"""Support for Buienalarm weather service."""

import logging
from datetime import timedelta
from typing import NamedTuple

from homeassistant.const import LENGTH_MILLIMETERS, TEMP_CELSIUS

SensorType = NamedTuple(
    "SensorType",
    [
        ("name", str),
        ("unit", str),
        ("icon", str),
    ],
)


LOGGER = logging.getLogger(__package__)
UPDATE_INTERVAL = timedelta(seconds=300)
ATTRIBUTION = "Data provided by Buienalarm B.V."
DEFAULT_TIMEFRAME = 60
DEFAULT_NAME = "ba"
ICON_THERMOMETER = "mdi:thermometer"
ICON_WEATHER_POURING = "mdi:weather-pouring"
ITEM_TEMP = "temperature"
ITEM_PRECIP_NOW = "precipitation"
ITEM_PRECIP_FORECAST_AVG = "precipitation_forecast_average"
ITEM_PRECIP_FORECAST_TOTAL = "precipitation_forecast_total"
ITEM_NEXT_RAIN_FORECAST = "next_rain_forecast"
SENSOR_TYPES = {
    ITEM_TEMP: SensorType(
        "Temperature",
        TEMP_CELSIUS,
        ICON_THERMOMETER),
    ITEM_PRECIP_NOW: SensorType(
        "Precipitation",
        LENGTH_MILLIMETERS + "/h",
        ICON_WEATHER_POURING
    ),
    ITEM_PRECIP_FORECAST_AVG: SensorType(
        "Precipitation forecast average",
        LENGTH_MILLIMETERS + "/h",
        ICON_WEATHER_POURING,
    ),
    ITEM_PRECIP_FORECAST_TOTAL: SensorType(
        "Precipitation forecast total",
        LENGTH_MILLIMETERS,
        ICON_WEATHER_POURING
    ),
    ITEM_NEXT_RAIN_FORECAST: SensorType(
        "Next rain forecast",
        None,
        ICON_WEATHER_POURING
    ),
}
CONF_TIMEFRAME = "timeframe"
CONF_CONDITION_PRECIPITATION = "precipitation"
