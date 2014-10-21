import json, base

class restFrame(object):
    def __init__(self):
        self.dictOut = {}

    def mkPairings(self, lstFns):
        """links attributes of this object to passed in dictionary of functions"""
        self.__dict__.update(lstFns)
        return True

    def getFn (self, strFn):
        if callable(getattr(self,strFn,None)):
            return (getattr(self,strFn))
        else:
            return (False)

def application(environ, start_response, appFrame):
    myApp = appFrame
    appFrame.environ = environ
    myMethod = environ.get('REQUEST_METHOD').lower()
    myApp.dictOut['method'] = myMethod
    myFn = appFrame.getFn(myMethod)
    status = '500 ERROR'
    if myFn:
        try:
            myApp.dictOut['response'] = myFn()
            status = '200 OK'
        except Exception as e:
            myApp.dictOut['error'] = str(e)
    else:
        myApp.dictOut['error'] = "Method {} unknown".format(myMethod)
    myApp.dictOut['timestamp'] = base.lstNow()
    response_body = json.dumps(myApp.dictOut)
    response_headers = [('Content-Type', 'application/json'), ('Content-Length', str(len(str(response_body))))]
    start_response(status, response_headers)
    return response_body
