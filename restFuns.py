def getFuns(myInit):
    """factory to build the functions object, with the init"""
    return myFunctions(myInit).fns

class myFunctions(object):
    """The object to hold the http response functions"""
    
    def __init__(self,extRef):
        self.extRef = extRef

    def _fnDict(self):
        return {k:getattr(self,k) for k in
            ('get','put','post','delete')}
    
    @property
    def fns(self):
        """build and return a dict with get,put,post,delete functions"""
        return self._fnDict()
        
    @property
    def inputDoc(self):
        clen = int(self.extRef.environ.get('CONTENT_LENGTH',0))
        if clen:
            mret = self.extRef.environ['wsgi.input'].read(clen)
        else:
            mret = None
        return mret

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
        
    def delete(self):
        """the function to handle a DELETE request
        delFunction should implement a method to unlink/deactivate an existing resource"""
        return('DEL FN docin is %s'%self.inputDoc)
