from h11 import Request
from starlette.datastructures import Headers
from Module.Form.MessageForm import MessageForm
from Module.Session.SessionAuth import SessionAuth
from Module.Session.SessionAuthHeader import SessionAuthHeader
def getSession(sid:str, token:str)->SessionAuth:
    auth = SessionAuth()
    from main import session
    form:MessageForm = session.get_data(sid)
    if form.getStatus() is True and form.getExecute() is True:
        data:dict = form.getData()
        uToken:str = data.get('token')
        print(uToken,token)
        if uToken == token:
            auth.clear()
            auth.status = True
            auth.connect = True
            auth.uid = data.get('uid')
            auth.token = data.get('token')
        else:
            auth.clear()
            auth.connect = True
        return auth
    else:
        auth.clear()
        return auth
def setSession(sid:str, token:str, uid:str)->bool:
    print(sid, token)
    data:dict = {
        "token":token,
        "uid":uid,
    }
    from main import session
    if session.set_data(sid, data).getStatus() is True:
        return True
    return False
def getHeader(request:Request)->SessionAuthHeader:
    headers:Headers = request.headers
    token = headers.get('token', None)
    sid = headers.get('sid', None)
    print(sid, token)
    res:SessionAuthHeader = SessionAuthHeader()
    res.token = token
    res.sid = sid
    return res
def deleteSession(sid:str)->bool:
    from main import session
    return session.delete(sid).getStatus()