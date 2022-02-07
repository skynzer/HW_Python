import csv
import names
import random


def create_digits(name, dig_list):
    with open(name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(dig_list)


def create_names(name, names_list):
    with open(name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(names_list)


def create_emails(name, emails_list):
    with open(name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(emails_list)


def create_nne(name, nne_dict):
    with open(name, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["number", "name", "email"])
        writer.writeheader()
        writer.writerows(nne_dict)


def update_nne(file_name):
    with open(file_name, "r", newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=["number", "name", "email"])
        for j in reader:
            ff.append(j)

    with open(file_name, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[*ff[0].keys(), "date"])
        writer.writeheader()
        for i in ff[1:]:
            i["date"] = random.randint(1900, 2022)
            writer.writerow(i)
    #     # writer.writeheader()#     writer = csv.DictWriter(csv_f, fieldnames=columns)
    # #     # writer.writeheader()


digits_list = []
name_list = []
email_list = []
dict_list = []
for i in range(0, 451):
    digits_list.append([i])
    rand_name = names.get_full_name()
    email = rand_name.replace(" ", "_") + "@yahoo.com"
    name_list.append([rand_name])
    email_list.append([email])
    dict_list.append({"number": i, "name": rand_name, "email": email})

create_digits("digits_2.csv", digits_list[10:351])
create_names("names_2.csv", name_list[:400])
create_emails("emails_2.csv", email_list[:400])
create_nne("nee_2.csv", dict_list[0:450])
# update_nne("nee.csv")
