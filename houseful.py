import pandas as pd
import requests
import json
import time

# Postal codes for regions in Nova Scotia
nava_scotia = [ 
    "B0C", "B0E", "B0H", "B0J", "B0K", "B0L", "B0M", "B0N", "B0P", "B0R", "B0S", "B0T", "B0V", "B0W",
    "B1A", "B1B", "B1C", "B1E", "B1G", "B1H", "B1J", "B1K", "B1L", "B1M", "B1N", "B1P", "B1R", "B1S", 
    "B1T", "B1V", "B1W", "B1X", "B1Y", "B2A", "B2C", "B2E", "B2G", "B2H", "B2J", "B2N", "B2R", "B2S", 
    "B2T", "B2V", "B2W", "B2X", "B2Y", "B2Z", "B3A", "B3B", "B3E", "B3G", "B3H", "B3J", "B3K", "B3L", 
    "B3M", "B3N", "B3P", "B3R", "B3S", "B3T", "B3V", "B3Z", "B4A", "B4B", "B4C", "B4E", "B4G", "B4H", 
    "B4N", "B4P", "B4R", "B4V", "B5A", "B6L", "B9A" 
]

new_brunsweek = [
    "E1A", "E1B", "E1C", "E1E", "E1H", "E1J", "E1N", "E1V", "E1W", "E1X",
    "E2A", "E2E", "E2G", "E2H", "E2J", "E2K", "E2L", "E2M", "E2N", "E2P", "E2R", "E2S", "E2V",
    "E3A", "E3B", "E3C", "E3E", "E3G", "E3L", "E3N", "E3V", "E3Y", "E3Z",
    "E4A", "E4B", "E4C", "E4E", "E4G", "E4H", "E4J", "E4K", "E4L", "E4M", "E4N", "E4P", "E4R", "E4S", "E4T", "E4V", "E4W", "E4X", "E4Y", "E4Z",
    "E5A", "E5B", "E5C", "E5E", "E5G", "E5H", "E5J", "E5K", "E5L", "E5M", "E5N", "E5P", "E5R", "E5S", "E5T", "E5V", 
    "E6A", "E6B", "E6C", "E6E", "E6G", "E6H", "E6J", "E6K", "E6L",
    "E7A", "E7B", "E7C", "E7E", "E7G", "E7H", "E7J", "E7K", "E7L", "E7M", "E7N", "E7P",
    "E8A", "E8B", "E8C", "E8E", "E8G", "E8J", "E8K", "E8L", "E8M", "E8N", "E8P", "E8R", "E8S", "E8T",
    "E9A", "E9B", "E9C", "E9E", "E9G", "E9G"
]

pei = [
    "C0A", "C0B", "C1A", "C1B", "C1C", "C1E", "C1N"
]

new_foundland = [
    "A0A", "A0B", "A0C", "A0E", "A0G", "A0H", "A0J", "A0K", "A0L", "A0M", "A0N", "A0P", "A0R",
    "A1A", "A1B", "A1C", "A1E", "A1G", "A1H", "A1K", "A1L", "A1M", "A1N", "A1S", "A1V", "A1W", "A1X", "A1Y",
    "A2A", "A2B", "A2H", "A2N", "A2V", "A5A", "A8A"
]


buildings_NS = []
houseful_NB = []

# Function to handle retries and timeouts
def get_request_with_retries(url, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            # Make the request with a timeout
            res = requests.get(url, timeout=timeout)
            # If the request is successful, return the response
            if res.status_code == 200:
                return res
            else:
                print(f"Failed to fetch data: Status code {res.status_code}")
                break  # Exit if the response is not successful
        except requests.exceptions.ReadTimeout:
            print(f"Read timeout occurred for {url}. Retrying... ({attempt + 1}/{retries})")
            time.sleep(2)  # Wait for 2 seconds before retrying
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            break  # Exit if there's a different kind of request exception
    return None  # Return None if all retries fail

# Function to fetch building data for Nova Scotia
def get_NS_buildings():
    for region in nava_scotia:  
        page = 1
        while True:
            url = f"https://www.houseful.ca/api/search/?path=%2Fns%2F{region}%2Fp-{page}"
            res = get_request_with_retries(url)  # Use the retry function to fetch data
            
            if res:
                data = json.loads(res.content)
                listings = data.get('data', {}).get('listings', [])
                
                # If listings are empty, break out of the loop as we've reached the last page
                if not listings:
                    break
                
                for listing in listings:
                    address = listing.get('fullAddress')
                    geo = listing.get('geo',{})
                    lat = geo.get('lat')
                    lng = geo.get('lng')
                    listPrice = listing.get('listPrice')
                    bath = listing.get('bath')
                    bed = listing.get('bed')
                    sqft = listing.get('sqftTotal')
                    lotSize = listing.get('lotSize')
                    propertyType = listing.get('propertyTypeDisplayName')
                    propertyStyle = listing.get('propertyArchStyle')
                    yearBuilt = listing.get('yearBuilt')

                    building = {
                        "address" : address,
                        "lat": lat,
                        "lng": lng,
                        "price": listPrice,
                        "bed": bed,
                        "bath": bath,
                        "sqft" : sqft,
                        "lotSize": lotSize,
                        "property_type": propertyType,
                        "property_style": propertyStyle,
                        "year_built": yearBuilt
                    }

                    buildings_NS.append(building)

                # Move to the next page
                page += 1
            else:
                print(f"Failed to fetch data for region {region} on page {page}.")
                break  # Exit the loop if there's an issue with the request
    
    return buildings_NS

# Function to fetch building data for Nova Scotia
def get_NB_buildings():
    for region in new_brunsweek:  
        page = 1
        while True:
            url = f"https://www.houseful.ca/api/search/?path=%2Fns%2F{region}%2Fp-{page}"
            res = get_request_with_retries(url)  # Use the retry function to fetch data
            
            if res:
                data = json.loads(res.content)
                listings = data.get('data', {}).get('listings', [])
                
                # If listings are empty, break out of the loop as we've reached the last page
                if not listings:
                    break
                
                for listing in listings:
                    address = listing.get('fullAddress')
                    lat = listing.get('lat')
                    lng = listing.get('lng')
                    listPrice = listing.get('listPrice')
                    bath = listing.get('bath')
                    bed = listing.get('bed')
                    sqft = listing.get('sqftTotal')
                    lotSize = listing.get('lotSize')
                    propertyType = listing.get('propertyTypeDisplayName')
                    propertyStyle = listing.get('propertyArchStyle')
                    yearBuilt = listing.get('yearBuilt')

                    building = {
                        "address" : address,
                        "lat": lat,
                        "lng": lng,
                        "price": listPrice,
                        "bed": bed,
                        "bath": bath,
                        "sqft" : sqft,
                        "lotSize": lotSize,
                        "property_type": propertyType,
                        "property_style": propertyStyle,
                        "year_built": yearBuilt
                    }

                    houseful_NB.append(building)

                # Move to the next page
                page += 1
            else:
                print(f"Failed to fetch data for region {region} on page {page}.")
                break  # Exit the loop if there's an issue with the request
    
    return houseful_NB


# Fetch buildings data
# buildings_NS = get_NS_buildings()
houseful_NB =  get_NB_buildings()

# Save to CSV
df = pd.DataFrame(houseful_NB)
df.to_csv('houseful_NB.csv', index=False)
