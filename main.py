import requests
import time
import json
import matplotlib.pyplot as plt

def get_location(phone_number):
    url = "https://api.geofinder.com/v1/lookup?phone_number={}".format(phone_number)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["latitude"], data["longitude"]
    else:
        return None

def display_location_on_map(latitude, longitude):
    plt.figure()
    plt.plot(longitude, latitude, "o")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Location of Phone Number")
    plt.show()

def track_location_over_time(phone_number):
    locations = []
    while True:
        latitude, longitude = get_location(phone_number)
        locations.append((latitude, longitude))
        time.sleep(5)

    for latitude, longitude in locations:
        display_location_on_map(latitude, longitude)

def send_alert_if_phone_moves(phone_number, start_latitude, start_longitude, end_latitude, end_longitude):
    while True:
        latitude, longitude = get_location(phone_number)
        if latitude < start_latitude or latitude > end_latitude or longitude < start_longitude or longitude > end_longitude:
            send_email("Phone number has moved outside of specified area")
        time.sleep(5)

def main():
    phone_number = input("Enter the phone number: ")

    latitude, longitude = get_location(phone_number)
    print("The location of the phone number is {} {}".format(latitude, longitude))

    # Display the location on a map.
    display_location_on_map(latitude, longitude)

    # Track the location of the phone number over time.
    track_location_over_time(phone_number)

    # Send an alert if the phone number moves outside of a specified area.
    start_latitude = 47.60621
    start_longitude = -122.33207
    end_latitude = 47.60621
    end_longitude = -122.33207
    send_alert_if_phone_moves(phone_number, start_latitude, start_longitude, end_latitude, end_longitude)

if __name__ == "__main__":
    main()
