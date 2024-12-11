class UserIdForm:
    def __init__(self):
        self.__no:int|None = None
        self.__type:int|None = None
        self.__id:str|None = None
        self.__uno:int|None = None
        self.__create:float|None = None
        self.__update:float|None = None
        self.__delete:float|None = None
        self.__status:bool|None = None
    def clear(self)->None:
        self.__init__()
    def show(self)->dict:
        return self.__dict__
    @classmethod
    def from_dict(cls, data: dict):
        obj = cls()
        for key, value in data.items():
            attr_name = str(key).lower()
            if hasattr(obj, attr_name):
                setattr(obj, attr_name, value)
        return obj