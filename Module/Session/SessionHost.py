class SessionHost:
    def __init__(self):
        self.__hostname:str = "localhost"
        self.__port:int = 6379
        self.__namespace:str = "default"
        self.__decode:bool = True
    # All Input
    def setHost(self, hostname:str, port:int, namespace:str, decode:bool = True)->None:
        self.__hostname = hostname
        self.__port = port
        self.__namespace = namespace
        self.__decode = decode
    def getHost(self)->dict:
        return {
            "hostname" : self.__hostname,
            "port" : self.__port,
            "namespace" : self.__namespace,
            "decode" : self.__decode
        }
    # Hostname
    @property
    def hostname(self)->str:
        return self.__hostname
    @hostname.setter
    def hostname(self, hostname)->None:
        self.__hostname = hostname
    # Port
    @property
    def port(self)->int:
        return self.__port
    @port.setter
    def port(self, port)->None:
        self.__port = port
    # Namespace
    @property
    def namespace(self)->str:
        return self.__namespace
    @namespace.setter
    def namespace(self, namespace)->None:
        self.__namespace = namespace
    # Decode
    @property
    def decode(self)->bool:
        return self.__decode
    @decode.setter
    def decode(self, decode)->None:
        self.__decode = decode