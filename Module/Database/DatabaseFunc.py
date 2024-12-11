from Module.Database.DataCore import DataCore
from system.System import DBSpace
def DatabaseQuery(database:str,query:str, param:list, commit:bool = False)->DataCore:
    core: DataCore = DataCore()
    core.database = database
    core.query = query
    core.param = param
    core.commit = commit
    core.execute()
    return core