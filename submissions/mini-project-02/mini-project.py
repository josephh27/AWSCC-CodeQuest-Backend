import json
import sys

class PasswordManager:
    def __init__(self):
        with open('credentials.json', 'r') as file:
            data = json.load(file)
            self.storage = data

    def update_storage(self):
        with open('credentials.json', 'w') as file:
            json.dump(self.storage, file, indent=4)

    def add_credentials(self, website, email, password):
        new_entry = {}
        new_entry['website'] =  website
        new_entry['email'] =  email
        new_entry['password'] =  password
        self.storage.append(new_entry)
        self.update_storage()

    def view_credentials(self):
        for credential in self.storage:
            print(f"Website: {credential['website']}")
            print(f"\tEmail: {credential['email']}")
            print(f"\tPassword: {credential['password']}\n")

    def search(self, number):
        match number:
            case 1:
                category = 'website'
            case 2:
                category = 'email'
            case 3:
                category = 'password'

        value = input(f"Please input the {category}: ")
        result_found = False
        for credential in self.storage:
            if value.lower() == credential[category].lower():
                print(f"Website: {credential['website']}")
                print(f"\tEmail: {credential['email']}")
                print(f"\tPassword: {credential['password']}\n")
                result_found = True
        
        if not result_found:
            print("No matching credential found.\n")


    def delete_credential(self, delete_idx):
        del self.storage[delete_idx]
        self.update_storage()

    def update_credential(self, updated_idx, updated_website, updated_email, updated_password):
        # Updating the selected credential
        self.storage[updated_idx]['website'] = updated_website
        self.storage[updated_idx]['email'] = updated_email
        self.storage[updated_idx]['password'] = updated_password
        self.update_storage()

    def evaluate_choice(self, choice):
        if choice == 1:
            new_website = input("Enter name of website: ")
            new_email = input("Enter email: ")
            new_password = input("Enter password: ")
            self.add_credentials(new_website, new_email, new_password)

        elif choice == 2:
            self.view_credentials()

        elif choice == 3:
            while True:
                print("(1) Website name")
                print("(2) Email")
                print("(3) Password")
                category = int(input("Search by: "))
                if category in [1, 2, 3]:
                    break
                else:
                    print("Please input a valid value.\n")
            self.search(category)

        elif choice == 4:
            try:
                for idx, credential in enumerate(self.storage):
                    print(f"({idx})")
                    print(f"Website: {credential['website']}")
                    print(f"\tEmail: {credential['email']}")
                    print(f"\tPassword: {credential['password']}\n")
                delete_idx = int(input("Please input the assigned number of credential to be deleted: "))
                self.delete_credential(delete_idx)
            except:
                print("Please input a proper number.")

        elif choice == 5:
            try:
                for idx, credential in enumerate(self.storage):
                    print(f"({idx})")
                    print(f"Website: {credential['website']}")
                    print(f"\tEmail: {credential['email']}")
                    print(f"\tPassword: {credential['password']}\n")

                # Gathering infos for the update
                updated_idx = int(input("Please input the assigned number of credential to be updated: "))
                updated_website = input("Enter name of website: ")
                updated_email = input("Enter email: ")
                updated_password = input("Enter password: ")
                self.update_credential(updated_idx, updated_website, updated_email, updated_password)


            except:
                print("Please input a proper number.")

        elif choice == 6:
            sys.exit()

        else: 
            raise ValueError()


if __name__ == '__main__':
    password_manager = PasswordManager()
    print("Welcome to the password manager!")
    while True:
        try:
            print("1 - Add a credential")
            print("2 - View all credentials")
            print("3 - Search for a credential")
            print("4 - Delete a credential")
            print("5 - Update a credential")
            print("6 - Exit")
            choice = int(input("Please choose an action: "))
            print("")
            password_manager.evaluate_choice(choice)

        except ValueError:
            print("Invalid choice.")
