#!/usr/bin/env python3

# Copyright (C) 2024 MuKonqi (Muhammed S.)

# GrelinTB is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GrelinTB is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GrelinTB.  If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import locale
import getpass
import random as rd
import threading
import subprocess
import socket
import platform
import time
import json

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
solus = "/etc/solus-release"
arch = "/etc/arch-release"
requirements = "/home/mukonqi/works/grelintb/app/requirements.txt"
process_number = 0
current_operations = []

if not os.path.isfile(debian) and not os.path.isfile(fedora) and not os.path.isfile(solus) and os.path.isfile(arch):
    print("The distribution you are using is not supported from GrelinTB. Please use Debian GNU/Linux, Fedora Linux, Solus and Arch Linux based distributions for GrelinTB. (1)")
    sys.exit(1)
try:
    with open("/usr/local/bin/grelintb/version.txt", "r") as version_file:
        version_current = version_file.readline()
except:
    print("Version file not found. (2)")
    sys.exit(2)
if not os.path.isfile(requirements):
    print("Requirements file not found. (3)")
    sys.exit(3)
if "root" in sys.argv[1:]:
    if os.getuid() != 0:
        print("Root rights are required for this feature. (4)")
        sys.exit(4)
    if "pcrename" in sys.argv[2:]:
        with open("/etc/hostname", "w") as pcname:
            pcname.write(str(sys.argv[3]))
    sys.exit(0)
elif os.getuid() == 0:
    print("GrelinTB already asks you for root rights when the need arises. (5)")
    sys.exit(5)

try:
    from tkinter import messagebox as mb
    from tkinter import filedialog as fd
    from tkinter import PhotoImage as pi
except:
    try:
        print("Installing Tkinter...")
        if os.path.isfile(debian):
            os.system("pkexec apt -y install python3-tk")
        elif os.path.isfile(fedora):
            os.system("pkexec dnf5 -y --nogpgcheck install python3-tkinter")
        elif os.path.isfile(solus):
            os.system("pkexec eopkg -y install python3-tkinter")
        elif os.path.isfile(arch):
            os.system("pkexec pacman --noconfirm -S tk")
        from tkinter import messagebox as mb
        from tkinter import filedialog as fd
        from tkinter import PhotoImage as pi
    except:
        os.system(__file__)
        sys.exit(0)
if not os.path.isfile("/bin/pip") and not os.path.isfile("/usr/bin/pip"):
    print("Installing pip...")
    if os.path.isfile(debian):
        os.system("pkexec apt -y install python3-pip")
    elif os.path.isfile(fedora):
        os.system("pkexec dnf5 -y --nogpgcheck install python3-pip")
    elif os.path.isfile(solus):
        os.system("pkexec eopkg -y install pip")
    elif os.path.isfile(arch):
        os.system("pkexec pacman --noconfirm -S python-pip")
try:
    import customtkinter as ui
    import datetime as dt
    import psutil
    import distro
except:
    try:
        print("Installing other requirements...")
        os.system(f"pip install -r {requirements}")
        import customtkinter as ui
        import datetime as dt
        import psutil
        import distro
    except:
        print("Installing other requirements with --break-system-packages parameter...")
        os.system(f"pip install -r {requirements} ; {__file__}")
        sys.exit(0)
        
username = getpass.getuser()
config = f"/home/{username}/.config/grelintb/"
local = f"/home/{username}/.local/share/grelintb/"
notes = f"/home/{username}/Notes/"
en = f"/home/{username}/.config/grelintb/language/en.txt"
tr = f"/home/{username}/.config/grelintb/language/tr.txt"
system = f"/home/{username}/.config/grelintb/appearance/system.txt"
light = f"/home/{username}/.config/grelintb/appearance/light.txt"
dark = f"/home/{username}/.config/grelintb/appearance/dark.txt"
grelintb = f"/home/{username}/.config/grelintb/theme/grelintb.txt"
random = f"/home/{username}/.config/grelintb/theme/random.txt"
dark_blue = f"/home/{username}/.config/grelintb/theme/dark_blue.txt"
blue = f"/home/{username}/.config/grelintb/theme/blue.txt"
green = f"/home/{username}/.config/grelintb/theme/green.txt"
if os.path.isfile(debian):
    pkg_type = "DEB"
    pkg_mngr = "APT & DPKG"
elif os.path.isfile(fedora):
    pkg_type = "RPM"
    pkg_mngr = "DNF"
elif os.path.isfile(solus):
    pkg_type = "EOPKG"
    pkg_mngr = "EOPKG"
elif os.path.isfile(arch):
    pkg_type = "Pacman"
    pkg_mngr = "Pacman"

if not os.path.isdir(config):
    os.system(f"mkdir {config}")
if not os.path.isdir(local):
    os.system(f"mkdir {local}")
if not os.path.isdir(f"{config}language/") or (not os.path.isfile(en) and not os.path.isfile(tr)):
    if locale.getlocale()[0] == "tr_TR":
        os.system(f"cd {config} ; mkdir language ; cd language ; touch tr.txt")
    else:
        os.system(f"cd {config} ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(f"{config}appearance/") or (not os.path.isfile(system) and not os.path.isfile(light) and not os.path.isfile(dark)):
    os.system(f"cd {config} ; mkdir appearance ; cd appearance ; touch system.txt")
if not os.path.isdir(f"{config}theme/") or (not os.path.isfile(grelintb) and not os.path.isfile(random) and not os.path.isfile(dark_blue) and not os.path.isfile(blue) and not os.path.isfile(green)):
    os.system(f"cd {config} ; mkdir theme ; cd theme ; touch grelintb.txt")
if not os.path.isdir(notes):
    os.system(f"mkdir {notes}")
if not os.path.isdir(f"{notes}.backups"):
    os.system(f"mkdir {notes}.backups")
if not os.path.isdir(f"{local}backups"):
    os.system(f"cd {local} ; mkdir backups")
if not os.path.isdir(f"{local}backups/bashrc"):
    os.system(f"cd {local}backups ; mkdir bashrc")
if not os.path.isdir(f"{local}backups/zshrc"):
    os.system(f"cd {local}backups ; mkdir zshrc")
if not os.path.isfile(f"/home/{username}/.bashrc"):
    os.system(f"cd /home/{username} ; touch .bashrc")
if not os.path.isfile(f"/home/{username}/.zshrc"):
    os.system(f"cd /home/{username} ; touch .zshrc")
if not os.path.isfile(f"{local}backups/bashrc/first"):
    os.system(f"cp /home/{username}/.bashrc {local}backups/bashrc/first")
if not os.path.isfile(f"{local}backups/zshrc/first"):
    os.system(f"cp /home/{username}/.zshrc {local}backups/zshrc/first")
os.system(f"cp /home/{username}/.bashrc {local}backups/bashrc/session")
os.system(f"cp /home/{username}/.zshrc {local}backups/zshrc/session")

if os.path.isfile(en):
    l_use = 0
elif os.path.isfile(tr):
    l_use = 1
try:
    with open("/home/mukonqi/works/grelintb/app/language.json", "r") as language_file:
        l_read = language_file.read()
    l_dict = json.loads(l_read, object_pairs_hook=dict)
except:
    print("Language file not found. (6)")
    sys.exit(6)
if os.path.isfile(system):
    ui.set_appearance_mode("System")
elif os.path.isfile(light):
    ui.set_appearance_mode("Light")
elif os.path.isfile(dark):
    ui.set_appearance_mode("Dark")
if os.path.isfile(grelintb):
    ui.set_default_color_theme("/usr/local/bin/grelintb/theme.json")
elif os.path.isfile(random):
    ui.set_default_color_theme(rd.choice(['blue', 'dark-blue', 'green', '/usr/local/bin/grelintb/theme.json']))
elif os.path.isfile(dark_blue):
    ui.set_default_color_theme('dark-blue')
elif os.path.isfile(blue):
    ui.set_default_color_theme('blue')
elif os.path.isfile(green):
    ui.set_default_color_theme('green')
if "sv" in sys.argv[1:]:
    version_current = sys.argv[(sys.argv[1:].index("set-version") + 2)]
if "st" in sys.argv[1:]:
    ui.set_default_color_theme("/home/mukonqi/works/grelintb/app/theme.json")

def update_status():
    if process_number <= 0:
        status.configure(text=l_dict['sidebar']['idle'][l_use])
    else:
        status.configure(text=f"{l_dict['sidebar']['running'][l_use]} ({process_number})")
def add_operation(operation: str, time: str):
    global current_operations, process_number
    process_number = process_number + 1
    update_status()
    current_operations.append([operation, time])
def delete_operation(operation: str, time: str):
    global current_operations, process_number
    process_number = process_number - 1
    update_status()
    current_operations.remove([operation, time])
def restart_system():
    ask_r = mb.askyesno(l_dict['globals']['warning'][l_use], l_dict['questions']['reboot'][l_use])
    if ask_r == True:
        os.system("pkexec reboot")
def install_app(appname: str, packagename: str):
    global ask_a
    global process_number
    ask_a = mb.askyesno(l_dict['globals']['warning'][l_use], f"{appname} {l_dict['questions']['install'][l_use]}")
    if ask_a == True:
        time_process = str(time.strftime("%H:%M:%S", time.localtime()))
        add_operation(f"{l_dict['operations']['install'][l_use]}: {appname}", time_process)
        if os.path.isfile(debian):
            subprocess.Popen(f'pkexec apt -y install {packagename}', shell=True)
        elif os.path.isfile(fedora):
            subprocess.Popen(f'pkexec dnf5 -y --nogpgcheck install {packagename}', shell=True)
        elif os.path.isfile(solus):
            subprocess.Popen(f'pkexec eopkg -y install {packagename}', shell=True)
        elif os.path.isfile(arch):
            subprocess.Popen(f'pkexec pacman --noconfirm -S  {packagename}', shell=True)
        delete_operation(f"{l_dict['operations']['install'][l_use]}: {appname}", time_process)
    elif ask_a == False:
        mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['cancelled'][l_use])
def restart_grelintb():
    global ask_g
    ask_g = mb.askyesno(l_dict['globals']['warning'][l_use], l_dict['questions']['grelintb'][l_use])
    if ask_g == True:
        root.destroy()
        os.system(__file__)

class Sidebar(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global status
        self.grid_rowconfigure((5, 9, 16), weight=1)
        self.text = ui.CTkButton(self, text="GrelinTB", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io/grelintb/index.html", shell=True), font=ui.CTkFont(size=20, weight="bold"), fg_color="transparent")
        self.version_b = ui.CTkButton(self, text=f"{l_dict['sidebar']['version'][l_use]}{version_current}", command=self.changelog, fg_color="transparent")
        self.mukonqi_b = ui.CTkButton(self, text=f"{l_dict['sidebar']['developer'][l_use]}MuKonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent")
        self.license_b = ui.CTkButton(self, text=f"{l_dict['sidebar']['license'][l_use]}GPLv3+", command=self.license, fg_color="transparent")
        self.credit_b = ui.CTkButton(self, text=f"{l_dict['sidebar']['credit'][l_use]}G. M. Icons", command=self.credit, fg_color="transparent")
        self.update_b = ui.CTkButton(self, text=l_dict['operations']['update'][l_use], command=lambda:self.check_update('sidebar'))
        self.reset_b = ui.CTkButton(self, text=l_dict['operations']['reset'][l_use], command=self.reset)
        self.uninstall_b = ui.CTkButton(self, text=l_dict['operations']['uninstall'][l_use], command=self.uninstall)
        self.theme_label = ui.CTkLabel(self, text=l_dict['sidebar']['theme'][l_use])
        self.theme_menu = ui.CTkOptionMenu(self, values=["GrelinTB", l_dict['sidebar']['random'][l_use], l_dict['sidebar']['dark-blue'][l_use], l_dict['sidebar']['blue'][l_use], l_dict['sidebar']['green'][l_use]], command=self.change_theme)
        self.appearance_label = ui.CTkLabel(self, text=l_dict['sidebar']['appearance'][l_use])
        self.appearance_menu = ui.CTkOptionMenu(self, values=[l_dict['sidebar']['system'][l_use], l_dict['sidebar']['light'][l_use], l_dict['sidebar']['dark'][l_use]], command=self.change_appearance)
        self.language_label = ui.CTkLabel(self, text=l_dict['sidebar']['language'][l_use])
        self.language_menu = ui.CTkOptionMenu(self, values=["English (İngilizce)", "Türkçe (Turkish)"], command=self.change_language)
        status = ui.CTkButton(self, text=l_dict['sidebar']['idle'][l_use], command=self.running_processes, font=ui.CTkFont(size=12, weight="bold"))
        if os.path.isfile(random):
            self.theme_menu.set(l_dict['sidebar']['random'][l_use])
        elif os.path.isfile(grelintb):
            self.theme_menu.set("GrelinTB")
        elif os.path.isfile(dark_blue):
            self.theme_menu.set(l_dict['sidebar']['dark-blue'][l_use])
        elif os.path.isfile(blue):
            self.theme_menu.set(l_dict['sidebar']['blue'][l_use])
        elif os.path.isfile(green):
            self.theme_menu.set(l_dict['sidebar']['green'][l_use])
        if os.path.isfile(system):
            self.appearance_menu.set(l_dict['sidebar']['system'][l_use])
        elif os.path.isfile(light):
            self.appearance_menu.set(l_dict['sidebar']['light'][l_use])
        elif os.path.isfile(dark):
            self.appearance_menu.set(l_dict['sidebar']['dark'][l_use])
        if os.path.isfile(en):
            self.language_menu.set("English (İngilizce)")
        elif os.path.isfile(tr):
            self.language_menu.set("Türkçe (Turkish)")
        self.text.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.version_b.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
        self.mukonqi_b.grid(row=2, column=0, sticky="nsew", padx=10, pady=0)
        self.license_b.grid(row=3, column=0, sticky="nsew", padx=10, pady=0)
        self.credit_b.grid(row=4, column=0, sticky="nsew", padx=10, pady=0)
        self.update_b.grid(row=6, column=0, sticky="nsew", padx=10, pady=5)
        self.reset_b.grid(row=7, column=0, sticky="nsew", padx=10, pady=5)
        self.uninstall_b.grid(row=8, column=0, sticky="nsew", padx=10, pady=5)
        self.theme_label.grid(row=10, column=0, sticky="nsew", padx=10, pady=0)
        self.theme_menu.grid(row=11, column=0, sticky="nsew", padx=10, pady=(0, 5))
        self.appearance_label.grid(row=12, column=0, sticky="nsew", padx=10, pady=0)
        self.appearance_menu.grid(row=13, column=0, sticky="nsew", padx=10, pady=(0, 5))
        self.language_label.grid(row=14, column=0, sticky="nsew", padx=10, pady=0)
        self.language_menu.grid(row=15, column=0, sticky="nsew", padx=10, pady=(0, 5))
        status.grid(row=17, column=0, sticky="nsew", padx=10, pady=(0, 5))
    def changelog(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.frame = ui.CTkScrollableFrame(self.window, fg_color="transparent")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.window.title(f"{l_dict['changelog']['changelogs'][l_use]}{version_current}")
        self.label1 = ui.CTkLabel(self.frame, text=f"{l_dict['changelog']['major'][l_use]}{version_current}", font=ui.CTkFont(size=14, weight="bold"))
        self.label2 = ui.CTkLabel(self.frame, text=f"{l_dict['changelog']['minor'][l_use]}{version_current}", font=ui.CTkFont(size=14, weight="bold"))
        with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as self.cl_major_file:
            self.cl_major_text = self.cl_major_file.read()
        with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as self.cl_minor_file:
            self.cl_minor_text = self.cl_minor_file.read()
        self.textbox1 = ui.CTkTextbox(self.frame)
        self.textbox1.insert("0.0", self.cl_major_text)
        self.textbox1.configure(state="disabled")
        self.textbox2 = ui.CTkTextbox(self.frame)
        self.textbox2.insert("0.0", self.cl_minor_text)
        self.textbox2.configure(state="disabled")
        self.label1.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.textbox1.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.label2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
        self.textbox2.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
    def license(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.title(l_dict['license']['license'][l_use])
        self.label = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text=l_dict['license']['label'][l_use])
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as self.license_file:
            self.license_text = self.license_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", self.license_text)
        self.textbox.configure(state="disabled")
        self.label.grid(row=0, column=0, sticky="nsew", pady=10)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
    def credit(self):
        self.credit_mb = mb.askyesno(l_dict['credit']['credit'][l_use], l_dict['credit']['label'][l_use])
        if self.credit_mb == True:
            subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048", shell=True)
    def update(self, string: str):
        os.system("pkexec /usr/local/bin/grelintb/update.sh")
        mb.showinfo(l_dict['globals']["information"][l_use], l_dict['sidebar']["updated"][l_use])
        restart_grelintb()
    def check_update(self, caller: str):
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            self.window = ui.CTkToplevel()
            self.window.geometry("540x540")
            self.window.minsize(540, 540)
            self.window.grid_rowconfigure(0, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
            self.frame = ui.CTkScrollableFrame(self.window, fg_color="transparent")
            self.frame.grid_columnconfigure(0, weight=1)
            self.frame.grid(row=0, column=0, sticky="nsew")
            self.window.title(f"{l_dict['changelog']['changelogs'][l_use]}{version_latest}")
            self.label1 = ui.CTkLabel(self.frame, text=f"{l_dict['changelog']['major'][l_use]}{version_latest}", font=ui.CTkFont(size=14, weight="bold"))
            self.label2 = ui.CTkLabel(self.frame, text=f"{l_dict['changelog']['minor'][l_use]}{version_latest}", font=ui.CTkFont(size=14, weight="bold"))
            if caller == 'sidebar':
                self.button = ui.CTkButton(self.window, text=l_dict["operations"]["update"][l_use], command=lambda:Sidebar.update(self, 'sidebar'))
            elif caller == "startup":
                self.button = ui.CTkButton(self.window, text=l_dict["operations"]["update"][l_use], command=lambda:Sidebar.update(self, "startup"))
            with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as self.cl_major_file:
                self.cl_major_text = self.cl_major_file.read()
            with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as self.cl_minor_file:
                self.cl_minor_text = self.cl_minor_file.read()
            self.textbox1 = ui.CTkTextbox(self.frame)
            self.textbox1.insert("0.0", str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/major-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
            self.textbox1.configure(state="disabled")
            self.textbox2 = ui.CTkTextbox(self.frame)
            self.textbox2.insert("0.0", str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/minor-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
            self.textbox2.configure(state="disabled")
            self.label1.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
            self.textbox1.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
            self.label2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
            self.textbox2.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
            self.button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        elif caller != "startup":
            mb.showinfo(l_dict['globals']['information'][l_use], l_dict['changelog']['up-to-date'][l_use])
    def reset(self):
        os.system("pkexec /usr/local/bin/grelintb/reset.sh")
        os.system(f"rm -rf /home/{username}/.config/grelintb")
        mb.showinfo(l_dict['globals']["information"][l_use], l_dict['sidebar']["reset"][l_use])
        restart_grelintb()
    def uninstall(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        os.system(f"rm -rf /home/{username}/.config/grelintb")
        mb.showinfo(l_dict['globals']["information"][l_use], l_dict['sidebar']['uninstalled'][l_use])
        sys.exit(0)
    def change_theme(self, new_theme: str):
        if new_theme == "GrelinTB":
            os.system(f"rm {config}theme/* ; touch {config}theme/grelintb.txt")
        elif new_theme == l_dict['sidebar']['random'][l_use]:
            os.system(f"rm {config}theme/* ; touch {config}theme/random.txt")
        elif new_theme == l_dict['sidebar']['dark-blue'][l_use]:
            os.system(f"rm {config}theme/* ; touch {config}theme/dark_blue.txt")
        elif new_theme == l_dict['sidebar']['blue'][l_use]:
            os.system(f"rm {config}theme/* ; touch {config}theme/blue.txt")
        elif new_theme == l_dict['sidebar']['green'][l_use]:
            os.system(f"rm {config}theme/* ; touch {config}theme/green.txt")
        restart_grelintb()
    def change_appearance(self, new_appearance: str):
        if new_appearance == l_dict['sidebar']['system'][l_use]:
            ui.set_appearance_mode("System")
            os.system(f"rm {config}appearance/* ; touch {config}appearance/system.txt")
        elif new_appearance == l_dict['sidebar']['light'][l_use]:
            ui.set_appearance_mode("Light")
            os.system(f"rm {config}appearance/* ; touch {config}appearance/light.txt")
        elif new_appearance == l_dict['sidebar']['dark'][l_use]:
            ui.set_appearance_mode("Dark")
            os.system(f"rm {config}appearance/* ; touch {config}appearance/dark.txt")
    def change_language(self, new_language: str):
        if new_language == "English (İngilizce)":
            os.system(f"rm {config}language/* ; touch {config}language/en.txt")
        elif new_language == "Türkçe (Turkish)":
            os.system(f"rm {config}language/* ; touch {config}language/tr.txt")
        restart_grelintb()
    def running_processes(self):
        if current_operations != []:
            self.number = 0
            self.window = ui.CTkToplevel()
            self.window.geometry("540x540")
            self.window.minsize(540, 540)
            self.window.grid_rowconfigure(0, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
            self.frame = ui.CTkScrollableFrame(self.window, fg_color="transparent")
            self.frame.grid(row=0, column=0, sticky="nsew")
            self.frame.grid_columnconfigure(0, weight=1)
            self.window.title(l_dict['running-processes']['running-processes'][l_use])
            for self.progress in current_operations:
                self.number = self.number + 1
                ui.CTkLabel(self.frame, fg_color=["#b9b9b9", "#1f1f1f"], corner_radius=20, text=f"{self.progress[0]} - {self.progress[1]}", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.number, column=0, pady=5, padx=10, sticky="nsew")
        else:
            mb.showwarning(l_dict['globals']['warning'][l_use], l_dict['running-processes']['no-process'][l_use])

class Startup(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.scrollable = ui.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable.grid(row=0, column=0, sticky="nsew")
        self.scrollable.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.scrollable.configure(label_text=f"{l_dict['startup']['welcome'][l_use]}{username}!", label_font=ui.CTkFont(size=16, weight="bold"))
        self.weather = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['weather'][l_use]}{l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold")) 
        self.system = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['system'][l_use], font=ui.CTkFont(size=15, weight="bold")) 
        self.hostname = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['hostname'][l_use]}{str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
        self.distro = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['distro'][l_use]}{distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
        self.kernel = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['kernel'][l_use]}{platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
        self.packages = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['packages'][l_use]}{l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
        self.uptime = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['uptime'][l_use]}{os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
        self.boot_time = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['boot-time'][l_use]}{str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
        self.usages = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['usages'][l_use], font=ui.CTkFont(size=15, weight="bold"))
        self.cpu_usage = ui.CTkLabel(self.scrollable, text=f"CPU: {l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
        self.disk_usage = ui.CTkLabel(self.scrollable, text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.ram_usage = ui.CTkLabel(self.scrollable, text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
        self.swap_usage = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['swap'][l_use]}%{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.refresh_button = ui.CTkButton(self, text=l_dict['startup']['refresh'][l_use], command=self.refresh, font=ui.CTkFont(size=15, weight="bold"))
        self.weather.grid(row=0, column=0, pady=(0, 10), columnspan=4)
        self.system.grid(row=1, column=0, pady=(0, 7.5), columnspan=4)
        self.hostname.grid(row=2, column=0, pady=(0, 7.5), columnspan=4)
        self.distro.grid(row=3, column=0, pady=(0, 7.5), columnspan=4)
        self.kernel.grid(row=4, column=0, pady=(0, 7.5), columnspan=4)
        self.packages.grid(row=5, column=0, pady=(0, 7.5), columnspan=4)
        self.uptime.grid(row=6, column=0, pady=(0, 7.5), columnspan=4)
        self.boot_time.grid(row=7, column=0, pady=(0, 10), columnspan=4)
        self.usages.grid(row=8, column=0, pady=(0, 7.5), columnspan=4)
        self.cpu_usage.grid(row=9, column=0, pady=(0, 10))
        self.disk_usage.grid(row=9, column=1, pady=(0, 10))
        self.ram_usage.grid(row=9, column=2, pady=(0, 10))
        self.swap_usage.grid(row=9, column=3, pady=(0, 10))
        self.refresh_button.grid(row=1, column=0, pady=(10, 0), sticky="nsew")
        self.weather_thread = threading.Thread(target=lambda:self.weather_def(), daemon=True)
        self.weather_thread.start()
        self.packages_thread = threading.Thread(target=lambda:self.packages_def(), daemon=True)
        self.packages_thread.start()
        self.cpu_usage_thread = threading.Thread(target=lambda:self.cpu_usage_def(), daemon=True)
        self.cpu_usage_thread.start()
        self.other_def("startup")
    def weather_def(self):
        self.weather.configure(text=l_dict['startup']['weather'][l_use]+subprocess.Popen('curl -H "Accept-en" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])
    def packages_def(self):
        if os.path.isfile(debian):
            self.packages.configure(text=f"{l_dict['startup']['packages'][l_use]}{subprocess.Popen('dpkg --list | grep ^i | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (DEB), {subprocess.Popen('flatpak list | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (Flatpak)".replace("\n", ""))
        elif os.path.isfile(fedora):
            self.packages.configure(text=f"{l_dict['startup']['packages'][l_use]}{subprocess.Popen('dnf5 list --installed | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (RPM), {subprocess.Popen('flatpak list | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (Flatpak)".replace("\n", ""))
        elif os.path.isfile(solus):
            self.packages.configure(text=f"{l_dict['startup']['packages'][l_use]}{subprocess.Popen('eopkg --list-installed | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (EOPKG), {subprocess.Popen('flatpak list | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (Flatpak)".replace("\n", ""))
        elif os.path.isfile(arch):
            self.packages.configure(text=f"{l_dict['startup']['packages'][l_use]}{subprocess.Popen('pacman -Q | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (PACMAN), {subprocess.Popen('flatpak list | wc --lines', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]} (Flatpak)".replace("\n", ""))
    def cpu_usage_def(self):
        self.cpu_usage.configure(text=f"CPU: %{str(psutil.cpu_percent(5))}")
    def other_def(self, mode: str):
        self.temps_ok = False
        self.fans_ok = False
        if hasattr (psutil, "sensors_temperatures") and psutil.sensors_temperatures():
            self.temps_ok = True
            self.temps_number = 10
            self.temps = psutil.sensors_temperatures()
            self.temps_header = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['temperatures'][l_use], font=ui.CTkFont(size=15, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
            for self.temps_name, self.temps_entries in self.temps.items():
                self.temps_number = self.temps_number + 1
                self.temps_label = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=f"{l_dict['startup']['hardware'][l_use]}{self.temps_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.temps_entry in self.temps_entries:
                    self.temps_number = self.temps_number + 1
                    ui.CTkLabel(self.scrollable, text=f"{self.temps_entry.label or self.temps_name}: {l_dict['startup']['current'][l_use]} = {self.temps_entry.current} °C, {l_dict['startup']['high'][l_use]} = {self.temps_entry.high} °C, {l_dict['startup']['critical'][l_use]} = {self.temps_entry.critical} °C", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_fans") and psutil.sensors_fans():
            self.fans_ok = True
            if self.temps_ok == True:
                self.fans_number = self.temps_number + 1
            else:
                self.fans_number = 10
            self.fans = psutil.sensors_fans()
            self.fans_header = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['fans'][l_use], font=ui.CTkFont(size=15, weight="bold")).grid(row=self.fans_number, column=0, pady=(5, 7.5), columnspan=4)
            for self.fans_name, self.fans_entries in self.fans.items():
                self.fans_number = self.fans_number + 1
                self.fans_label = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=f"{l_dict['startup']['hardware'][l_use]}{self.fans_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.fans_entry in self.fans_entries:
                    self.fans_number = self.fans_number + 1
                    ui.CTkLabel(self.scrollable, text=f"{self.fans_entry.label or self.fans_name}: {self.fans_entry.current} RPM", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_battery") and psutil.sensors_battery():
            if self.fans_ok == True:
                self.batt_number = self.fans_number + 1
            elif self.temps_ok == True:
                self.batt_number = self.temps_number + 1
            else:
                self.batt_number = 10
            self.batt = psutil.sensors_battery()
            if mode == "startup":
                self.header_text = ui.CTkLabel(self.scrollable, fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['battery'][l_use], font=ui.CTkFont(size=15, weight="bold")).grid(row=self.batt_number, column=0, pady=(5, 7.5), columnspan=4)
                self.charge_text = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['charge'][l_use]}{str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                if self.batt.power_plugged:
                    self.remaining_text = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['remaining'][l_use]}{str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                    self.status_text = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['status'][l_use]}{str(l_dict['startup']['charging'][l_use] if self.batt.percent < 100 else l_dict['startup']['charged'][l_use])}", font=ui.CTkFont(size=13, weight="bold"))
                    self.plugged_text = ui.CTkLabel(self.scrollable, text=l_dict['startup']['plugged-yes'][l_use], font=ui.CTkFont(size=13, weight="bold"))
                else:
                    self.remaining_text = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['remaining'][l_use]}{str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                    self.status_text = ui.CTkLabel(self.scrollable, text=f"{l_dict['startup']['status'][l_use]}{l_dict['startup']['discharging'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
                    self.plugged_text = ui.CTkLabel(self.scrollable, text=l_dict['startup']['plugged-no'][l_use], font=ui.CTkFont(size=13, weight="bold"))
                self.charge_text.grid(row=self.batt_number + 1, column=0, pady=(0, 5), columnspan=4)
                self.remaining_text.grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                self.status_text.grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                self.plugged_text.grid(row=self.batt_number + 4, column=0, pady=(0, 5), columnspan=4)
            elif mode == "refresh":
                self.charge_text.configure(text=f"{l_dict['startup']['charge'][l_use]}{str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                if self.batt.power_plugged:
                    self.remaining_text.configure(text=f"{l_dict['startup']['remaining'][l_use]}{str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                    self.status_text.configure(text=f"{l_dict['startup']['status'][l_use]}{str(l_dict['startup']['charging'][l_use] if self.batt.percent < 100 else l_dict['startup']['charged'][l_use])}", font=ui.CTkFont(size=13, weight="bold"))
                    self.plugged_text.configure(text=l_dict['startup']['plugged-yes'][l_use], font=ui.CTkFont(size=13, weight="bold"))
                else:
                    self.remaining_text.configure(text=f"{l_dict['startup']['remaining'][l_use]}{str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                    self.status_text.configure(text=f"{l_dict['startup']['status'][l_use]}{l_dict['startup']['discharging'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
                    self.plugged_text.configure(text=l_dict['startup']['plugged-no'][l_use], font=ui.CTkFont(size=13, weight="bold"))
    def refresh(self):
        self.weather.configure(text=f"{l_dict['startup']['weather'][l_use]}{l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold")) 
        self.system.configure(fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['system'][l_use], font=ui.CTkFont(size=15, weight="bold")) 
        self.hostname.configure(text=f"{l_dict['startup']['hostname'][l_use]}{str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
        self.distro.configure(text=f"{l_dict['startup']['distro'][l_use]}{distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
        self.kernel.configure(text=f"{l_dict['startup']['kernel'][l_use]}{platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
        self.packages.configure(text=f"{l_dict['startup']['packages'][l_use]}{l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
        self.uptime.configure(text=f"{l_dict['startup']['uptime'][l_use]}{os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
        self.boot_time.configure(text=f"{l_dict['startup']['boot-time'][l_use]}{str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
        self.usages.configure(fg_color=["#a9a9a9", "#2f2f2f"], corner_radius=20, text=l_dict['startup']['usages'][l_use], font=ui.CTkFont(size=15, weight="bold"))
        self.cpu_usage.configure(text=f"CPU: {l_dict['startup']['getting'][l_use]}", font=ui.CTkFont(size=13, weight="bold"))
        self.disk_usage.configure(text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.ram_usage.configure(text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
        self.swap_usage.configure(text=f"{l_dict['startup']['swap'][l_use]}%{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.refresh_button = ui.CTkButton(self, text=l_dict['startup']['refresh'][l_use], command=self.refresh, font=ui.CTkFont(size=15, weight="bold"))
        self.weather_thread = threading.Thread(target=lambda:self.weather_def(), daemon=True)
        self.weather_thread.start()
        self.packages_thread = threading.Thread(target=lambda:self.packages_def(), daemon=True)
        self.packages_thread.start()
        self.cpu_usage_thread = threading.Thread(target=lambda:self.cpu_usage_def(), daemon=True)
        self.cpu_usage_thread.start()
        self.other_def("refresh")

class NotesAndDocuments(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.mainpage = self.tabview.add(l_dict['nad']['home'][l_use])
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)
        self.mainbar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent")
        self.mainbar.grid(row=0, column=0, sticky="nsew", padx=(0, 7.5))
        self.mainbar.grid_columnconfigure((0, 1), weight=1)
        self.sidebar = ui.CTkFrame(self.mainpage, fg_color="transparent")
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=(7.5, 0))
        self.sidebar.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.notes_label = ui.CTkLabel(self.mainbar, text=l_dict['nad']['notes'][l_use], corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.backups_label = ui.CTkLabel(self.mainbar, text=l_dict['nad']['backups'][l_use], corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.entry = ui.CTkEntry(self.sidebar, placeholder_text=l_dict['nad']['note-or-document'][l_use])
        self.button1 = ui.CTkButton(self.sidebar, text=l_dict['nad']['create'][l_use], command=lambda:self.create("new"))
        self.button2 = ui.CTkButton(self.sidebar, text=l_dict['nad']['open'][l_use], command=self.open)
        self.button3 = ui.CTkButton(self.sidebar, text=l_dict['nad']['rename'][l_use], command=self.rename)
        self.button4 = ui.CTkButton(self.sidebar, text=l_dict['nad']['restore'][l_use], command=self.restore)
        self.button5 = ui.CTkButton(self.sidebar, text=l_dict['nad']['delete'][l_use], command=self.delete)
        self.notes = os.listdir(notes)
        self.notes.remove(".backups")
        self.backups = os.listdir(f"{notes}.backups")
        self.notes_number = 0
        self.backups_number = 0
        for note_name in self.notes:
            self.notes_number += 1
            ui.CTkButton(self.mainbar, text=note_name, command=lambda note_name = note_name: self.insert(f"{notes}{note_name}")).grid(row=self.notes_number, column=0, sticky="nsew", pady=(0, 10), padx=25)
        for backup_name in self.backups:
            self.backups_number += 1
            ui.CTkButton(self.mainbar, text=backup_name, command=lambda backup_name = backup_name: self.insert(f"{notes}.backups/{backup_name}")).grid(row=self.backups_number, column=1, sticky="nsew", pady=(0, 10), padx=25)
        self.pages = {}
        self.labels = {}
        self.contents = {}
        self.frames = {}
        self.saves = {}
        self.saves_closes = {}
        self.closes = {}
        self.names = {}
        self.files = {}
        self.useds = {}
        for i in range(1, 9):
            self.pages[f"page{i}"] = self.tabview.add(i)
            self.pages[f"page{i}"].grid_rowconfigure(1, weight=1)
            self.pages[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.labels[f"page{i}"] = ui.CTkLabel(self.pages[f"page{i}"], text=l_dict['nad']['note-or-document'][l_use])
            self.contents[f"page{i}"] = ui.CTkTextbox(self.pages[f"page{i}"], state="disabled")
            self.frames[f"page{i}"] = ui.CTkFrame(self.pages[f"page{i}"], fg_color="transparent")
            self.frames[f"page{i}"].grid_rowconfigure((0, 1, 2), weight=1)
            self.frames[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.saves[f"page{i}"] = ui.CTkButton(self.frames[f"page{i}"], text=l_dict['nad']['save'][l_use], command=lambda i = i: self.save(i), state="disabled")
            self.saves_closes[f"page{i}"] = ui.CTkButton(self.frames[f"page{i}"], text=l_dict['nad']['save-close'][l_use], command=lambda i = i: self.save_close(i), state="disabled")
            self.closes[f"page{i}"] = ui.CTkButton(self.frames[f"page{i}"], text=l_dict['nad']['close'][l_use], command=lambda i = i: self.close(i), state="disabled")
            self.labels[f"page{i}"].grid(row=0, column=0, columnspan=2, sticky="nsew")
            self.contents[f"page{i}"].grid(row=1, column=0, sticky="nsew")
            self.frames[f"page{i}"].grid(row=1, column=1, sticky="nsew", padx=(15, 0))
            self.saves[f"page{i}"].grid(row=0, column=0, sticky="nsew", pady=(0, 10))
            self.saves_closes[f"page{i}"].grid(row=1, column=0, sticky="nsew", pady=(0, 10))
            self.closes[f"page{i}"].grid(row=2, column=0, sticky="nsew")
            self.names[f"page{i}"] = i
            self.files[f"page{i}"] = None
            self.useds[f"page{i}"] = False
        self.notes_label.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=15)
        self.backups_label.grid(row=0, column=1, sticky="nsew", pady=(0, 10), padx=15)
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5))
        self.button5.grid(row=5, column=0, sticky="nsew")
    def insert(self, file: str):
        self.entry.delete(0, "end")
        self.entry.insert(0, file)
    def list(self, name):
        if name != None:
            self.insert(name)
        self.notes = os.listdir(notes)
        self.notes.remove(".backups")
        self.backups = os.listdir(f"{notes}.backups")
        self.notes_number = 0
        self.backups_number = 0
        for note_name in self.notes:
            self.notes_number += 1
            ui.CTkButton(self.mainbar, text=note_name, command=lambda note_name = note_name: self.insert(f"{notes}{note_name}")).grid(row=self.notes_number, column=0, sticky="nsew", pady=(0, 10), padx=25)
        for backup_name in self.backups:
            self.backups_number += 1
            ui.CTkButton(self.mainbar, text=backup_name, command=lambda backup_name = backup_name: self.insert(f"{notes}.backups/{backup_name}")).grid(row=self.backups_number, column=1, sticky="nsew", pady=(0, 10), padx=25)
    def create(self, mode: str):
        self.dialog = ui.CTkInputDialog(text=l_dict['nad']['create-description'][l_use], title=l_dict['nad']['create-title'][l_use])
        self.new_name = self.dialog.get_input()
        if self.new_name == None:
            return
        os.system(f"touch {notes}{self.new_name}")
        if not os.path.isfile(f"{notes}{self.new_name}"):
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['create-error'][l_use])
            return
        self.list(f"{notes}{self.new_name}")
        if mode == "new" and os.path.isfile(self.new_name):
            mb.showinfo(l_dict['globals']['information'][l_use], l_dict['nad']['create-successful'][l_use])
    def open(self):
        try:
            if self.entry.get() != "" and self.entry.get() != None:
                with open(self.entry.get(), "r") as self.file_entry:
                    self.text = self.file_entry.read()
            else:
                self.name = fd.askopenfilename()
                with open(self.name, "r") as self.file_fd:
                    self.text = self.file_fd.read()
                self.entry.delete(0, "end")
                self.entry.insert(0, self.name)
            self.which_page = 0
            if self.useds["page1"] == False:
                self.which_page = 1
            elif self.useds["page2"] == False:
                self.which_page = 2
            elif self.useds["page3"] == False:
                self.which_page = 3
            elif self.useds["page4"] == False:
                self.which_page = 4
            elif self.useds["page5"] == False:
                self.which_page = 5
            elif self.useds["page6"] == False:
                self.which_page = 6
            elif self.useds["page7"] == False:
                self.which_page = 7
            elif self.useds["page8"] == False:
                self.which_page = 8
            else:
                mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['all-slots-are-full'][l_use])
                return
            self.labels[f"page{self.which_page}"].configure(text=self.entry.get())
            self.contents[f"page{self.which_page}"].configure(state="normal")
            self.contents[f"page{self.which_page}"].insert("0.0", self.text)
            if os.path.dirname(self.entry.get()) == f"{notes}.backups":
                self.contents[f"page{self.which_page}"].configure(state="disabled")
            else:
                self.saves[f"page{self.which_page}"].configure(state="normal")
                self.saves_closes[f"page{self.which_page}"].configure(state="normal")
            self.closes[f"page{self.which_page}"].configure(state="normal")
            self.files[f"page{self.which_page}"] = self.entry.get()
            self.useds[f"page{self.which_page}"] = True
            try:
                self.tabview.rename(self.names[f"page{self.which_page}"], os.path.basename(self.entry.get())[:4])
                self.tabview.set(os.path.basename(self.entry.get())[:4])
                self.names[f"page{self.which_page}"] = os.path.basename(self.entry.get())[:4]
            except:
                try:
                    self.tabview.set(self.which_page)
                except:
                    self.tabview.set(os.path.basename(self.entry.get())[:4])
        except:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['open-error'][l_use])
    def rename(self):
        if os.path.dirname(self.entry.get()) == f"{notes}.backups":
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['cant-be-renamed'][l_use])
            return
        if not os.path.isfile(self.entry.get()):
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['no-error'][l_use])
            return
        self.dialog = ui.CTkInputDialog(text=l_dict['nad']['rename-description'][l_use], title=l_dict['nad']['rename-title'][l_use])
        self.new_name = self.dialog.get_input()
        if self.new_name == None:
            return
        if f"{os.path.dirname(self.entry.get())}/" == notes:
            os.system(f"cp {self.entry.get()} {notes}.backups/{os.path.basename(self.entry.get())}")
        if not os.path.isfile(f"{os.path.dirname(self.entry.get())}/{self.new_name}"):
            os.system(f"touch {os.path.dirname(self.entry.get())}/{self.new_name}")
        os.system(f"mv {self.entry.get()} {os.path.dirname(self.entry.get())}/{self.new_name}")
        if not os.path.isfile(f"{os.path.dirname(self.entry.get())}/{self.new_name}"):
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['rename-error'][l_use])
            return
        self.list(f"{os.path.dirname(self.entry.get())}/{self.new_name}")
        mb.showinfo(l_dict['globals']['information'][l_use], l_dict['nad']['rename-successful'][l_use])
    def restore(self):
        if os.path.dirname(self.entry.get()) == f"{notes}.backups":
            os.system(f"cp {self.entry.get()} {notes}{os.path.basename(self.entry.get())}")
            with open(self.entry.get(), "r") as self.file_original:
                self.needed = self.file_original.read()
            with open(f"{notes}{os.path.basename(self.entry.get())}", "r") as self.file_target:
                self.final = self.file_target.read()
        elif f"{os.path.dirname(self.entry.get())}/" == notes:
            os.system(f"cp {notes}.backups/{os.path.basename(self.entry.get())} {self.entry.get()}")
            with open(f"{notes}.backups/{os.path.basename(self.entry.get())}", "r") as self.file_original:
                self.needed = self.file_original.read()
            with open(self.entry.get(), "r") as self.file_target:
                self.final = self.file_target.read()
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['restore-error'][l_use])
            return
        if self.needed == self.final:
            self.list(None)
            mb.showinfo(l_dict['globals']['information'][l_use], l_dict['nad']['restore-successful'][l_use])
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['restore-error'][l_use])
    def delete(self):
        if not os.path.isfile(self.entry.get()):
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['no-error'][l_use])
            return
        if f"{os.path.dirname(self.entry.get())}/" == notes:
            os.system(f"cp {self.entry.get()} {notes}.backups/{os.path.basename(self.entry.get())}")
        os.system(f"rm {self.entry.get()}")
        if not os.path.isfile(self.entry.get()):
            self.entry.delete(0, "end")
            self.list(None)
            mb.showinfo(l_dict['globals']['information'][l_use], l_dict['nad']['delete-successful'][l_use])
        else: 
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['delete-error'][l_use])
    def save(self, caller: str):
        try:
            if f"{os.path.dirname(self.files[f"page{caller}"])}/" == notes:
                os.system(f"cp {self.files[f"page{caller}"]} {notes}.backups/{os.path.basename(self.files[f"page{caller}"])}")
            with open(self.files[f"page{caller}"], "w+") as self.file_save:
                self.file_save.write(self.contents[f"page{caller}"].get("0.0", 'end'))
            with open(self.files[f"page{caller}"], "r") as self.file_control:
                self.control = self.file_control.read()
            self.list(None)
            if self.control == self.contents[f"page{caller}"].get("0.0", 'end'):
                mb.showinfo(l_dict['globals']['information'][l_use], l_dict['nad']['save-successful'][l_use])
            else:
                mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['save-error'][l_use])
        except:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['nad']['save-error'][l_use])
    def close(self, caller: str):
        self.labels[f"page{caller}"].configure(text=l_dict['nad']['note-or-document'][l_use])
        self.contents[f"page{caller}"].configure(state="normal")
        self.contents[f"page{caller}"].delete("0.0", 'end')
        self.contents[f"page{caller}"].configure(state="disabled")
        self.saves[f"page{caller}"].configure(state="disabled")
        self.saves_closes[f"page{caller}"].configure(state="disabled")
        self.closes[f"page{caller}"].configure(state="disabled")
        self.names[f"page{caller}"] = caller
        self.files[f"page{caller}"] = None
        self.useds[f"page{caller}"] = False
    def save_close(self, caller: str):
        self.save(caller)
        self.close(caller)

class Packages(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25, fg_color="transparent")
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.mainpage = self.tabview.add(l_dict['store']['home'][l_use])
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)
        self.mainbar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent")
        self.mainbar.grid(row=0, column=0, sticky="nsew", padx=(0, 7.5))
        self.mainbar.grid_columnconfigure((0, 1), weight=1)
        self.sidebar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent", width=125)
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=(7.5, 0))
        self.sidebar.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.traditionals_label = ui.CTkLabel(self.mainbar, text=pkg_type, corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.flatpaks_label = ui.CTkLabel(self.mainbar, text="Flatpak", corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.entry = ui.CTkEntry(self.sidebar, placeholder_text=l_dict['store']['packages'][l_use])
        self.button1 = ui.CTkButton(self.sidebar, text=f"{l_dict['operations']['search'][l_use]}", command=lambda:self.go([pkg_mngr, "search"]))
        self.button2 = ui.CTkButton(self.sidebar, text=f"{l_dict['operations']['search'][l_use]} (Flatpak)", command=lambda:self.go(["flatpak", "search"]))
        self.button3 = ui.CTkButton(self.sidebar, text=l_dict['operations']['install'][l_use], command=lambda:self.go(["auto", "install"]))
        self.button4 = ui.CTkButton(self.sidebar, text=l_dict['operations']['reinstall'][l_use], command=lambda:self.go(["auto", "reinstall"]))
        self.button5 = ui.CTkButton(self.sidebar, text=l_dict['operations']['uninstall'][l_use], command=lambda:self.go(["auto", "uninstall"]))
        self.button6 = ui.CTkButton(self.sidebar, text=l_dict['operations']['update'][l_use], command=lambda:self.go(["auto", "update"]))
        if os.path.isfile(debian):
            self.traditionals = ["Firefox-ESR", "Firefox", "VLC", "LibreOffice", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Lolcat"]
        elif os.path.isfile(fedora):
            self.traditionals = ["Firefox", "VLC", "LibreOffice", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Fastfetch", "Lolcat"]
        elif os.path.isfile(solus):
            self.traditionals = ["Firefox", "VLC", "LibreOffice-All", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "Neofetch", "Lolcat"]
        elif os.path.isfile(arch):
            self.traditionals = ["Firefox", "VLC", "LibreOffice-Fresh", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Fastfetch", "Lolcat"]
        self.traditionals_number = 0
        self.flatpaks = [["Firefox", "org.mozilla.Firefox"], ["Brave Browser", "com.brave.Browser"], [f"Google Chrome{l_dict['store']['proprietary'][l_use]}", "com.google.Chrome"], [f"Microsoft Edge{l_dict['store']['proprietary'][l_use]}", "com.microsoft.Edge"], ["Chromium", "org.chromium.Chromium"], ["Librewolf", "io.gitlab.librewolf-community"], [f"Discord{l_dict['store']['proprietary'][l_use]}", "com.discordapp.Discord"], ["Signal", "org.signal.Signal"], ["Telegram", "org.telegram.desktop"], [f"Spotify{l_dict['store']['proprietary'][l_use]}", "com.spotify.Client"], ["Tuta", "com.tutanota.Tutanota"], ["OBS Studio", "com.obsproject.Studio"], ["VLC", "org.videolan.VLC"], ["Audacity", "org.audacityteam.Audacity"], ["LibreOffice", "org.libreoffice.LibreOffice"], ["Blender", "org.blender.Blender"], ["GIMP", "org.gimp.GIMP"], ["Inkspace", "org.inkscape.Inkscape"], ["Design", "io.github.dubstar_04.design"], ["Plots", "com.github.alexhuntley.Plots"], [f"Visual Studio Code{l_dict['store']['proprietary'][l_use]}", "com.visualstudio.code"], ["VSCodium", "com.vscodium.codium"], ["Bitwarden", "com.bitwarden.desktop"], ["Okular", "org.kde.okular"], [f"Steam{l_dict['store']['proprietary'][l_use]}", "com.valvesoftware.Steam"], ["Heroic Games Launcher", "com.heroicgameslauncher.hgl"], ["Lutris", "net.lutris.Lutris"], ["ProtonUp-Qt", "net.davidotek.pupgui2"], ["Protontricks", "com.github.Matoking.protontricks"], ["Bottles", "com.usebottles.bottles"], ["Wine", "org.winehq.Wine"], ["Flatseal", "com.github.tchx84.Flatseal"]]
        self.flatpaks_number = 0
        for traditional in self.traditionals:
            self.traditionals_number += 1
            ui.CTkButton(self.mainbar, text=traditional, command=lambda traditional = traditional: self.insert(traditional.lower())).grid(row=self.traditionals_number, column=0, sticky="nsew", pady=(0, 10), padx=25)
        for f_prettyname, f_name in self.flatpaks:
            self.flatpaks_number += 1
            ui.CTkButton(self.mainbar, text=f_prettyname, command=lambda f_name = f_name: self.insert(f_name)).grid(row=self.flatpaks_number, column=1, sticky="nsew", pady=(0, 10), padx=25)        
        self.pages = {}
        self.labels = {}
        self.outputs = {}
        self.closes = {}
        self.useds = {}
        for i in range(1, 15):
            self.pages[f"page{i}"] = self.tabview.add(i)
            self.pages[f"page{i}"].grid_rowconfigure(1, weight=1)
            self.pages[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.labels[f"page{i}"] = ui.CTkLabel(self.pages[f"page{i}"], text=f"{l_dict['operations']['process'][l_use]} {i}")
            self.outputs[f"page{i}"] = ui.CTkTextbox(self.pages[f"page{i}"], state="disabled")
            self.closes[f"page{i}"] = ui.CTkButton(self.pages[f"page{i}"], text=l_dict['store']['close'][l_use], command=lambda i = i: self.close(i), state="disabled")
            self.labels[f"page{i}"].grid(row=0, column=0, sticky="nsew")
            self.outputs[f"page{i}"].grid(row=1, column=0, sticky="nsew")
            self.closes[f"page{i}"].grid(row=2, column=0, sticky="nsew", pady=(10, 0))
            self.useds[f"page{i}"] = False
        self.traditionals_label.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=15)
        self.flatpaks_label.grid(row=0, column=1, sticky="nsew", pady=(0, 10), padx=15)
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button5.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(0, 10))
        self.button6.grid(row=6, column=0, sticky="nsew", padx=(0, 10))
    def insert(self, name):
        self.entry.delete(0, "end")
        self.entry.insert(0, name)
    def do(self, operation, target, use, time):
        if target == "" or target == None:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['packages-name-error'][l_use])
            return
        add_operation(f"{l_dict['operations'][operation[1]][l_use]}: {target}", time)
        if "." in target or operation[0] == "flatpak":
            if not os.path.isfile('/usr/bin/flatpak') and not os.path.isfile('/bin/flatpak'):
                self.ask_f = mb.askyesno(l_dict['globals']['warning'][l_use], f"Flatpak {l_dict['questions']['install'][l_use]}")
                if self.ask_f == True:
                    delete_operation(f"{l_dict['operations'][operation[1]][l_use]}: {target}", time)
                    add_operation(f"{l_dict['operations']['install'][l_use]}: Flatpak", time)
                    if os.path.isfile(debian):
                        self.command = 'pkexec apt -y install flatpak ; flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
                    elif os.path.isfile(fedora):
                        self.command = 'flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
                    elif os.path.isfile(solus):
                        self.command = 'pkexec eopkg -y install flatpak ; flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
                    elif os.path.isfile(arch):
                        self.command = 'pkexec pacman --noconfirm -S flatpak ; flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo'
                else:
                    mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['cancelled'][l_use])
                    return
            else:
                if operation[1] == "search":
                    self.command = f"flatpak {operation[1]} {target}"
                else:
                    self.command = f"flatpak {operation[1]} {target} -y"
        else:
            if os.path.isfile(debian):
                if operation[1] == 'search':
                    self.command = f"apt -y search {target}"
                elif operation[1] == 'install':
                    self.command = f"pkexec apt -y install {target}"
                elif operation[1] == 'reinstall':
                    self.command = f"pkexec apt -y install --reinstall {target}"
                elif operation[1] == 'uninstall':
                    self.command = f"pkexec apt -y autoremove --purge {target}"
                elif operation[1] == 'update':
                    self.command = f"pkexec apt -y upgrade {target}"
            elif os.path.isfile(fedora):
                if operation[1] == 'search':
                    self.command = f"dnf5 -y --nogpgcheck search {target}"
                elif operation[1] == 'install':
                    self.command = f"pkexec dnf5 -y --nogpgcheck install {target}"
                elif operation[1] == 'reinstall':
                    self.command = f"pkexec dnf5 -y --nogpgcheck reinstall {target}"
                elif operation[1] == 'uninstall':
                    self.command = f"pkexec dnf5 -y --nogpgcheck remove {target}"
                elif operation[1] == 'update':
                    self.command = f"pkexec dnf5 -y --nogpgcheck update {target}"
            elif os.path.isfile(solus):
                if operation[1] == 'search':
                    self.command = f"eopkg -y search {target}"
                elif operation[1] == 'install':
                    self.command = f"pkexec eopkg -y install {target}"
                elif operation[1] == 'reinstall':
                    self.command = f"pkexec eopkg -y install --reinstall {target}"
                elif operation[1] == 'uninstall':
                    self.command = f"pkexec eopkg -y remove --purge {target}"
                elif operation[1] == 'update':
                    self.command = f"pkexec eopkg -y upgrade {target}"
            elif os.path.isfile(arch):
                if operation[1] == 'search':
                    self.command = f"pacman --noconfirm -Ss {target}"
                elif operation[1] == 'install' or operation[1] == 'reinstall':
                    self.command = f"pkexec pacman --noconfirm -S {target}"
                elif operation[1] == 'uninstall':
                    self.command = f"pkexec pacman --noconfirm -Rns {target}"
                elif operation[1] == 'update':
                    self.command = f"pkexec pacman --noconfirm -Syu {target}"
        if not os.path.isfile('/usr/bin/flatpak') and not os.path.isfile('/bin/flatpak') and self.ask_f == True:
            self.labels[f"page{use}"].configure(text=f"{l_dict['operations']['install'][l_use]}: Flatpak")
        else:
            self.labels[f"page{use}"].configure(text=f"{l_dict['operations'][operation[1]][l_use]}: {target}")
        self.useds[f"page{use}"] = True
        self.tabview.set(use)
        with subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.out)
                self.outputs[f"page{use}"].configure(state="disabled")
        self.closes[f"page{use}"].configure(state="normal")
        if not os.path.isfile('/usr/bin/flatpak') and not os.path.isfile('/bin/flatpak') and self.ask_f == True:
            if os.path.isfile(debian) or os.path.isfile(solus) or os.path.isfile(arch):
                restart_system()
            delete_operation(f"{l_dict['operations']['install'][l_use]}: Flatpak", time)
            self.entry.delete(0, "end")
            self.entry.insert(0, target)
            self.ask_f = None
            self.go(operation)
            return
        else:
            delete_operation(f"{l_dict['operations'][operation[1]][l_use]}: {target}", time)
        if self.run_command.returncode == 0:
            mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['failed'][l_use])
    def go(self, wanted: str):
        if self.useds["page1"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 1, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page2"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 2, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page3"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 3, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page4"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 4, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page5"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 5, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page6"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 6, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page7"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 7, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page8"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 8, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page9"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 9, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page10"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 10, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page11"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 11, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page12"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 12, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page13"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 13, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page14"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 14, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['all-slots-are-full'][l_use])
            return
    def close(self, caller: str):
        self.labels[f"page{caller}"].configure(text=f"{l_dict['operations']['process'][l_use]} {caller}")
        self.outputs[f"page{caller}"].configure(state="normal")
        self.outputs[f"page{caller}"].delete("0.0", 'end')
        self.outputs[f"page{caller}"].configure(state="disabled")
        self.closes[f"page{caller}"].configure(state="disabled")
        self.useds[f"page{caller}"] = False

class DEsWMsCs(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25, fg_color="transparent")
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.mainpage = self.tabview.add(l_dict['store']['home'][l_use])
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)
        self.mainbar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent")
        self.mainbar.grid(row=0, column=0, sticky="nsew", padx=(0, 7.5))
        self.mainbar.grid_columnconfigure(0, weight=1)
        self.sidebar = ui.CTkFrame(self.mainpage, fg_color="transparent")
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=(7.5, 0))
        self.sidebar.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.dewmc = ui.StringVar(None)
        self.deswmscs_label = ui.CTkLabel(self.mainbar, text=l_dict['store']['deswmscs'][l_use], corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.selected = ui.CTkLabel(self.sidebar, textvariable=self.dewmc)
        self.button1 = ui.CTkButton(self.sidebar, text=l_dict['operations']['install'][l_use], command=lambda:self.go('install'))
        self.button2 = ui.CTkButton(self.sidebar, text=l_dict['operations']['reinstall'][l_use], command=lambda:self.go('reinstall'))
        self.button3 = ui.CTkButton(self.sidebar, text=l_dict['operations']['uninstall'][l_use], command=lambda:self.go('uninstall'))
        self.button4 = ui.CTkButton(self.sidebar, text=l_dict['operations']['update'][l_use], command=lambda:self.go('update'))
        if os.path.isfile(debian):
            self.deswmscs = ["KDE-Plasma-Desktop", "GNOME", "Cinnamon", "Mate", "Xfce4", "LXDE", "LXQt", "Openbox", "bspwm", "Qtile", "Herbstluftwm", "Awesome", "IceWM", "i3", "Sway", "Xmonad"]
        elif os.path.isfile(fedora):
            self.deswmscs = ["GNOME", "KDE", "Budgie", "Cinnamon", "Deepin", "MATE", "Xfce", "LXDE", "LXQt", "Phosh", "Sugar", "Sway", "i3", "Hyprland", "Openbox", "Fluxbox", "Blackbox", "bspwm", "Basic"]
        elif os.path.isfile(solus):
            self.deswmscs = ["Budgie", "GNOME", "KDE", "Xfce", "Mate", "Fluxbox", "Openbox", "i3", "bspwm"]
        elif os.path.isfile(arch):
            self.deswmscs = ["Budgie", "Cinnamon", "Cutefish", "Deepin", "Enlightenment", "GNOME", "GNOME-Flashback", "Plasma", "LXDE", "LXDE-GTK3", "LXQt", "Mate", "Pantheon", "Phosh", "Sugar", "UKUI", "Xfce4", "Hyprland", "Fluxbox", "IceWM", "openmotif", "Openbox", "PekWM", "Xorg-TWM", "Herbstluftwm", "i3-WM", "Notion", "Stumpwm", "Awesome", "Qtile", "xmonad"]
        self.deswmscs_number = 0
        for dewmc in self.deswmscs:
            self.deswmscs_number += 1
            ui.CTkButton(self.mainbar, text=dewmc, command=lambda dewmc = dewmc: self.dewmc.set(dewmc)).grid(row=self.deswmscs_number, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.pages = {}
        self.labels = {}
        self.outputs = {}
        self.closes = {}
        self.useds = {}
        for i in range(1, 15):
            self.pages[f"page{i}"] = self.tabview.add(i)
            self.pages[f"page{i}"].grid_rowconfigure(1, weight=1)
            self.pages[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.labels[f"page{i}"] = ui.CTkLabel(self.pages[f"page{i}"], text=f"{l_dict['operations']['process'][l_use]} {i}")
            self.outputs[f"page{i}"] = ui.CTkTextbox(self.pages[f"page{i}"], state="disabled")
            self.closes[f"page{i}"] = ui.CTkButton(self.pages[f"page{i}"], text=l_dict['store']['close'][l_use], command=lambda i = i: self.close(i), state="disabled")
            self.labels[f"page{i}"].grid(row=0, column=0, sticky="nsew")
            self.outputs[f"page{i}"].grid(row=1, column=0, sticky="nsew")
            self.closes[f"page{i}"].grid(row=2, column=0, sticky="nsew", pady=(10, 0))
            self.useds[f"page{i}"] = False
        self.deswmscs_label.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=15)
        self.selected.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5))
        self.button4.grid(row=4, column=0, sticky="nsew")
    def do(self, operation, target, use, time):
        if target == None or target == "":
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['deswmscs-name-error'][l_use])
            return
        add_operation(f"{l_dict['operations'][operation][l_use]}: {target}", time)
        if os.path.isfile(debian):
            if target.lower() != "mate":
                if operation == 'install':
                    self.command = f"pkexec apt -y install {target.lower()}"
                elif operation == 'reinstall':
                    self.command = f"pkexec apt -y install --reinstall {target.lower()}"
                elif operation == 'uninstall':
                    self.command = f"pkexec apt -y autoremove --purge {target.lower()}"
                elif operation == 'update':
                    self.command = f"pkexec apt -y upgrade {target.lower()}"
            elif target.lower() == "mate":
                if operation == 'install':
                    self.command = f"pkexec apt -y install mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == 'reinstall':
                    self.command = f"pkexec apt -y install --reinstall mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == 'uninstall':
                    self.command = f"pkexec apt -y autoremove --purge mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == 'update':
                    self.command = f"pkexec apt -y upgrade mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
        elif os.path.isfile(fedora):
            if target in ["KDE", "Xfce", "Phosh", "LXDE", "LXQt", "Cinnamon", "Mate", "Sugar", "Deepin", "Budgie", "Basic", "Sway", "Deepin", "i3"]:
                if operation == 'install':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck install @{target.lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'reinstall':
                    mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['dnf-nosupport'][l_use])
                    delete_operation(f"{l_dict['operations'][operation][l_use]}: {target}", time)
                    return
                elif operation == 'uninstall':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck remove @{target.lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'update':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck upgrade @{target.lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
            elif target in ["Openbox", "Fluxbox", "Blackbox", "bspwm"]:
                if operation == 'install':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck install {target.lower()} ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'reinstall':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck reinstall {target.lower()}; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'uninstall':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck remove {target.lower()} ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'update':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck upgrade {target.lower()} ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
            elif target == "GNOME":
                if operation == 'install':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck install @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'reinstall':
                    mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['dnf-nosupport'][l_use])
                    delete_operation(f"{l_dict['operations'][operation][l_use]}: {target}", time)
                    return
                elif operation == 'uninstall':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck remove @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == 'update':
                    self.command = f"pkexec bash -c 'dnf5 -y --nogpgcheck upgrade @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"                        
        elif os.path.isfile(solus):
            if target.lower() not in ["openbox", "fluxbox", "bspwm"]:
                if operation == 'install':
                    self.command = f"pkexec eopkg -y install -c desktop.{target.lower()}"
                elif operation == 'reinstall':
                    self.command = f"pkexec eopkg -y install --reinstall -c desktop.{target.lower()}"
                elif operation == 'uninstall':
                    self.command = f"pkexec eopkg -y remove --purge -c desktop.{target.lower()}"
                elif operation == 'update':
                    self.command = f"pkexec eopkg -y upgrade -c desktop.{target.lower()}"
            else:
                if operation == 'install':
                    self.command = f"pkexec eopkg -y install {target.lower()}"
                elif operation == 'reinstall':
                    self.command = f"pkexec eopkg -y install --reinstall {target.lower()}"
                elif operation == 'uninstall':
                    self.command = f"pkexec eopkg -y remove --purge {target.lower()}"
                elif operation == 'update':
                    self.command = f"pkexec eopkg -y upgrade {target.lower()}"           
        elif os.path.isfile(solus):
            if target.lower() not in ["openbox", "fluxbox", "bspwm"]:
                if operation == 'install':
                    self.command = f"pkexec eopkg -y install -c desktop.{target.lower()}"
                elif operation == 'reinstall':
                    self.command = f"pkexec eopkg -y install --reinstall -c desktop.{target.lower()}"
                elif operation == 'uninstall':
                    self.command = f"pkexec eopkg -y remove --purge -c desktop.{target.lower()}"
                elif operation == 'update':
                    self.command = f"pkexec eopkg -y upgrade -c desktop.{target.lower()}"
            else:
                if operation == 'install':
                    self.command = f"pkexec eopkg -y install {target.lower()}"
                elif operation == 'reinstall':
                    self.command = f"pkexec eopkg -y install --reinstall {target.lower()}"
                elif operation == 'uninstall':
                    self.command = f"pkexec eopkg -y remove --purge {target.lower()}"
                elif operation == 'update':
                    self.command = f"pkexec eopkg -y upgrade {target.lower()}"        
        elif os.path.isfile(arch):
            if operation == 'install':
                self.command = f"pkexec pacman --noconfirm -S {target.lower()}"
            elif operation == 'reinstall':
                self.command = f"pkexec pacman --noconfirm -S {target.lower()}"
            elif operation == 'uninstall':
                self.command = f"pkexec pacman --noconfirm -Rns {target.lower()}"
            elif operation == 'update':
                self.command = f"pkexec pacman --noconfirm -Syu {target.lower()}"
        self.labels[f"page{use}"].configure(text=f"{l_dict['operations'][operation][l_use]}: {target}")
        self.useds[f"page{use}"] = True
        self.tabview.set(use)
        with subprocess.Popen(self.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.out)
                self.outputs[f"page{use}"].configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.err)
                self.outputs[f"page{use}"].configure(state="disabled")
        self.closes[f"page{use}"].configure(state="normal")
        delete_operation(f"{l_dict['operations'][operation][l_use]}: {target}", time)
        if self.run_command.returncode == 0:
            mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['failed'][l_use])
    def go(self, wanted: str):
        if self.useds["page1"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 1, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page2"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 2, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page3"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 3, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page4"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 4, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page5"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 5, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page6"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 6, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page7"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 7, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page8"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 8, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page9"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 9, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page10"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 10, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page11"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 11, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page12"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 12, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page13"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 13, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page14"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.dewmc.get(), 14, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['all-slots-are-full'][l_use])
            return
    def close(self, caller: str):
        self.labels[f"page{caller}"].configure(text=f"{l_dict['operations']['process'][l_use]} {caller}")
        self.outputs[f"page{caller}"].configure(state="normal")
        self.outputs[f"page{caller}"].delete("0.0", 'end')
        self.outputs[f"page{caller}"].configure(state="disabled")
        self.closes[f"page{caller}"].configure(state="disabled")
        self.useds[f"page{caller}"] = False
        
class Scripts(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25, fg_color="transparent")
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.mainpage = self.tabview.add(l_dict['store']['home'][l_use])
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)
        self.mainbar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent")
        self.mainbar.grid(row=0, column=0, sticky="nsew", padx=(0, 7.5))
        self.mainbar.grid_columnconfigure((0, 1), weight=1)
        self.traditionals_label = ui.CTkLabel(self.mainbar, text=pkg_mngr, corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.flatpaks_label = ui.CTkLabel(self.mainbar, text="Flatpak", corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.button11 = ui.CTkButton(self.mainbar, text=l_dict['store']['update'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['update'][l_use]]))
        self.button12 = ui.CTkButton(self.mainbar, text=l_dict['store']['sync'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['sync'][l_use]]))
        self.button13 = ui.CTkButton(self.mainbar, text=l_dict['store']['clean'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['clean'][l_use]]))
        self.button14 = ui.CTkButton(self.mainbar, text=l_dict['store']['remove'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['remove'][l_use]]))
        self.button15 = ui.CTkButton(self.mainbar, text=l_dict['store']['fix'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['fix'][l_use]]))
        self.button16 = ui.CTkButton(self.mainbar, text=l_dict['store']['history'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['history'][l_use]]))
        self.button17 = ui.CTkButton(self.mainbar, text=l_dict['store']['list'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['list'][l_use]]))
        self.button18 = ui.CTkButton(self.mainbar, text=l_dict['store']['leaves'][l_use], command=lambda:self.go([pkg_mngr, l_dict['store']['leaves'][l_use]]))
        self.button21 = ui.CTkButton(self.mainbar, text=l_dict['store']['update'][l_use], command=lambda:self.go(["flatpak", l_dict['store']['update'][l_use]]))
        self.button22 = ui.CTkButton(self.mainbar, text=l_dict['store']['remove'][l_use], command=lambda:self.go(["flatpak", l_dict['store']['remove'][l_use]]))
        self.button23 = ui.CTkButton(self.mainbar, text=l_dict['store']['repair'][l_use], command=lambda:self.go(["flatpak", l_dict['store']['repair'][l_use]]))
        self.button24 = ui.CTkButton(self.mainbar, text=l_dict['store']['history'][l_use], command=lambda:self.go(["flatpak", l_dict['store']['history'][l_use]]))
        self.button25 = ui.CTkButton(self.mainbar, text=l_dict['store']['list'][l_use], command=lambda:self.go(["flatpak", l_dict['store']['list'][l_use]]))
        if not os.path.isfile(fedora):
            self.button18.configure(state="disabled")
        if os.path.isfile(fedora):
            self.button15.configure(state="disabled")
        if os.path.isfile(arch):
            self.button12.configure(state="disabled")
        if os.path.isfile(solus):
            self.button12.configure(state="disabled")
            self.button15.configure(state="disabled")
        self.pages = {}
        self.labels = {}
        self.outputs = {}
        self.closes = {}
        self.useds = {}
        for i in range(1, 15):
            self.pages[f"page{i}"] = self.tabview.add(i)
            self.pages[f"page{i}"].grid_rowconfigure(1, weight=1)
            self.pages[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.labels[f"page{i}"] = ui.CTkLabel(self.pages[f"page{i}"], text=f"{l_dict['operations']['process'][l_use]} {i}")
            self.outputs[f"page{i}"] = ui.CTkTextbox(self.pages[f"page{i}"], state="disabled")
            self.closes[f"page{i}"] = ui.CTkButton(self.pages[f"page{i}"], text=l_dict['store']['close'][l_use], command=lambda i = i: self.close(i), state="disabled")
            self.labels[f"page{i}"].grid(row=0, column=0, sticky="nsew")
            self.outputs[f"page{i}"].grid(row=1, column=0, sticky="nsew")
            self.closes[f"page{i}"].grid(row=2, column=0, sticky="nsew", pady=(10, 0))
            self.useds[f"page{i}"] = False
        self.traditionals_label.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=15)
        self.button11.grid(row=1, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button12.grid(row=2, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button13.grid(row=3, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button14.grid(row=4, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button15.grid(row=5, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button16.grid(row=6, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button17.grid(row=7, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.button18.grid(row=8, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.flatpaks_label.grid(row=0, column=1, sticky="nsew", pady=(0, 10), padx=15)
        self.button21.grid(row=1, column=1, sticky="nsew", pady=(0, 10), padx=25)
        self.button22.grid(row=2, column=1, sticky="nsew", pady=(0, 10), padx=25)
        self.button23.grid(row=3, column=1, sticky="nsew", pady=(0, 10), padx=25)
        self.button24.grid(row=4, column=1, sticky="nsew", pady=(0, 10), padx=25)
        self.button25.grid(row=5, column=1, sticky="nsew", pady=(0, 10), padx=25)
    def do(self, operation, use, time):
        add_operation(f"{operation[0]}: {operation[1]}", time)
        if operation[0] == "flatpak":
            if operation[1] == l_dict['store']['update'][l_use]:
                self.command = f"flatpak update -y"
            elif operation[1] == l_dict['store']['remove'][l_use]:
                self.command = f"flatpak uninstall --unused -y"
            elif operation[1] == l_dict['store']['repair'][l_use]:
                self.command = f"flatpak repair"
            elif operation[1] == l_dict['store']['history'][l_use]:
                self.command = f"flatpak history"
            elif operation[1] == l_dict['store']['list'][l_use]:
                self.command = f"flatpak list"
        else:
            if os.path.isfile(debian):
                if operation[1] == l_dict['store']['update'][l_use]:
                    self.command = 'pkexec apt -y upgrade'
                elif operation[1] == l_dict['store']['sync'][l_use]:
                    self.command = 'pkexec apt -y dist-upgrade'
                elif operation[1] == l_dict['store']['clean'][l_use]:
                    self.command = 'pkexec apt -y autoclean'
                elif operation[1] == l_dict['store']['remove'][l_use]:
                    self.command = 'pkexec apt -y autoremove'
                elif operation[1] == l_dict['store']['fix'][l_use]:
                    self.command = 'pkexec bash -c "apt-get -y install -f ; dpkg --configure -a ; aptitude -y install"'
                elif operation[1] == l_dict['store']['history'][l_use]:
                    self.command = 'cat /var/log/dpkg.log'
                elif operation[1] == l_dict['store']['list'][l_use]:
                    self.command = 'dpkg --list | grep ^i'
            elif os.path.isfile(fedora):
                if operation[1] == l_dict['store']['update'][l_use]:
                    self.command = 'pkexec dnf5 -y --nogpgcheck upgrade'
                elif operation[1] == l_dict['store']['sync'][l_use]:
                    self.command = 'pkexec dnf5 -y --nogpgcheck distro-sync'
                elif operation[1] == l_dict['store']['clean'][l_use]:
                    self.command = 'pkexec dnf5 -y --nogpgcheck clean all'
                elif operation[1] == l_dict['store']['remove'][l_use]:
                    self.command = 'pkexec dnf5 -y --nogpgcheck autoremove'
                elif operation[1] == l_dict['store']['history'][l_use]:
                    self.command = 'dnf5 history list'
                elif operation[1] == l_dict['store']['list'][l_use]:
                    self.command = 'dnf5 list --installed'
                elif operation[1] == l_dict['store']['leaves'][l_use]:
                    self.command = 'dnf5 leaves'
            elif os.path.isfile(solus):
                if operation[1] == l_dict['store']['update'][l_use]:
                    self.command = 'pkexec eopkg -y upgrade'
                elif operation[1] == l_dict['store']['clean'][l_use]:
                    self.command = 'pkexec eopkg -y dc'
                elif operation[1] == l_dict['store']['remove'][l_use]:
                    self.command = 'pkexec eopkg -y rmf'
                elif operation[1] == l_dict['store']['history'][l_use]:
                    self.command = 'eopkg history'
                elif operation[1] == l_dict['store']['list'][l_use]:
                    self.command = 'eopkg list-installed'
            elif os.path.isfile(arch):
                if operation[1] == l_dict['store']['update'][l_use]:
                    self.command = 'pkexec pacman --noconfirm -Syu'
                elif operation[1] == l_dict['store']['clean'][l_use]:
                    self.command = 'pkexec pacman --noconfirm -Scc'
                elif operation[1] == l_dict['store']['remove'][l_use]:
                    self.command = 'pacman --noconfirm -Qdtq | pacman --noconfirm -Rs -'
                elif operation[1] == l_dict['store']['fix'][l_use]:
                    self.command = 'pacman --noconfirm -Dk'
                elif operation[1] == l_dict['store']['history'][l_use]:
                    self.command = 'cat /var/log/pacman.log'
                elif operation[1] == l_dict['store']['list'][l_use]:
                    self.command = 'pacman -Q'
        self.labels[f"page{use}"].configure(text=f"{operation[0]}: {operation[1]}")
        self.useds[f"page{use}"] = True
        self.tabview.set(use)
        with subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.out)
                self.outputs[f"page{use}"].configure(state="disabled")
        self.closes[f"page{use}"].configure(state="normal")
        delete_operation(f"{operation[0]}: {operation[1]}", time)
        if self.run_command.returncode == 0:
            mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['failed'][l_use])
    def go(self, wanted: str):
        if self.useds["page1"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 1, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page2"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 2, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page3"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 3, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page4"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 4, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page5"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 5, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page6"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 6, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page7"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 7, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page8"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 8, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page9"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 9, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page10"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 10, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page11"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 11, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page12"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 12, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page13"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 13, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        elif self.useds["page14"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, 14, str(time.strftime("%H:%M:%S", time.localtime()))), daemon=False)
            self.thread.start()
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['all-slots-are-full'][l_use])
            return
    def close(self, caller: str):
        self.labels[f"page{caller}"].configure(text=f"{l_dict['operations']['process'][l_use]} {caller}")
        self.outputs[f"page{caller}"].configure(state="normal")
        self.outputs[f"page{caller}"].delete("0.0", 'end')
        self.outputs[f"page{caller}"].configure(state="disabled")
        self.closes[f"page{caller}"].configure(state="disabled")
        self.useds[f"page{caller}"] = False
        
class SystemdServices(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25, fg_color="transparent")
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.mainpage = self.tabview.add(l_dict['store']['home'][l_use])
        self.mainpage.grid_columnconfigure(0, weight=1)
        self.mainpage.grid_rowconfigure(0, weight=1)
        self.mainbar = ui.CTkScrollableFrame(self.mainpage, fg_color="transparent")
        self.mainbar.grid(row=0, column=0, sticky="nsew", padx=(0, 7.5))
        self.mainbar.grid_columnconfigure((0, 1), weight=1)
        self.sidebar = ui.CTkFrame(self.mainpage, fg_color="transparent")
        self.sidebar.grid(row=0, column=1, sticky="nsew", padx=(7.5, 0))
        self.sidebar.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.running_label = ui.CTkLabel(self.mainbar, text=l_dict['store']['running'][l_use], corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.active_label = ui.CTkLabel(self.mainbar, text=l_dict['store']['active'][l_use], corner_radius=25, fg_color=["#b9b9b9", "#1f1f1f"], font=ui.CTkFont(size=15, weight="bold"))
        self.entry = ui.CTkEntry(self.sidebar, placeholder_text=l_dict['store']['service-name'][l_use])
        self.button1 = ui.CTkButton(self.sidebar, text=l_dict['store']['status'][l_use], command=lambda:self.go(["", "status"]))
        self.button2 = ui.CTkButton(self.sidebar, text=l_dict['store']['enable'][l_use], command=lambda:self.go(["pkexec", "enable"]))
        self.button3 = ui.CTkButton(self.sidebar, text=l_dict['store']['disable'][l_use], command=lambda:self.go(["pkexec", "disable"]))
        self.button4 = ui.CTkButton(self.sidebar, text=l_dict['store']['start'][l_use], command=lambda:self.go(["pkexec", "start"]))
        self.button5 = ui.CTkButton(self.sidebar, text=l_dict['store']['stop'][l_use], command=lambda:self.go(["pkexec", "stop"]))
        self.running_number = 0
        self.active_number = 0
        with subprocess.Popen(r"systemctl list-units --type=service --state=running | awk '/.*\.service/ {print $1}'", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.list_running:
            for running in self.list_running.stdout:
                self.running_number += 1
                ui.CTkButton(self.mainbar, text=running.replace(".service", "").replace("\n", ""), command=lambda running = running: self.insert(running.replace("\n", ""))).grid(row=self.running_number, column=1, sticky="nsew", pady=(0, 10), padx=25)        
        with subprocess.Popen(r"systemctl list-units --type=service --state=active | awk '/.*\.service/ {print $1}'", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.list_active:
            for active in self.list_active.stdout:
                self.active_number += 1
                ui.CTkButton(self.mainbar, text=active.replace(".service", "").replace("\n", ""), command=lambda active = active: self.insert(active.replace("\n", ""))).grid(row=self.active_number, column=0, sticky="nsew", pady=(0, 10), padx=25)
        self.pages = {}
        self.labels = {}
        self.outputs = {}
        self.closes = {}
        self.useds = {}
        for i in range(1, 15):
            self.pages[f"page{i}"] = self.tabview.add(i)
            self.pages[f"page{i}"].grid_rowconfigure(1, weight=1)
            self.pages[f"page{i}"].grid_columnconfigure(0, weight=1)
            self.labels[f"page{i}"] = ui.CTkLabel(self.pages[f"page{i}"], text=f"{l_dict['operations']['process'][l_use]} {i}")
            self.outputs[f"page{i}"] = ui.CTkTextbox(self.pages[f"page{i}"], state="disabled")
            self.closes[f"page{i}"] = ui.CTkButton(self.pages[f"page{i}"], text=l_dict['store']['close'][l_use], command=lambda i = i: self.close(i), state="disabled")
            self.labels[f"page{i}"].grid(row=0, column=0, sticky="nsew")
            self.outputs[f"page{i}"].grid(row=1, column=0, sticky="nsew")
            self.closes[f"page{i}"].grid(row=2, column=0, sticky="nsew", pady=(10, 0))
            self.useds[f"page{i}"] = False
        self.running_label.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=15)
        self.active_label.grid(row=0, column=1, sticky="nsew", pady=(0, 10), padx=15)
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5))
        self.button5.grid(row=5, column=0, sticky="nsew")
    def insert(self, name):
        self.entry.delete(0, "end")
        self.entry.insert(0, name)  
    def do(self, operation, target, use):
        self.labels[f"page{use}"].configure(text=f"{l_dict['store'][operation[1]][l_use]}: {target}")
        self.useds[f"page{use}"] = True
        self.tabview.set(use)
        with subprocess.Popen(f"{operation[0]} SYSTEMD_COLORS=0 systemctl {operation[1]} {target}", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.out)
                self.outputs[f"page{use}"].configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.outputs[f"page{use}"].configure(state="normal")
                self.outputs[f"page{use}"].insert("end", self.err)
                self.outputs[f"page{use}"].configure(state="disabled")
        self.closes[f"page{use}"].configure(state="normal")
        if self.run_command.returncode != 0:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['failed'][l_use])        
    def go(self, wanted):
        if self.useds["page1"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 1), daemon=False)
            self.thread.start()
        elif self.useds["page2"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 2), daemon=False)
            self.thread.start()
        elif self.useds["page3"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 3), daemon=False)
            self.thread.start()
        elif self.useds["page4"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 4), daemon=False)
            self.thread.start()
        elif self.useds["page5"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 5), daemon=False)
            self.thread.start()
        elif self.useds["page6"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 6), daemon=False)
            self.thread.start()
        elif self.useds["page7"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 7), daemon=False)
            self.thread.start()
        elif self.useds["page8"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 8), daemon=False)
            self.thread.start()
        elif self.useds["page9"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 9), daemon=False)
            self.thread.start()
        elif self.useds["page10"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 10), daemon=False)
            self.thread.start()
        elif self.useds["page11"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 11), daemon=False)
            self.thread.start()
        elif self.useds["page12"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 12), daemon=False)
            self.thread.start()
        elif self.useds["page13"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 13), daemon=False)
            self.thread.start()
        elif self.useds["page14"] == False:
            self.thread = threading.Thread(target=lambda:self.do(wanted, self.entry.get(), 14), daemon=False)
            self.thread.start()
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['store']['all-slots-are-full'][l_use])
            return
    def close(self, caller: str):
        self.labels[f"page{caller}"].configure(text=f"{l_dict['operations']['process'][l_use]} {caller}")
        self.outputs[f"page{caller}"].configure(state="normal")
        self.outputs[f"page{caller}"].delete("0.0", 'end')
        self.outputs[f"page{caller}"].configure(state="disabled")
        self.closes[f"page{caller}"].configure(state="disabled")
        self.useds[f"page{caller}"] = False

class Store(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.packages_tab = self.tabview.add(l_dict['store']['packages'][l_use])
        self.packages_tab.grid_columnconfigure(0, weight=1)
        self.packages_tab.grid_rowconfigure(0, weight=1)
        self.deswmscs_tab = self.tabview.add(l_dict['store']['deswmscs'][l_use])
        self.deswmscs_tab.grid_columnconfigure(0, weight=1)
        self.deswmscs_tab.grid_rowconfigure(0, weight=1)
        self.scripts_tab = self.tabview.add(l_dict['store']['scripts'][l_use])
        self.scripts_tab.grid_columnconfigure(0, weight=1)
        self.scripts_tab.grid_rowconfigure(0, weight=1)
        self.systemdservices_tab = self.tabview.add(f"Systemd\n{l_dict['store']['services'][l_use]}{l_dict['globals']['i'][l_use]}")
        self.systemdservices_tab.grid_columnconfigure(0, weight=1)
        self.systemdservices_tab.grid_rowconfigure(0, weight=1)
        self.packages_thread = threading.Thread(target=self.packages, daemon=True)
        self.packages_thread.start()
        self.deswmcs_thread = threading.Thread(target=self.deswmcs, daemon=True)
        self.deswmcs_thread.start()
        self.scripts_thread = threading.Thread(target=self.scripts, daemon=True)
        self.scripts_thread.start()
        self.systemdservices_thread = threading.Thread(target=self.systemdservices, daemon=True)
        self.systemdservices_thread.start()
    def packages(self):
        self.packages_frame = Packages(self.packages_tab, fg_color="transparent")
        self.packages_frame.grid(row=0, column=0, sticky="nsew")
    def deswmcs(self):
        self.deswmscs_frame = DEsWMsCs(self.deswmscs_tab, fg_color="transparent")
        self.deswmscs_frame.grid(row=0, column=0, sticky="nsew")
    def scripts(self):
        self.scripts_frame = Scripts(self.scripts_tab, fg_color="transparent")
        self.scripts_frame.grid(row=0, column=0, sticky="nsew")
    def systemdservices(self):
        self.systemdservices_frame = SystemdServices(self.systemdservices_tab, fg_color="transparent")
        self.systemdservices_frame.grid(row=0, column=0, sticky="nsew")

class BashrcZshrc(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, fg_color="transparent", corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.use = ui.StringVar(value="bashrc")
        self.switch = ui.CTkSwitch(self, text="Bashrc / Zshrc", offvalue="bashrc", onvalue="zshrc", command=self.set, variable=self.use)
        self.switch.grid(row=1, column=0, sticky="ns", padx=0, pady=0)
        self.options = self.tabview.add(l_dict['tools']['options'][l_use])
        self.file = self.tabview.add(l_dict['tools']['file'][l_use])
        self.options.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.options.grid_columnconfigure((0, 1, 2), weight=1)
        self.file.grid_columnconfigure(0, weight=1)
        self.file.grid_rowconfigure(0, weight=1)
        self.label1 = ui.CTkLabel(self.options, text=l_dict['tools']['add-without'][l_use])
        self.button1 = ui.CTkButton(self.options, text=l_dict['tools']['welcome'][l_use], command=lambda:self.add(f'echo "{l_dict['tools']['hello'][l_use]} {username}!"'))
        self.button2 = ui.CTkButton(self.options, text=l_dict['tools']['system'][l_use], command=lambda:self.add('neofetch'))
        self.button3 = ui.CTkButton(self.options, text=l_dict['tools']['memory'][l_use], command=lambda:self.add('free -h'))
        self.label2 = ui.CTkLabel(self.options, text=l_dict['tools']['add-with'][l_use])
        self.button4 = ui.CTkButton(self.options, text=l_dict['tools']['welcome'][l_use], command=lambda:self.add(f'echo "{l_dict['tools']['hello'][l_use]} {username}!" | lolcat'))
        self.button5 = ui.CTkButton(self.options, text=l_dict['tools']['system'][l_use], command=lambda:self.add('neofetch | lolcat'))
        self.button6 = ui.CTkButton(self.options, text=l_dict['tools']['memory'][l_use], command=lambda:self.add('free -h | lolcat'))
        self.label3 = ui.CTkLabel(self.options, text=l_dict['tools']['undo'][l_use])
        self.button7 = ui.CTkButton(self.options, text=l_dict['tools']['last'][l_use], command=lambda:self.undo('latest'))
        self.button8 = ui.CTkButton(self.options, text=l_dict['tools']['session'][l_use], command=lambda:self.undo('session'))
        self.button9 = ui.CTkButton(self.options, text=l_dict['tools']['all'][l_use], command=lambda:self.undo('first'))
        self.textbox = ui.CTkTextbox(self.file)
        self.button = ui.CTkButton(self.file, text=l_dict['tools']['save'][l_use], command=self.save)
        with open(f"/home/{username}/.bashrc", "r") as self.bashrc:
            self.content = self.bashrc.read()
        self.textbox.insert("0.0", self.content)
        self.label1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.button1.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.button2.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.button3.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
        self.label2.grid(row=1, column=1, sticky="nsew", pady=5, padx=5)
        self.button4.grid(row=2, column=1, sticky="nsew", pady=5, padx=5)
        self.button5.grid(row=3, column=1, sticky="nsew", pady=5, padx=5)
        self.button6.grid(row=4, column=1, sticky="nsew", pady=5, padx=5)
        self.label3.grid(row=1, column=2, sticky="nsew", pady=5, padx=5)
        self.button7.grid(row=2, column=2, sticky="nsew", pady=5, padx=5)
        self.button8.grid(row=3, column=2, sticky="nsew", pady=5, padx=5)
        self.button9.grid(row=4, column=2, sticky="nsew", pady=5, padx=5)
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.button.grid(row=1, column=0, sticky="nsew", pady=2.5)
    def set(self):
        if self.use.get() == "bashrc" and not os.path.isfile("/usr/bin/bash") and not os.path.isfile("/bin/bash"):
            install_app("Bash", "bash")
        elif self.use.get() == "zshrc" and not os.path.isfile("/usr/bin/zsh") and not os.path.isfile("/bin/zsh"):
            install_app("Zsh", "zsh")
        with open(f"/home/{username}/.{self.use.get()}", "r") as self.file:
            self.content = self.file.read()
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", self.content)
    def save(self):
        os.system(f"cp /home/{username}/.{self.use.get()} {local}backups/{self.use.get()}/latest")
        with open(f"/home/{username}/.{self.use.get()}", "w+") as self.file:
            self.file.write(self.textbox.get("0.0", 'end'))
        with open(f"/home/{username}/.{self.use.get()}") as self.file:
            self.output = self.file.read()
        if self.output == self.textbox.get("0.0", 'end'):
            mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])
        else:
            mb.showerror(l_dict['globals']['error'][l_use], l_dict['globals']['failed'][l_use])
    def add(self, goal):
        if "lolcat" in goal and not os.path.isfile("/usr/bin/lolcat") and not os.path.isfile("/bin/lolcat"):
            install_app("Lolcat", "lolcat")
            if ask_a == False:
                return
        if "neofetch" in goal and not os.path.isfile("/usr/bin/neofetch") and not os.path.isfile("/bin/neofetch"):
            install_app("Neofetch", "neofetch")
            if ask_a == False:
                return
        os.system(f"cp /home/{username}/.{self.use.get()} {local}backups/{self.use.get()}/latest")
        os.system(f"echo '{goal}' >> /home/{username}/.{self.use.get()}")
        mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])
    def undo(self, goal):
        os.system(f"cp {local}backups/{self.use.get()}/{goal} /home/{username}/.{self.use.get()}")
        mb.showinfo(l_dict['globals']["information"][l_use], l_dict['globals']['completed'][l_use])

class ComputerName(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)
        with open("/etc/hostname", "r") as file:
            self.computername = file.read()
        self.label = ui.CTkLabel(self, text=f"{l_dict['tools']['current'][l_use]}{self.computername}")
        self.entry = ui.CTkEntry(self, placeholder_text=l_dict['tools']['new'][l_use])
        self.button = ui.CTkButton(self, text=l_dict['tools']['apply'][l_use], command=self.apply)
        self.label.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.button.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
    def apply(self):
        subprocess.Popen("pkexec grelintb root pcrename "+self.entry.get(), shell=True)
        restart_system()

class Distros(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="transparent")
        self.label = ui.CTkLabel(self, text=l_dict['tools']['source'][l_use])
        self.label.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.distros = [["Fedora", l_dict['tools']['fedora'][l_use], "https://fedoraproject.org/"], ["Pop!_OS", l_dict['tools']['pop'][l_use], "https://pop.system76.com/"], ["openSUSE", l_dict['tools']['opensuse'][l_use], "https://www.opensuse.org/"], ["Arch", l_dict['tools']['arch'][l_use], "https://archlinux.org/"], ["Gentoo", l_dict['tools']['gentoo'][l_use], "https://www.gentoo.org/"], ["Mint", l_dict['tools']['mint'][l_use], "https://linuxmint.com/"], ["MX", l_dict['tools']['mx'][l_use], "https://mxlinux.org/"], ["Debian", l_dict['tools']['debian'][l_use], "https://debian.org/"], ["Ubuntu", l_dict['tools']['ubuntu'][l_use], "https://ubuntu.com/"]]
        for self.name, self.content, self.website in self.distros:
            self.tabview.add(self.name)
            self.tabview.tab(self.name).grid_columnconfigure(0, weight=1)
            self.tabview.tab(self.name).rowconfigure(0, weight=1)
            ui.CTkLabel(self.tabview.tab(self.name), text=self.content).grid(row=0, column=0, sticky="nsew")
            ui.CTkButton(self.tabview.tab(self.name), text=l_dict['tools']['open'][l_use], command=lambda website = self.website:subprocess.Popen(f"xdg-open {website}", shell=True)).grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        # if os.path.isfile(en):
        #     self.text1 = ui.CTkLabel(self.distro1, text="MX Linux is a cooperative venture between the antiX and MX Linux communities."+
        #         "\nDesigned to combine high stability and robust performance."+
        #         "\nMX's graphical tools and tools from antiX make it easy to use.")
        #     self.button1 = ui.CTkButton(self.distro1, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))
        #     self.text2 = ui.CTkLabel(self.distro2, text="Linux Mint is designed to work out of the box."+
        #         "\nIt comes fully equipped with the applications most people need."+
        #         "\n\nNote from GrelinTB developer: I really recommend it for first time Linux users.")
        #     self.button2 = ui.CTkButton(self.distro2, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
        #     self.text3 = ui.CTkLabel(self.distro3, text="EndeavorOS doesn't bother installing Arch manually."+
        #         "\nwithout the hassle of installing it manually for both x86_64 and ARM systems."+
        #         "\nAfter installation, you’re provided with good environment and guide.")
        #     self.button3 = ui.CTkButton(self.distro3, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
        #     self.text4 = ui.CTkLabel(self.distro4, text="Debian, although very old, is still supported."+
        #         "\nToday, most of distributions are based on it."+
        #         "\nDebian offers a very stable experience, but this makes it less up-to-date.")
        #     self.button4 = ui.CTkButton(self.distro4, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
        #     self.text5 = ui.CTkLabel(self.distro5, text="Manjaro is a distribution based on Arch Linux. It is aimed at the end user."+
        #         "\n\nNote from GrelinTB developer: For Arch base, I suggest you look for other alternatives.")
        #     self.button5 = ui.CTkButton(self.distro5, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
        #     self.text6 = ui.CTkLabel(self.distro6, text="Ubuntu targets many audiences. There are many variants."+
        #         "\n\nNote from GrelinTB developer: In Ubuntu, telemetry is turned on by default, but it can be turned off."+
        #         "\nAt worst, it forces you to use Snap. Personally, I prefer Flatpak over Snap."+
        #         "\nPersonally, instead of Ubuntu, I recommend Linux Mint with Pop!_OS.")
        #     self.button6 = ui.CTkButton(self.distro6, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
        #     self.text7 = ui.CTkLabel(self.distro7, text="Fedora is powered by Red Hat. Fedora is the test environment for RHEL."+
        #         "\nFedora has many spins for different desktop environments."+
        #         "\n\nNote from GrelinTB developer: I think Fedora is the middle ground of ease, stability, up-to-date."+
        #         "\nFedora is one of the distributions I recommend and like.")
        #     self.button7 = ui.CTkButton(self.distro7, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
        #     self.text8 = ui.CTkLabel(self.distro8, text="Pop!_OS is an Ubuntu based distribution developed by System76."+
        #         "\nIt offers a separate download option for Nvidia users."+
        #         "\nBy default it uses Systemd-boot instead of GRUB."+
        #         "\nIt currently uses customized GNOME, but its own desktop environment (Cosmic) is being built.")
        #     self.button8 = ui.CTkButton(self.distro8, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
        #     self.text9 = ui.CTkLabel(self.distro9, text="Target audience is users migrating from Windows and Mac."+
        #         "\nIts purpose is ease of use."+
        #         "\n\nNote from GrelinTB developer: I find the Pro version logic absurd."+
        #         "\nBecause I think Zorin OS has no advantages over the others.")
        #     self.button9 = ui.CTkButton(self.distro9, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
        #     self.text10 = ui.CTkLabel(self.distro10, text="The only distribution here that GrelinTB does not support."+
        #         "\nIt targets many audiences and has its own tools. Its tools are often praised."+
        #         "\nTumbleweed (more up-to-date), Leap (more stable).")
        #     self.button10 = ui.CTkButton(self.distro10, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True))
        # elif os.path.isfile(tr):
        #     self.text1 = ui.CTkLabel(self.distro1, text="MX Linux, antiX ve MX Linux toplulukları arasında bir işbirliği girişimidir."+
        #         "\nYüksek kararlılık ve sağlam performansla birleştirmek için tasarlanmıştır."+
        #         "\nMX'in grafiksel araçları ve antiX'in araçları kullanımı kolaylaştırır.")
        #     self.button1 = ui.CTkButton(self.distro1, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))
        #     self.text2 = ui.CTkLabel(self.distro2, text="Linux Mint, kutudan çıktığı gibi çalışmak üzere tasarlanmıştır."+
        #         "\nÇoğu insanın ihtiyaç duyduğu uygulamalarla tam donanımlı olarak gelir."+
        #         "\n\nGrelinTB geliştiricisinin notu: İlk kez Linux kullanacaklar için gerçekten öneririm.")
        #     self.button2 = ui.CTkButton(self.distro2, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
        #     self.text3 = ui.CTkLabel(self.distro3, text="EndeavourOS, Arch'ı manuel olarak yükleme zahmetine sokmaz."+
        #         "\nKendisi Arch deneyimi sağlayan Arch tabanlı bir dağıtımdır."+
        #         "\nKurulumdan sonra, size iyi bir ortam ve rehber sağlanır.")
        #     self.button3 = ui.CTkButton(self.distro3, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
        #     self.text4 = ui.CTkLabel(self.distro4, text="Debian, çok eski olmasına rağmen halen desteklenmektedir."+
        #         "\nBugün çoğu dağıtım onu taban alır."+
        #         "\nDebian çok stabil bir deneyim sunar fakat bu güncelliği azaltır.")
        #     self.button4 = ui.CTkButton(self.distro4, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
        #     self.text5 = ui.CTkLabel(self.distro5, text="Manjaro, Arch Linux tabanlı bir dağıtımdır. Son kullanıcıyı hedef alır."+
        #         "\n\nGrelinTB geliştiricisinin notu: Arch tabanı için başka alternatiflere yönelmenizi öneririm.")
        #     self.button5 = ui.CTkButton(self.distro5, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
        #     self.text6 = ui.CTkLabel(self.distro6, text="Ubuntu birçok kitleyi hedefler. Birçok türevi vardır."+
        #         "\n\nGrelinTB geliştiricisinin notu: Ubuntu'da varsayılan olarak telemetriler açık gelir ama kapıtabilir."+
        #         "\nEn kötüsü ise sizi Snap kullanmaya zorlar. Şahsen ben Snap yerine Flatpak tercih ederim."+
        #         "\nŞahsen Ubuntu yerine, Pop!_OS ile Linux Mint öneririm.")
        #     self.button6 = ui.CTkButton(self.distro6, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
        #     self.text7 = ui.CTkLabel(self.distro7, text="Fedora, Red Hat tarafından desteklenmektedir. Fedora, RHEL için test ortamıdır."+
        #         "\nFedora'nın farklı masaüstü ortamları için birçok döndürmesi vardır."+
        #         "\n\nGrelinTB geliştiricisinin notu: Bence Fedora; kolaylığın, stabilliğin, güncelliğin tam ortasıdır."+
        #         "\nFedora, önerdiğim ve sevdiğim dağıtımlardandır.")
        #     self.button7 = ui.CTkButton(self.distro7, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
        #     self.text8 = ui.CTkLabel(self.distro8, text="Pop!_OS, System76 tarafından geliştirilen Ubuntu tabanlı bir dağıtımdır."+
        #         "\nNvidia kullanıcıları için ayrı bir indirme seçeneği sunar."+
        #         "\nVarsayılan olarak GRUB yerine Systemd-boot kullanır."+
        #         "\nŞu anda özelleştirilmiş GNOME kullanmakta fakat kendi masaüstü ortamı (Cosmic) yapılmakta.")
        #     self.button8 = ui.CTkButton(self.distro8, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
        #     self.text9 = ui.CTkLabel(self.distro9, text="Hedef kitlesi Windows'tan ve Mac'ten geçen kullanıcılardır."+
        #         "\nAmacı ise kullanım kolaylığıdır."
        #         "\n\nGrelinTB geliştiricisinin notu: Ben Pro sürüm mantığını saçma buluyorum."+
        #         "\nÇünkü bence Zorin OS'un diğerlerine göre artısı yok.")
        #     self.button9 = ui.CTkButton(self.distro9, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
        #     self.text10 = ui.CTkLabel(self.distro10, text="Burada GrelinTB'nin desteklemediği tek dağıtım."+
        #         "\nBirçok kitleyi hedef alır ve kendi araçları vardır. Araçları çok sık övülmektedir."+
        #         "\nTumbleweed (daha güncel), Leap (daha stabil) olarak ikiye ayrılır.")
        #     self.button10 = ui.CTkButton(self.distro10, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True))

class Calcer(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.history_label = ui.CTkLabel(self, text=l_dict['tools']['previous'][l_use], height=15, font=ui.CTkFont(size=13, weight="bold"))
        self.history_button = ui.CTkButton(self, text=l_dict['tools']['delete'][l_use], command=self.delete_history)
        self.entry = ui.CTkEntry(self)
        self.history_text = ui.CTkTextbox(self, fg_color="transparent")
        if os.path.isfile(f"{local}calc-history"):
            with open(f"{local}calc-history", "r") as self.file:
                self.output = self.file.read()
            self.history_text.insert("0.0", self.output)
        self.history_text.configure(state="disabled")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=2.5, padx=2.5)
        self.button1 = ui.CTkButton(self, text="0", command=lambda:self.entry.insert("end", "0")).grid(row=1, column=0, sticky="nsew", pady=2.5, padx=2.5)
        self.button2 = ui.CTkButton(self, text="1", command=lambda:self.entry.insert("end", "1")).grid(row=1, column=1, sticky="nsew", pady=2.5, padx=2.5)
        self.button3 = ui.CTkButton(self, text="2", command=lambda:self.entry.insert("end", "2")).grid(row=1, column=2, sticky="nsew", pady=2.5, padx=2.5)
        self.button4 = ui.CTkButton(self, text="3", command=lambda:self.entry.insert("end", "3")).grid(row=1, column=3, sticky="nsew", pady=2.5, padx=2.5)
        self.button5 = ui.CTkButton(self, text="4", command=lambda:self.entry.insert("end", "4")).grid(row=2, column=0, sticky="nsew", pady=2.5, padx=2.5)
        self.button6 = ui.CTkButton(self, text="5", command=lambda:self.entry.insert("end", "5")).grid(row=2, column=1, sticky="nsew", pady=2.5, padx=2.5)
        self.button7 = ui.CTkButton(self, text="6", command=lambda:self.entry.insert("end", "6")).grid(row=2, column=2, sticky="nsew", pady=2.5, padx=2.5)
        self.button8 = ui.CTkButton(self, text="7", command=lambda:self.entry.insert("end", "7")).grid(row=2, column=3, sticky="nsew", pady=2.5, padx=2.5)
        self.button9 = ui.CTkButton(self, text="8", command=lambda:self.entry.insert("end", "8")).grid(row=3, column=0, sticky="nsew", pady=2.5, padx=2.5)
        self.button10 = ui.CTkButton(self, text="9", command=lambda:self.entry.insert("end", "9")).grid(row=3, column=1, sticky="nsew", pady=2.5, padx=2.5)
        self.button11 = ui.CTkButton(self, text="=", command=self.calc).grid(row=3, column=2, sticky="nsew", pady=2.5, padx=2.5)
        self.button12 = ui.CTkButton(self, text=l_dict['tools']['clear'][l_use], command=lambda:self.entry.delete(0, "end")).grid(row=3, column=3, sticky="nsew", pady=2.5, padx=2.5)
        self.button13 = ui.CTkButton(self, text="+", command=lambda:self.entry.insert("end", "+")).grid(row=4, column=0, sticky="nsew", pady=2.5, padx=2.5)
        self.button14 = ui.CTkButton(self, text="-", command=lambda:self.entry.insert("end", "-")).grid(row=4, column=1, sticky="nsew", pady=2.5, padx=2.5)
        self.button15 = ui.CTkButton(self, text="*", command=lambda:self.entry.insert("end", "*")).grid(row=4, column=2, sticky="nsew", pady=2.5, padx=2.5)
        self.button16 = ui.CTkButton(self, text="/", command=lambda:self.entry.insert("end", "/")).grid(row=4, column=3, sticky="nsew", pady=2.5, padx=2.5)
        self.history_label.grid(row=0, column=4, sticky="nsew", pady=2.5, padx=2.5)
        self.history_text.grid(row=1, column=4, rowspan=3, sticky="nsew", pady=2.5, padx=2.5)
        self.history_button.grid(row=4, column=4, sticky="nsew", pady=2.5, padx=2.5)
    def calc(self):
        try:
            self.process = str(self.entry.get())
            self.result = str(eval(self.entry.get()))
            self.entry.delete(0, "end")
            self.entry.insert(0, self.result)
            with open(f"{local}calc-history", "a+") as self.file:
                self.file.write(self.process+"="+self.result+"\n")
            with open(f"{local}calc-history", "r") as self.file:
                self.output = self.file.read()
            self.history_text.configure(state="normal")
            self.history_text.delete("0.0", "end")
            self.history_text.insert("0.0", self.output)
            self.history_text.configure(state="disabled")
        except Exception as error:
            mb.showerror(l_dict['globals']['error'][l_use], f"{l_dict['tools']['error'][l_use]}{error}")
    def delete_history(self):
        subprocess.Popen(f"rm {local}calc-history", shell=True)
        self.history_text.configure(state="normal")
        self.history_text.delete("0.0", "end")
        self.history_text.configure(state="disabled")

class Tools(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.bashrczshrc_tab = self.tabview.add(l_dict['tools']['bashrczshrc'][l_use])
        self.bashrczshrc_tab.grid_columnconfigure(0, weight=1)
        self.bashrczshrc_tab.grid_rowconfigure(0, weight=1)
        self.computername_tab = self.tabview.add(l_dict['tools']['computername'][l_use])
        self.computername_tab.grid_columnconfigure(0, weight=1)
        self.computername_tab.grid_rowconfigure(0, weight=1)
        self.distros_tab = self.tabview.add(l_dict['tools']['distros'][l_use])
        self.distros_tab.grid_columnconfigure(0, weight=1)
        self.distros_tab.grid_rowconfigure(0, weight=1)
        self.calcer_tab = self.tabview.add(l_dict['tools']['calcer'][l_use])
        self.calcer_tab.grid_columnconfigure(0, weight=1)
        self.calcer_tab.grid_rowconfigure(0, weight=1)
        self.bashrczshrc_thread = threading.Thread(target=self.bashrczshrc, daemon=True)
        self.bashrczshrc_thread.start()
        self.computername_thread = threading.Thread(target=self.computername, daemon=True)
        self.computername_thread.start()
        self.distros_thread = threading.Thread(target=self.distros, daemon=True)
        self.distros_thread.start()
        self.calcer_thread = threading.Thread(target=self.calcer, daemon=True)
        self.calcer_thread.start()
    def bashrczshrc(self):
        self.bashrczshrc_frame=BashrcZshrc(self.bashrczshrc_tab, fg_color="transparent")
        self.bashrczshrc_frame.grid(row=0, column=0, sticky="nsew")
    def computername(self):
        self.computername_frame=ComputerName(self.computername_tab, fg_color="transparent")
        self.computername_frame.grid(row=0, column=0, sticky="nsew")
    def distros(self):
        self.distros_frame=Distros(self.distros_tab)
        self.distros_frame.grid(row=0, column=0, sticky="nsew")
    def calcer(self):
        self.calcer_frame =Calcer(self.calcer_tab)
        self.calcer_frame.grid(row=0, column=0, sticky="nsew")

class Root(ui.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("GrelinTB")
        self.geometry("960x540")
        self.minsize(960, 540)
        self.icon = pi(file = '/usr/local/bin/grelintb/icon.png')
        self.wm_iconphoto(True, self.icon)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.sidebar_frame = Sidebar(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.tabview = ui.CTkTabview(self, corner_radius=50)
        self.tabview.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        if dt.date.today().strftime("%d/%m") == "04/12":
            self.title(f"GrelinTB - {str(dt.datetime.now().strftime('%d/%m/%Y'))}: {l_dict['root']['04-12-2008'][l_use]}")
        if dt.datetime.now().weekday() == 0:
            self.check_update_thread = threading.Thread(target=lambda:Sidebar.check_update(self, "startup"), daemon=True)
            self.check_update_thread.start()
        self.startup_tab = self.tabview.add(l_dict['root']['startup'][l_use])
        self.startup_tab.grid_columnconfigure(0, weight=1)
        self.startup_tab.grid_rowconfigure(0, weight=1)
        self.nad_tab = self.tabview.add(l_dict['root']['nad'][l_use])
        self.nad_tab.grid_columnconfigure(0, weight=1)
        self.nad_tab.grid_rowconfigure(0, weight=1)
        self.store_tab = self.tabview.add(l_dict['root']['store'][l_use])
        self.store_tab.grid_columnconfigure(0, weight=1)
        self.store_tab.grid_rowconfigure(0, weight=1)
        self.tools_tab = self.tabview.add(l_dict['root']['tools'][l_use])
        self.tools_tab.grid_columnconfigure(0, weight=1)
        self.tools_tab.grid_rowconfigure(0, weight=1)
        self.startup_thread = threading.Thread(target=self.startup, daemon=True)
        self.startup_thread.start()
        self.nad_thread = threading.Thread(target=self.nad, daemon=True)
        self.nad_thread.start()
        self.store_thread = threading.Thread(target=self.store, daemon=True)
        self.store_thread.start()
        self.tools_thread = threading.Thread(target=self.tools, daemon=True)
        self.tools_thread.start()
    def startup(self):
        self.startup_frame=Startup(self.startup_tab)
        self.startup_frame.grid(row=0, column=0, sticky="nsew")
    def nad(self):
        self.nad_frame=NotesAndDocuments(self.nad_tab)
        self.nad_frame.grid(row=0, column=0, sticky="nsew")
    def store(self):
        self.store_frame=Store(self.store_tab)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
    def tools(self):
        self.tools_frame=Tools(self.tools_tab)
        self.tools_frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    if "-h" in sys.argv[1:] or '--help' in sys.argv[1:]:
        print(f"{l_dict['cli']['copyright'][l_use]}\n{l_dict['cli']['welcome'][l_use]}{username}!\n{l_dict['cli']['information'][l_use]}\n{l_dict['cli']['version-info'][l_use]}{version_current}\n{l_dict['cli']['developer-info'][l_use]}\n{l_dict['cli']['license-info'][l_use]}\n{l_dict['cli']['credit-info'][l_use]}\n{l_dict['cli']['parameters'][l_use]}\n{l_dict['cli']['help'][l_use]}\n{l_dict['cli']['info'][l_use]}\n{l_dict['cli']['changelog'][l_use]}\n{l_dict['cli']['developer'][l_use]}\n{l_dict['cli']['license'][l_use]}\n{l_dict['cli']['credit'][l_use]}\n{l_dict['cli']['update'][l_use]}\n{l_dict['cli']['reset'][l_use]}\n{l_dict['cli']['uninstall'][l_use]}\n{l_dict['cli']['none'][l_use]}")
        sys.exit(0)
    elif "-i" in sys.argv[1:] or "--info" in sys.argv[1:]:
        subprocess.Popen("xdg-open https://mukonqi.github.io/grelintb/index.html", shell=True)
        sys.exit(0)
    elif '-ch' in sys.argv[1:] or '--changelog' in sys.argv[1:]:
        with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as cl_major_file:
            cl_major_text = cl_major_file.read()
        with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as cl_minor_file:
            cl_minor_text = cl_minor_file.read()
        print(f" | {l_dict['changelog']['major'][l_use]}{version_current}\n{cl_major_text}\n\n | {l_dict['changelog']['minor'][l_use]}{version_current}\n{cl_minor_text}")
        sys.exit(0)
    elif '-dev' in sys.argv[1:] or '--developer' in sys.argv[1:]:
        subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True)
        sys.exit(0)
    elif '-l' in sys.argv[1:] or "--license" in sys.argv[1:]:
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as l_file:
            l_text = l_file.read()
        print(l_text)
        sys.exit(0)
    elif '-c' in sys.argv[1:] or '--credit' in sys.argv[1:]:
        subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048")
        sys.exit(0)
    elif 'up' in sys.argv[1:] or 'update' in sys.argv[1:]:
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            print(f" | {l_dict['changelog']['major'][l_use]}{version_current}\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/major-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n\n | {l_dict['changelog']['minor'][l_use]}{version_current}\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/minor-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}")
            question = input(l_dict['cli']['want'][l_use])
            if question.lower() == "y" or question.lower() == "e":
                os.system("pkexec /usr/local/bin/grelintb/update.sh")          
        else:
            print(l_dict['changelog']['up-to-date'][l_use])
        sys.exit(0)
    elif 'rs' in sys.argv[1:] or 'reset' in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/reset.sh")
        os.system(f"rm -rf /home/{username}/.config/grelintb")
        sys.exit(0)
    elif 'un' in sys.argv[1:] or 'uninstall' in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        os.system(f"rm -rf /home/{username}/.config/grelintb")
        sys.exit(0)
    else:
        root = Root(className="grelintb")
        root.mainloop()