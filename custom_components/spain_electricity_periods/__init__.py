"""Spanish Electricity Periods integration for Home Assistant."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Spanish Electricity Periods from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, (Platform.SENSOR,))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(
        entry, (Platform.SENSOR,)
    )
