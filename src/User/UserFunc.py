from Module.Database.DataCore import DataCore
from Module.Database.DatabaseFunc import DatabaseQuery
from Module.Function.Function import SecurityString
from src.User.UserForm import UserForm
from system.Config import DB_USER_READ, DB_USER_WRITE
from system.System import DBSpace

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
    return UserColumnsChange(no, "NAME", str(sec_pass))

def UserNameChange(no:int, value:str)->None|bool:
    return UserColumnsChange(no, "NAME", str(value))

def UserSexChange(no:int, value:int)->None|bool:
    return UserColumnsChange(no, "SEX", str(value))

def UserNameFirstChange(no:int, value:str)->None|bool:
    return UserColumnsChange(no, "NAME_FIRST", str(value))

def UserNameMidChange(no:int, value:str)->None|bool:
    return UserColumnsChange(no, "NAME_MID", str(value))

def UserNameLastChange(no:int, value:str)->None|bool:
    return UserColumnsChange(no, "NAME_LAST", str(value))

def UserStatusChange(no:int, value:int)->None|bool:
    return UserColumnsChange(no, "STATUS", str(value))

def UserCreateChange(no:int, value:float)->None|bool:
    return UserColumnsChange(no, "STATUS", str(value))

def UserUpdateChange(no:int, value:float)->None|bool:
    return UserColumnsChange(no, "STATUS", str(value))

def UserDeleteChange(no:int, value:float)->None|bool:
    return UserColumnsChange(no, "STATUS", str(value))

def UserColumnsChange(no:int, columns:str , value:str)->None|bool:
    database = DB_USER_READ
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