from h11 import Request

from Module.Form.MessageForm import MessageForm
from Module.Session.SessionAuth import SessionAuth
def authMode(sid:str, token:str)->SessionAuth:
    auth = SessionAuth()
    from main import session
    form:MessageForm = session.get_data(sid)
    if form.getStatus() is True:
        data:dict = form.getData()
        uToken:str = data.get('token')
        print(uToken,token)
        if uToken == token:
            auth.clear()
            auth.status = True
            auth.uid = data.get('uid')
            auth.token = data.get('token')
        else:
            auth.clear()
        return auth
    else:
        auth.clear()
        return auth

def authSave(sid:str, token:str, uid:str)->bool:
    print(sid, token)
    data:dict = {
        "token":token,
        "uid":uid,
    }
    from main import session
    if session.set_data(sid, data) is True:
        return True
    return False

def authHeader(request:Request)->dict:
    headers = request.headers
    token = headers["Auth-Token"]
    sid = headers["Auth-Sid"]
    return {"sid":sid, "token":token}