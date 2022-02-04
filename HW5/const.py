S_EMAIL = "User_email: "
S_NAME = "User_name: "
S_PASSWD = "User_password: "
S_PHONE = "User_phone: "
S_EXIST = "User with entered email already exists or email forbidden! Data not changed!"
S_DEL = "--------------------====================--------------------"


def unique_check(email, user_emails):
    if (email in user_emails) or email == "all":
        return False
    else:
        return True


