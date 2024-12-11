import pymysql
from Module.Database.DatabaseHost import DatabaseHost
from Module.Form.MessageForm import MessageForm
from Module.Form.MessageFormData import MessageFormData
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
        if self.__state and self.__client is not None:
            return True
        try:
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
    def query(self, query:str, param:list=None, commit:bool = False)->MessageForm|None:
        form = MessageForm()
        if self.connect():
            try:
                with self.__client.cursor() as cursor:
                    form.clear()
                    res = MessageFormData()
                    cursor.execute(query, param or ())
                    if commit:
                        self.__client.commit()
                    results = cursor.fetchall()
                    res.count = len(results)
                    res.lists = results
                    res.row = cursor.rowcount if cursor.rowcount is not None else 0
                    res.id = cursor.lastrowid if cursor.lastrowid is not None else ""
                    form.status(True).code(200).dataForm(res).execute(True).timerEnd()
                    return form
            except pymysql.MySQLError as e:
                form.clear()
                form.status(False).code(e.args[0]).message(e.args[1]).execute(False).timerEnd()
                return form
            finally:
                self.close()
        else:
            form.clear()
            form.status(False).code(500).message("Error Connection").execute(False).timerEnd()
            return form