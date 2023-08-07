import argparse
import requests
import hashlib
import time

def fetch_marvel_characters(api_key, private_key, namestartswith=None, length=None):
    timestamp = str(int(time.time()))

    # Generate an MD5 hash using timestamp, private key, and public key
    hash_value = hashlib.md5(f'{timestamp}{private_key}{api_key}'.encode()).hexdigest()

    # Base URL for Marvel API
    base_url = 'https://gateway.marvel.com/v1/public/'

    # API endpoint (e.g., 'characters')
    endpoint = 'characters'

    # Initialize parameters dictionary with required parameters
    params = {
        'apikey': api_key,
        'ts': timestamp,
        'hash': hash_value
    }

    # Add optional parameters if provided
    if namestartswith:
        params['nameStartsWith'] = namestartswith
    if length:
        params['limit'] = length

    # Make the API request
    try:
        response = requests.get(f'{base_url}{endpoint}', params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        results = data['data']['results']
        return results
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP Error: {http_err}")
    except Exception as err:
        raise Exception(f"Error: {err}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Marvel characters")
    parser.add_argument("--api_key", required=True, help="Your Marvel API public key")
    parser.add_argument("--private_key", required=True, help="Your Marvel API private key")
    parser.add_argument("--namestartswith", help="Filter characters by name starting with")
    parser.add_argument("--length", type=int, help="Number of characters to fetch")
    
    args = parser.parse_args()
    
    characters = fetch_marvel_characters(args.api_key, args.private_key, args.namestartswith, args.length)
    
    # Further processing or printing of characters
