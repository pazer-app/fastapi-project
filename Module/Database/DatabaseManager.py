from Module.Database.DatabaseClient import DatabaseClient
from Module.Database.DatabaseHost import DatabaseHost
class DatabaseManager:
    def __init__(self):
        self.__list:dict = {}
    def host(self, name:str)->DatabaseHost:
        if name not in self.__list:
            self.__list[name] = DatabaseHost()
        return self.__list[name]
    def hostForm(self, name:str, form:DatabaseHost)->None:
        self.__list[name] = form
    def client(self, name:str)->DatabaseClient:
        return DatabaseClient(self.host(name))