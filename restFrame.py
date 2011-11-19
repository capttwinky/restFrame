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
    myApp.environ = environ
    myOut = myApp.dictOut
    myMethod = environ.get('REQUEST_METHOD').lower()
    myOut['method'] = myMethod
    myFn = myApp.getFn(myMethod)
    status = '500 ERROR'
    if myFn:
        try:
            myOut['response'] = myFn()
            status = '200 OK'
        except Exception as e:
            myOut['error'] = str(e)
    else:
        myOut['error'] = "%s unknown"%myMethod
    myOut['timestamp'] = base.lstNow()
    response_body = json.dumps(myOut)
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(str(response_body))))]
    start_response(status, response_headers)
    return response_body
