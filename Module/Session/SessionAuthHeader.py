class SessionAuthHeader:
    def __init__(self):
        self.__token:str|None = None
        self.__sid:str|None = None
    def clear(self)->None:
        self.__token = None
        self.__sid= None
    def show(self)->dict:
        return {
            'token': self.__token,
            'sid': self.__sid,
        }
    @property
    def token(self)->str|None:
        return self.__token
    @token.setter
    def token(self, token:str|None = None)->None:
        self.__token = token
    @property
    def sid(self)->str|None:
        return self.__sid
    @sid.setter
    def sid(self, sid:str|None = None)->None:
        self.__sid = sid