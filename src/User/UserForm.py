class UserForm:
    def __init__(self):
        self.no: int | None = None
        self.name_first: str | None = None
        self.name_mid: str | None = None
        self.name_last: str | None = None
        self.name: str | None = None
        self.sex: int | None = None
        self.create: float | None = None
        self.update: float | None = None
        self.delete: float | None = None
        self.status: int | None = None
    def clear(self)->None:
        self.__init__()
    def show(self) -> dict:
        return {"ss":self.__dict__}
    @classmethod
    def from_dict(cls, data: dict):
        obj = cls()
        for key, value in data.items():
            attr_name = str(key).lower()
            if hasattr(obj, attr_name):
                setattr(obj, attr_name, value)
        return obj
