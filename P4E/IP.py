import requests

try:
    # Fetch IP address and location information
    response = requests.get('https://ipinfo.io/json')
    response.raise_for_status()
    ip_data = response.json()
    ip_address = ip_data['ip']
    loc = ip_data['loc']  # Location coordinates (latitude,longitude)

    # Fetch date and time using IP address
    response = requests.get(f'http://worldtimeapi.org/api/ip/{ip_address}.json')
    response.raise_for_status()
    time_data = response.json()
    current_time = time_data['datetime']

    # Print the date and time
    print(f"The current date and time in your location (based on your IP address {ip_address}) is: {current_time}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    