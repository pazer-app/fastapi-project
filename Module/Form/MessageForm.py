import time
from starlette.responses import JSONResponse
from Module.Form.MessageFormData import MessageFormData
from Module.Form.MessageFormDate import MessageFormDate
class MessageForm:
    def __init__(self):
        self.__status: bool|None = False
        self.__statusCode: int = 500
        self.__code:int|None = None
        self.__data:dict|list|None = None
        self.__message:str|None = None
        self.__security:bool|None = None
        self.__index:int|None = None
        self.__indexString:str|None = None
        self.__timer:bool = False
        self.__error:dict|None = None
        self.__dataForm:MessageFormData|None = None
        self.__execute:bool|None = None
        self.__date:MessageFormDate|None = MessageFormDate()
        self.__date.start = time.time()
    def clear(self)->"MessageForm":
        self.__status = False
        self.__statusCode = 500
        self.__code= None
        self.__data = None
        self.__message = None
        self.__security = None
        self.__index = None
        self.__indexString = None
        self.__timer = False
        self.__error = None
        self.__dataForm = None
        self.__execute = None
        return self
    def getExecute(self)->bool|None:
        return self.__execute
    def getError(self)->dict|None:
        return self.__error
    def getDataForm(self)-> MessageFormData|None:
        return self.__dataForm
    def getIndexString(self) -> str|None:
        return self.__indexString
    def getIndex(self) -> int|None:
        return self.__index
    def getStatusCode(self)->int:
        return self.__statusCode
    def getStatus(self)->bool|None:
        return self.__status
    def getCode(self)->int|None:
        return self.__code
    def getData(self)->dict|list|None:
        return self.__data
    def getMessage(self)->str|None:
        return self.__message
    def getSecurity(self)->bool|None:
        return self.__security
    def getTimer(self)->bool|None:
        return self.__timer
    def getDate(self)->dict|None:
        return self.__date
    def execute(self, value:bool|None = None)->"MessageForm":
        self.__execute = value
        return self
    def error(self, value:dict|None = None)->"MessageForm":
        self.__error = value
        return self
    def dataForm(self, value:MessageFormData|None = None)->"MessageForm":
        self.__dataForm = value
        return self
    def status(self, value:bool|None = None)->"MessageForm":
        self.__status = value
        return self
    def code(self, value:int|None = None)->"MessageForm":
        self.__code = value
        return self
    def data(self, value: dict|list|None = None)-> "MessageForm":
        self.__data = value
        return self
    def message(self, value:str|None = None)->"MessageForm":
        self.__message = value
        return self
    def security(self, value:bool|None = None)->"MessageForm":
        self.__security = value
        return self
    def timer(self, value:bool|None = None)->"MessageForm":
        self.__timer = value
        return self
    def statusCode(self, value:int = 500)->"MessageForm":
        self.__statusCode = value
        return self
    def index(self, value:int|None = None)->"MessageForm":
        self.__index = value
        return self
    def indexString(self, value:str|None = None)->"MessageForm":
        self.__indexString = value
        return self
    def timerEnd(self)->"MessageForm":
        self.__timer = True
        self.__date.end = time.time()
        self.__date.run = self.__date.end - self.__date.start
        return self
    def show(self)->dict:
        res:dict = {}
        if self.__code is not None:
            res["code"] = self.__code
        if self.__status is not None:
            res["status"] = self.__status
        if self.__data is not None:
            res["data"] = self.__data
        if self.__message is not None:
            res["message"] = self.__message
        if self.__security is not None:
            res["security"] = self.__security
        if self.__execute is not None:
            res["execute"] = self.__execute
        if self.__error is not None:
            res["error"] = self.__error
        if self.__timer is not None:
            if self.__timer is True:
                res["time"] = self.__date.show()
        return res
    def json(self, code:int|None = None)->JSONResponse:
        if code is not None:
            self.statusCode(code)
        return JSONResponse(
            content=self.show(),
            status_code=self.getStatusCode(),
        )