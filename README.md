# Weather-App
This is a simple command-line weather application that fetches real-time weather data using the OpenWeatherMap API.

## Features
- Get current weather conditions for any city
- Displays:
  - Temperature (C)
  - Weather Description
  - Humidity
  - "Feels like" Temperature

## Requirements
- Python 3
- requests library
- OpenWeatherMap API Key (find at: [openweathermap.org](https://openweathermap.org/))

## Usage 
1. Clone Repo:
```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```
2. Open Script and replace the api key with your own
3. Run script
```bash
python3 Weather\ app.py
```

## Expected Output
```bash
Enter a city: Toronto
Weather in Toronto, CA: 
Clouds, broken clouds
Temp: 15.2°C
Feels like: 14.5°C
Humidity: 78%
```
### Note:
This script does not handle invalid city names, this is just a simple program to practice using API keys.
