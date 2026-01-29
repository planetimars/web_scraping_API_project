import requests
import json
from datetime import datetime

print("HAPI 2: MARRJA E TE DHENAVE TE MOTIT NGA OPEN-METEO")
print("=" * 60)

api_url = "https://api.open-meteo.com/v1/forecast"
params = {
    'latitude': 41.3275,
    'longitude': 19.8189,
    'current': 'temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m',
    'timezone': 'Europe/Tirane'
}

try:
    print("Dergimi i kerkeses ne Open-Meteo API...")
    response = requests.get(api_url, params=params, timeout=10)

    if response.status_code == 200:
        weather_data = response.json()

        kodi_ne_shqip = {
            0: 'i kthjelle',
            1: 'kryesisht i kthjelle',
            2: 'pjellore',
            3: 'me re',
            45: 'mjegull',
            48: 'mjegull me brym',
            51: 'shire e lehte',
            53: 'shire e moderuar',
            55: 'shire e forte',
            61: 'shi i lehte',
            63: 'shi i moderuar',
            65: 'shi i forte',
            95: 'stuhi'
        }

        current = weather_data['current']
        weather_code = current['weather_code']

        moti_info = {
            'qyteti': 'Tirane',
            'temperatura': current['temperature_2m'],
            'lagështia': current['relative_humidity_2m'],
            'kodi_motit': weather_code,
            'pershkrimi': kodi_ne_shqip.get(weather_code, 'e panjohur'),
            'era_shpejtesia': current['wind_speed_10m'],
            'data_marries': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'timestamp_api': current['time'],
            'burimi': 'Open-Meteo'
        }

        with open('moti_tirane.json', 'w', encoding='utf-8') as f:
            json.dump(moti_info, f, indent=2, ensure_ascii=False)

        print("Te dhenat e motit u ruajten ne moti_tirane.json")
        print(f"\nMoti ne Tirane:")
        print(f"Temperatura: {moti_info['temperatura']}°C")
        print(f"Lagështia: {moti_info['lagështia']}%")
        print(f"Pershkrimi: {moti_info['pershkrimi']}")
        print(f"Era: {moti_info['era_shpejtesia']} km/h")

    else:
        print(f"Gabim API: Status code {response.status_code}")

except Exception as e:
    print(f"Gabim: {e}")