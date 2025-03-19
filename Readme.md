# Weather Alert SMS

This Python script fetches weather forecasts from OpenWeather API and sends an SMS alert via Twilio if rain is expected in the next 12 hours.

## Features

- Uses OpenWeather API to check upcoming weather conditions.
- Sends an SMS notification using Twilio if rain is predicted.
- Automatable via PythonAnywhere for scheduled execution.

## Setup & Installation

### Prerequisites

- Python 3.x
- Twilio Account
- OpenWeather API Key
- PythonAnywhere (for automation, optional)

### Install Dependencies

```sh
pip install requests twilio python-dotenv
```

### Environment Variables

Create a `.env` file in the project directory with:

```
TWILIO_ACCOUNT_SID=<Your Twilio SID>
TWILIO_AUTH_TOKEN=<Your Twilio Auth Token>
TWILIO_PHONE_NUMBER=<Your Twilio Phone Number>
RECEIVER_PHONE_NUMBER=<Your Verified Receiver Number>
WEATHER_API_KEY=<Your OpenWeather API Key>
```

### Running the Script

```sh
python weather_alert.py
```

## Automating on PythonAnywhere

1. Upload the script to PythonAnywhere.
2. Open the **Tasks** tab and add a new scheduled task.
3. Set the task command:
   ```sh
   python3 /home/yourusername/weather_alert.py
   ```
4. Choose the frequency (e.g., every 6 hours).
5. Save and activate the task.

Now, the script will run automatically based on your schedule.

## License

This project is open-source and free to use under the MIT License.
