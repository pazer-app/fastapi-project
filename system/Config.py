# CONFIG - START

# CONFIG VARS - START
DB_SPACE = "PZ"
DB_USER_READ = "user_read"
DB_USER_WRITE = "user_write"
DB_AUTH_READ = "auth_read"
DB_AUTH_WRITE = "auth_write"
DB_MAIN_READ= "main_read"
DB_MAIN_WRITE = "main_write"
# CONFIG VARS - END

# LOGGER SETTING - START
LoggerEnable:bool = True
# LOGGER SETTING - END

# APP CORE SETTING - START
SystemConfig:dict = {
    "allow_cors" : True,
    "allow_origins" : ["http://localhost:5173"],
    "allow_credentials" : True,
    "allow_methods" : ["*"],
    "allow_headers" : ["*"],
}
# APP CORE SETTING - END

# SESSION SETTING - START
SessionHostInfo:dict = {
    "hostname" : "127.0.0.1",
    "port" : 6379,
    "namespace" : "test",
    "decode" : True,
}
# SESSION SETTING - END

# DATABASE SETTING - START
DatabaseHostInfo:dict = {
    "main_read" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    },
    "main_write" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    },
    "auth_read" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    },
    "auth_write" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    },
    "user_read" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    },
    "user_write" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "expexp",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8mb4",
    }
}
# DATABASE SETTING - END

# MESSAGE RESPONSE SETTING - START
MESSAGE_RESPONSE = {
    200: {
        "description": "OK.",
        "content": {
            "application/json": {
                "example": {
                    "code":200,
                    "status":"True",
                    "message":"string|None",
                    "security":"bool|None",
                    "data": "array|None",
                    "time": "dict|None",
                }
            }
        },
    },
    400: {
        "description": "Bad Request.",
        "content": {
            "application/json": {
                "example": {
                    "code": 400,
                    "status": "False",
                    "message": "string|None",
                }
            }
        },
    },
    422: {
        "description": "Unprocessable Content.",
        "content": {
            "application/json": {
                "example": {
                    "code": 422,
                    "status":"False",
                    "message":"Execution cannot proceed due to invalid input.",
                    "error" : "dict|None"
                }
            }
        },
    },
}
# MESSAGE RESPONSE SETTING - END

# CONFIG -END