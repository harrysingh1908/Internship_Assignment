import requests
import time

def send_get_request(url):
    
    try:
        response = requests.get(url)
        return response
    except Exception as e:
        print(f"An error occured : {e}")
        return None

def automate_requests(url, interval):
    
    while True:
        response = send_get_request(url)
        if response.status_code == 200:
            print("Status Code:", response.status_code)
            print("Response Text:", response.text[:100])  # Print only the first 100 characters
        else:
            print(f"Failed to retrieve data. Status Code: {response.status_code}")
        time.sleep(interval)


# Example usage:
url = "http://www.example.com"
interval = 2
automate_requests(url, interval)
