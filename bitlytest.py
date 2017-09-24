import urllib2
import json

TOKEN = 'f7a834152cfb4b8792ad0012bdeb847d283859c0'
ROOT_URL = 'https://api-ssl.bitly.com'
SHORTEN = '/v3/shorten?access_token={}&longUrl={}'
longurl = 'http://127.0.0.1:5000/newrequest/new'
encode = urllib2.quote(longurl, safe='')

try:
    url = ROOT_URL + SHORTEN.format(TOKEN, encode)
    response = urllib2.urlopen(url).read()
    jr = json.loads(response)
    print jr['data']['url']

except Exception as e:
    print e

print url
