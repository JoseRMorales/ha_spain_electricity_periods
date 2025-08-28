# Spain Electricity Periods Home Assistant Integration

Automatically track Spanish electricity tariff periods (Valle, Llano, Punta) in Home Assistant

## Features
- **Real-time Period Detection:** Automatically determines the current electricity period (Valle, Llano, or Punta)
- **Spanish Holiday Support:** Includes all Spanish national holidays when Valle period applies all day
- **Weekend Handling:** Automatically applies Valle period during weekends
- **Rich Attributes:** Provides additional information like current time, date, weekend status, and holiday status
- **Time Zone Aware:** Uses Home Assistant's configured timezone for accurate period calculation
- **Configurable via UI:** Set up and manage the integration through Home Assistant's UI

## Electricity Periods

The integration follows the Spanish electricity market time periods:

### Weekdays
- **Valle (Valley - Lowest rates):** 00:00 - 08:00 and 22:00 - 00:00
- **Llano (Flat - Medium rates):** 08:00 - 10:00, 14:00 - 18:00
- **Punta (Peak - Highest rates):** 10:00 - 14:00, 18:00 - 22:00

### Weekends & Holidays
- **Valle (Valley):** All day (00:00 - 00:00)

## Installation

### HACS (Recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=JoseRMorales&category=Integration&repository=ha_spain_electricity_periods)

Alternatively, you can install this integration manually by following the steps below.
1. Go to HACS > Integrations > Custom Repositories.
2. Add this repository: `https://github.com/JoseRMorales/ha_spain_electricity_periods` as an integration.
3. Install **Spain Electricity Periods** from HACS.
4. Restart Home Assistant.

### Manual
1. Copy the `custom_components/spain_electricity_periods` folder to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.

## Configuration
1. In Home Assistant, go to **Settings > Devices & Services**.
2. Click **Add Integration**.
3. Search for **Spain Electricity Periods** and follow the prompts to set it up.

## Entities
- `sensor.spain_electricity_period`: Shows the current electricity period (`Valle`, `Llano`, or `Punta`)

## State Attributes
The sensor provides the following attributes:
- `current_time`: Current time in HH:MM format
- `current_date`: Current date in YYYY-MM-DD format
- `is_weekend`: Boolean indicating if it's a weekend
- `is_holiday`: Boolean indicating if it's a Spanish national holiday
- `period_type`: Current period type (same as the sensor state)

## License
[MIT License](LICENSE)
