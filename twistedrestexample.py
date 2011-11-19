import os
import sys
import site
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor

from restexample import application

resource = WSGIResource(reactor, reactor.getThreadPool(), application)
