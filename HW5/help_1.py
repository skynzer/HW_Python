def act_help():
    with open("help.txt", 'r') as rf:
        reader = rf.read()
        print("st" + reader.lstrip())
