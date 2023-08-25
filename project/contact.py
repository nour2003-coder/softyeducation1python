""" import json
import os

# Collect user input
data = {
    "name": input("name: "),
    "email": input("email: "),
    "age": input("age: "),
    "classe": input("classe: ")
}

# Create a directory to store JSON files if it doesn't exist
path = os.getcwd()
pathf = os.path.join(path, "project")
os.makedirs(pathf, exist_ok=True)

# Save user input in a JSON file
pathj = os.path.join(pathf, data['name'] + ".json")
with open(pathj, "w") as jsonfile:
     content = json.dumps(data)
     jsonfile.write(content)

# Read and print data from all JSON files in the directory
files = os.listdir(pathf)
list=[]
for file in files:
    #get only json files
    if file.endswith(".json"):
        pathi = os.path.join(pathf, file)
        list.append(pathi)
contact=[]
for i in list:
    with open( i, 'r') as jsonfile:
        content = jsonfile.read()
        data = json.loads(content)
        contact.append(data)
name=input(" give me the name you are searching for")
for i in contact:
    nam=i.get("name")
    if (name==nam):
        contacts=i
        break
data = {
    "name": input("edit name: "),
    "email": input("edit email: "),
    "age": input("edit age: "),
    "classe": input("edit classe: ")
}
pathj = os.path.join(pathf, data['name'] + ".json")
with open(pathj, "w") as jsonfile:
     content = json.dumps(data)
     jsonfile.write(content)
pathj = os.path.join(pathf, contacts.get("name") + ".json")
try:
    os.remove(pathj)
    print(f"File '{pathj}' deleted successfully.")
except FileNotFoundError:
    print(f"File '{pathj}' not found.")

 """
import json
import os

def add_contact(pathf):
    data = {
        "name": input("name: "),
        "email": input("email: "),
        "age": input("age: "),
        "classe": input("classe: ")
    }

    pathj = os.path.join(pathf, data['name'] + ".json")
    with open(pathj, "w") as jsonfile:
        content = json.dumps(data)
        jsonfile.write(content)

def search_contact(contact_list):
    name = input("Give me the name you are searching for: ")
    for contact in contact_list:
        if contact.get("name") == name:
            return contact
    return None

def update_contact(contact):
    data = {
        "name": input("edit name: "),
        "email": input("edit email: "),
        "age": input("edit age: "),
        "classe": input("edit classe: ")
    }
    return data

def delete_contact(pathf, contact):
    pathj = os.path.join(pathf, contact.get("name") + ".json")
    try:
        os.remove(pathj)
        print(f"Contact '{contact.get('name')}' deleted successfully.")
    except FileNotFoundError:
        print(f"Contact '{contact.get('name')}' not found.")

def main():
    path = os.getcwd()
    pathf = os.path.join(path, "project")
    os.makedirs(pathf, exist_ok=True)

    contact_list = []

    files = os.listdir(pathf)
    for file in files:
        if file.endswith(".json"):
            pathi = os.path.join(pathf, file)
            with open(pathi, 'r') as jsonfile:
                content = jsonfile.read()
                data = json.loads(content)
                contact_list.append(data)

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(pathf)
        elif choice == "2":
            contact = search_contact(contact_list)
            if contact:
                print("Contact found:")
                print(contact)
            else:
                print("Contact not found.")
        elif choice == "3":
            contact = search_contact(contact_list)
            if contact:
                updated_data = update_contact(contact)
                with open(os.path.join(pathf, contact.get("name") + ".json"), "w") as jsonfile:
                    content = json.dumps(updated_data)
                    jsonfile.write(content)
                print("Contact updated successfully.")
            else:
                print("Contact not found.")
        elif choice == "4":
            contact = search_contact(contact_list)
            if contact:
                delete_contact(pathf, contact)
            else:
                print("Contact not found.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
""" The line if __name__ == "__main__": is a common construct in Python scripts that ensures that the code 
block underneath it is only executed if the script is run directly as the main program, rather than being imported as a module into another script.

 """
 #the script is a standalone program that can be executed directly.