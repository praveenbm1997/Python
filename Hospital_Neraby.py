import requests
import time
import json
from datetime import datetime
import urllib.parse

# Get API key from google place api
# Enable the Place API in GCP console and Generate the API key
API_KEY = 'Google Map API Key'
if not API_KEY:
    raise ValueError("API key not found. Set the GOOGLE_MAPS_API_KEY environment variable.")

# format for location (latitude, longitude)
location = '12.3163,76.6454'  
radius = 5000
place_type = 'hospital'

encoded_location = urllib.parse.quote(location)

nearby_search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={encoded_location}&radius={radius}&type={place_type}&key={API_KEY}"

hospitals = []

try:
    while nearby_search_url:
        response = requests.get(nearby_search_url)
        response.raise_for_status()
        data = response.json()

        for place in data.get('results', []):
            hospital = {
                'Name': place.get('name'),
                'Address': place.get('vicinity'),
                'Rating': place.get('rating'),
                'Place ID': place.get('place_id')
            }
            
            place_details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={hospital['Place ID']}&fields=name,formatted_phone_number,rating&key={API_KEY}"
            
            try:
                details_response = requests.get(place_details_url)
                details_response.raise_for_status()
                details_data = details_response.json()
                
                if 'result' in details_data:
                    hospital['Phone Number'] = details_data['result'].get('formatted_phone_number', 'Not Available')
                
                hospitals.append(hospital)
                
                # Delay to avoid hitting rate limits
                time.sleep(0.2)
            
            except requests.RequestException as e:
                print(f"Error fetching details for {hospital['Name']}: {e}")

        # Check for next page
        nearby_search_url = data.get('next_page_token')
        if nearby_search_url:
            nearby_search_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={nearby_search_url}&key={API_KEY}"
            time.sleep(2)  # Waiting before making the next request

except requests.RequestException as e:
    print(f"Error fetching nearby places: {e}")

# Creating a dictionary with metadata and hospital data
output_data = {
    "metadata": {
        "timestamp": datetime.now().isoformat(),
        "location": location,
        "radius": radius,
        "place_type": place_type
    },
    "hospitals": hospitals
}

# Generate a filename with the current timestamp
filename = f"hospitals_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

print(f"Data has been saved to {filename}")

# Print a summary of the data
print(f"\nSummary:")
print(f"Total hospitals found: {len(hospitals)}")
print(f"Data saved to: {filename}")