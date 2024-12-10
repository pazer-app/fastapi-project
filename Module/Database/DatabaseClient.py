import pymysql
from Module.Database.DatabaseHost import DatabaseHost
from Module.Form.MessageForm import MessageForm
from Module.Logger.Logger import Logger
from system.Config import LoggerEnable
class DatabaseClient:
    def __init__(self, host:DatabaseHost):
        self.log = Logger(LoggerEnable)
        self.__host:DatabaseHost = host
        self.__state:bool = False
        self.__client:pymysql.connector.connect|None = None
    def host(self)->DatabaseHost:
        return self.__host
    def connect(self)->bool:
        self.log.info("Connecting to database")
        if self.__state and self.__client is not None:
            return True
        try:
            print(self.__host.hostname)
            connection = pymysql.connect(
                host=self.__host.hostname,
                user=self.__host.username,
                password=self.__host.password,
                database=self.__host.database,
                port=self.__host.port,
                charset=self.__host.charset,
                cursorclass=pymysql.cursors.DictCursor,
            )
            self.__client = connection
            self.__state = True
            return True
        except pymysql.MySQLError:
            self.__client = None
            self.__state = False
            return False
    def close(self)->bool:
        if self.__client is not None:
            self.__client.close()
        self.__client = None
        self.__state = False
        return True
    def query(self, query:str, param:list=None)->dict|None:
        form = MessageForm()
        if self.connect():
            try:
                with self.__client.cursor() as cursor:
                    form.clear()
                    res:dict = {}
                    cursor.execute(query, param or ())
                    results = cursor.fetchall()
                    res["count"] = len(results)
                    res["list"] = results
                    res["rows"] = cursor.rowcount if cursor.rowcount is not None else 0
                    res["id"] = cursor.lastrowid if cursor.lastrowid is not None else 0
                    form.status(True).code(200).data(res).timer(True)
                    return form.show()
            except pymysql.MySQLError as e:
                form.clear()
                form.status(False).code(e.args[0]).message(e.args[1]).timer(True)
                return form.show()
            finally:
                self.close()
        else:
            form.clear()
            form.status(False).code(500).message("Error Connection").timer(True)
            return form.show()