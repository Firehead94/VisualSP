import json
import os
import uuid
import src.datastorage.FileHelper as FileHelper
import src.datastorage.User as User


################################################################
#
# Contains static methods to assist with user file management
# on local storage. Use update_user when creating new
# user
# Created by: Justin Scott
#
################################################################
class UserHelper:

    ############################################
    #
    # Deletes user file of specified username
    # by deleting the local user file from
    # the location set in the config.py
    #
    ############################################
    @staticmethod
    def delete_user(username):
        os.remove(FileHelper.USER_FLDR + username + ".json")

    ##################################################
    #
    # Get a user using username and returns user
    # dict holding all user info. See User.py
    #
    ##################################################
    @staticmethod
    def get_user(username):
        with open(FileHelper.USER_FLDR + username + ".json") as file:
            user = json.load(file)
        file.close()
        return user

    #################################################
    #
    # Update local user file using a user object
    # by dumping the contents of the internal
    # dictionary of the user object.
    #
    #################################################
    @staticmethod
    def update_user(currentuser):
        if isinstance(currentuser, User.User):
            print(FileHelper.USER_FLDR + currentuser.user["USERNAME"] + ".json")
            with open(FileHelper.USER_FLDR + currentuser.user["USERNAME"] + ".json", "w") as outfile:
                json.dump(currentuser.user, outfile, indent=2)
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

