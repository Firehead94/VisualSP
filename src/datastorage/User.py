import src.utilities.SystemUtils as SystemUtils
import src.datastorage.UserHelper as UserHelper


################################################################
#
# User object to be used with program for reference on who
# is currently using the program
# Created by: Justin Scott
#
################################################################

class User:

    user = {
        "UUID": "",
        "USERNAME": "Username",
        "FIRST_NAME": "Firstname",
        "LAST_NAME": "Lastname",
        "TIMESTAMP": SystemUtils.getTimeStamp(),
        "ACCESS_LEVEL": "Guest"
    }

    # Blank user template, populates timestamp with current and generates UUID
    def __init__(self, un = "Username", fn = "First", ln = "Last", al = "Guest", uuid = str(UserHelper.UserHelper.getUUID()), ts = SystemUtils.getTimeStamp()):
        self.user["USERNAME"] = un
        self.user["FIRST_NAME"] = fn
        self.user["LAST_NAME"] = ln
        self.user["ACCESS_LEVEL"] = al
        self.user["TIMESTAMP"] = ts
        self.user["UUID"] = uuid

    # Updates k with v in user
    def update(self, k, v):
        for key in self.user:
            if key == k:
                self.user.update({k: v})

    # Updates timestamp and
    # Saves current user to local device
    def save(self):
        self.update("TIMESTAMP", SystemUtils.getTimeStamp())
        UserHelper.UserHelper.update_user(self)


# Create user from disctionary object
def loadUser(userdict):
    user = User(userdict["USERNAME"], userdict["FIRST_NAME"], userdict["LAST_NAME"], userdict["ACCESS_LEVEL"], userdict["UUID"], userdict["TIMESTAMP"])
    return user


def newUser(username, first, last):
    user = User(username, first, last)
    return user
