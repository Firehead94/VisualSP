import json
import os
import settings.config as config
import uuid
import user.User

################################################################
#
# Contains static methods to assist with user file management
# on local storage. Use update_user when creating new
# user
#
################################################################
global savePath

class UserHelper:
    global savePath
    savePAth = config.APPDATA_LOC + config.DEFAULT_LOCAL_PATH + config.DEFAULT_USER_FOLDER + "\\"

    ############################################
    #
    # Deletes user file of specified username
    # by deleting the local user file from
    # the location set in the config.py
    #
    ############################################
    @staticmethod
    def delete_user(username):
        os.remove(savePath + username + ".txt")

    ##################################################
    #
    # Get a user using username and returns user
    # object holding all user info. See User.py
    #
    ##################################################
    @staticmethod
    def get_user(username):
        with open(savePath + username + ".txt") as file:
            user = json.load(file)
        file.close()
        retuser = user.User(user)
        return retuser

    #################################################
    #
    # Update local user file using a user object
    # by dumping the contents of the internal
    # dictionary of the user object.
    #
    #################################################
    @staticmethod
    def update_user(currentuser):
        if isinstance(currentuser, user.User):
            with open(savePath + currentuser.user["username"]+".txt", "w") as outfile:
                json.dump(currentuser.user, outfile)
            outfile.close()
            return True
        return False

    #######################################################
    #
    # Get new uuid object, use str(UserHelper.User.getUUID())
    # if you need a string of the hex value
    #
    #######################################################
    @staticmethod
    def getUUID():
        return uuid.uuid1()

