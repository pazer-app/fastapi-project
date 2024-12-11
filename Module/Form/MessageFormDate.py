class MessageFormDate:
    def __init__(self):
        self.__start:float|None = None
        self.__end:float|None = None
        self.__run:float|None = None
    def show(self)->dict:
        return {
            'start': self.__start,
            'end': self.__end,
            'run': self.__run,
        }
    @property
    def start(self)->float|None:
        return self.__start
    @start.setter
    def start(self,value:float)->None:
        self.__start = value
    @property
    def end(self)->float|None:
        return self.__end
    @end.setter
    def end(self,value:float)->None:
        self.__end = value
    @property
    def run(self)->float|None:
        return self.__run
    @run.setter
    def run(self,value:float)->None:
        self.__run = value