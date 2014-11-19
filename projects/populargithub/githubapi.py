import requests, json, datetime, pickle

url = 'https://api.github.com/users/BenLiyanage/repos' 
url = 'https://api.github.com/repositories'
r = requests.get(url)

print r
print '\n\n\n'
myJson = r.json()
print len(myJson)

mostPopular = 0

print r.headers['X-RateLimit-Limit']
print r.headers['X-RateLimit-Remaining']
s = int(r.headers['X-RateLimit-Reset'])
print datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
print type(r.headers)
print pickle.dumps(r.headers)

for repo in myJson:
    #print json.dumps(repo)
    exit()
    #if repo['fork'] == False: # and repo['stargazers_count'] > mostPopular:
        # this is expensive in terms of the rate limit
        # stargazers_count = len(requests.get(repo['stargazers_url']).json())
        # if stargazers_count > mostPopular:
            # mostPopularRepo = repo['full_name']
            # mostPopular = stargazers_count

print mostPopularRepo
