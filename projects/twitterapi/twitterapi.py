import urllib2
import time
import datetime

# Set the request authentication headers
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
headers = {}
#'DecibelAppID': '<Your Application ID>',
#           'DecibelAppKey': '<Your Application Key>',
#           'DecibelTimestamp': timestamp}

# Send the GET request
url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=-1&screen_name=benliyanange&count=5000'      
req = urllib2.Request(url, None, headers)

# Read the response
resp = urllib2.urlopen(req).read()
print resp;

