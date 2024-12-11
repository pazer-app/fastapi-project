import json
import redis
from redis import Redis
from Module.Form.MessageForm import MessageForm
from Module.Session.SessionHost import SessionHost
class Session:
    def __init__(self):
        self.__state:bool = False
        self.__client:Redis|None = None
        self.__host:SessionHost = SessionHost()
    def host(self)->SessionHost:
        return self.__host
    def connect(self)->bool:
        try:
            redis_client = redis.Redis(host=self.__host.hostname, port=self.__host.port, decode_responses=True)
            if redis_client.ping():
                self.__state = True
                self.__client = redis_client
                return True
            else:
                self.close()
                return False
        except redis.ConnectionError:
            self.close()
            return False
    def  close(self)->None:
        if self.__client is not None:
            self.__client.close()
        self.__state = False
        self.__client = None
    def _get_key(self, key)->str:
        return f"{self.__host.namespace}:{key}"
    def get_data(self, key)->MessageForm:
        form:MessageForm = MessageForm()
        try:
            if self.__state is False or self.__client.ping() is False:
                self.connect()
            if self.__client.ping():
                namespaced_key = self._get_key(key)
                data:str = self.__client.get(namespaced_key)
                if data is None:
                    form.status(False).message("Session Get Completed. - No Session").execute(True).timerEnd()
                    return form
                else:
                    form.status(True).message("Session Get Completed - Session").data(json.loads(data)).execute(True).timerEnd()
                    return form
            else:
                form.clear()
                form.status(False).message("Client Error").execute(False).timerEnd()
                return form
        except True:
            form.clear()
            form.status(False).message("Client Error").execute(False).timerEnd()
            return form
    def set_data(self, key, data:dict)->MessageForm:
        form:MessageForm = MessageForm()
        try:
            if self.__state is False or self.__client.ping() is False:
                self.connect()
            if self.__client.ping():
                namespaced_key = self._get_key(key)
                self.__client.set(namespaced_key, json.dumps(data))
                form.clear()
                form.status(True).message("Session Save Completed").execute(True).timerEnd()
                return form
            else:
                form.clear()
                form.status(False).message("Client Error").execute(False).timerEnd()
                return form
        except True:
            form.clear()
            form.status(False).message("Client Error").execute(False).timerEnd()
            return form
    def delete(self, key)->MessageForm:
        form:MessageForm = MessageForm()
        try:
            if self.__state is False or self.__client.ping() is False:
                self.connect()
            if self.__client.ping():
                namespaced_key = self._get_key(key)
                self.__client.delete(namespaced_key)
                form.clear()
                form.status(True).message("Session Delete Completed").execute(True).timerEnd()
                return form
            else:
                form.clear()
                form.status(False).message("Client Error").execute(False).timerEnd()
                return form
        except True:
            form.clear()
            form.status(False).message("Client Error").execute(False).timerEnd()
            return form