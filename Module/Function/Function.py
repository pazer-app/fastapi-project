import hashlib

from fastapi import Header
class AuthHeaders:
    def __init__(
        self,
        token: str = Header(None, alias="Auth-Token"),
        sid: str = Header(None, alias="Auth-Sid")
    ):
        self.token = token
        self.sid = sid

def SecurityString(value:str)->str:
    md5_hash = hashlib.md5(value.encode())
    hashed_data = md5_hash.hexdigest()
    return hashed_data