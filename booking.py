import requests
from config import API_KEY, SECRET

# Bookeo API URL
BOOKEO_API_URL = 'https://api.bookeo.com/v2/bookings'

def get_upcoming_bookings():
    headers = {
        'Authorization': f'Basic {API_KEY}:{SECRET}'
    }
    params = {
        'startTime': '2024-10-20T00:00:00Z'  # Example future date
    }
    response = requests.get(BOOKEO_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        bookings = response.json()
        return bookings
    else:
        print(f"Error: {response.status_code}")
        return None

# Fetch and print bookings
def main():
    bookings = get_upcoming_bookings()
    if bookings:
        for booking in bookings['data']:
            print(f"Tour: {booking['tour']}, Date: {booking['startTime']}, Customer: {booking['customer']['name']}")
    
if __name__ == "__main__":
    main()
