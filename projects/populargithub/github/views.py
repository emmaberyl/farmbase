from django.shortcuts import render
from github.models import *
from django.template import RequestContext, loader
from django.http import HttpResponse
import requests, json, datetime, pickle, sys
from django.db.models.base import ObjectDoesNotExist

# Create your views here.
def QueueStatus(request):
    myRateLimit = RateLimit.objects.all()
    template = loader.get_template('github/ratelimit.html')
    context = RequestContext(request, { 'myRateLimit': myRateLimit})
    return HttpResponse(template.render(context))
    
def populate(request):
    #get the last polling time
    #todo
    
    apiBaseURL = 'https://api.github.com/'
    
    #get open source repositories
    url = apiBaseURL + 'repositories'
    r = requests.get(url)
    output = ""
    counter = 0
    for remoteRepo in r.json():
        # try to look up this repo
        counter+=1
        if counter == 10:
            break
        output += "\n-------------\n Json Object"
        output += json.dumps(remoteRepo, indent=4, separators=(',', ': ')) 
        output += "\nGetting id:" + str(remoteRepo["id"])
        
        try:
            myRepo = Repo.objects.get(pk = remoteRepo["id"])
        except ObjectDoesNotExist:
            myRepo = Repo(id = remoteRepo["id"])
        finally:
            # get pull requests
            # get request is dependant on ratelimiting parameters that we may have captured
            remotePullRequestURL = apiBaseURL + "repos/" + myRepo.full_name + "/pulls?state=all"
            output += "pulls url: " + remotePullRequestURL
            remotePullRequests = requests.get(remotePullRequestURL)
            
            # update base description
            myRepo.full_name = remoteRepo["full_name"]
            myRepo.description = remoteRepo["description"]
            myRepo.html_url = remoteRepo["html_url"]
            if 'Etag' in remotePullRequests.headers:
                myRepo.pulls_Etag = remotePullRequests.headers['ETag']
            #myRepo.pulls_Last_Modified = remotePullRequests.headers['Last-Modified']
            myRepo.save()
            
            output += "importing pull requests"
            for remotePullRequest in remotePullRequests.json():
                try:
                    
                    
                    try:
                        myPullRequest = myRepo.pullrequest_set.get(pk=remotePullRequest['number'])
                    except ObjectDoesNotExist:
                        myPullRequest = PullRequest(number = remotePullRequest['number'], repo = myRepo)
                    finally:
                        #figure out if we need to create the user
                        try:
                            myUser = User.objects.get(pk = remotePullRequest['user']['id'])
                        except:
                            myUser = User(pk = remotePullRequest['user']['id'], login = remotePullRequest['user']['login'])
                            myUser.save()
                            
                        myPullRequest.user = myUser
                        
                        myPullRequest.state = remotePullRequest['state']
                        myPullRequest.created_at = remotePullRequest['created_at']
                        myPullRequest.updated_at = remotePullRequest['updated_at']
                        myPullRequest.closed_at = remotePullRequest['closed_at']
                        myPullRequest.merged_at = remotePullRequest['merged_at']

                        myPullRequest.save()
                except exception as e:
                    output += "error({0}): {1}".format(e.errno, e.strerror)
                    output += "error on pull request: "
                    output += json.dumps(remotePullRequest, indent=4, separators=(',', ': '))
                    return HttpResponse("<pre>" + output + "</pre>")
            output += str(list(myRepo.pullrequest_set.all()))
            
        #break
        # update stats on repo
    return HttpResponse("<pre>" + output + "</pre>")