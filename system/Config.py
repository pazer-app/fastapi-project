from src.Database.DatabaseHost import DatabaseHost
from src.Database.DatabaseManager import DatabaseManager
dbms:DatabaseManager = DatabaseManager()
LoggerEnable:bool = True
database_read:str = "main_read"
database_write:str = "main_write"
__main_read:DatabaseHost = dbms.host(database_read)
__main_read.setHost("localhost","master","expexp","master")
__main_write:DatabaseHost = dbms.host(database_write)
__main_write.setHost("localhost","master","expexp","master")