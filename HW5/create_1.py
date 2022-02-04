def create_user(email,
                name,
                password,
                phone,
                user_emails,
                user_storage):
    user_info = [email, name, password, phone]
    user_emails.append(email)
    user_storage[email] = {"name": name,
                           "password": password,
                           "phone": phone}
    print(user_info)
    return None
