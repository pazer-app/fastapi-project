from system.Config import LoggerEnable
from datetime import datetime
def Logger(tag:str,message:str) -> None:
    if LoggerEnable is True:
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{date}][{tag}]:{message}")
def Log(message) -> None:
    Logger("TEXT",message)
def LogDebug(message) -> None:
    Logger("DEBUG", message)
def LogInfo(message) -> None:
    Logger("INFO", message)
def LogWarning(message) -> None:
    Logger("WARNING", message)
def LogError(message) -> None:
    Logger("ERROR", message)