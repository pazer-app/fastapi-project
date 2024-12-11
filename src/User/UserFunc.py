from Module.Database.DataCore import DataCore
from Module.Database.DatabaseFunc import DatabaseQuery
from Module.Function.Function import SecurityString
from src.User.UserForm import UserForm
from system.Config import DB_USER_READ, DB_USER_WRITE
from system.System import DBSpace

def UserEmail()->bool:
    return True
def UserEmailAdd()->bool:
    return True
def UserEmailDelete()->bool:
    return True
def UserEmailSearch()->bool:
    return True
def UserEmailModify()->bool:
    return True

def UserId()->bool:
    return True
def UserIdAdd()->bool:
    return True
def UserIdDelete()->bool:
    return True
def UserIdSearch()->bool:
    return True
def UserIdModify()->bool:
    return True

def UserNick()->bool:
    return True
def UserNickAdd()->bool:
    return True
def UserNickDelete()->bool:
    return True
def UserNickSearch()->bool:
    return True
def UserNickModify()->bool:
    return True

def UserAdd()->bool:
    return True
def UserList()->bool:
    return True
def UserSearch()->bool:
    return True
def UserDelete()->bool:
    return True

def UserNo(no:int)->UserForm|None:
    database = DB_USER_READ
    query = f"SELECT `NO`,`NAME_FIRST`,`NAME_MID`,`NAME_LAST`,`NAME`,`SEX`,`CREATE`,`UPDATE`,`DELETE`,`STATUS` FROM {DBSpace("USER")} WHERE `NO` = %s limit 1"
    param = [no]
    core:DataCore = DatabaseQuery(database,query,param)
    res = core.res()
    if res.getStatus() is True:
        dataForm = res.getDataForm()
        if dataForm.count != 0:
            for items in dataForm.lists:
                data:dict = dict(items)
                user:UserForm = UserForm().from_dict(data)
                return user
    return None

def UserPassCheck(no:int, password:str)->None|bool:
    sec_pass: str = SecurityString(password)
    database = DB_USER_READ
    query = f"SELECT `NO`,`PASSWORD` FROM {DBSpace("USER")} WHERE `PASSWORD` = %s AND `NO` = %s limit 1"
    param = [sec_pass, no]
    core: DataCore = DatabaseQuery(database,query,param)
    res = core.res()
    if res.getStatus() is True:
        dataForm = res.getDataForm()
        if res.getExecute():
            if dataForm.count != 0:
                return True
            else:
                return False
    return None

def UserPasswordChange(no:int, value:str)->None|bool:
    sec_pass: str = SecurityString(value)
    return UserModify(no, "PASSWORD", str(sec_pass))

def UserModify(no:int, columns:str , value:str)->None|bool:
    database = DB_USER_WRITE
    query = f"UPDATE {DBSpace("USER")} SET `{columns}` = %s WHERE (`NO` = %s )"
    param = [value, no]
    commit = True
    core: DataCore = DatabaseQuery(database,query,param,commit)
    res = core.res()
    if res.getStatus() is True:
        dataForm = res.getDataForm()
        if res.execute():
            if dataForm.row != 0:
                return True
            else:
                return False
    return None