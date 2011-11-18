def getFuns(myInit):
    """factory to build the functions object, with the init"""
    return myFunctions(myInit).fns

class myFunctions(object):
    """The object to hold the http response functions"""
    
    _fnDict = lambda self: {"get":self.get,"put":self.put,"post":self.post,"delete":self.delfn}
    
    def __init__(self,extRef):
        self.extRef = extRef
        self._fnDict = myFunctions._fnDict(self)  #override this for instance-specific dictionaries
        
    @property
    def fns(self):
        """build and return a dict with get,put,post,delete functions"""
        return (self._fnDict)
        
    @property
    def inputDoc(self):
        return self.extRef.environ['wsgi.input'].read()

    def get(self):
        """the function to handle a GET request - this example outputs a dir of both fnList and restFrame objects
        getFunction should implement a read request and be idempotent to the resource requested"""
        return(dir(self),dir(self.extRef))
        
    def post(self):
        """the function to handle a POST request
        postFunction should implement a method to create a new resource"""
        return(str(self.inputDoc))
        
    def put(self):
        """the function to handle a PUT request - this example outputs the restFrame object's environ
        putFunction should implement a method to update this resource"""
        return(str(self.extRef.environ))
        
    def delfn(self):
        """the function to handle a DELETE request
        delFunction should implement a method to unlink/deactivate an existing resource"""
        return('DEL FN docin is %s'%self.inputDoc)
