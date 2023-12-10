from customtkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import json
import sys

root = CTk()
root.geometry("500x500")
root.title("Address Book")
root.resizable(0,0)
root.config(bg="#8c251d")
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)
root.grid_rowconfigure(4, weight = 1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_propagate(False)


# The global variables
credentials = []
categories = ["Website", "Email", "Password"]
website = StringVar()
email = StringVar()
password = StringVar()

# The creation of listbox and scrollbar
list_frame = CTkFrame(root)
list_frame.grid(row=1, column=1)
list_frame.grid_propagate(False)

scroll = tkinter.Scrollbar(list_frame, orient=VERTICAL)
select = tkinter.Listbox(list_frame, yscrollcommand=scroll.set, height=15, width=30, activestyle='dotbox', bg="#fcff69", font = "flix 10 bold", selectmode=SINGLE)
# The configuration of the scrollbar
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=RIGHT, fill=BOTH, expand=1)

# The creation of the combo box
combo_box = ttk.Combobox(root, value=categories, width=13)
combo_box.grid(row=4, column=2, rowspan=3)
combo_box.current(0)

def Selected():
    if len(select.curselection()) > 0:
        return int(select.curselection()[0])
    else:
        messagebox.showerror("Error", "No credential selected!")

class PasswordManager:
    def __init__(self):
        # with open('credentials.json', 'r') as file:
        #     data = json.load(file)
        #     self.storage = data
        pass

    def update_storage(self):
        # with open('credentials.json', 'w') as file:
        #     json.dump(self.storage, file, indent=4)
        pass

    def add_credentials(self, website, email, password):
        # new_entry = {}
        # new_entry['website'] =  website
        # new_entry['email'] =  email
        # new_entry['password'] =  password
        # self.storage.append(new_entry)
        # self.update_storage()
        pass

    def view_credentials(self):
        # for credential in self.storage:
        #     print(f"Website: {credential['website']}")
        #     print(f"\tEmail: {credential['email']}")
        #     print(f"\tPassword: {credential['password']}\n")
        pass

    def search(self, number):
        # match number:
        #     case 1:
        #         category = 'website'
        #     case 2:
        #         category = 'email'
        #     case 3:
        #         category = 'password'

        # value = input(f"Please input the {category}: ")
        # result_found = False
        # for credential in self.storage:
        #     if value.lower() == credential[category].lower():
        #         print(f"Website: {credential['website']}")
        #         print(f"\tEmail: {credential['email']}")
        #         print(f"\tPassword: {credential['password']}\n")
        #         result_found = True
        
        # if not result_found:
            # print("No matching credential found.\n")
        pass


    def delete_credential(self, delete_idx):
        # del self.storage[delete_idx]
        # self.update_storage()
        pass

    def update_credential(self, updated_idx, updated_website, updated_email, updated_password):
        # Updating the selected credential
        # self.storage[updated_idx]['website'] = updated_website
        # self.storage[updated_idx]['email'] = updated_email
        # self.storage[updated_idx]['password'] = updated_password
        # self.update_storage()
        pass

password_manager = PasswordManager()

# The creation of entries and labels
website_frame = CTkFrame(master=root, width=200, height=200, bg_color='#8c251d',  fg_color='#8c251d')
website_label = CTkLabel(master=website_frame, text="Website: ", font=("Open Sans Medium", 14, "bold"), width=100, anchor='w')
website_entry = CTkEntry(website_frame, textvariable=website, width=200)
website_frame.grid_columnconfigure(0, weight=1)
website_frame.grid_columnconfigure(1, weight=1)
website_frame.grid(row=2, column=0, sticky='w', columnspan=2)
website_label.grid(row=0, column=0, padx=(10, 10))
website_entry.grid(row=0, column=1)

email_frame = CTkFrame(master=root, width=200, height=200, bg_color='#8c251d',  fg_color='#8c251d')
email_label = CTkLabel(master=email_frame, text="Email: ", font=("Open Sans Medium", 14, "bold"), width=100, anchor='w')
email_entry = CTkEntry(email_frame, textvariable=email, width=200)
email_frame.grid_columnconfigure(0, weight=1)
email_frame.grid_columnconfigure(1, weight=1)
email_frame.grid(row=3, column=0, sticky='w', columnspan=2)
email_label.grid(row=0, column=0, padx=(10, 10))
email_entry.grid(row=0, column=1)

password_frame = CTkFrame(master=root, width=200, height=200, bg_color='#8c251d',  fg_color='#8c251d')
password_label = CTkLabel(master=password_frame, text="Password: ", font=("Open Sans Medium", 14, "bold"), width=100, anchor='w')
password_entry = CTkEntry(password_frame, textvariable=password, width=200)
password_frame.grid_columnconfigure(0, weight=1)
password_frame.grid_columnconfigure(1, weight=1)
password_frame.grid(row=4, column=0, sticky='w', columnspan=2)
password_label.grid(row=0, column=0, padx=(10, 10))
password_entry.grid(row=0, column=1)

# The creation of buttons in the frame
# left side buttons frame
left_frame = CTkFrame(master=root, bg_color='#8c251d',  fg_color='#8c251d')
reset_button = CTkButton(left_frame, text="RESET", height=30, width=65, command = lambda: password_manager.add_credentials())
reset_button.grid(row=1, column=0, pady=(35, 0), sticky="E")
delete_button = CTkButton(left_frame, text="DELETE", height=30, width=65, command = lambda: password_manager.add_credentials())
delete_button.grid(row=2, column=0, pady=(35, 0), sticky="E")
exit_button = CTkButton(left_frame, text="EXIT", height=30, width=65, command = lambda: password_manager.add_credentials())
exit_button.grid(row=3, column=0, pady=(35, 0), sticky="E")
left_frame.grid(row=1, column=0, rowspan=3, sticky='n', pady=(8, 0))
# right side buttons frame
right_frame = CTkFrame(master=root, bg_color='#8c251d',  fg_color='#8c251d')
view_button = CTkButton(right_frame, text="VIEW", height=30, width=65, command = lambda: password_manager.add_credentials())
view_button.grid(row=1, column=0, pady=(35, 0), sticky="E")
add_button = CTkButton(right_frame, text="ADD", height=30, width=65, command = lambda: password_manager.add_credentials())
add_button.grid(row=2, column=0, pady=(35, 0), sticky="E")
edit_button = CTkButton(right_frame, text="EDIT", height=30, width=65, command = lambda: password_manager.add_credentials())
edit_button.grid(row=3, column=0, pady=(35, 0), sticky="E")
right_frame.grid(row=1, column=2, rowspan=3, sticky='n', pady=(8, 0))

root.mainloop()