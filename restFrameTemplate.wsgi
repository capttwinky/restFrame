import os
import sys

apppath = os.path.dirname(os.path.realpath(__file__))
if apppath not in sys.path:
    sys.path.append(apppath)
    
import restFuns
from restFrame import restFrame
from restFrame import application as rfApp

class AppClass:
    """"""
    def __init__(self, environ, start_response):
        self.application = rfApp
        self.environ = environ
        self.start = start_response
        self.frame = restFrame()
        self.fns = restFuns.getFuns(self.frame)
        self.frame.mkPairings(self.fns)
        
    def __iter__(self):
        yield self.application(self.environ, self.start, self.frame)
        
def application(environ, start_response):    
    return AppClass(environ, start_response)
