class SessionHost:
    def __init__(self):
        self.__hostname:str|None = None
        self.__port:int|None = None
        self.__namespace:str|None = None
        self.__decode:bool|None = None
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
    def clear(self)->None:
        self.__hostname = None
        self.__port = None
        self.__namespace = None
        self.__decode = None
    # Hostname
    @property
    def hostname(self)->str|None:
        return self.__hostname
    @hostname.setter
    def hostname(self, hostname:str|None = None)->None:
        self.__hostname = hostname
    # Port
    @property
    def port(self)->int|None:
        return self.__port
    @port.setter
    def port(self, port:int|None = None)->None:
        self.__port = port
    # Namespace
    @property
    def namespace(self)->str|None:
        return self.__namespace
    @namespace.setter
    def namespace(self, namespace:str|None = None)->None:
        self.__namespace = namespace
    # Decode
    @property
    def decode(self)->bool|None:
        return self.__decode
    @decode.setter
    def decode(self, decode:bool|None)->None:
        self.__decode = decode