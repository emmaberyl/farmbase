#!/usr/bin/python

import urllib2
import time
import datetime
import twitter

def DeleteUserNoFailing(id):
    try:
        result = api.DestroyFriendship(id)
        return result
    except Exception as e:
        if e == "Rate limit exceeded":
            #wait 5 minutes and try again
            sleep(300)
            DeleteUserNoFailing(id)
        else:
            print "failed: " + str(e)
            return ""

api = twitter.Api(
    consumer_key='b23FnkffFlzz20sSAstUdoFxG',
    consumer_secret='HHQgoXl3otqdbmvifitedZpWzbiaGw1DYY5sqUmic9TW4SXvqT',
    access_token_key='490826867-s61pgHrlvHrCXEwmCirpNlVWrMvRR6jjYZX6CX5Z',
    access_token_secret='6doHGC9O98vVHTEvmPkCMv5fe53YHzcUfODIaDZrtNaRq'
)

me = api.VerifyCredentials()

users = api.GetFriendIDs()

#print users

counter = 0

for id in users:
    print "Deleting " + str(id)
    result = DeleteUserNoFailing(id)

#print api.GetFollowers()