class SessionAuth:
    def __init__(self):
        self.__connect:bool = False
        self.__status:bool = False
        self.__token:str|None = None
        self.__uid:str|None = None
    def clear(self)->None:
        self.__connect = False
        self.__status= False
        self.__token = None
        self.__uid = None
    def show(self)->dict:
        res:dict = {
            'connect': self.__connect,
            'status': self.__status,
            'token': self.__token,
            'uid': self.__uid,
        }
        return res
    @property
    def connect(self)->bool:
        return self.__connect
    @connect.setter
    def connect(self,value:bool)->None:
        self.__connect = value
    @property
    def status(self)->bool:
        return self.__status
    @status.setter
    def status(self, status:bool)->None:
        self.__status = status
    @property
    def token(self)->str|None:
        return self.__token
    @token.setter
    def token(self, token:str|None = None)->None:
        self.__token = token
    @property
    def uid(self)->str|None:
        return self.__uid
    @uid.setter
    def uid(self, uid:str|None = None)->None:
        self.__uid = uid