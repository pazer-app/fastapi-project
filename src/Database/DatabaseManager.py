from src.Database.DatabaseClient import DatabaseClient
from src.Database.DatabaseHost import DatabaseHost
class DatabaseManager:
    def __init__(self):
        self.__list:dict = {}
    def host(self, name:str) -> DatabaseHost:
        if name not in self.__list:
            self.__list[name] = DatabaseHost()
        return self.__list[name]
    def client(self, name:str) -> DatabaseClient:
        return DatabaseClient(self.host(name))