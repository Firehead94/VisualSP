import json
import os
import settings.config


class UserHelper:

    # Create New User Object
    @staticmethod
    def new_user(currentuser):
        with open(settings.config.storage["path" + settings.config.osType] + currentuser["username"]+".txt", "w") as outfile:
            json.dump(currentuser, outfile)
        outfile.close()

    # Delete passed User UUID
    @staticmethod
    def delete_user(username):
        os.remove(settings.config.storage["path" + settings.config.osType] + username + ".txt")

    # Get a user using username and returns user dictionary
    @staticmethod
    def get_user(username):
        with open(settings.config.storage["path" + settings.config.osType] + username + ".txt") as file:
            user = json.load(file)
        file.close()
        return user

    # Update User Objects
    @staticmethod
    def update_user(currentuser):
        with open(settings.config.storage["path" + settings.config.osType] + currentuser["username"]+".txt", "w") as outfile:
            json.dump(currentuser, outfile)
        outfile.close()
