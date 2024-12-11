class MessageFormData:
    def __init__(self):
        self.__count:int|None = None
        self.__lists:dict|list|None = None
        self.__row:int|None = None
        self.__id:str|None = None
    @property
    def count(self)->int|None:
        return self.__count
    @count.setter
    def count(self, value:int|None = None)->None:
        self.__count = value
    @property
    def lists(self)->dict|list|None:
        return self.__lists
    @lists.setter
    def lists(self, value:dict|list|None = None)->None:
        self.__lists = value
    @property
    def row(self)->int|None:
        return self.__row
    @row.setter
    def row(self, value:int|None = None)->None:
        self.__row = value
    @property
    def id(self)->str|None:
        return self.__id
    @id.setter
    def id(self, value:str|None = None)->None:
        self.__id = value
    def show(self)->dict:
        return {
            "count": self.count,
            "list": self.lists,
            "row": self.row,
            "id": self.id
        }