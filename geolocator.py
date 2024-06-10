import requests
import os 


while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Get IP from user
    ip_address = input("Enter the IP Address: ")
    print("\n")

    try:
        # Send request to get IP info
        ip_info = requests.get(f"http://ip-api.com/json/{ip_address}")
        ip_info = ip_info.json()

        # Check if the IP is valid
        if ip_info['status'] != "success":
            print("Invalid IP Address. Please try again.")
            continue  # Ask for IP again
    except:
        print("Unable to retrieve information. Please try again.")
        continue  # Ask for IP again

    print(f"IP Address: {ip_info['query']}")
    print(f"Country: {ip_info['country']}")
    print(f"City: {ip_info['city']}")
    print(f"Coordinates: {ip_info['lat']}, {ip_info['lon']}")
    print(f"Region: {ip_info['regionName']}")
    print(f"Timezone: {ip_info['timezone']}")
    print(f"Organization: {ip_info['org']}")
    print(f"Google Maps: https://www.google.com/maps/?q={ip_info['lat']},{ip_info['lon']}")

    input("\nPress Enter to continue...")
