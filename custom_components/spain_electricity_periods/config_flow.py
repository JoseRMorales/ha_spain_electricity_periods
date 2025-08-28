"""Config flow for Spanish Electricity Periods integration."""

from typing import Any

import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class SpanishElectricityPeriodsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Spanish Electricity Periods."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> None:
        """Handle the initial step."""
        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(title="Spanish Electricity Periods", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
