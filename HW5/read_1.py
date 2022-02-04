import const


def msg_user_form(email, user_storage):
    message = const.S_EMAIL + email + "\n" \
              + const.S_NAME + user_storage[email]["name"] + "\n" \
              + const.S_PASSWD + user_storage[email]["password"] + "\n" \
              + const.S_PHONE + user_storage[email]["phone"]
    return message


def read_info(email, user_emails, user_storage):
    if email in user_emails:
        return msg_user_form(email, user_storage)
    elif email == "all":
        message = all_user_info(user_storage)
    else:
        message = "No user with email: " + email
    return message


def all_user_info(user_storage):
    message = ""
    for k, v in user_storage.items():
        message = message + const.S_EMAIL + k + ", " \
                  + const.S_NAME + v["name"] + ", " \
                  + const.S_PASSWD + v["password"] + ", "\
                  + const.S_PHONE + v["phone"] + "\n"
    return message.rstrip()


