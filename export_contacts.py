import csv
def export_contact(contact: list) -> None:
    header = ['name','account_type','usernamename']
    with open(file="contacts.csv",mode="a") as file:
        wr = csv.writer(file)
        wr.writerow(contact)

if __name__ == "__main__":
    export_contact(["test","test","test"])