import sys

class SaveRegistration:
    def __init__(obj, email, password, fileName):
        obj.email = email
        obj.password = password
        obj.fileName = fileName

    def appendToFile(obj):
        f = open(obj.fileName, "a")
        f.write(obj.email + ":" + obj.password + "\n")
        f.close()

    def doesUserExist(obj):
        with open(obj.fileName) as f:
           lines = f.readlines()
        
        for entry in lines:
            if obj.email in entry:
                return 1

    def isValidUser(obj):
        with open(obj.fileName) as f:
           lines = f.readlines()
        
        for entry in lines:
            if obj.email in entry and obj.password in entry:
                return 1
                