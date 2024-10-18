import subprocess
import json
import pandas as pd

# Step 1: Define the coordinates
coordinates = [
    # Nova Scotia
    {"southwestCorner": {"lat": 44.09987583855046, "lng": -64.8595484109375}, "northeastCorner": {"lat": 46.039362563179, "lng": -62.233815989062506}},
    # New Brunswick
    {"southwestCorner": {"lat": 45.6129205149985, "lng": -67.77478261093749}, "northeastCorner": {"lat": 47.501280262588544, "lng": -65.14905018906249}},
    # PEI
    {"southwestCorner": {"lat": 44.59966689435915, "lng": -63.920805876367204}, "northeastCorner": {"lat": 44.84360876459064, "lng": -63.59258932363283}},
]

# Initialize an empty list to store all results
all_data = []

# Step 2: Iterate over each set of coordinates and fetch data using curl
for coordinate in coordinates:
    # Convert the coordinate dictionary to a JSON string for use in --data-raw
    coordinate_json = json.dumps(coordinate)
    
    # Define the curl command as a list (for subprocess.run)
    curl_command = [
        'curl', 'https://api.foodbankscanada.ca/api/branch/bounding-box',
        '-H', 'accept: */*',
        '-H', 'accept-language: en-US,en;q=0.9',
        '-H', 'content-type: application/json;charset=utf-8',
        '-H', 'origin: https://foodbankscanada.ca',
        '-H', 'priority: u=1, i',
        '-H', 'referer: https://foodbankscanada.ca/',
        '-H', 'sec-ch-ua: "Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        '-H', 'sec-ch-ua-mobile: ?0',
        '-H', 'sec-ch-ua-platform: "Windows"',
        '-H', 'sec-fetch-dest: empty',
        '-H', 'sec-fetch-mode: cors',
        '-H', 'sec-fetch-site: same-site',
        '-H', 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        '--data-raw', coordinate_json
    ]

    # Run the curl command and capture the output
    result = subprocess.run(curl_command, capture_output=True, text=True)
    
    # Parse the JSON response and append the data from this request to the main list
    response_data = json.loads(result.stdout)
    all_data.extend(response_data)

# Step 3: Convert the JSON data to a DataFrame and save as CSV
df = pd.DataFrame(all_data)
df.to_csv("./data/foodbanks_NS.csv", index=False)
