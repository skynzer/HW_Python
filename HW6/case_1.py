import csv
import names
import random


def create_empty_file(name):
    f = open(name, "w")
    f.close()


def create_file_with_0_to_150(name):
    with open(name, "w") as f:
        writer = csv.writer(f)
        for i in range(0, 151):
            writer.writerow([i])


def create_names(name):
    with open(name, "w") as f:
        writer = csv.writer(f)
        for i in range(0, 100):
            writer.writerow([names.get_full_name()])


def create_emails(name):
    with open(name, "w") as f:
        writer = csv.writer(f)
        for i in range(0, 100):
            writer.writerow([names.get_full_name().replace(" ", "_")+"@gmail.com"])


def create_nne(name):
    with open(name, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["number", "name", "email"])
        writer.writeheader()
        for i in range(0, 100):
            rand_name = names.get_full_name()
            writer.writerow({"number": i, "name": rand_name, "email": rand_name.replace(" ", "_")+"@gmail.com"})


create_empty_file("empty.csv")
create_file_with_0_to_150("digits.csv")
create_names("names.csv")
create_emails("emails.csv")
create_nne("nee.csv")

