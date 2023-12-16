# Version of project with a graphical user interface
from customtkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import json

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
combo_box = ttk.Combobox(root, value=categories, font=("Open Sans Medium", 12), width=13)
combo_box.grid(row=2, column=2)
combo_box.current(0)



# Start of utility functions
def Selected():
    if len(select.curselection()) > 0:
        return int(select.curselection()[0])
    else:
        messagebox.showerror("Error", "No credential selected!")
# For synching the listbox with the credentials array
def select_set():
    select.delete(0, END)
    key_map = {
        categories[0]: 'website',
        categories[1]: 'email',
        categories[2]: 'password',
    }

    # Get the corresponding keys in the JSON file from the selected category in the combox
    selected_key = key_map[combo_box.get()]
    credentials.sort(key=lambda elem: elem[selected_key])
    for credential in credentials:
        # Insert the following values in the credentials list according to the category chosen
        select.insert(END, credential[selected_key])

# End of utility functions

class PasswordManager:
    def __init__(self):
        with open('credentials.json', 'r') as file:
            data = json.load(file)
            for credential in data:
                credentials.append(credential)
        select_set()

    def update_storage(self):
        with open('credentials.json', 'w') as file:
            json.dump(credentials, file, indent=4)

    def add_credentials(self):
        website_value = website.get()
        email_value = email.get()
        password_value = password.get()
        if website_value != "" and email_value != "" and password_value != "":
            new_entry = {}
            new_entry['website'] =  website_value
            new_entry['email'] =  email_value
            new_entry['password'] =  password_value
            credentials.append(new_entry)
            self.update_storage()
            select_set()

    def view_credentials(self):
        WEBSITE = credentials[Selected()]['website']
        EMAIL = credentials[Selected()]['email']
        PASSWORD = credentials[Selected()]['password']
        website.set(WEBSITE)
        email.set(EMAIL)
        password.set(PASSWORD)

    def search_credential(self):
        search_value = search_entry.get() # Get current value in the search bar
        search_by = combo_box.get() # Get current value in the combo box

        if not search_value: 
            messagebox.showerror("Empty", "Please fill out the search bar.")
            return
        
        for idx in range(len(credentials)):
            # These conditional statements decide the category of information it is going to traverse
            if search_by == categories[0]:
                # Searches for a possible parent string for the current value in search bar from the information in credentials
                if search_value.lower() in (credentials[idx]['website']):
                    select.select_set(idx)
            elif search_by == categories[1]:
                if search_value.lower() in (credentials[idx]['email']):
                    select.select_set(idx)
            elif search_by == categories[2]:
                if search_value.lower() in (credentials[idx]['password']):
                    select.select_set(idx)

        # Handling cases where the search entry is not found
        if search_by == categories[0] and not len(select.curselection()):
            messagebox.showerror("Error", "Search entry not found in the websites!")
        elif search_by == categories[1] and not len(select.curselection()):
            messagebox.showerror("Error", "Search entry not found in the emails!")
        elif search_by == categories[2] and not len(select.curselection()):
            messagebox.showerror("Error", "Search entry not found in the passwords!")
                

    def delete_credential(self):
        if len(select.curselection()) != 0:
            result = messagebox.askyesno("Confirmation", "Do you want to delete this credential? ")
            if result:
                del credentials[Selected()]
                self.update_storage()
                select_set()
        else:
            messagebox.showerror("Error", "Please select a credential.")

    def update_credential(self):
        if Selected() is None:
            return
        
        website_value = website.get()
        email_value = email.get()
        password_value = password.get()
        updated_credential = {
            "website": website_value,
            "email": email_value,
            "password": password_value
        }

        credentials[Selected()] = updated_credential
        self.update_storage()
        select_set()
    
    def reset_inputs(self):
        website.set('')
        email.set('')
        password.set('')

    def exit(self):
        root.destroy()

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
reset_button = CTkButton(left_frame, text="RESET", height=35, width=80, font=("Calibri", 17), fg_color='#C0A533', command = lambda: password_manager.reset_inputs())
reset_button.grid(row=0, column=0, pady=(35, 0), sticky="E")
delete_button = CTkButton(left_frame, text="DELETE", height=35, width=80, font=("Calibri", 17), fg_color='#CB0425', command = lambda: password_manager.delete_credential())
delete_button.grid(row=1, column=0, pady=(35, 0), sticky="E")
exit_button = CTkButton(left_frame, text="EXIT",  height=35, width=80, font=("Calibri", 17), fg_color='#1A1A1B', command = lambda: password_manager.exit())
exit_button.grid(row=2, column=0, pady=(35, 0), sticky="E")
left_frame.grid(row=1, column=0, rowspan=3, sticky='n', pady=(8, 0))
# right side buttons frame
right_frame = CTkFrame(master=root, bg_color='#8c251d',  fg_color='#8c251d')
add_button = CTkButton(right_frame, text="ADD", height=35, width=80, font=("Calibri", 17), fg_color='#238636', command = lambda: password_manager.add_credentials())
add_button.grid(row=0, column=0, pady=(35, 0), sticky="E")
edit_button = CTkButton(right_frame, text="EDIT", height=35, width=80, font=("Calibri", 17), fg_color='#617E8C', command = lambda: password_manager.update_credential())
edit_button.grid(row=1, column=0, pady=(35, 0), sticky="E")
right_frame.grid(row=1, column=2, rowspan=3, sticky='n', pady=(8, 0))

search_entry = CTkEntry(root, width=120, bg_color='#8c251d')
search_entry.grid(row=3, column=2)
search_button = CTkButton(root, text="SEARCH", height=30, width=65, bg_color='#8c251d', command = lambda: password_manager.search_credential())
search_button.grid(row=4, column=2)


# Event listeners
def fillout(e):
    if len(select.curselection()) != 0:
        search_entry.delete(0, END)
        search_entry.insert(0, select.get(select.curselection()))
        password_manager.view_credentials()


combo_box.bind('<KeyRelease>', lambda e: select_set())
combo_box.bind('<<ComboboxSelected>>', lambda e: select_set())
select.bind('<<ListboxSelect>>', fillout)

root.mainloop()