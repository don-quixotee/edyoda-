def loginRequired(func):
    def login(username, password, value):
        if username =="username" and password == "password":
            return func(username, password, value)
        else:
            return "Auauthorised"

    return login

@loginRequired
def updateEmail(username, password, newEmail):
    return 'New email is {} '.format(newEmail)

def updateName(username, password, newName):
    return "New email is {} ". format(newName)

def changePassword(username, password, newPassword):
    return "New Password is {} ".format(newPassword)


print(updateEmail("username","password","abc@xyz.com"))
print(updateName("username","password","AB"))
print(changePassword("username","password", "abc@125"))