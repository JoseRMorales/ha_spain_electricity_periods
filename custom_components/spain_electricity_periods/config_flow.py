"""Config flow for Spain Electricity Periods integration."""

from typing import Any

import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN


class SpainElectricityPeriodsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Spain Electricity Periods."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Handle the initial step."""
        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(title="Spain Electricity Periods", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
