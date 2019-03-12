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
        "USERNAME":"Username",
        "FIRST_NAME":"Firstname",
        "LAST_NAME":"Lastname",
        "TIMESTAMP":"",
        "ACCESS_LEVEL":"Guest"
        }

    # Blank user template, populates timestamp with current and generates UUID
    def __init__(self):
        self.user["TIMESTAMP"] = system.SystemHelper.getTimeStamp()
        self.user["UUID"] = str(UserHelper.UserHelper.getUUID())
        self.loadUser(self.user)

    # Create user from disctionary object
    def loadUser(self, userdict):
        self.user["USERNAME"] = userdict["USERNAME"]
        self.user["FIRST_NAME"] = userdict["FIRST_NAME"]
        self.user["LAST_NAME"] = userdict["LAST_NAME"]
        self.user["TIMESTAMP"] = userdict["TIMESTAMP"]
        self.user["ACCESS_LEVEL"] = userdict["ACCESS_LEVEL"]
        self.user["UUID"] = userdict["UUID"]
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
        UserHelper.UserHelper.update_user(self.user)






