import time
class MessageForm:
    def __init__(self):
        self.__status: bool|None = False
        self.__code:int|None = None
        self.__data:dict|None = None
        self.__message:str|None = None
        self.__security:bool|None = None
        self.__timer:bool = False
        self.__date:dict = {
            "start" : time.time(),
            "end" : 0.0,
            "run" : 0.0,
        }
    def clear(self)->"MessageForm":
        self.__status = None
        self.__code = None
        self.__data = None
        self.__message = None
        self.__security = False
        return self
    def status(self, status:bool) -> "MessageForm":
        self.__status = status
        return self
    def code(self, code:int) -> "MessageForm":
        self.__code = code
        return self
    def data(self, data:dict|None = None) -> "MessageForm":
        self.__data = data
        return self
    def message(self, message:str|None = None) -> "MessageForm":
        self.__message = message
        return self
    def security(self, security:bool) -> "MessageForm":
        self.__security = security
        return self
    def timer(self, timer:bool) -> "MessageForm":
        self.__timer = timer
        return self
    def show(self) -> dict:
        res:dict = {}
        if self.__status is not None:
            res["status"] = self.__status
        if self.__code is not None:
            res["code"] = self.__code
        if self.__data is not None:
            res["data"] = self.__data
        if self.__message is not None:
            res["message"] = self.__message
        if self.__security is not None:
            res["security"] = self.__security
        if self.__timer is not None:
            if self.__timer is True:
                self.__date["end"] = time.time()
                self.__date["run"] = self.__date["end"] - self.__date["start"]
                res["time"] = self.__date
        return res