"""Spanish Electricity Periods sensor platform."""

from datetime import datetime, time

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import dt as dt_util

from .const import LOGGER

SPANISH_HOLIDAYS = [
    (1, 6),  # January 6 - Epifanía del Señor
    (5, 1),  # May 1 - Día del Trabajo
    (8, 15),  # August 15 - Asunción de la Virgen
    (10, 12),  # October 12 - Fiesta nacional de España
    (11, 1),  # November 1 - Todos los Santos
    (12, 6),  # December 6 - Día de la Constitución
    (12, 8),  # December 8 - La Inmaculada Concepción
    (12, 25),  # December 25 - Navidad
]

# Time periods
VALLE_WEEKDAY_START = time(0, 0)  # 00:00
VALLE_WEEKDAY_END = time(8, 0)  # 08:00

LLANO_MORNING_START = time(8, 0)  # 08:00
LLANO_MORNING_END = time(10, 0)  # 10:00

PUNTA_MORNING_START = time(10, 0)  # 10:00
PUNTA_MORNING_END = time(14, 0)  # 14:00

LLANO_AFTERNOON_START = time(14, 0)  # 14:00
LLANO_AFTERNOON_END = time(18, 0)  # 18:00

PUNTA_EVENING_START = time(18, 0)  # 18:00
PUNTA_EVENING_END = time(20, 0)  # 20:00 (actually 22:00 but there's a gap)

LLANO_NIGHT_START = time(22, 0)  # 22:00
LLANO_NIGHT_END = time(0, 0)  # 00:00 (midnight)


async def async_setup_entry(
    _: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Spanish Electricity Periods sensor."""
    async_add_entities([SpanishElectricityPeriod()], update_before_add=True)
    LOGGER.info("Spanish Electricity Periods sensor added.")


class SpanishElectricityPeriod(SensorEntity):
    """Spanish Electricity Periods sensor."""

    _attr_translation_key = "spanish_electricity_period"
    _attr_should_poll = False
    _attr_has_entity_name = True

    def __init__(self) -> None:
        """Initialize the sensor."""
        self._attr_name = "Spanish Electricity Period"
        self._attr_unique_id = "spanish_electricity_period"
        self._attr_icon = "mdi:flash"
        self._state = None

    @property
    def state(self) -> str | None:
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self) -> dict:
        """Return additional state attributes."""
        now = dt_util.now()
        return {
            "current_time": now.strftime("%H:%M"),
            "current_date": now.strftime("%Y-%m-%d"),
            "is_weekend": self._is_weekend(now),
            "is_holiday": self._is_holiday(now),
            "period_type": self._state,
        }

    def _is_weekend(self, dt: datetime) -> bool:
        """Check if the given datetime is a weekend (Saturday=5, Sunday=6)."""
        return dt.weekday() >= 5

    def _is_holiday(self, dt: datetime) -> bool:
        """Check if the given date is a Spanish holiday."""
        return (dt.month, dt.day) in SPANISH_HOLIDAYS

    def _is_valle_day(self, dt: datetime) -> bool:
        """Check if the given date should use Valle period all day."""
        return self._is_weekend(dt) or self._is_holiday(dt)

    def _get_period_for_time(self, dt: datetime) -> str:
        """Determine the period period for the given datetime."""
        current_time = dt.time()

        # If it's weekend or holiday, it's always Valle
        if self._is_valle_day(dt):
            return "Valle"

        # Weekday period logic
        # Valle: 00:00 - 08:00
        if VALLE_WEEKDAY_START <= current_time < VALLE_WEEKDAY_END:
            return "Valle"

        # Llano: 08:00 - 10:00 (morning)
        if LLANO_MORNING_START <= current_time < LLANO_MORNING_END:
            return "Llano"

        # Punta: 10:00 - 14:00 (morning peak)
        if PUNTA_MORNING_START <= current_time < PUNTA_MORNING_END:
            return "Punta"

        # Llano: 14:00 - 18:00 (afternoon)
        if LLANO_AFTERNOON_START <= current_time < LLANO_AFTERNOON_END:
            return "Llano"

        # Punta: 18:00 - 22:00 (evening peak)
        if PUNTA_EVENING_START <= current_time < time(22, 0):
            return "Punta"

        # Llano: 22:00 - 00:00 (night)
        if time(22, 0) <= current_time or current_time < VALLE_WEEKDAY_START:
            return "Llano"

        # Default fallback
        return "Valle"

    async def async_update(self) -> None:
        """Update the sensor state."""
        now = dt_util.now()
        self._state = self._get_period_for_time(now)
        LOGGER.debug(
            "Spanish Period updated: %s at %s",
            self._state,
            now.strftime("%Y-%m-%d %H:%M:%S"),
        )
