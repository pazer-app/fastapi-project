class DatabaseHost:
    def __init__(self):
        self.__hostname:str = "localhost"
        self.__username:str = ""
        self.__password:str = ""
        self.__database:str = ""
        self.__port:int = 3306
        self.__charset:str = "utf8mb4"
    # Host to Dict
    def getData(self) -> dict:
        return {
            "hostname":self.__hostname,
            "username":self.__username,
            "password":self.__password,
            "database":self.__database,
            "port":self.__port,
            "charset":self.__charset
        }
    # All Input
    def setHost(self,
                hostname:str,
                username:str,
                password:str,
                database:str,
                port:int = 3306,
                charset:str = "utf8mb4"
                ) -> None:
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__database = database
        self.__port = port
        self.__charset = charset
    # Hostname
    @property
    def hostname(self) -> str:
        return self.__hostname
    @hostname.setter
    def hostname(self, hostname) -> None:
        self.__hostname = hostname
    # Username
    @property
    def username(self) -> str:
        return self.__username
    @username.setter
    def username(self, username) -> None:
        self.__username = username
    # Password
    @property
    def password(self) -> str:
        return self.__password
    @password.setter
    def password(self, password) -> None:
        self.__password = password
    # Database
    @property
    def database(self) -> str:
        return self.__database
    @database.setter
    def database(self, database) -> None:
        self.__database = database
    # Port
    @property
    def port(self) -> int:
        return self.__port
    @port.setter
    def port(self, port) -> None:
        self.__port = port
    # Charset
    @property
    def charset(self) -> str:
        return self.__charset
    @charset.setter
    def charset(self, charset) -> None:
        self.__charset = charset