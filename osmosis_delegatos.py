import requests
import json

addresses = []
validator = "osmovaloper15ft5d3dp9e9u4c3jxpxaqfmucnnrmgqtt454my"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Content-type': 'application/json'  # This is another valid field
}

print("Started")
i = 0
while True:
    nextPage = i * 50
    response = requests.get(
        "https://api.mintscan.io/v1/osmosis/validators/" + validator + "/delegators?limit=50&offset=" + str(
            nextPage),
        headers=headers)
    json_data = json.loads(response.text)
    arrayLen = len(json_data['delegators'])
    if arrayLen > 0:
        i += 1
        for one in json_data['delegators']:
            addresses.append(one['delegator_address'])
        print("Total Addresses: " + str(len(addresses)))
    else:
        break
print("Exporting..")
with open('data.json', 'w') as f:
    json.dump(addresses, f)

print("Exported total addresses: " + str(len(addresses)))
