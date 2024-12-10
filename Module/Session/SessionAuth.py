class SessionAuth:
    def __init__(self):
        self.__status:bool = False
        self.__token:str|None = None
        self.__uid:str|None = None
    def clear(self)->None:
        self.__status:bool = False
        self.__token:str|None = None
        self.__uid:str|None = None
    def show(self)->dict:
        res:dict = {
            'status': self.__status,
            'token': self.__token,
            'uid': self.__uid,
        }
        return res
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status:bool):
        self.__status = status
    @property
    def token(self):
        return self.__token
    @token.setter
    def token(self, token:str|None):
        self.__token = token
    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid:str|None):
        self.__uid = uid