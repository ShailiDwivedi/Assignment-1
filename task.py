import json
import requests as r
#Extract data on the Gross Domestic Product (GDP) of South American countries using the World Bank API:

def get_api_data(api):
    print("HAriom")
    response = r.get(api)
    if response.status_code == 200:
        print("Successfully fetched the data")
        return response.json()
    else:
        print(f"Error: {response.status_code}. Failed to fetch data.")
        print("Response content:", response.content)







