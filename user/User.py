from user import UserHelper
import uuid
import system.SystemHelper
import settings.config

################################################################
#
# User object to be used with program for reference on who
# is currently using the program
#
################################################################

class User:

    user = {
        "UUID":"",
        "USERNAME":"",
        "FIRST_NAME":"",
        "LAST_NAME":"",
        "TIMESTAMP":"",
        "ACCESS_LEVEL":""
        }

    # Blank user template, populates timestamp with current and generates UUID
    def __init__(self):
        self.User.user["TIMESTAMP"] = system.SystemHelper.getTimeStamp()
        self.user["UUID"] = UserHelper.UserHelper.getUUID()
        self.save()

    # Create user from disctionary object
    def __init__(self, userdict):
        self.user["USERNAME"] = userdict["USERNAME"]
        self.user["FIRST_NAME"] = userdict["FIRST_NAME"]
        self.user["LAST_NAME"] = userdict["LAST_NAME"]
        self.user["TIMESTAMP"] = userdict["TIMESTAMP"]
        self.user["ACCESS_LEVEL"] = userdict["ACCESS_LEVEL"]
        self.user["UUID"] = userdict["UUID"]
        self.save()

    # For creating new users
    # Username, First Name, Last Name
    def __init__(self, un, fn, ln):
        self.user["USERNAME"] = un
        self.user["FIRST_NAME"] = fn
        self.user["LAST_NAME"] = ln
        self.user["TIMESTAMP"] = system.SystemHelper.getTimeStamp()
        self.user["ACCESS_LEVEL"] = settings.config.DEFAULT_ACCESS_LEVEL
        self.user["UUID"] = UserHelper.UserHelper.getUUID()
        self.save()

    # For creating user object based off existing user
    # Username, First Name, Last Name, Timestamp of last access, Access Level
    def __init__(self, uid, un, fn, ln, ts, al):
        self.user["USERNAME"] = un
        self.user["FIRST_NAME"] = fn
        self.user["LAST_NAME"] = ln
        self.user["TIMESTAMP"] = ts
        self.user["ACCESS_LEVEL"] = al
        self.user["UUID"] = uid
        self.save()

    # Updates k with v in user
    def update(k, v, self):
        for key in self.user:
            if key == k:
                self.user = {k:v}
                yield True
        yield False

    # Updates timestamp and
    # Saves current user to local device
    def save(self):
        self.update("TIMESTAMP", system.SystemHelper.getTimeStamp())
        UserHelper.update_user(self.user)






