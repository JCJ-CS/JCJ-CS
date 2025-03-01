import requests
from datetime import datetime

# Fetch IP address
response = requests.get('https://api.ipify.org?format=json')
ip_data = response.json()
ip_address = ip_data['ip']

# Fetch date and time
response = requests.get(f'http://worldtimeapi.org/api/ip/{ip_address}')
time_data = response.json()
current_time = time_data['datetime']

# Print the date and time
print(f"The current date and time in your location (based on your IP address {ip_address}) is: {current_time}")