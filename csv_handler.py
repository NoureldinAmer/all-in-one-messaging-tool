import csv
import pandas as pd

def export_contact(contact: list) -> None:
    with open(file="contacts.csv",mode="a") as file:
        wr = csv.writer(file)
        wr.writerow(contact)


def import_contacts_names() -> list:
    filename = open('contacts.csv', 'r')
    file = csv.DictReader(filename)
    #use sets to avoid duplicates
    contacts = set()
    # iterating over each row and append
    for col in file:    
        contacts.add(col['name'])

    return contacts    

def import_contact_detals(contact_name: str) -> dict:
    contact_details = {
        "name" : contact_name,
        "dicord_username" : None,
        "email_address" : None,
        "slack_username" : None,
        "twitter_username" : None,
    }
    df = pd.read_csv('contacts.csv')
    print(len(df))
    for i in range(len(df)):
        if df.iloc[i][0] == contact_name and df.iloc[i][1] == "discord":
            contact_details["dicord_username"] = df.iloc[i][2]
        elif df.iloc[i][0] == contact_name and df.iloc[i][1] == "email":
            contact_details["email_address"] = df.iloc[i][2]
        elif df.iloc[i][0] == contact_name and df.iloc[i][1] == "slack":
            contact_details["slack_username"] = df.iloc[i][2]
        elif df.iloc[i][0] == contact_name and df.iloc[i][1] == "twitter":
            contact_details["twitter_username"] == df.iloc[i][2]
    return contact_details



if __name__ == "__main__":
    print(import_contact_detals("Clement"))
