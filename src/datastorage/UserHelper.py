import json
import os
import uuid
import src.datastorage.FileHelper as FileHelper
import src.datastorage.User as User
import pickle
import src.utilities.SystemUtils as SystemUtils


################################################################
#
# Contains static methods to assist with user file management
# on local storage. Use update_user when creating new
# user
# Created by: Justin Scott / Jacob Stade
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
        os.remove(FileHelper.USER_FLDR + username + ".pkl")

    ##################################################
    #
    # Get a user using username and returns user
    # dict holding all user info. See User.py
    #
    ##################################################
    @staticmethod
    def get_user(username):
        with open(FileHelper.USER_FLDR + username + ".pkl", "rb") as file:
            user = pickle.load(file)
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
            print("File Updated: ",FileHelper.USER_FLDR + currentuser.user["USERNAME"] + ".pkl")
            with open(FileHelper.USER_FLDR + currentuser.user["USERNAME"] + ".pkl", "wb") as outfile:
                pickle.dump(currentuser.user, outfile, protocol=pickle.HIGHEST_PROTOCOL)
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

