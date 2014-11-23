## DESCRIPTION

Complete Python Development Environment on top of a Vagrant VM.



## REQUIREMENTS


* [VirtualBox](http://www.virtualbox.org/)
* [VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](http://www.vagrantup.com/)
* [git](http://git-scm.com/downloads)
or one of the Github GUI clients: [OSX](http://mac.github.com/), [Windows] (http://windows.github.com/), [Eclipse](http://eclipse.github.com/)
* [python-dev-bootstrap](https://github.com/AnthonyNystrom/python-dev-bootstrap)

		Clone this repo: $ git clone git@github.com:AnthonyNystrom/python-dev-bootstrap.git
		Or, using one of the Github GUI clients, click the button: Clone in {platform}

## BASIC USAGE

1. Assuming you have met the above requirements. 
2. Provision a new Vagrant VM (using PythonDevBootstrapPrecise as example)

        $ cd python-dev-bootstrap (Wherever your cloned path is for this repo)
        $ vagrant up
 		$ vagrant ssh
 		$ sudo su (Gets you to root) :)
 		

 		
The above will build a 512MB virtual machine running Ubuntu with the following installed and configured:

1. Python
2. PIL
3. PIP
4. SciPy
5. BioPy
5. Redis, MongoDB, Postgres, MySQL, Elastic Search
6. Django
7. SQLAlchemy
8. Bottle
9. Twisted
10. Vim
11. IDLE
12. gEdit
13. SublimeText2
14. Pyes
15. POW (Python on Wheels) & Dep...
16. pyQt
17. NumPy
18. numarray
19. matplotlib
20. scrape
21. Beautiful Soup
22. pythonweb
23. mechanize
24. flask

Hint: Not everything of this is installed by default. Change comments at the end of manifests/init.pp to influence it.
	
## TESTING A DJANGO APP FROM VAGRANT

		$ python manage.py runserver 0.0.0.0:8000
	
And open web browser to the IP address specified in network configuration within the Vagrantfile, e.g.:

http://192.168.33.10:8000/

