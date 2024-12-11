from Module.Database.DatabaseClient import DatabaseClient
from Module.Form.MessageForm import MessageForm
class DataCore:
    def __init__(self):
        self.__database:str|None = None
        self.__query:str|None = None
        self.__result:MessageForm = MessageForm()
        self.__param:list|None = None
        self.__commit:bool = False
        self.__result.status(False)
    def clear(self)->None:
        self.__query = None
        self.__result.clear()
        self.__param = None
        self.__database = None
        self.__commit = False
        self.__result.status(False)
    def show(self)->dict:
        return {
            "query":self.__query,
            "params":self.__param,
            "commit":self.__commit,
            "database":self.__database,
        }
    def execute(self)->bool:
        from main import dbms
        if self.__database is None:
            return False
        if self.__query is None:
            return False
        if self.__param is None:
            return False
        client:DatabaseClient = dbms.client(self.__database)
        self.__result = client.query(self.__query,self.__param,self.__commit)
    def res(self)->MessageForm|None:
        return self.__result
    @property
    def query(self)->str|None:
        return self.__query
    @query.setter
    def query(self,value:str|None = None)->None:
        self.__query = value
    @property
    def result(self)->MessageForm|None:
        return self.__result
    @result.setter
    def result(self,value:MessageForm|None=None)->None:
        self.__result = value
    @property
    def param(self)->list|None:
        return self.__param
    @param.setter
    def param(self,value:list|None=None)->None:
        self.__param = value
    @property
    def commit(self)->bool:
        return self.__commit
    @commit.setter
    def commit(self,value:bool = False)->None:
        self.__commit = value
    @property
    def database(self)->str|None:
        return self.__database
    @database.setter
    def database(self,value:str|None=None)->None:
        self.__database = value