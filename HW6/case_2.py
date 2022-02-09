import csv
import names
import random
import datetime


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
        offset = 1
        for k in range(offset, len(ff)):
            date = datetime.datetime.now()
            if k < 50 + offset:
                ff[k]["date"] = date.replace(year=random.randint(1980, 1990))
            elif k < 150 + offset:
                ff[k]["date"] = date.replace(year=random.randint(1991, 2000))
            elif k < 300 + offset:
                ff[k]["date"] = date.replace(year=random.randint(2001, 2010))
            else:
                ff[k]["date"] = date.replace(year=random.randint(2011, 2021))
            writer.writerow(ff[k])


def create_combo(nne_file_name, combo_file_name, names_list):
    with open(nne_file_name, "r", newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=["number", "name", "email", "date"])
        for j in reader:
            ff.append([j["name"], j["date"]])
        ff = ff + names_list
        sorted_data = sorted(ff[1:])

    with open(combo_file_name, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "date", "phone", "gender", "salary"])
        writer.writeheader()
        gender_list = ["Male", "Female"]
        new_raw = {}
        phone_gen = lambda dig_str: "+" + dig_str[11:][::-1] + "(" + dig_str[8:11][::-1] + ")" \
                                    + "-" + dig_str[4:8][::-1] + '-' + dig_str[0:4][::-1]
        for k in range(1000):
            if len(sorted_data[k]) == 1:
                new_raw["name"] = sorted_data[k][0]
                new_raw["date"] = datetime.datetime.now()
                new_raw["email"] = new_raw["name"].replace(" ", "_") + "@yahoo.com"
                new_raw["phone"] = phone_gen(str(random.randint(111110000000, 99999999999999))[::-1])
                new_raw["gender"] = gender_list[random.randint(0, 1)]
                new_raw["salary"] = random.randint(1000, 99999)
            else:
                new_raw["name"] = sorted_data[k][0]
                new_raw["date"] = sorted_data[k][1]
                new_raw["email"] = new_raw["name"].replace(" ", "_") + "@yahoo.com"
                new_raw["phone"] = phone_gen(str(random.randint(111110000000, 99999999999999))[::-1])
                new_raw["gender"] = gender_list[random.randint(0, 1)]
                new_raw["salary"] = random.randint(1000, 99999)
            writer.writerow(new_raw)


digits_list = []
name_list = []
email_list = []
dict_list = []
for i in range(0, 1000):
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
update_nne("nee_2.csv")
create_combo("nee_2.csv", "combo.csv", name_list[450:])

# update_nne("nee.csv")
