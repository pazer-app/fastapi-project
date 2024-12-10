from datetime import datetime
class Logger:
    def __init__(self, enable:bool = True):
        self.__enable:bool = True
    def enable(self, enable:bool)->None:
        self.__enable = enable
    def tag(self, tag:str, value:str)->None:
        if self.__enable is True:
            now = datetime.now()
            date = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{date}][{tag}]: {value}")
    def info(self, value:str)->None:
        self.tag("INFO", value)
    def warning(self, value:str)->None:
        self.tag("WARNING", value)
    def error(self, value:str)->None:
        self.tag("ERROR", value)
    def debug(self, value:str)->None:
        self.tag("DEBUG", value)
    def system(self, value:str)->None:
        self.tag("SYSTEM", value)
    def critical(self, value:str)->None:
        self.tag("CRITICAL", value)
    def text(self, value:str)->None:
        self.tag("TEXT", value)
    def message(self, value:str)->None:
        self.tag("MESSAGE", value)