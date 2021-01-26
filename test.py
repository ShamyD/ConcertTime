import requests

'''artist_id = '379603'
api_key = '1'
searchstring = 'https://api.songkick.com/api/3.0/artists/' + artist_id + '/gigography.json?apikey=' + api_key
print(searchstring)'''

response = requests.get('https://opendata-download-metobs.smhi.se/api')
print(response.status_code)