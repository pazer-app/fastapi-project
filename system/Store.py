from Module.Database.DatabaseManager import DatabaseManager
from Module.Logger.Logger import Logger
from Module.Session.Session import Session
class Store:
    def __init__(self):
        self.__dbms:DatabaseManager=DatabaseManager()
        self.__session:Session = Session()
        self.__logger:Logger = Logger()
    def dbms(self)->DatabaseManager:
        return self.__dbms
    def session(self)->Session:
        return self.__session
    def log(self)->Logger:
        return self.__logger