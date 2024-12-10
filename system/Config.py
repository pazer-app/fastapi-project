LoggerEnable:bool = True
SystemConfig:dict = {
    "allow_cors" : True,
    "allow_origins" : ["http://localhost:5173"],
    "allow_credentials" : True,
    "allow_methods" : ["*"],
    "allow_headers" : ["*"],
}
SessionHostInfo:dict = {
    "hostname" : "127.0.0.1",
    "port" : 6379,
    "namespace" : "test",
    "decode" : True,
}
DatabaseHostInfo:dict = {
    "main_read" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "test",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8",
    },
    "main_write" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "test",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8",
    },
    "auth_read" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "test",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8",
    },
    "auth_write" : {
        "hostname" : "localhost",
        "username" : "master",
        "password" : "test",
        "database" : "master",
        "port" : 3306,
        "charset" : "utf8",
    }
}
DB_AUTH_READ = "auth_read"
DB_AUTH_WRITE = "auth_write"
DB_MAIN_READ= "main_read"
DB_MAIN_WRITE = "main_write"