import requests
import json

'''artist_id = '379603'
api_key = '1'
searchstring = 'https://api.songkick.com/api/3.0/artists/' + artist_id + '/gigography.json?apikey=' + api_key
print(searchstring)'''


response = requests.get('https://opendata-download-metobs.smhi.se/api/version/latest.json')
print(response.status_code)
print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
