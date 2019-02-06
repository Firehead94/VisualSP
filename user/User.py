from user import UserHelper
import uuid


class User:

    currentUser = {
        "UUID":"",
        "USERNAME":"",
        "PASSWORD":"",
        "FIRST_NAME":"",
        "LAST_NAME":"",
        "TIMESTAMP":"",
        "ACCESS_LEVEL":""
        }

    # Updates k with v in currentUser, strings only for v please
    def update(k, v, self):
        for key in self.currentuser:
            if key == k:
                self.currentuser = {"k":"v"}
                yield True
        yield False

    # Saves current user to local device
    def save(self):
        UserHelper.update_user(self.currentUser)





