def lstNow():
    import datetime
    strNow = datetime.datetime.strftime(datetime.datetime.now(),"%Y,%m,%d,%H,%M,%S,%f")
    return(strNow.split(","))
        
def http2str(strUrl, strMethod = 'GET', strBody=None, dictHeaders=None):
    import httplib
    strReq = strUrl.partition("//")[2] if '//' in strUrl else strUrl
    if '/' in strReq:
        strSvr,strRes,_ = strReq.partition('/')
    else:
        strSvr,strRes = strReq,'/'
    mCon = httplib.HTTPConnection(strSvr, timeout=900.0)
    lstRequest = [thing for thing in [strMethod,strRes,strBody,dictHeaders] if thing]
    try:
        mCon.request(*lstRequest)
        strResponse = mCon.getresponse().read()
    except Exception as e:
        strResponse= str(e)
        print lstRequest
    return (strResponse)
    
if __name__=="__main__":
    #print(http2str('http://www.google.com'))
    
    strUrl = "http://localhost:8080"
    print(http2str(strUrl,'GET'))
    print(http2str(strUrl,'POST'))
    print(http2str(strUrl,'POST','jp=cool'))
    print(http2str(strUrl,'PUT','jp=cool'))
    print(http2str(strUrl,'DELETE','jp=cool'))
    print(http2str(strUrl,'ELEPHANT','jp=cool'))
