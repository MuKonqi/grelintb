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

with open("/usr/local/bin/grelintb/version.txt", "r") as version_file:
    version_current = version_file.readline()

import os

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
solus = "/etc/solus-release"
arch = "/etc/arch-release"

if not os.path.isfile(debian) and not os.path.isfile(fedora) and not os.path.isfile(solus) and not os.path.isfile(arch):
    exit("The distribution you are using is not supported from GrelinTB. Exiting...")

import sys

if "root" in sys.argv[1:]:
    if os.getuid() == 0:
        exit("Root rights are required for this feature.")
    if "pcrename" in sys.argv[2:]:
        with open("/etc/hostname", "w") as pcname:
            pcname.write(str(sys.argv[3]))
    exit()
elif os.getuid() == 0:
    exit("GrelinTB already asks you for root rights when the need arises. Exiting...") 

import locale
import getpass
import random as rd
import threading
import subprocess
import datetime as dt
import socket
import platform
import time
try:
    from tkinter import messagebox as mb
    from tkinter import filedialog as fd
    from tkinter import PhotoImage as pi
except:
    print("Installing Tkinter...")
    if os.path.isfile(debian):
        os.system("pkexec apt install python3-tk -y")
    elif os.path.isfile(fedora):
        os.system("pkexec dnf install python3-tkinter -y")
    elif os.path.isfile(solus):
        os.system("pkexec eopkg install python3-tkinter -y")
    elif os.path.isfile(arch):
        os.system("pkexec pacman -S tk --noconfirm")
if not os.path.isfile("/bin/pip") and not os.path.isfile("/usr/bin/pip"):
    print("Installing Pip...")
    if os.path.isfile(debian):
        os.system("pkexec apt install python3-pip -y")
    elif os.path.isfile(fedora):
        os.system("pkexec dnf install python3-pip -y")
    elif os.path.isfile(solus):
        os.system("pkexec eopkg install pip -y")
    elif os.path.isfile(arch):
        os.system("pkexec pacman -S python-pip --noconfirm")
try:
    import customtkinter as ui
except:
    try:
        print("Installing CustomTkinter...")
        os.system("pip install customtkinter ; grelintb")
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install customtkinter --break-system-packages ; grelintb")
    exit()
try:
    import psutil
except:
    try:
        print("Installing psutil...")
        os.system("pip install psutil ; grelintb")
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install psutil --break-system-packages ; grelintb")
    exit()
try:
    import distro
except:
    try:
        print("Installing distro...")
        os.system("pip install distro ; grelintb")
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install distro --break-system-packages ; grelintb")
    exit()

username = getpass.getuser()
config = "/home/"+username+"/.config/grelintb/"
notes = "/home/"+username+"/Notes/"
en = "/home/"+username+"/.config/grelintb/language/en.txt"
tr = "/home/"+username+"/.config/grelintb/language/tr.txt"
system = "/home/"+username+"/.config/grelintb/theme/system.txt"
light = "/home/"+username+"/.config/grelintb/theme/light.txt"
dark = "/home/"+username+"/.config/grelintb/theme/dark.txt"
dark_blue = "/home/"+username+"/.config/grelintb/color/dark_blue.txt"
blue = "/home/"+username+"/.config/grelintb/color/blue.txt"
green = "/home/"+username+"/.config/grelintb/color/green.txt"
random = "/home/"+username+"/.config/grelintb/color/random.txt"
process_number = 0
current_operations = []

if not os.path.isdir(config):
    os.system("cd /home/"+username+"/.config ; mkdir grelintb")
if not os.path.isdir(config+"language/") or (not os.path.isfile(en) and not os.path.isfile(tr)):
    if locale.getlocale()[0] == "tr_TR":
        os.system("cd "+config+" ; mkdir language ; cd language ; touch tr.txt")
    else:
        os.system("cd "+config+" ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(config+"theme/") or (not os.path.isfile(system) and not os.path.isfile(light) and not os.path.isfile(dark)):
    os.system("cd "+config+" ; mkdir theme ; cd theme ; touch system.txt")
if not os.path.isdir(config+"color/") or (not os.path.isfile(dark_blue) and not os.path.isfile(dark) and not os.path.isfile(green) and not os.path.isfile(random)):
    os.system("cd "+config+" ; mkdir color ; cd color ; touch random.txt")
if not os.path.isdir(notes):
    os.system("cd /home/"+username+" ; mkdir Notes")
if not os.path.isfile(f"/home/{username}/.bashrc"):
    os.system("cd /home/"+username+" ; touch .bashrc")
if not os.path.isfile(f"/home/{username}/.zshrc"):
    os.system("cd /home/"+username+" ; touch .zshrc")
if not os.path.isfile("/home/"+username+"/.bashrc-first-grelintb.bak"):
    os.system("cd /home/"+username+" ; cp .bashrc .bashrc-first-grelintb.bak")
if not os.path.isfile("/home/"+username+"/.zshrc-first-grelintb.bak"):
    os.system("cd /home/"+username+" ; cp .zshrc .zshrc-first-grelintb.bak")

if os.path.isfile(system):
    ui.set_appearance_mode("System")
elif os.path.isfile(light):
    ui.set_appearance_mode("Light")
elif os.path.isfile(dark):
    ui.set_appearance_mode("Dark")
if os.path.isfile(dark_blue):
    ui.set_default_color_theme("dark-blue")
elif os.path.isfile(blue):
    ui.set_default_color_theme("blue")
elif os.path.isfile(green):
    ui.set_default_color_theme("green")
elif os.path.isfile(random):
    ui.set_default_color_theme(rd.choice(["blue", "dark-blue", "green"]))

def update_status():
    if process_number <= 0:
        if os.path.isfile(en):
            status.configure(text="Status: Ready")
        elif os.path.isfile(tr):
            status.configure(text="Durum: Hazır")
    else:
        if os.path.isfile(en):
            status.configure(text="Status: Running")
        elif os.path.isfile(tr):
            status.configure(text="Durum: Çalışıyor")
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
    global ask_r
    if os.path.isfile(en):
        ask_r = mb.askyesno("Warning", "Your system needs to be restarted for the changes to be completed.\nDo you want to reboot immediately?")
    elif os.path.isfile(tr):
        ask_r = mb.askyesno("Uyarı", "Değişikliklerin tamamlanması için sisteminizin yeniden başlatılması gerekiyor.\nHemen yeniden başlatmak ister misiniz?")
    if ask_r == True:
        os.system("pkexec reboot")

def install_app(appname: str, packagename: str):
    global ask_a
    global process_number
    if os.path.isfile(en):
        ask_a = mb.askyesno("Warning", appname+" can't found on your system.\nWe can try installing "+appname+" to your computer.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_a = mb.askyesno("Uyarı", appname+" sisteminizde bulunamadı.\nBiz sisteminize "+appname+" yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
    if ask_a == True:
        time_process = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            add_operation(f"Installing {appname}", time_process)
        elif os.path.isfile(tr):
            add_operation(f"{appname} Kuruluyor", time_process)
        if os.path.isfile(debian):
            cmd = os.system('pkexec apt install '+packagename+' -y')
        elif os.path.isfile(fedora):
            cmd = os.system('pkexec dnf install --nogpgcheck '+packagename+' -y')
        elif os.path.isfile(solus):
            cmd = os.system('pkexec eopkg install '+packagename+' -y')
        elif os.path.isfile(arch):
            cmd = os.system('pkexec pacman -S '+packagename+' --noconfirm')
        if os.path.isfile(en):
            delete_operation(f"Installing {appname}", time_process)
        elif os.path.isfile(tr):
            delete_operation(f"{appname} Kuruluyor", time_process)
    elif ask_a == False:
        if os.path.isfile(en):
            mb.showerror("Error", appname+" installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", appname+" kurulumu ve işlem iptal edildi.")
def install_flatpak():
    global ask_f
    global process_number
    if os.path.isfile(en):
        ask_f = mb.askyesno("Warning", "Flatpak package manager can't found on your system.\nWe can try installing Flatpak package manager to your computer.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_f = mb.askyesno("Uyarı", "Flatpak paket yöneticisi sisteminizde bulunamadı.\nBiz sisteminize Flatpak paket yöneticisi yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
    if ask_f == True:
        time_process = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            add_operation(f"Installing Flatpak", time_process)
        elif os.path.isfile(tr):
            add_operation(f"Flatpak Kuruluyor", time_process)
        if os.path.isfile(fedora):
            cmd1 = os.system('pkexec apt install flatpak -y')
            cmd2 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
            restart_system()
        elif os.path.isfile(fedora):
            cmd1 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
        elif os.path.isfile(solus):
            cmd1 = os.system('pkexec eopkg install flatpak -y')
            cmd2 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
            restart_system()
        elif os.path.isfile(arch):
            cmd1 = os.system('pkexec pacman -S flatpak --noconfirm')
            restart_system()
        if ask_r == False:
            ask_f = False
            if os.path.isfile(en):
                mb.showinfo("Information", "Flatpak package manager installation could not be completed, process cancelled.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme", "Flatpak paket yöneticisi kurulumu tamamlanamadı, işlem iptal edildi.")
        if os.path.isfile(en):
            delete_operation(f"Installing Flatpak", time_process)
        elif os.path.isfile(tr):
            delete_operation(f"Flatpak Kuruluyor", time_process)
    elif ask_f == False:
        if os.path.isfile(en):
            mb.showerror("Error", "Flatpak package manager installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", "Flatpak paket yöneticisi kurulumu ve işlem iptal edildi.")

def update():
    root.destroy()
    os.system("pkexec /usr/local/bin/grelintb/update.sh")
    if os.path.isfile(en):
        mb.showinfo("Successful", "GrelinTB has been updated.")
    elif os.path.isfile(tr):
        mb.showinfo("Başarılı", "GrelinTB güncellendi.")
    os.system("grelintb")
    exit()

def main_successful():
    if os.path.isfile(en):
        mb.showinfo("Information","Process completed.")
    elif os.path.isfile(tr):
        mb.showinfo("Bilgilendirme","İşlem tamamlandı.")

class Sidebar(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global status
        self.grid_rowconfigure((4, 8, 15), weight=1)
        self.text = ui.CTkButton(self, text="GrelinTB", command=lambda:subprocess.Popen("xdg-open https://github.com/mukonqi/grelintb/wiki", shell=True), font=ui.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color=("gray14", "gray84"))
        self.language_menu = ui.CTkOptionMenu(self, values=["English", "Türkçe"], command=self.change_language)
        if os.path.isfile(en):
            self.version_b = ui.CTkButton(self, text=f"Version: {version_current}", command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Developer: Mukonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_and_credits_b = ui.CTkButton(self, text="License and Credits", command=self.license_and_credits, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Update", command=lambda:self.check_update("sidebar"))
            self.reset_b = ui.CTkButton(self, text="Reset", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Uninstall", command=self.uninstall)
            self.color_label = ui.CTkLabel(self, text="Color Theme:", anchor="w")
            self.color_menu = ui.CTkOptionMenu(self, values=["Random", "Dark Blue", "Blue", "Green"], command=self.change_color)
            self.appearance_label = ui.CTkLabel(self, text="Appearance:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Language:", anchor="w")
            status = ui.CTkButton(self, text="Status: Ready", command=self.show_operations, font=ui.CTkFont(size=12, weight="bold"))
            self.language_menu.set("English")
            if os.path.isfile(system):
                self.appearance_menu.set("System")
            elif os.path.isfile(light):
                self.appearance_menu.set("Light")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Dark")
            if os.path.isfile(random):
                self.color_menu.set("Random")
            elif os.path.isfile(dark_blue):
                self.color_menu.set("Dark Blue")
            elif os.path.isfile(blue):
                self.color_menu.set("Blue")
            elif os.path.isfile(green):
                self.color_menu.set("Green")
        elif os.path.isfile(tr):
            self.version_b = ui.CTkButton(self, text=f"Sürüm: {version_current}", command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Geliştirici: Mukonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_and_credits_b = ui.CTkButton(self, text="Lisans ve Krediler", command=self.license_and_credits, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Güncelle", command=lambda:self.check_update("sidebar"))
            self.reset_b = ui.CTkButton(self, text="Sıfırla", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Kaldır", command=self.uninstall)
            self.color_label = ui.CTkLabel(self, text="Renk Teması:", anchor="w")
            self.color_menu = ui.CTkOptionMenu(self, values=["Rastgele", "Koyu Mavi", "Mavi", "Yeşil"], command=self.change_color)
            self.appearance_label = ui.CTkLabel(self, text="Görünüm:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["Sistem", "Açık", "Koyu"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Dil:", anchor="w")
            status = ui.CTkButton(self, text="Durum: Hazır", command=self.show_operations, font=ui.CTkFont(size=12, weight="bold"))
            self.language_menu.set("Türkçe")
            if os.path.isfile(system):
                self.appearance_menu.set("Sistem")
            elif os.path.isfile(light):
                self.appearance_menu.set("Açık")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Koyu")
            if os.path.isfile(random):
                self.color_menu.set("Rastgele")
            elif os.path.isfile(dark_blue):
                self.color_menu.set("Koyu Mavi")
            elif os.path.isfile(blue):
                self.color_menu.set("Mavi")
            elif os.path.isfile(green):
                self.color_menu.set("Yeşil")
        self.text.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.version_b.grid(row=1, column=0, padx=10, pady=0)
        self.mukonqi_b.grid(row=2, column=0, padx=10, pady=0)
        self.license_and_credits_b.grid(row=3, column=0, padx=10, pady=0)
        self.update_b.grid(row=5, column=0, padx=10, pady=5)
        self.reset_b.grid(row=6, column=0, padx=10, pady=5)
        self.uninstall_b.grid(row=7, column=0, padx=10, pady=5)
        self.color_label.grid(row=9, column=0, padx=10, pady=(5, 0))
        self.color_menu.grid(row=10, column=0, padx=10, pady=(0, 5))
        self.appearance_label.grid(row=11, column=0, padx=10, pady=(5, 0))
        self.appearance_menu.grid(row=12, column=0, padx=10, pady=(0, 5))
        self.language_label.grid(row=13, column=0, padx=10, pady=(5, 0))
        self.language_menu.grid(row=14, column=0, padx=10, pady=(0, 5))
        status.grid(row=16, column=0, padx=10, pady=(0, 5))
    def changelog(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.window.title("Changelog For "+version_current)
            self.label = ui.CTkLabel(self.window, text="Current version: "+version_current+"\nThe changelog for the "+version_current+" version is below:", font=ui.CTkFont(size=16, weight="bold"))
            with open("/usr/local/bin/grelintb/changelog-en.txt", "r") as cc_file:
                cc_text = cc_file.read()
        elif os.path.isfile(tr):
            self.window.title(version_current+" için Değişiklik Günlüğü")
            self.label = ui.CTkLabel(self.window, text="Şimdiki sürüm: "+version_current+"\n\n"+version_current+" sürümünün değişiklik günlüğü aşağıdadır:", font=ui.CTkFont(size=16, weight="bold"))
            with open("/usr/local/bin/grelintb/changelog-tr.txt", "r") as cc_file:
                cc_text = cc_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", cc_text)
        self.textbox.configure(state="disabled")
        self.label.grid(row=0, column=0, sticky="nsew", pady=10)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    def license_and_credits(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.window.title("License And Credits")
            self.label1 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Copyright (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB licensed under GPLv3 or later.")
            self.label2 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Credits")
            self.button1 = ui.CTkButton(self.window, text="Lolcat (for colorful commands in terminal)", command=lambda:subprocess.Popen("xdg-open https://github.com/busyloop/lolcat", shell=True))
            self.button2 = ui.CTkButton(self.window, text="wttr.in (for weather forecast)", command=lambda:subprocess.Popen("xdg-open https://github.com/chubin/wttr.in", shell=True))
            self.button3 = ui.CTkButton(self.window, text="Google Material Symbols (for application icon)", command=lambda:subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048", shell=True))    
        elif os.path.isfile(tr):
            self.window.title("Lisans Ve Krediler")
            self.label1 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Telif Hakkı (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB GPLv3 veya sonrası altında lisanslanmıştır.")
            self.label2 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Krediler")
            self.button1 = ui.CTkButton(self.window, text="Lolcat (terminaldeki renkli komutlar için)", command=lambda:subprocess.Popen("xdg-open https://github.com/busyloop/lolcat", shell=True))
            self.button2 = ui.CTkButton(self.window, text="wttr.in (hava durumu için)", command=lambda:subprocess.Popen("xdg-open https://github.com/chubin/wttr.in", shell=True))
            self.button3 = ui.CTkButton(self.window, text="Google Material Symbols (uygulama ikonu için)", command=lambda:subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048", shell=True))  
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as license_file:
            license_text = license_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", license_text)
        self.textbox.configure(state="disabled")
        self.label1.grid(row=0, column=0, sticky="nsew", pady=(10, 5))
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=20)
        self.label2.grid(row=2, column=0, sticky="nsew", pady=(10, 0))
        self.button1.grid(row=3, column=0, sticky="nsew", padx=50, pady=5)
        self.button2.grid(row=4, column=0, sticky="nsew", padx=50, pady=5)
        self.button3.grid(row=5, column=0, sticky="nsew", padx=50, pady=(5, 10))
    def check_update(self, string: str):
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            self.window = ui.CTkToplevel()
            self.window.geometry("540x540")
            self.window.minsize(540, 540)
            self.window.grid_rowconfigure(1, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
            if os.path.isfile(en):
                self.window.title("Changelog For "+version_latest)
                self.label = ui.CTkLabel(self.window, text="New version found: "+version_latest+"\n\nThe changelog for the "+version_latest+" version is below:", font=ui.CTkFont(size=16, weight="bold"))
                self.button = ui.CTkButton(self.window, text="Update To "+version_latest, command=update)
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-en.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(tr):
                self.window.title(version_latest+" için Değişiklik Günlüğü")
                self.label = ui.CTkLabel(self.window, text="Yeni sürüm bulundu: "+version_latest+"\n\n"+version_latest+" sürümünün değişiklik günlüğü aşağıdadır:", font=ui.CTkFont(size=16, weight="bold"))
                self.button = ui.CTkButton(self.window, text=version_latest+" Sürümüne Güncelle", command=update)
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-tr.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.textbox = ui.CTkTextbox(self.window)
            self.textbox.insert("0.0", cl_text)
            self.label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            self.textbox.grid(row=1, column=0, sticky="nsew", padx=50, pady=10)
            self.button.grid(row=2, column=0, sticky="nsew", padx=100, pady=10)
            self.textbox.configure(state="disabled")
        elif string != "startup":
            if os.path.isfile(en):
                mb.showinfo("Information","GrelinTB is up to date.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","GrelinTB güncel.")
    def reset(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/update.sh")
        if os.path.isfile(en):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("Successful", "GrelinTB has been reset.")
        elif os.path.isfile(tr):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("Başarılı", "GrelinTB sıfırlandı.")
        os.system("grelintb")
        exit()
    def uninstall(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        os.system("cd /home/"+username+" ; rm .*-grelintb*")
        if os.path.isfile(en):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("See you!","GrelinTB was uninstalled from your system.")
        elif os.path.isfile(tr):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("Görüşürüz!","GrelinTB sisteminizden kaldırıldı.")
        exit()
    def change_color(self, new_color: str):
        if new_color == "Dark Blue" or new_color == "Koyu Mavi":
            os.system("cd "+config+"color ; rm * ; touch dark-blue.txt")
        elif new_color == "Blue" or new_color == "Mavi":
            os.system("cd "+config+"color ; rm * ; touch blue.txt")
        elif new_color == "Green" or new_color == "Yeşil":
            os.system("cd "+config+"color ; rm * ; touch green.txt")
        elif new_color == "Random" or new_color == "Rastgele":
            os.system("cd "+config+"color ; rm * ; touch random.txt")
        root.destroy()
        os.system("grelintb")
        exit()
    def change_appearance(self, new_appearance: str):
        if new_appearance == "System" or new_appearance == "Sistem":
            ui.set_appearance_mode("System")
            os.system("cd "+config+"theme ; rm * ; touch system.txt")
        elif new_appearance == "Light" or new_appearance == "Açık":
            ui.set_appearance_mode("Light")
            os.system("cd "+config+"theme ; rm * ; touch light.txt")
        elif new_appearance == "Dark" or new_appearance == "Koyu":
            ui.set_appearance_mode("Dark")
            os.system("cd "+config+"theme ; rm * ; touch dark.txt")
    def change_language(self, new_language: str):
        if new_language == "English":
            os.system("cd "+config+"language ; rm * ; touch en.txt")
        elif new_language == "Türkçe":
            os.system("cd "+config+"language ; rm * ; touch tr.txt")
        root.destroy()
        os.system("grelintb")
        exit()
    def show_operations(self):
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
            if os.path.isfile(en):
                self.window.title("List Of All Operations")
            elif os.path.isfile(tr):
                self.window.title("Tüm İşlemlerin Listesi")
            for self.progress in current_operations:
                self.number = self.number + 1
                if os.path.isfile(en):
                    ui.CTkLabel(self.frame, fg_color=["gray100", "gray20"], corner_radius=20, text=f"{self.progress[0]}\nStarted at {self.progress[1]} time.", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.number, column=0, pady=5, padx=10, sticky="nsew")
                elif os.path.isfile(tr):
                    ui.CTkLabel(self.frame, fg_color=["gray100", "gray20"], corner_radius=20, text=f"{self.progress[0]}\n{self.progress[1]} vaktinde başladı.", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.number, column=0, pady=5, padx=10, sticky="nsew")
        else:
            if os.path.isfile(en):
                mb.showwarning("Warning", "There are no processes running at the moment.")
            elif os.path.isfile(tr):
                mb.showwarning("Uyarı", "Şu anda çalışan hiçbir işlem yok.")

class Startup(ui.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        if os.path.isfile(en):
            self.configure(label_text=f"Welcome {username}!", label_font=ui.CTkFont(size=15, weight="bold"))
            self.weather = ui.CTkLabel(self, text=f"Weather Forecast: Getting", font=ui.CTkFont(size=13, weight="bold")) 
            self.system = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"System", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname = ui.CTkLabel(self, text=f"Host: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro = ui.CTkLabel(self, text=f"Distribution: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel = ui.CTkLabel(self, text=f"Kernel: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime = ui.CTkLabel(self, text=f"Uptime: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time = ui.CTkLabel(self, text=f"Boot Time: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Usages", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage = ui.CTkLabel(self, text=f"CPU: Getting", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage = ui.CTkLabel(self, text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage = ui.CTkLabel(self, text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage = ui.CTkLabel(self, text=f"Swap: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        elif os.path.isfile(tr):
            self.configure(label_text=f"Merhabalar {username}!", label_font=ui.CTkFont(size=15, weight="bold"))
            self.weather = ui.CTkLabel(self, text=f"Hava Durumu: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))   
            self.system = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Sistem", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname = ui.CTkLabel(self, text=f"Ana Bilgisayar Adı: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro = ui.CTkLabel(self, text=f"Dağıtım: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel = ui.CTkLabel(self, text=f"Çekirdek: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime = ui.CTkLabel(self, text=f"Çalışma Süresi: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time = ui.CTkLabel(self, text=f"Önyüklenme Vakti: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Kullanımlar", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage = ui.CTkLabel(self, text=f"CPU: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage = ui.CTkLabel(self, text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage = ui.CTkLabel(self, text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage = ui.CTkLabel(self, text=f"Takas: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.weather.grid(row=0, column=0, pady=(7.5, 10), columnspan=4)
        self.system.grid(row=2, column=0, pady=(0, 7.5), columnspan=4)
        self.hostname.grid(row=3, column=0, pady=(0, 7.5), columnspan=4)
        self.distro.grid(row=4, column=0, pady=(0, 7.5), columnspan=4)
        self.kernel.grid(row=5, column=0, pady=(0, 7.5), columnspan=4)
        self.uptime.grid(row=6, column=0, pady=(0, 7.5), columnspan=4)
        self.boot_time.grid(row=7, column=0, pady=(0, 10), columnspan=4)
        self.usages.grid(row=8, column=0, pady=(0, 7.5), columnspan=4)
        self.cpu_usage.grid(row=9, column=0, pady=(0, 10))
        self.disk_usage.grid(row=9, column=1, pady=(0, 10))
        self.ram_usage.grid(row=9, column=2, pady=(0, 10))
        self.swap_usage.grid(row=9, column=3, pady=(0, 10))
        self.weather_thread = threading.Thread(target=lambda:self.weather_def(), daemon=True)
        self.weather_thread.start()
        self.cpu_usage_thread = threading.Thread(target=lambda:self.cpu_usage_def(), daemon=True)
        self.cpu_usage_thread.start()
        self.other_thread = threading.Thread(target=lambda:self.other_def(), daemon=True)
        self.other_thread.start()
    def weather_def(self):
        if os.path.isfile(en):
            self.weather.configure(text="Weather Forecast: "+str(subprocess.Popen('curl -H "Accept-Language: en" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
        elif os.path.isfile(tr):
            self.weather.configure(text="Hava Durumu: "+str(subprocess.Popen('curl -H "Accept-Language: tr" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
    def cpu_usage_def(self):
        self.cpu_usage.configure(text=f"CPU: %{str(psutil.cpu_percent(5))}")
    def other_def(self):
        if hasattr (psutil, "sensors_temperatures") and psutil.sensors_temperatures():
            self.temps_ok = True
            self.temps_number = 10
            self.temps = psutil.sensors_temperatures()
            if os.path.isfile(en):
                self.temps_header = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Temperatures", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
            elif os.path.isfile(tr):
                self.temps_header= ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Sıcaklıklar", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
            for self.temps_name, self.temps_entries in self.temps.items():
                self.temps_number = self.temps_number + 1
                if os.path.isfile(en):
                    self.temps_label = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Hardware: {self.temps_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
                elif os.path.isfile(tr):
                    self.temps_label = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Donanım: {self.temps_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.temps_entry in self.temps_entries:
                    self.temps_number = self.temps_number + 1
                    if os.path.isfile(en): 
                        ui.CTkLabel(self, text=f"{self.temps_entry.label or self.temps_name}: Current = {self.temps_entry.current} °C, High = {self.temps_entry.high} °C, Critical = {self.temps_entry.critical} °C", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 5), columnspan=4)
                    elif os.path.isfile(tr): 
                        ui.CTkLabel(self, text=f"{self.temps_entry.label or self.temps_name}: Current = {self.temps_entry.current} °C, Yüksek = {self.temps_entry.high} °C, Kritik = {self.temps_entry.critical} °C", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_fans") and psutil.sensors_fans():
            self.fans_ok = True
            if self.temps_ok == True:
                self.fans_number = self.temps_number + 1
            else:
                self.fans_number = 10
            if os.path.isfile(en):
                self.fans_header = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Fans", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.fans_number, column=0, pady=(5, 7.5), columnspan=4)
            elif os.path.isfile(tr):
                self.fans_header = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Fanlar", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.fans_number, column=0, pady=(5, 7.5), columnspan=4)
            self.fans = psutil.sensors_fans()
            for self.fans_name, self.fans_entries in self.fans.items():
                self.fans_number = self.fans_number + 1
                if os.path.isfile(en):
                    self.fans_label = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Hardware: {self.fans_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 7.5), columnspan=4)
                elif os.path.isfile(tr):
                    self.fans_label = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Donanım: {self.fans_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.fans_entry in self.fans_entries:
                    self.fans_number = self.fans_number + 1
                    ui.CTkLabel(self, text=f"{self.fans_entry.label or self.fans_name}: {self.fans_entry.current} RPM", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_battery") and psutil.sensors_battery():
            if self.fans_ok == True:
                self.batt_number = self.fans_number + 1
            elif self.temps_ok == True:
                self.batt_number = self.temps_number + 1
            else:
                self.batt_number = 10
            if os.path.isfile(en):
                self.batt_header = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Battery", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.batt_number, column=0, pady=(5, 7.5), columnspan=4)
            elif os.path.isfile(tr):
                self.batt_header = ui.CTkLabel(self, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Batarya", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.batt_number, column=0, pady=(5, 7.5), columnspan=4)
            self.batt = psutil.sensors_battery()
            if os.path.isfile(en):
                ui.CTkLabel(self, text=f"Charge: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 1, column=0, pady=(0, 5), columnspan=4)
                if self.batt.power_plugged:
                    ui.CTkLabel(self, text=f"Status: {str('Charging' if self.batt.percent < 100 else 'Fully Charged')}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Plugged In: Yes", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                else:
                    ui.CTkLabel(self, text=f"Remaining: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Status: Discharging", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Plugged In: No", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 4, column=0, pady=(0, 5), columnspan=4)
            elif os.path.isfile(tr):
                ui.CTkLabel(self, text=f"Şarj: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 1, column=0, pady=(0, 5), columnspan=4)
                if self.batt.power_plugged:
                    ui.CTkLabel(self, text=f"Durum: {str('Şarj Oluyor' if self.batt.percent < 100 else 'Şarj Oldu')}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Şarja Takılı: Evet", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                else:
                    ui.CTkLabel(self, text=f"Kalan: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Durum: Şarj Azalıyor", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                    ui.CTkLabel(self, text=f"Şarja Takılı: Hayır", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.batt_number + 4, column=0, pady=(0, 5), columnspan=4)
        
class NotesAndDocuments(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.content = ui.CTkTextbox(self)
        self.content.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.options = ui.CTkFrame(self, fg_color="transparent")
        self.options.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.options.grid_rowconfigure((2, 3, 4, 5, 6), weight=1)
        self.options.grid_columnconfigure(0, weight=1)
        self.notes = os.listdir(notes)
        if os.path.isfile(en):
            self.list = ui.CTkOptionMenu(self.options, values=["List Of Your Notes"]+ self.notes, command=self.option)
            self.entry = ui.CTkEntry(self.options, placeholder_text="Name")
            self.button1 = ui.CTkButton(self.options, text="Take A New Note", command=self.new_note)
            self.button2 = ui.CTkButton(self.options, text="Open", command=self.open)
            self.button3 = ui.CTkButton(self.options, text="Rename", command=self.rename)
            self.button4 = ui.CTkButton(self.options, text="Save", command=self.save)
            self.button5 = ui.CTkButton(self.options, text="Delete", command=self.delete)
        elif os.path.isfile(tr):
            self.list = ui.CTkOptionMenu(self.options, values=["Notlarınızın Listesi"] + self.notes, command=self.option)
            self.entry = ui.CTkEntry(self.options, placeholder_text="Ad")
            self.button1 = ui.CTkButton(self.options, text="Yeni Bir Not Al", command=self.new_note)
            self.button2 = ui.CTkButton(self.options, text="Aç", command=self.open)
            self.button3 = ui.CTkButton(self.options, text="Yeniden Adlandır", command=self.rename)
            self.button4 = ui.CTkButton(self.options, text="Kaydet", command=self.save)
            self.button5 = ui.CTkButton(self.options, text="Sil", command=self.delete)
        self.list.grid(row=0, column=0, sticky="nsew", pady=(0, 10), padx=(15, 0))
        self.entry.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button1.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button2.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button3.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button4.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button5.grid(row=6, column=0, sticky="nsew", pady=0, padx=(15, 0))
    def option(self, note_name: str):
        if note_name != "List Of Your Notes" and note_name != "Notlarınızın Listesi":
            self.entry.delete(0, "end")
            self.entry.insert(0, f"{notes}{note_name}")
        else:
            self.entry.delete(0, "end")
    def new_note(self):
        if os.path.isfile(en):
            self.dialog = ui.CTkInputDialog(text=f"Type a new note name.", title="Type New Name")
        elif os.path.isfile(tr):
            self.dialog = ui.CTkInputDialog(text=f"Yeni bir not adı girin.", title="Yeni Ad Girin")
        self.new_name = self.dialog.get_input()
        if self.new_name == None:
            if os.path.isfile(en):
                mb.showerror("Error", "Taking a new note was canceled.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Yeni bir not alma iptal edildi.")
            return
        os.system(f"touch {notes}{self.new_name}")
        self.entry.delete(0, "end")
        self.entry.insert(0, f"{notes}{self.new_name}")
        self.notes = os.listdir(notes)
        if os.path.isfile(en):
            mb.showinfo("Information", f"The note was created.")
            self.list.configure(values=["List Of Your Notes"] + self.notes)
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme", f"Not oluşturuldu.")
            self.list.configure(values=["Notlarınızın Listesi"] + self.notes)
    def open(self):
        try:
            if self.entry.get() != "List Of Your Notes" and self.entry.get() != "Notlarınızın Listesi" and self.entry.get() != "" :
                with open(self.entry.get(), "r") as self.file_lo:
                    self.text = self.file_lo.read()
            else:
                self.file_a = fd.askopenfilename()
                with open(self.file_a, "r") as self.file_ao:
                    self.text = self.file_ao.read()
                self.entry.delete(0, "end")
                self.entry.insert(0, self.file_a)
        except:
            if os.path.isfile(en):
                mb.showerror("Error","The note or document could not be opened.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Not ya da belge açılamadı.")
            return
        self.content.delete("0.0", 'end')
        self.content.insert("0.0", self.text)
    def rename(self):
        if not os.path.isfile(self.entry.get()):
            if os.path.isfile(en):
                mb.showerror("Error","There is no such note or document.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Öyle bir not ya da belge yok.")
            return
        if os.path.isfile(en):
            self.dialog = ui.CTkInputDialog(text=f"Type a new file name for {self.entry.get()}.", title="Type New Name")
        elif os.path.isfile(tr):
            self.dialog = ui.CTkInputDialog(text=f"{self.entry.get()} için yeni bir ad girin.", title="Yeni Ad Girin")
        self.new_name = self.dialog.get_input()
        if self.new_name == None:
            if os.path.isfile(en):
                mb.showerror("Error", f"Renaming {self.entry.get()} was canceled.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", f"{self.entry.get()} notunu ya da belgesini yeniden adlandırmadan vazgeçildi.")
            return
        os.system(f"mv {self.entry.get()} {os.path.dirname(self.entry.get())}/{self.new_name}")
        self.entry.delete(0, "end")
        self.entry.insert(0, f"{notes}{self.new_name}")
        self.notes = os.listdir(notes)
        if os.path.isfile(en):
            mb.showinfo("Information", f"The note or document was renamed as {self.new_name}.")
            self.list.configure(values=["List Of Your Notes"] + self.notes)
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme", f"Not ya da belge {self.new_name} olarak yeniden adlandırıldı.")
            self.list.configure(values=["Notlarınızın Listesi"] + self.notes)
    def save(self):
        with open(self.entry.get(), "w+") as self.file:
            self.file.write(self.content.get("0.0", 'end'))
        with open(self.entry.get()) as self.file:
            self.output = self.file.read()
        self.notes = os.listdir(notes)
        if self.output == self.content.get("0.0", 'end'):
            if os.path.isfile(en):
                mb.showinfo("Information","The note or document saved.")
                self.list.configure(values=["List Of Your Notes"] + self.notes)
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","Not ya da belge kaydedildi.")
                self.list.configure(values=["Notlarınızın Listesi"] + self.notes)
        else:
            if os.path.isfile(en):
                mb.showerror("Error","The note or document could not be saved.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Not ya da belge kaydedilemedi.")
    def delete(self):
        if not os.path.isfile(self.entry.get()):
            if os.path.isfile(en):
                mb.showerror("Error","There is no such note or document.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Öyle bir not ya da belge yok.")
            return
        os.system(f"rm {self.entry.get()}")
        self.notes = os.listdir(notes)
        if os.path.isfile(self.entry.get()):
            if os.path.isfile(en):
                mb.showerror("Error","The note or document could not be deleted.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Not ya da belge silinemedi.")
            return
        else:
            if os.path.isfile(en):
                mb.showinfo("Information","The note or document was deleted.")
                self.list.configure(values=["List Of Your Notes"] + self.notes)
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","Not ya da belge silindi.")
                self.list.configure(values=["Notlarınızın Listesi"] + self.notes)

class TraditionalPackages(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((2, 3, 4, 5, 6), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.app_text = "Application"
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Packages")
            self.button1 = ui.CTkButton(self.frame, text="Search", command=lambda:self.go_main("search"))
            self.button2 = ui.CTkButton(self.frame, text="Install", command=lambda:self.go_main("install"))
            self.button3 = ui.CTkButton(self.frame, text="Reinstall", command=lambda:self.go_main("reinstall"))
            self.button4 = ui.CTkButton(self.frame, text="Uninstall", command=lambda:self.go_main("uninstall"))
            self.button5 = ui.CTkButton(self.frame, text="Update", command=lambda:self.go_main("update"))
        elif os.path.isfile(tr):
            self.app_text = "Uygulama"
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Paketler")
            self.button1 = ui.CTkButton(self.frame, text="Ara", command=lambda:self.go_main("search"))
            self.button2 = ui.CTkButton(self.frame, text="Kur", command=lambda:self.go_main("install"))
            self.button3 = ui.CTkButton(self.frame, text="Yeniden Kur", command=lambda:self.go_main("reinstall"))
            self.button4 = ui.CTkButton(self.frame, text="Kaldır", command=lambda:self.go_main("uninstall"))
            self.button5 = ui.CTkButton(self.frame, text="Güncelle", command=lambda:self.go_main("update"))
        if os.path.isfile(debian):
            self.app = ui.CTkOptionMenu(self.frame, values=[self.app_text, "Firefox-ESR", "Firefox", "VLC", "LibreOffice", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Lolcat"], command=self.option)
        elif os.path.isfile(fedora):
            self.app = ui.CTkOptionMenu(self.frame, values=[self.app_text, "Firefox", "VLC", "LibreOffice", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Fastfetch", "Lolcat"], command=self.option)
        elif os.path.isfile(solus):
            self.app = ui.CTkOptionMenu(self.frame, values=[self.app_text, "Firefox", "VLC", "LibreOffice-All", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "Neofetch", "Lolcat"], command=self.option)
        elif os.path.isfile(arch):
            self.app = ui.CTkOptionMenu(self.frame, values=[self.app_text, "Firefox", "VLC", "LibreOffice-Fresh", "GParted", "GIMP", "Wine", "Ark", "Rhythmbox", "Spectacle", "Okular", "GNOME-Boxes", "Grub-Customizer", "Goverlay", "gamemode", "Mangohud", "Dolphin", "Nautilus", "Nemo", "Caja", "Thunar", "PCManFM", "PCManFM-Qt", "Neofetch", "Fastfetch", "Lolcat"], command=self.option)
        self.app.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.entry.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button1.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button2.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=6, column=0, sticky="nsew", pady=0, padx=(10, 0))
    def name_error(self):
        if os.path.isfile(en):
            mb.showerror("Error", "Please select application from list or enter packages name below.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", "Lütfen listeden uygulama seçin ya da aşağıda paketlerin adını girin.")
    def option(self, package: str):
        if package == "Application" or package == "Uygulama":
            self.name_error()
            self.entry.delete(0, "end")
        else:
            self.entry.delete(0, "end")
            self.entry.insert(0, package.lower())
    def do_main(self, operation: str):
        if self.entry.get() == "":
            self.name_error()
            return
        self.app.configure(state="disabled")
        self.entry.configure(state="disabled")
        self.button1.configure(state="disabled")
        self.button2.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.button4.configure(state="disabled")
        self.button5.configure(state="disabled")
        self.time = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            if operation == "search":
                add_operation(f"Searching {self.entry.get()}", self.time)
            elif operation == "install":
                add_operation(f"Installing {self.entry.get()}", self.time)
            elif operation == "reinstall":
                add_operation(f"Reinstalling {self.entry.get()}", self.time)
            elif operation == "uninstall":
                add_operation(f"Uninstalling {self.entry.get()}", self.time)
            elif operation == "update":
                add_operation(f"Updating {self.entry.get()}", self.time)
        elif os.path.isfile(tr):
            if operation == "search":
                add_operation(f"{self.entry.get()} Aranıyor", self.time)
            elif operation == "install":
                add_operation(f"{self.entry.get()} Kuruluyor", self.time)
            elif operation == "reinstall":
                add_operation(f"{self.entry.get()} Yeniden Kuruluyor", self.time)
            elif operation == "uninstall":
                add_operation(f"{self.entry.get()} Kaldırılıyor", self.time)
            elif operation == "update":
                add_operation(f"{self.entry.get()} Güncelleniyor", self.time)
        if os.path.isfile(debian):
            if operation == "search":
                cmd = subprocess.Popen('apt search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "install":
                cmd = subprocess.Popen('pkexec apt install '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "reinstall":
                cmd = subprocess.Popen('pkexec apt install --reinstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "uninstall":
                cmd = subprocess.Popen('pkexec apt autoremove --purge '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "update":
                cmd = subprocess.Popen('pkexec apt upgrade '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(fedora):
            if operation == "search":
                cmd = subprocess.Popen('dnf --nogpgcheck search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "install":
                cmd = subprocess.Popen('pkexec dnf --nogpgcheck install '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "reinstall":
                cmd = subprocess.Popen('pkexec dnf --nogpgcheck reinstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "uninstall":
                cmd = subprocess.Popen('pkexec dnf --nogpgcheck remove '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "update":
                cmd = subprocess.Popen('pkexec dnf --nogpgcheck upgrade '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(solus):
            if operation == "search":
                cmd = subprocess.Popen('eopkg search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "install":
                cmd = subprocess.Popen('pkexec eopkg install '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "reinstall":
                cmd = subprocess.Popen('pkexec eopkg install --reinstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "uninstall":
                cmd = subprocess.Popen('pkexec eopkg remove --purge -'+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "update":
                cmd = subprocess.Popen('pkexec eopkg upgrade '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(arch):
            if operation == "search":
                cmd = subprocess.Popen('pacman -Ss '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "install":
                cmd = subprocess.Popen('pkexec pacman -S '+self.entry.get()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "reinstall":
                cmd = subprocess.Popen('pkexec pacman -S '+self.entry.get()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "uninstall":
                cmd = subprocess.Popen('pkexec pacman -Rns '+self.entry.get()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "update":
                cmd = subprocess.Popen('pkexec pacman -Syu '+self.entry.get()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        if os.path.isfile(en):
            if operation == "search":
                delete_operation(f"Searching {self.entry.get()}", self.time)
            elif operation == "install":
                delete_operation(f"Installing {self.entry.get()}", self.time)
            elif operation == "reinstall":
                delete_operation(f"Reinstalling {self.entry.get()}", self.time)
            elif operation == "uninstall":
                delete_operation(f"Uninstalling {self.entry.get()}", self.time)
            elif operation == "update":
                delete_operation(f"Updating {self.entry.get()}", self.time)
        elif os.path.isfile(tr):
            if operation == "search":
                delete_operation(f"{self.entry.get()} Aranıyor", self.time)
            elif operation == "install":
                delete_operation(f"{self.entry.get()} Kuruluyor", self.time)
            elif operation == "reinstall":
                delete_operation(f"{self.entry.get()} Yeniden Kuruluyor", self.time)
            elif operation == "uninstall":
                delete_operation(f"{self.entry.get()} Kaldırılıyor", self.time)
            elif operation == "update":
                delete_operation(f"{self.entry.get()} Güncelleniyor", self.time)
        self.app.configure(state="normal")
        self.entry.configure(state="normal")
        self.button1.configure(state="normal")
        self.button2.configure(state="normal")
        self.button3.configure(state="normal")
        self.button4.configure(state="normal")
        self.button5.configure(state="normal")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class FlatpakPackages(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Packages")
            self.button1 = ui.CTkButton(self.frame, text="Search", command=lambda:self.go_main("search"))
            self.button2 = ui.CTkButton(self.frame, text="Install", command=lambda:self.go_main("install"))
            self.button3 = ui.CTkButton(self.frame, text="Reinstall", command=lambda:self.go_main("reinstall"))
            self.button4 = ui.CTkButton(self.frame, text="Uninstall", command=lambda:self.go_main("uninstall"))
            self.button5 = ui.CTkButton(self.frame, text="Update", command=lambda:self.go_main("update"))
        elif os.path.isfile(tr):
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Paketler")
            self.button1 = ui.CTkButton(self.frame, text="Ara", command=lambda:self.go_main("search"))
            self.button2 = ui.CTkButton(self.frame, text="Kur", command=lambda:self.go_main("install"))
            self.button3 = ui.CTkButton(self.frame, text="Yeniden Kur", command=lambda:self.go_main("reinstall"))
            self.button4 = ui.CTkButton(self.frame, text="Kaldır", command=lambda:self.go_main("uninstall"))
            self.button5 = ui.CTkButton(self.frame, text="Güncelle", command=lambda:self.go_main("update"))
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=5, column=0, sticky="nsew", pady=0, padx=(10, 0))
    def do_main(self, operation: str):
        if self.entry.get() == "":
            if os.path.isfile(en):
                mb.showerror("Error", "Please enter packages name below.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Lütfen paketlerin adını girin.")
            return
        self.entry.configure(state="disabled")
        self.button1.configure(state="disabled")
        self.button2.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.button4.configure(state="disabled")
        self.button5.configure(state="disabled")
        self.time = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            if operation == "search":
                add_operation(f"Searching {self.entry.get()} (Flatpak)", self.time)
            elif operation == "install":
                add_operation(f"Installing {self.entry.get()} (Flatpak)", self.time)
            elif operation == "reinstall":
                add_operation(f"Reinstalling {self.entry.get()} (Flatpak)", self.time)
            elif operation == "uninstall":
                add_operation(f"Uninstalling {self.entry.get()} (Flatpak)", self.time)
            elif operation == "update":
                add_operation(f"Updating {self.entry.get()} (Flatpak)", self.time)
        elif os.path.isfile(tr):
            if operation == "search":
                add_operation(f"{self.entry.get()} Aranıyor (Flatpak)", self.time)
            elif operation == "install":
                add_operation(f"{self.entry.get()} Kuruluyor (Flatpak)", self.time)
            elif operation == "reinstall":
                add_operation(f"{self.entry.get()} Yeniden Kuruluyor (Flatpak)", self.time)
            elif operation == "uninstall":
                add_operation(f"{self.entry.get()} Kaldırılıyor (Flatpak)", self.time)
            elif operation == "update":
                add_operation(f"{self.entry.get()} Güncelleniyor (Flatpak)", self.time)
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
            install_flatpak()
            if ask_f == False:
                return
        if operation == "search":
            cmd = subprocess.Popen('flatpak search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif operation == "install":
            cmd = subprocess.Popen('flatpak install '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif operation == "reinstall":
            cmd = subprocess.Popen('flatpak install --reinstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif operation == "uninstall":
            cmd = subprocess.Popen('flatpak uninstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif operation == "update":
            cmd = subprocess.Popen('flatpak update '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        if os.path.isfile(en):
            if operation == "search":
                delete_operation(f"Searching {self.entry.get()} (Flatpak)", self.time)
            elif operation == "install":
                delete_operation(f"Installing {self.entry.get()} (Flatpak)", self.time)
            elif operation == "reinstall":
                delete_operation(f"Reinstalling {self.entry.get()} (Flatpak)", self.time)
            elif operation == "uninstall":
                delete_operation(f"Uninstalling {self.entry.get()} (Flatpak)", self.time)
            elif operation == "update":
                delete_operation(f"Updating {self.entry.get()} (Flatpak)", self.time)
        elif os.path.isfile(tr):
            if operation == "search":
                delete_operation(f"{self.entry.get()} Aranıyor (Flatpak)", self.time)
            elif operation == "install":
                delete_operation(f"{self.entry.get()} Kuruluyor (Flatpak)", self.time)
            elif operation == "reinstall":
                delete_operation(f"{self.entry.get()} Yeniden Kuruluyor (Flatpak)", self.time)
            elif operation == "uninstall":
                delete_operation(f"{self.entry.get()} Kaldırılıyor (Flatpak)", self.time)
            elif operation == "update":
                delete_operation(f"{self.entry.get()} Güncelleniyor (Flatpak)", self.time)
        self.entry.configure(state="normal")
        self.button1.configure(state="normal")
        self.button2.configure(state="normal")
        self.button3.configure(state="normal")
        self.button4.configure(state="normal")
        self.button5.configure(state="normal")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class DEWM(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((2, 3, 4, 5), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.text = ui.CTkLabel(self.frame, text="Desktop Environment\nWindow Manager")
            self.button1 = ui.CTkButton(self.frame, text="Install", command=lambda:self.go_main("install"))
            self.button2 = ui.CTkButton(self.frame, text="Reinstall", command=lambda:self.go_main("reinstall"))
            self.button3 = ui.CTkButton(self.frame, text="Uninstall", command=lambda:self.go_main("uninstall"))
            self.button4 = ui.CTkButton(self.frame, text="Update", command=lambda:self.go_main("update"))
        elif os.path.isfile(tr):
            self.text = ui.CTkLabel(self.frame, text="Masaüstü Ortamı\nPencere Yöneticisi")
            self.button1 = ui.CTkButton(self.frame, text="Kur", command=lambda:self.go_main("install"))
            self.button2 = ui.CTkButton(self.frame, text="Yeniden Kur", command=lambda:self.go_main("reinstall"))
            self.button3 = ui.CTkButton(self.frame, text="Kaldır", command=lambda:self.go_main("uninstall"))
            self.button4 = ui.CTkButton(self.frame, text="Güncelle", command=lambda:self.go_main("update"))
        if os.path.isfile(debian):
            self.dewm = ui.CTkOptionMenu(self.frame, values=["KDE-Plasma-Desktop", "GNOME", "Cinnamon", "Mate", "Xfce4", "LXDE", "LXQt", "Openbox", "bspwm", "Qtile", "Herbstluftwm", "Awesome", "IceWM", "i3", "Sway", "Xmonad"])
        elif os.path.isfile(fedora):
            self.dewm = ui.CTkOptionMenu(self.frame, values=["GNOME", "KDE", "Xfce", "Phosh", "LXDE", "LXQt", "Cinnamon", "Mate", "Sugar", "Deepin", "Budgie", "Basic", "Sway", "Deepin", "i3", "Openbox", "Fluxbox", "Blackbox", "bspwm"])
        elif os.path.isfile(solus):
            self.dewm = ui.CTkOptionMenu(self.frame, values=["Budgie", "GNOME", "KDE", "Xfce", "Mate", "Fluxbox", "Openbox", "i3", "bspwm"])
        elif os.path.isfile(arch):
            self.dewm = ui.CTkOptionMenu(self.frame, values=["Budgie", "Cinnamon", "Cutefish", "Deepin", "Enlightenment", "GNOME", "GNOME-Flashback", "Plasma", "LXDE", "LXDE-GTK3", "LXQt", "Mate", "Pantheon", "Phosh", "Sugar", "UKUI", "Xfce4", "Fluxbox", "IceWM", "openmotif", "Openbox", "PekWM", "Xorg-TWM", "Herbstluftwm", "i3-WM", "Notion", "Stumpwm", "Awesome", "Qtile", "xmonad"])
        self.text.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.dewm.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button1.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button2.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=5, column=0, sticky="nsew", pady=0, padx=(10, 0))
    def do_main(self, operation: str):
        self.dewm.configure(state="disabled")
        self.button1.configure(state="disabled")
        self.button2.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.button4.configure(state="disabled")
        self.time = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            if operation == "install":
                add_operation(f"Installing {self.dewm.get()}", self.time)
            elif operation == "reinstall":
                add_operation(f"Reinstalling {self.dewm.get()}", self.time)
            elif operation == "uninstall":
                add_operation(f"Uninstalling {self.dewm.get()}", self.time)
            elif operation == "update":
                add_operation(f"Updating {self.dewm.get()}", self.time)
        elif os.path.isfile(tr):
            if operation == "install":
                add_operation(f"{self.dewm.get()} Kuruluyor", self.time)
            elif operation == "reinstall":
                add_operation(f"{self.dewm.get()} Yeniden Kuruluyor", self.time)
            elif operation == "uninstall":
                add_operation(f"{self.dewm.get()} Kaldırılıyor", self.time)
            elif operation == "update":
                add_operation(f"{self.dewm.get()} Güncelleniyor", self.time)
        if os.path.isfile(debian):
            if self.dewm.get().lower() != "mate":
                if operation == "install":
                    cmd = subprocess.Popen('pkexec apt install '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec apt install --reinstall '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec apt autoremove --purge '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec apt upgrade '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif self.dewm.get().lower() == "mate":
                if operation == "install":
                    cmd = subprocess.Popen('pkexec apt install mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec apt install --reinstall mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec apt autoremove --purge mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec apt upgrade mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(fedora):
            if self.dewm.get() in ["KDE", "Xfce", "Phosh", "LXDE", "LXQt", "Cinnamon", "Mate", "Sugar", "Deepin", "Budgie", "Basic", "Sway", "Deepin", "i3"]:
                if operation == "install":
                    cmd = subprocess.Popen('pkexec bash -c "dnf install --nogpgcheck @'+self.dewm.get().lower()+'-desktop-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf reinstall --nogpgcheck @'+self.dewm.get().lower()+'-desktop-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf remove --nogpgcheck @'+self.dewm.get().lower()+'-desktop-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uodate":
                    cmd = subprocess.Popen('pkexec bash -c "dnf upgrade --nogpgcheck @'+self.dewm.get().lower()+'-desktop-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif self.dewm.get() in ["Openbox", "Fluxbox", "Blackbox", "bspwm"]:
                if operation == "install":
                    cmd = subprocess.Popen('pkexec bash -c "dnf install --nogpgcheck '+self.dewm.get().lower()+'-desktop -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf reinstall --nogpgcheck '+self.dewm.get().lower()+'-desktop -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf remove --nogpgcheck '+self.dewm.get().lower()+'-desktop -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec bash -c "dnf upgrade --nogpgcheck '+self.dewm.get().lower()+'-desktop -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif self.dewm.get() == "GNOME":
                if operation == "install":
                    cmd = subprocess.Popen('pkexec bash -c "dnf install --nogpgcheck @workstation-product-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf reinstall --nogpgcheck @workstation-product-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec bash -c "dnf remove --nogpgcheck @workstation-product-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec bash -c "dnf upgrade --nogpgcheck @workstation-product-environment -y ; SYSTEMD_COLORS=0 systemctl set-default graphical.target"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)             
        elif os.path.isfile(solus):
            if self.dewm.get().lower() not in ["openbox", "fluxbox", "bspwm"]:
                if operation == "install":
                    cmd = subprocess.Popen('pkexec eopkg install -c desktop.'+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec eopkg install --reinstall -c desktop.'+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec eopkg remove --purge -c desktop.'+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec eopkg upgrade -c desktop.'+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            else:
                if operation == "install":
                    cmd = subprocess.Popen('pkexec eopkg install '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "reinstall":
                    cmd = subprocess.Popen('pkexec eopkg install --reinstall '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "uninstall":
                    cmd = subprocess.Popen('pkexec eopkg remove --purge '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
                elif operation == "update":
                    cmd = subprocess.Popen('pkexec eopkg upgrade '+self.dewm.get().lower()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)        
        elif os.path.isfile(arch):
            if operation == "install":
                cmd = subprocess.Popen('pkexec pacman -S '+self.dewm.get().lower()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "reinstall":
                cmd = subprocess.Popen('pkexec pacman -S '+self.dewm.get().lower()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "uninstall":
                cmd = subprocess.Popen('pkexec pacman -Rns '+self.dewm.get().lower()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "update":
                cmd = subprocess.Popen('pkexec pacman -Syu '+self.dewm.get().lower()+' --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        if os.path.isfile(en):
            if operation == "install":
                delete_operation(f"Installing {self.dewm.get()}", self.time)
            elif operation == "reinstall":
                delete_operation(f"Reinstalling {self.dewm.get()}", self.time)
            elif operation == "uninstall":
                delete_operation(f"Uninstalling {self.dewm.get()}", self.time)
            elif operation == "update":
                delete_operation(f"Updating {self.dewm.get()}", self.time)
        elif os.path.isfile(tr):
            if operation == "install":
                delete_operation(f"{self.dewm.get()} Kuruluyor", self.time)
            elif operation == "reinstall":
                delete_operation(f"{self.dewm.get()} Yeniden Kuruluyor", self.time)
            elif operation == "uninstall":
                delete_operation(f"{self.dewm.get()} Kaldırılıyor", self.time)
            elif operation == "update":
                delete_operation(f"{self.dewm.get()} Güncelleniyor", self.time)
        self.dewm.configure(state="normal")
        self.button1.configure(state="normal")
        self.button2.configure(state="normal")
        self.button3.configure(state="normal")
        self.button4.configure(state="normal")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class TraditionalScripts(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.button1 = ui.CTkButton(self.frame, text="Update All Packages", command=lambda:self.go_main("update"))
            self.button2 = ui.CTkButton(self.frame, text="Do More Complex Updates\n(etc. Distribution Upgrades)", command=lambda:self.go_main("dist_update"))
            self.button3 = ui.CTkButton(self.frame, text="Clean Package Cache", command=lambda:self.go_main("clean"))
            self.button4 = ui.CTkButton(self.frame, text="Remove Unnecessary Packages", command=lambda:self.go_main("remove"))
            self.button5 = ui.CTkButton(self.frame, text="Fix Broken Dependencies", command=lambda:self.go_main("fix"))
            self.button6 = ui.CTkButton(self.frame, text="Show History", command=lambda:self.go_main("history"))
            self.button7 = ui.CTkButton(self.frame, text="List Installed Packages", command=lambda:self.go_main("list"))
        elif os.path.isfile(tr):
            self.button1 = ui.CTkButton(self.frame, text="Tüm Paketleri Güncelle", command=lambda:self.go_main("update"))
            self.button2 = ui.CTkButton(self.frame, text="Daha Karmaşık Güncellemelar Yap\n(örn. Dağıtım Güncellemeleri)", command=lambda:self.go_main("dist_update"))
            self.button3 = ui.CTkButton(self.frame, text="Paket Önbelleğini Temizle", command=lambda:self.go_main("clean"))
            self.button4 = ui.CTkButton(self.frame, text="Gereksiz Paketleri Kaldır", command=lambda:self.go_main("remove"))
            self.button5 = ui.CTkButton(self.frame, text="Bozuk Bağımlılıkları Düzelt", command=lambda:self.go_main("fix"))
            self.button6 = ui.CTkButton(self.frame, text="Geçmişi Göster", command=lambda:self.go_main("history"))
            self.button7 = ui.CTkButton(self.frame, text="Kurulu Paketleri Listele", command=lambda:self.go_main("list"))            
        if os.path.isfile(solus):
            self.button2.configure(state="disabled")
            self.button5.configure(state="disabled")
        self.button1.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button2.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button6.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button7.grid(row=6, column=0, sticky="nsew", padx=(10, 0))
    def do_main(self, operation: str):
        self.button1.configure(state="disabled")
        self.button2.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.button4.configure(state="disabled")
        self.button5.configure(state="disabled")
        self.button6.configure(state="disabled")
        self.button7.configure(state="disabled")
        self.time = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            if operation == "update":
                add_operation(f"Updating All Packages", self.time)
            elif operation == "dist_update":
                add_operation(f"Doing More Complex Updates", self.time)
            elif operation == "clean":
                add_operation(f"Cleaning Up Package Cache", self.time)
            elif operation == "remove":
                add_operation(f"Removing Unnecessary Packages", self.time)
            elif operation == "fix":
                add_operation(f"Fixing Broken Dependencies", self.time)
            elif operation == "history":
                add_operation(f"Getting History", self.time)
            elif operation == "list":
                add_operation(f"Getting Installed Packages", self.time)
        elif os.path.isfile(tr):
            if operation == "update":
                add_operation(f"Tüm Paketler Güncelleniyor", self.time)
            elif operation == "dist_update":
                add_operation(f"Daha Karmaşık Güncellemeler Yapılıyor", self.time)
            elif operation == "clean":
                add_operation(f"Paket Önbelleği Temizleniyor", self.time)
            elif operation == "remove":
                add_operation(f"Gereksiz Paketler Kaldırılıyor", self.time)
            elif operation == "fix":
                add_operation(f"Bozuk Bağımlılıklar Düzeltiliyor", self.time)
            elif operation == "history":
                add_operation(f"Geçmiş Alınıyor", self.time)
            elif operation == "list":
                add_operation(f"Kurulu Paketler Alınıyor", self.time)
        if os.path.isfile(debian):
            if operation == "update":
                cmd = subprocess.Popen('pkexec apt upgrade -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "dist_update":
                cmd = subprocess.Popen('pkexec apt dist-upgrade -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "clean":
                cmd = subprocess.Popen('pkexec apt-get autoclean -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "remove":
                cmd = subprocess.Popen('pkexec apt autoremove -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "fix":
                cmd = subprocess.Popen('pkexec bash -c "apt-get install -f -y ; dpkg --configure -a ; aptitude install -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "history":
                cmd = subprocess.Popen('cat /var/log/dpkg.log', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "list":
                cmd = subprocess.Popen('dpkg --list | grep ^i', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(fedora):
            if operation == "update":
                cmd = subprocess.Popen('pkexec dnf upgrade -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "dist_update":
                cmd = subprocess.Popen('pkexec dnf distro-sync -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "clean":
                cmd = subprocess.Popen('pkexec dnf clean all -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "remove":
                cmd = subprocess.Popen('pkexec dnf autoremove -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "fix":
                cmd = subprocess.Popen('pkexec dnf repoquery --unsatisfied -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "history":
                cmd = subprocess.Popen('dnf history', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "list":
                cmd = subprocess.Popen('dnf list installed', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(solus):
            if operation == "update":
                cmd = subprocess.Popen('pkexec eopkg upgrade -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "clean":
                cmd = subprocess.Popen('pkexec eopkg dc -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "remove":
                cmd = subprocess.Popen('pkexec eopkg rmf -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "history":
                cmd = subprocess.Popen('eopkg history', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "list":
                cmd = subprocess.Popen('eopkg list-installed', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif os.path.isfile(arch):
            if operation == "update":
                cmd = subprocess.Popen('pkexec pacman -Syu --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "dist_update":
                cmd = subprocess.Popen('pkexec pacman -Syu --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "clean":
                cmd = subprocess.Popen('pkexec pacman -Scc --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "remove":
                cmd = subprocess.Popen('pacman -Qdtq | pacman -Rs - --noconfirm', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "fix":
                cmd = subprocess.Popen('pacman -Dk', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "history":
                cmd = subprocess.Popen('cat /var/log/pacman.log', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif operation == "list":
                cmd = subprocess.Popen('pacman -Q', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        if os.path.isfile(en):
            if operation == "update":
                delete_operation(f"Updating All Packages", self.time)
            elif operation == "dist_update":
                delete_operation(f"Doing More Complex Updates", self.time)
            elif operation == "clean":
                delete_operation(f"Cleaning Up Package Cache", self.time)
            elif operation == "remove":
                delete_operation(f"Removing Unnecessary Packages", self.time)
            elif operation == "fix":
                delete_operation(f"Fixing Broken Dependencies", self.time)
            elif operation == "history":
                delete_operation(f"Getting History", self.time)
            elif operation == "list":
                delete_operation(f"Getting Installed Packages", self.time)
        elif os.path.isfile(tr):
            if operation == "update":
                delete_operation(f"Tüm Paketler Güncelleniyor", self.time)
            elif operation == "dist_update":
                delete_operation(f"Daha Karmaşık Güncellemeler Yapılıyor", self.time)
            elif operation == "clean":
                delete_operation(f"Paket Önbelleği Temizleniyor", self.time)
            elif operation == "remove":
                delete_operation(f"Gereksiz Paketler Kaldırılıyor", self.time)
            elif operation == "fix":
                delete_operation(f"Bozuk Bağımlılıklar Düzeltiliyor", self.time)
            elif operation == "history":
                delete_operation(f"Geçmiş Alınıyor", self.time)
            elif operation == "list":
                delete_operation(f"Kurulu Paketler Alınıyor", self.time)
        self.button1.configure(state="normal")
        self.button2.configure(state="normal")
        self.button3.configure(state="normal")
        self.button4.configure(state="normal")
        self.button5.configure(state="normal")
        self.button6.configure(state="normal")
        self.button7.configure(state="normal")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class FlatpakScripts(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.button1 = ui.CTkButton(self.frame, text="Update All Packages", command=lambda:self.go_main("update -y"))
            self.button2 = ui.CTkButton(self.frame, text="Remove Unnecessary Packages", command=lambda:self.go_main("uninstall --unused -y"))
            self.button3 = ui.CTkButton(self.frame, text="Repair Flatpak Installation", command=lambda:self.go_main("repair"))
            self.button4 = ui.CTkButton(self.frame, text="Show History", command=lambda:self.go_main("history"))
            self.button5 = ui.CTkButton(self.frame, text="List Installed Packages", command=lambda:self.go_main("list"))
        elif os.path.isfile(tr):
            self.button1 = ui.CTkButton(self.frame, text="Tüm Paketleri Güncelle", command=lambda:self.go_main("update -y"))
            self.button2 = ui.CTkButton(self.frame, text="Gereksiz Paketleri Kaldır", command=lambda:self.go_main("uninstall --unused -y"))
            self.button3 = ui.CTkButton(self.frame, text="Flatpak Kurulumunu Onar", command=lambda:self.go_main("repair"))
            self.button4 = ui.CTkButton(self.frame, text="Geçmişi Göster", command=lambda:self.go_main("history"))
            self.button5 = ui.CTkButton(self.frame, text="Kurulu Paketleri Listele", command=lambda:self.go_main("list"))            
        self.button1.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button2.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=4, column=0, sticky="nsew", padx=(10, 0))
    def do_main(self, operation: str):
        self.button1.configure(state="disabled")
        self.button2.configure(state="disabled")
        self.button3.configure(state="disabled")
        self.button4.configure(state="disabled")
        self.button5.configure(state="disabled")
        self.time = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            if operation == "update -y":
                add_operation(f"Updating All Packages (Flatpak)", self.time)
            elif operation == "uninstall --unused -y":
                add_operation(f"Removing Unnecessary Packages (Flatpak)", self.time)
            elif operation == "repair":
                add_operation(f"Repairing Flatpak Installation", self.time)
            elif operation == "history":
                add_operation(f"Getting History (Flatpak)", self.time)
            elif operation == "list":
                add_operation(f"Getting Installed Packages (Flatpak)", self.time)
        elif os.path.isfile(tr):
            if operation == "updat -ye":
                add_operation(f"Tüm Paketler Güncelleniyor (Flatpak)", self.time)
            elif operation == "uninstall --unused -y":
                add_operation(f"Gereksiz Paketler Kaldırılıyor (Flatpak)", self.time)
            elif operation == "repair":
                add_operation(f"Flatpak Kurulumu Onarılıyor", self.time)
            elif operation == "history":
                add_operation(f"Geçmiş Alınıyor (Flatpak)", self.time)
            elif operation == "list":
                add_operation(f"Kurulu Paketler Alınıyor (Flatpak)", self.time)
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
            install_flatpak()
            if ask_f == False:
                if os.path.isfile(en):
                    self.status.configure(text="Ready")
                elif os.path.isfile(tr):
                    self.status.configure(text="Hazır")
                return
        cmd = subprocess.Popen('flatpak '+operation, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        if os.path.isfile(en):
            if operation == "update -y":
                delete_operation(f"Updating All Packages (Flatpak)", self.time)
            elif operation == "uninstall --unused -y":
                delete_operation(f"Removing Unnecessary Packages (Flatpak)", self.time)
            elif operation == "repair":
                delete_operation(f"Repairing Flatpak Installation", self.time)
            elif operation == "history":
                delete_operation(f"Getting History (Flatpak)", self.time)
            elif operation == "list":
                delete_operation(f"Getting Installed Packages (Flatpak)", self.time)
        elif os.path.isfile(tr):
            if operation == "updat -ye":
                delete_operation(f"Tüm Paketler Güncelleniyor (Flatpak)", self.time)
            elif operation == "uninstall --unused -y":
                delete_operation(f"Gereksiz Paketler Kaldırılıyor (Flatpak)", self.time)
            elif operation == "repair":
                delete_operation(f"Flatpak Kurulumu Onarılıyor", self.time)
            elif operation == "history":
                delete_operation(f"Geçmiş Alınıyor (Flatpak)", self.time)
            elif operation == "list":
                delete_operation(f"Kurulu Paketler Alınıyor (Flatpak)", self.time)
        self.button1.configure(state="normal")
        self.button2.configure(state="normal")
        self.button3.configure(state="normal")
        self.button4.configure(state="normal")
        self.button5.configure(state="normal")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class SystemdServices(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.configure(state="disabled")
        self.frame = ui.CTkFrame(self, fg_color="transparent")
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.frame.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Service Name")
            self.button1 = ui.CTkButton(self.frame, text="Status", command=lambda:self.go_main("status"))
            self.button2 = ui.CTkButton(self.frame, text="Enable", command=lambda:self.go_main("enable"))
            self.button3 = ui.CTkButton(self.frame, text="Disable", command=lambda:self.go_main("disable"))
            self.button4 = ui.CTkButton(self.frame, text="Start", command=lambda:self.go_main("start"))
            self.button5 = ui.CTkButton(self.frame, text="Stop", command=lambda:self.go_main("stop"))
        elif os.path.isfile(tr):
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Servis Adı")
            self.button1 = ui.CTkButton(self.frame, text="Durum", command=lambda:self.go_main("status"))
            self.button2 = ui.CTkButton(self.frame, text="Aktifleştir", command=lambda:self.go_main("enable"))
            self.button3 = ui.CTkButton(self.frame, text="Devre Dışı Bırak", command=lambda:self.go_main("disable"))
            self.button4 = ui.CTkButton(self.frame, text="Başlat", command=lambda:self.go_main("start"))
            self.button5 = ui.CTkButton(self.frame, text="Durdur", command=lambda:self.go_main("stop"))
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=5, padx=(10, 0))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=5, column=0, sticky="nsew", padx=(10, 0))
    def do_main(self, operation: str):
        if self.entry.get() == "":
            if os.path.isfile(en):
                mb.showerror("Error", "Please enter service name below.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Lütfen servis adı girin.")
            return
        cmd = subprocess.Popen('pkexec bash -c "SYSTEMD_COLORS=0 systemctl '+operation+' '+self.entry.get()+'"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        main_successful()
    def go_main(self, process: str):
        t = threading.Thread(target=lambda:self.do_main(process), daemon=False)
        t.start()

class Store(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        if os.path.isfile(en):
            self.traditionalpackages = self.tabview.add("Traditional\nPackages")
            self.flatpakpackages = self.tabview.add("Flatpak\nPackages")
            self.dewm = self.tabview.add("Desktop Environments\nWindow Managers")
            self.traditionalscripts = self.tabview.add("Traditional\nScripts")
            self.flatpakscripts = self.tabview.add("Flatpak\nScripts")
            self.systemd = self.tabview.add("Systemd\nServices")
        elif os.path.isfile(tr):
            self.traditionalpackages = self.tabview.add("Geleneksel\nPaketler")
            self.flatpakpackages = self.tabview.add("Flatpak\nPaketleri")
            self.dewm = self.tabview.add("Masaüstü Ortamları\nPencere Yöneticileri")
            self.traditionalscripts = self.tabview.add("Geleneksel\nBetikler")
            self.flatpakscripts = self.tabview.add("Flatpak\nBetikleri")
            self.systemd = self.tabview.add("Systemd\nServisleri")
        self.traditionalpackages.grid_columnconfigure(0, weight=1)
        self.traditionalpackages.grid_rowconfigure(0, weight=1)
        self.traditionalpackages_frame=TraditionalPackages(self.traditionalpackages)
        self.traditionalpackages_frame.grid(row=0, column=0, sticky="nsew")
        self.flatpakpackages.grid_columnconfigure(0, weight=1)
        self.flatpakpackages.grid_rowconfigure(0, weight=1)
        self.flatpakpackages_frame=FlatpakPackages(self.flatpakpackages)
        self.flatpakpackages_frame.grid(row=0, column=0, sticky="nsew")
        self.dewm.grid_columnconfigure(0, weight=1)
        self.dewm.grid_rowconfigure(0, weight=1)
        self.dewm_frame=DEWM(self.dewm)
        self.dewm_frame.grid(row=0, column=0, sticky="nsew")
        self.traditionalscripts.grid_columnconfigure(0, weight=1)
        self.traditionalscripts.grid_rowconfigure(0, weight=1)
        self.traditionalscripts_frame=TraditionalScripts(self.traditionalscripts)
        self.traditionalscripts_frame.grid(row=0, column=0, sticky="nsew")
        self.flatpakscripts.grid_columnconfigure(0, weight=1)
        self.flatpakscripts.grid_rowconfigure(0, weight=1)
        self.flatpakscripts_frame=FlatpakScripts(self.flatpakscripts)
        self.flatpakscripts_frame.grid(row=0, column=0, sticky="nsew")
        self.systemd.grid_columnconfigure(0, weight=1)
        self.systemd.grid_rowconfigure(0, weight=1)
        self.systemd_frame=SystemdServices(self.systemd)
        self.systemd_frame.grid(row=0, column=0, sticky="nsew")

class BashZshButtons(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.var = ui.StringVar(value=".bashrc")
        self.option = ui.CTkSwitch(self, text="Bash / Zsh", offvalue=".bashrc", onvalue=".zshrc", command=self.switch, variable=self.var)
        self.option.grid(row=0, column=0, sticky="ns", padx=0, pady=2.5, columnspan=3)
        if os.path.isfile(en):
            self.label1 = ui.CTkLabel(self, text="Add Without Colors")
            self.button1 = ui.CTkButton(self, text="My Username", command=self.username1)
            self.button2 = ui.CTkButton(self, text="System Information", command=self.systeminfo1)
            self.button3 = ui.CTkButton(self, text="Memory Consumption", command=self.memory1)
            self.label2 = ui.CTkLabel(self, text="Add With Colors")
            self.button4 = ui.CTkButton(self, text="My Username ", command=self.username2)
            self.button5 = ui.CTkButton(self, text="System Information", command=self.systeminfo2)
            self.button6 = ui.CTkButton(self, text="Memory Consumption", command=self.memory2)
            self.label3 = ui.CTkLabel(self, text="Undo")
            self.button7 = ui.CTkButton(self, text="Last Change", command=self.undo1)
            self.button8 = ui.CTkButton(self, text="Changes In This Session", command=self.undo2)
            self.button9 = ui.CTkButton(self, text="All Changes", command=self.undo3)
        elif os.path.isfile(tr):
            self.label1 = ui.CTkLabel(self, text="Renkler Olmadan Ekle")
            self.button1 = ui.CTkButton(self, text="Kullanıcı Adım", command=self.username1)
            self.button2 = ui.CTkButton(self, text="Sistem Bilgisi", command=self.systeminfo1)
            self.button3 = ui.CTkButton(self, text="RAM Tüketimi", command=self.memory1)
            self.label2 = ui.CTkLabel(self, text="Renklerle Ekle")
            self.button4 = ui.CTkButton(self, text="Kullanıcı Adım", command=self.username2)
            self.button5 = ui.CTkButton(self, text="Sistem Bilgisi", command=self.systeminfo2)
            self.button6 = ui.CTkButton(self, text="RAM Tüketimi", command=self.memory2)
            self.label3 = ui.CTkLabel(self, text="Geri Al")
            self.button7 = ui.CTkButton(self, text="Son Değişiklik", command=self.undo1)
            self.button8 = ui.CTkButton(self, text="Bu Oturumdaki Değişiklikler", command=self.undo2)
            self.button9 = ui.CTkButton(self, text="Tüm Değişiklikler", command=self.undo3)
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
    def switch(self):
        if self.var.get() == ".bashrc" and not os.path.isfile("/usr/bin/bash") and not os.path.isfile("/bin/bash"):
                install_app("Bash", "bash")
        elif self.var.get() == ".zshrc" and not os.path.isfile("/usr/bin/zsh") and not os.path.isfile("/bin/zsh"):
                install_app("Zsh", "zsh")
    def successful(self):
        if os.path.isfile(en):
            mb.showinfo("Information","Configuration completed.")
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme","Yapılandırma tamamlandı.")
    def username1(self):
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        if os.path.isfile(en):
            os.system(f"echo 'echo Hello {username}!' >> /home/{username}/{self.var.get()}")
        elif os.path.isfile(tr):
            os.system(f"echo 'echo Merhabalar {username}!' >> /home/{username}/{self.var.get()}")
        self.successful()
    def username2(self):
        if not os.path.isfile("/usr/bin/lolcat") and not os.path.isfile("/bin/lolcat"):
            install_app("Lolcat", "lolcat")
            if ask_a == False:
                return
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        if os.path.isfile(en):
            os.system(f"echo 'echo Hello {username}! | lolcat' >> /home/{username}/{self.var.get()}")
        elif os.path.isfile(tr):
            os.system(f"echo 'echo Merhabalar {username}! | lolcat' >> /home/{username}/{self.var.get()}")
        self.successful()
    def systeminfo1(self):
        if not os.path.isfile("/usr/bin/neofetch") and not os.path.isfile("/bin/neofetch"):
            install_app("Neofetch", "neofetch")
            if ask_a == False:
                return
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        os.system(f"echo 'neofetch' >> /home/{username}/{self.var.get()}")
        self.successful()
    def systeminfo2(self):
        if not os.path.isfile("/usr/bin/neofetch") and not os.path.isfile("/bin/neofetch"):
            install_app("Neofetch", "neofetch")
            if ask_a == False:
                return
        if not os.path.isfile("/usr/bin/lolcat") and not os.path.isfile("/bin/lolcat"):
            install_app("Lolcat", "lolcat")
            if ask_a == False:
                return
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        os.system(f"echo 'neofetch | lolcat' >> /home/{username}/{self.var.get()}")
        self.successful()
    def memory1(self):
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        os.system(f"echo 'free -h' >> /home/{username}/{self.var.get()}")
        self.successful()
    def memory2(self):
        if not os.path.isfile("/usr/bin/lolcat") and not os.path.isfile("/bin/lolcat"):
            install_app("Lolcat", "lolcat")
            if ask_a == False:
                return
        os.system(f"cp /home/{username}/{self.var.get()} /home/{username}/{self.var.get()}-grelintb.bak")
        os.system(f"echo 'free -h | lolcat' >> /home/{username}/{self.var.get()}")
        self.successful()
    def undo1(self):
        os.system(f"cp /home/{username}/{self.var.get()}-grelintb.bak /home/{username}/{self.var.get()}")
        self.successful()
    def undo2(self):
        os.system(f"cp /home/{username}/{self.var.get()}-session-grelintb.bak /home/{username}/{self.var.get()}")
        self.successful()
    def undo3(self):
        os.system(f"cp /home/{username}/{self.var.get()}-first-grelintb.bak /home/{username}/{self.var.get()}")
        self.successful()

class BashZshFile(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.textbox = ui.CTkTextbox(self)
        self.var = ui.StringVar(value="bash")
        self.option = ui.CTkSwitch(self, text="Bash / Zsh", offvalue="bash", onvalue="zsh", command=self.switch, variable=self.var)
        self.option.grid(row=0, column=0, sticky="ns", padx=0, pady=2.5)
        with open("/home/"+username+"/.bashrc", "r") as self.bashrc:
            self.content = self.bashrc.read()
        self.textbox.insert("0.0", self.content)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        if os.path.isfile(en):
            self.button = ui.CTkButton(self, text="Save", command=self.save)
        elif os.path.isfile(tr):
            self.button = ui.CTkButton(self, text="Kaydet", command=self.save)
        self.button.grid(row=2, column=0, sticky="nsew", pady=2.5)
    def switch(self):
        if self.var.get() == "bash":
            if not os.path.isfile("/usr/bin/bash") and not os.path.isfile("/bin/bash"):
                install_app("Bash", "bash")
            with open("/home/"+username+"/.bashrc", "r") as self.bashrc:
                self.content = self.bashrc.read()
        elif self.var.get() == "zsh":
            if not os.path.isfile("/usr/bin/zsh") and not os.path.isfile("/bin/zsh"):
                install_app("Zsh", "zsh")
            with open("/home/"+username+"/.zshrc", "r") as self.zshrc:
                self.content = self.zshrc.read()
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", self.content)
    def save(self):
        if self.var.get() == "bash":
            os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
            with open("/home/"+username+"/.bashrc", "w+") as self.file:
                self.file.write(self.textbox.get("0.0", 'end'))
            with open("/home/"+username+"/.bashrc") as self.file:
                self.output = self.file.read()
        elif self.var.get() == "zsh":
            os.system("cp /home/"+username+"/.zshrc /home/"+username+"/.zshrc-grelintb.bak")
            with open("/home/"+username+"/.zshrc", "w+") as self.file:
                self.file.write(self.textbox.get("0.0", 'end'))
            with open("/home/"+username+"/.zshrc") as self.file:
                self.output = self.file.read()
        if self.output == self.textbox.get("0.0", 'end'):
            if os.path.isfile(en):
                mb.showinfo("Information","The configuration saved.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","Yapılandırma kaydedildi.")
        else:
            if os.path.isfile(en):
                mb.showerror("Error","The configuration could not be saved.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Yapılandırma kaydedilemedi.")

class BashZsh(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, fg_color="transparent")
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        if os.path.isfile(f"/home/{username}/.bashrc"):
            os.system("cd /home/"+username+" ; cp .bashrc .bashrc-session-grelintb.bak")
        if os.path.isfile(f"/home/{username}/.zshrc"):
            os.system("cd /home/"+username+" ; cp .zshrc .zshrc-session-grelintb.bak")
        if os.path.isfile(en):
            self.buttons_tab = self.tabview.add("Options")
            self.file_tab = self.tabview.add("File")
        elif os.path.isfile(tr):
            self.buttons_tab = self.tabview.add("Seçenekler")
            self.file_tab = self.tabview.add("Dosya")
        self.buttons_tab.grid_columnconfigure(0, weight=1)
        self.buttons_tab.grid_rowconfigure(0, weight=1)
        self.file_tab.grid_columnconfigure(0, weight=1)
        self.file_tab.grid_rowconfigure(0, weight=1)
        self.buttons_frame = BashZshButtons(self.buttons_tab, fg_color="transparent").grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.file_frame = BashZshFile(self.file_tab, fg_color="transparent").grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

class ComputerName(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)
        with open("/etc/hostname", "r") as file:
            computername = file.read()
        if os.path.isfile(en):
            self.label = ui.CTkLabel(self, text="Computer's current name: "+computername)
            self.entry = ui.CTkEntry(self, placeholder_text="Enter a new name for computer.")
            self.button = ui.CTkButton(self, text="Apply", command=self.apply)
        elif os.path.isfile(tr):
            self.label = ui.CTkLabel(self, text="Bilgisayarın mevcut ismi: "+computername)
            self.entry = ui.CTkEntry(self, placeholder_text="Bilgisayar için yeni bir isim girin.")
            self.button = ui.CTkButton(self, text="Uygula", command=self.apply)
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
        if os.path.isfile(en):
            self.label = ui.CTkLabel(self, text="The source of the information is the distributions' own websites and my own knowledge and experience.")
        elif os.path.isfile(tr):
            self.label = ui.CTkLabel(self, text="Bilgilerin kaynağı dağıtımların kendi internet siteleri ve kendi bilgilerim ile deneyimleridir.")
        self.label.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.tabview = ui.CTkTabview(self)
        self.tabview.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.distro1 = self.tabview.add("MX Linux")
        self.distro2 = self.tabview.add("Linux Mint")
        self.distro3 = self.tabview.add("Endeavour")
        self.distro4 = self.tabview.add("Debian")
        self.distro5 = self.tabview.add("Manjaro")
        self.distro6 = self.tabview.add("Ubuntu")
        self.distro7 = self.tabview.add("Fedora")
        self.distro8 = self.tabview.add("Pop!_OS")
        self.distro9 = self.tabview.add("Zorin")
        self.distro10 = self.tabview.add("OpenSUSE")
        self.distro1.grid_columnconfigure(0, weight=1)
        self.distro1.grid_rowconfigure(0, weight=1)
        self.distro2.grid_columnconfigure(0, weight=1)
        self.distro2.grid_rowconfigure(0, weight=1)
        self.distro3.grid_columnconfigure(0, weight=1)
        self.distro3.grid_rowconfigure(0, weight=1)
        self.distro4.grid_columnconfigure(0, weight=1)
        self.distro4.grid_rowconfigure(0, weight=1)
        self.distro5.grid_columnconfigure(0, weight=1)
        self.distro5.grid_rowconfigure(0, weight=1)
        self.distro6.grid_columnconfigure(0, weight=1)
        self.distro6.grid_rowconfigure(0, weight=1)
        self.distro7.grid_columnconfigure(0, weight=1)
        self.distro7.grid_rowconfigure(0, weight=1)
        self.distro8.grid_columnconfigure(0, weight=1)
        self.distro8.grid_rowconfigure(0, weight=1)
        self.distro9.grid_columnconfigure(0, weight=1)
        self.distro9.grid_rowconfigure(0, weight=1)
        self.distro10.grid_columnconfigure(0, weight=1)
        self.distro10.grid_rowconfigure(0, weight=1)
        if os.path.isfile(en):
            self.text1 = ui.CTkLabel(self.distro1, text="MX Linux is a cooperative venture between the antiX and MX Linux communities."+
                "\nDesigned to combine high stability and robust performance."+
                "\nMX's graphical tools and tools from antiX make it easy to use.")
            self.button1 = ui.CTkButton(self.distro1, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))
            self.text2 = ui.CTkLabel(self.distro2, text="Linux Mint is designed to work out of the box."+
                "\nIt comes fully equipped with the applications most people need."+
                "\n\nNote from GrelinTB developer: I really recommend it for first time Linux users.")
            self.button2 = ui.CTkButton(self.distro2, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
            self.text3 = ui.CTkLabel(self.distro3, text="EndeavorOS doesn't bother installing Arch manually."+
                "\nwithout the hassle of installing it manually for both x86_64 and ARM systems."+
                "\nAfter installation, you’re provided with good environment and guide.")
            self.button3 = ui.CTkButton(self.distro3, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
            self.text4 = ui.CTkLabel(self.distro4, text="Debian, although very old, is still supported."+
                "\nToday, most of distributions are based on it."+
                "\nDebian offers a very stable experience, but this makes it less up-to-date.")
            self.button4 = ui.CTkButton(self.distro4, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
            self.text5 = ui.CTkLabel(self.distro5, text="Manjaro is a distribution based on Arch Linux. It is aimed at the end user."+
                "\n\nNote from GrelinTB developer: If you are going to use the Arch base, I suggest you look for other alternatives.")
            self.button5 = ui.CTkButton(self.distro5, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
            self.text6 = ui.CTkLabel(self.distro6, text="Ubuntu targets many audiences. There are many variants."+
                "\n\nNote from GrelinTB developer: In Ubuntu, telemetry is turned on by default, but it can be turned off."+
                "\nAt worst, it forces you to use Snap. Personally, I prefer Flatpak over Snap."+
                "\nPersonally, instead of Ubuntu, I recommend Linux Mint with Pop!_OS.")
            self.button6 = ui.CTkButton(self.distro6, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
            self.text7 = ui.CTkLabel(self.distro7, text="Fedora is powered by Red Hat. Fedora is the test environment for RHEL."+
                "\nFedora has many spins for different desktop environments."+
                "\n\nNote from GrelinTB developer: I think Fedora is the middle ground of ease, stability, up-to-date."+
                "\nFedora is one of the distributions I recommend and like.")
            self.button7 = ui.CTkButton(self.distro7, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
            self.text8 = ui.CTkLabel(self.distro8, text="Pop!_OS is an Ubuntu based distribution developed by System76."+
                "\nIt offers a separate download option for Nvidia users."+
                "\nBy default it uses Systemd-boot instead of GRUB."+
                "\nIt currently uses customized GNOME, but its own desktop environment (Cosmic) is being built.")
            self.button8 = ui.CTkButton(self.distro8, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
            self.text9 = ui.CTkLabel(self.distro9, text="Target audience is users migrating from Windows and Mac."+
                "\nIts purpose is ease of use."+
                "\n\nNote from GrelinTB developer: I find the Pro version logic absurd."+
                "\nBecause I think Zorin OS has no advantages over the others.")
            self.button9 = ui.CTkButton(self.distro9, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
            self.text10 = ui.CTkLabel(self.distro10, text="The only distribution here that GrelinTB does not support."+
                "\nIt targets many audiences and has its own tools. Its tools are often praised."+
                "\nTumbleweed (more up-to-date), Leap (more stable).")
            self.button10 = ui.CTkButton(self.distro10, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True))
        elif os.path.isfile(tr):
            self.text1 = ui.CTkLabel(self.distro1, text="MX Linux, antiX ve MX Linux toplulukları arasında bir işbirliği girişimidir."+
                "\nYüksek kararlılık ve sağlam performansla birleştirmek için tasarlanmıştır."+
                "\nMX'in grafiksel araçları ve antiX'in araçları kullanımı kolaylaştırır.")
            self.button1 = ui.CTkButton(self.distro1, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))
            self.text2 = ui.CTkLabel(self.distro2, text="Linux Mint, kutudan çıktığı gibi çalışmak üzere tasarlanmıştır."+
                "\nÇoğu insanın ihtiyaç duyduğu uygulamalarla tam donanımlı olarak gelir."+
                "\n\nGrelinTB geliştiricisinin notu: İlk kez Linux kullanacaklar için gerçekten öneririm.")
            self.button2 = ui.CTkButton(self.distro2, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
            self.text3 = ui.CTkLabel(self.distro3, text="EndeavourOS, Arch'ı manuel olarak yükleme zahmetine sokmaz."+
                "\nKendisi Arch deneyimi sağlayan Arch tabanlı bir dağıtımdır."+
                "\nKurulumdan sonra, size iyi bir ortam ve rehber sağlanır.")
            self.button3 = ui.CTkButton(self.distro3, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
            self.text4 = ui.CTkLabel(self.distro4, text="Debian, çok eski olmasına rağmen halen desteklenmektedir."+
                "\nBugün çoğu dağıtım onu taban alır."+
                "\nDebian çok stabil bir deneyim sunar fakat bu güncelliği azaltır.")
            self.button4 = ui.CTkButton(self.distro4, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
            self.text5 = ui.CTkLabel(self.distro5, text="Manjaro, Arch Linux tabanlı bir dağıtımdır. Son kullanıcıyı hedef alır."+
                "\n\nGrelinTB geliştiricisinin notu: Arch tabanı kullanacaksanız başka alternatiflere yönelmenizi öneririm.")
            self.button5 = ui.CTkButton(self.distro5, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
            self.text6 = ui.CTkLabel(self.distro6, text="Ubuntu birçok kitleyi hedefler. Birçok türevi vardır."+
                "\n\nGrelinTB geliştiricisinin notu: Ubuntu'da varsayılan olarak telemetriler açık gelir ama kapıtabilir."+
                "\nEn kötüsü ise sizi Snap kullanmaya zorlar. Şahsen ben Snap yerine Flatpak tercih ederim."+
                "\nŞahsen Ubuntu yerine, Pop!_OS ile Linux Mint öneririm.")
            self.button6 = ui.CTkButton(self.distro6, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
            self.text7 = ui.CTkLabel(self.distro7, text="Fedora, Red Hat tarafından desteklenmektedir. Fedora, RHEL için test ortamıdır."+
                "\nFedora'nın farklı masaüstü ortamları için birçok döndürmesi vardır."+
                "\n\nGrelinTB geliştiricisinin notu: Bence Fedora; kolaylığın, stabilliğin, güncelliğin tam ortasıdır."+
                "\nFedora, önerdiğim ve sevdiğim dağıtımlardandır.")
            self.button7 = ui.CTkButton(self.distro7, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
            self.text8 = ui.CTkLabel(self.distro8, text="Pop!_OS, System76 tarafından geliştirilen Ubuntu tabanlı bir dağıtımdır."+
                "\nNvidia kullanıcıları için ayrı bir indirme seçeneği sunar."+
                "\nVarsayılan olarak GRUB yerine Systemd-boot kullanır."+
                "\nŞu anda özelleştirilmiş GNOME kullanmakta fakat kendi masaüstü ortamı (Cosmic) yapılmakta.")
            self.button8 = ui.CTkButton(self.distro8, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
            self.text9 = ui.CTkLabel(self.distro9, text="Hedef kitlesi Windows'tan ve Mac'ten geçen kullanıcılardır."+
                "\nAmacı ise kullanım kolaylığıdır."
                "\n\nGrelinTB geliştiricisinin notu: Ben Pro sürüm mantığını saçma buluyorum."+
                "\nÇünkü bence Zorin OS'un diğerlerine göre artısı yok.")
            self.button9 = ui.CTkButton(self.distro9, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
            self.text10 = ui.CTkLabel(self.distro10, text="Burada GrelinTB'nin desteklemediği tek dağıtım."+
                "\nBirçok kitleyi hedef alır ve kendi araçları vardır. Araçları çok sık övülmektedir."+
                "\nTumbleweed (daha güncel), Leap (daha stabil) olarak ikiye ayrılır.")
            self.button10 = ui.CTkButton(self.distro10, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True))
        self.text1.grid(row=0, column=0, sticky="nsew")
        self.button1.grid(row=1, column=0, sticky="nsew")
        self.text2.grid(row=0, column=0, sticky="nsew")
        self.button2.grid(row=1, column=0, sticky="nsew")
        self.text3.grid(row=0, column=0, sticky="nsew")
        self.button3.grid(row=1, column=0, sticky="nsew")
        self.text4.grid(row=0, column=0, sticky="nsew")
        self.button4.grid(row=1, column=0, sticky="nsew")
        self.text5.grid(row=0, column=0, sticky="nsew")
        self.button5.grid(row=1, column=0, sticky="nsew")
        self.text6.grid(row=0, column=0, sticky="nsew")
        self.button6.grid(row=1, column=0, sticky="nsew")
        self.text7.grid(row=0, column=0, sticky="nsew")
        self.button7.grid(row=1, column=0, sticky="nsew")
        self.text8.grid(row=0, column=0, sticky="nsew")
        self.button8.grid(row=1, column=0, sticky="nsew")
        self.text9.grid(row=0, column=0, sticky="nsew")
        self.button9.grid(row=1, column=0, sticky="nsew")
        self.text10.grid(row=0, column=0, sticky="nsew")
        self.button10.grid(row=1, column=0, sticky="nsew")

class Calculator(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        if os.path.isfile(en):
            self.history_label = ui.CTkLabel(self, height=15, font=ui.CTkFont(size=13, weight="bold"), text="Previous Calculations")
            self.history_button = ui.CTkButton(self, text="Delete History", command=self.delete_history)
            self.button12 = ui.CTkButton(self, text="Clear", command=lambda:self.entry.delete(0, "end")).grid(row=3, column=3, sticky="nsew", pady=2.5, padx=2.5)
        elif os.path.isfile(tr):
            self.history_label = ui.CTkLabel(self, height=15, font=ui.CTkFont(size=13, weight="bold"), text="Önceki Hesaplamalar")
            self.history_button = ui.CTkButton(self, text="Geçmişi Temizle", command=self.delete_history)
            self.button12 = ui.CTkButton(self, text="Temizle", command=lambda:self.entry.delete(0, "end")).grid(row=3, column=3, sticky="nsew", pady=2.5, padx=2.5)
        self.entry = ui.CTkEntry(self)
        self.history_text = ui.CTkTextbox(self, fg_color="transparent")
        if os.path.isfile("/home/"+username+"/.calc-history-grelintb.txt"):
            with open("/home/"+username+"/.calc-history-grelintb.txt", "r") as self.file:
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
            with open("/home/"+username+"/.calc-history-grelintb.txt", "a+") as self.file:
                self.file.write(self.process+"="+self.result+"\n")
            with open("/home/"+username+"/.calc-history-grelintb.txt", "r") as self.file:
                self.output = self.file.read()
            self.history_text.configure(state="normal")
            self.history_text.delete("0.0", "end")
            self.history_text.insert("0.0", self.output)
            self.history_text.configure(state="disabled")
        except Exception as e:
            if os.path.isfile(en):
                mb.showerror("Error", "Possible syntax error: "+str(e)+"\nPlease try again.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Muhtemel sözdizimi hatası: "+str(e)+"\nLütfen tekrar deneyin.")
    def delete_history(self):
        subprocess.Popen("rm /home/"+username+"/.calc-history-grelintb.txt", shell=True)
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
        if os.path.isfile(en):
            self.bashzsh = self.tabview.add("Configure Bash and Zsh")
            self.computername = self.tabview.add("Change Computer's Name")
            self.distros = self.tabview.add("About Some Distributions")
            self.calculator = self.tabview.add("Calculator")
        elif os.path.isfile(tr):
            self.bashzsh = self.tabview.add("Bash'ı ve Zsh'ı Yapılandır")
            self.computername = self.tabview.add("Bilgisayarın Adını Değiştir")
            self.distros = self.tabview.add("Bazı Dağıtımlar Hakkında")
            self.calculator = self.tabview.add("Hesaplayıcı")
        self.bashzsh.grid_columnconfigure(0, weight=1)
        self.bashzsh.grid_rowconfigure(0, weight=1)
        self.bashzsh_frame=BashZsh(self.bashzsh, fg_color="transparent")
        self.bashzsh_frame.grid(row=0, column=0, sticky="nsew")
        self.computername.grid_columnconfigure(0, weight=1)
        self.computername.grid_rowconfigure(0, weight=1)
        self.computername_frame=ComputerName(self.computername, fg_color="transparent")
        self.computername_frame.grid(row=0, column=0, sticky="nsew")
        self.distros.grid_columnconfigure(0, weight=1)
        self.distros.grid_rowconfigure(0, weight=1)
        self.distros_frame=Distros(self.distros)
        self.distros_frame.grid(row=0, column=0, sticky="nsew")
        self.calculator.grid_columnconfigure(0, weight=1)
        self.calculator.grid_rowconfigure(0, weight=1)
        self.distros_frame=Calculator(self.calculator)
        self.distros_frame.grid(row=0, column=0, sticky="nsew")

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
            if os.path.isfile(en):
                mb.showinfo("Birthday","Today is the birthday of GrelinTB developer MuKonqi (Muhammed S.)!\nI hope he updated the information on his website on time this time :D")
            elif os.path.isfile(tr):
                mb.showinfo("Doğum Günü","Bugün GrelinTB geliştiricisi MuKonqi'nin (Muhammed S.) doğum günü!\nUmarım sitesindeki bilgiyi bu sefer zamanında güncellemiştir :D")
        if dt.datetime.now().weekday() == 0:
            self.check_update_thread = threading.Thread(target=lambda:Sidebar.check_update(self, "startup"), daemon=True)
            self.check_update_thread.start()
        if os.path.isfile(en):
            self.tab_startup = self.tabview.add("Startup")
            self.tab_notes_and_documents = self.tabview.add("Notes and Documents")
            self.tab_store = self.tabview.add("Store")
            self.tab_tools = self.tabview.add("Tools")
        elif os.path.isfile(tr):
            self.tab_startup = self.tabview.add("Başlangıç")
            self.tab_notes_and_documents = self.tabview.add("Notlar ve Belgeler")
            self.tab_store = self.tabview.add("Mağaza")
            self.tab_tools = self.tabview.add("Araçlar")
        self.tab_startup.grid_columnconfigure(0, weight=1)
        self.tab_startup.grid_rowconfigure(0, weight=1)
        self.startup_frame=Startup(self.tab_startup)
        self.startup_frame.grid(row=0, column=0, sticky="nsew")
        self.tab_notes_and_documents.grid_columnconfigure(0, weight=1)
        self.tab_notes_and_documents.grid_rowconfigure(0, weight=1)
        self.notes_and_documents_frame=NotesAndDocuments(self.tab_notes_and_documents)
        self.notes_and_documents_frame.grid(row=0, column=0, sticky="nsew")
        self.tab_store.grid_columnconfigure(0, weight=1)
        self.tab_store.grid_rowconfigure(0, weight=1)
        self.store_frame=Store(self.tab_store)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        self.tab_tools.grid_columnconfigure(0, weight=1)
        self.tab_tools.grid_rowconfigure(0, weight=1)
        self.tools_frame=Tools(self.tab_tools)
        self.tools_frame.grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    if "help" in sys.argv[1:] or "yardım" in sys.argv[1:]:
        if os.path.isfile(en):
            print("This is GrelinTB's help page.\nGrelinTB is great toolbox for some Linux distros.")
            print("Current version: "+version_current)
            print("Developer:       MuKonqi (Muhammed S.)")
            print("License:         GPLv3+")
            print("Credits:         Lolcat (for colorful commands in terminal), wttr.in (for weather forecast), Google Material Symbols (for application icon)")
            print("List of all parameters for GrelinTB:")
            print("  help:          Show this page")
            print("  grelintb:      Open website of GrelinTB's GitHub repository")
            print("  version:       Show changelog of "+version_current)
            print("  developer:     Open website of GrelinTB developer")
            print("  license:       Show license text of GPLv3")
            print("  reset:         Reset GrelinTB")
            print("  update:        Update GrelinTB")
            print("  uninstall:     Uninstall GrelinTB")  
            exit("                 Start GrelinTB normally (default)")
        elif os.path.isfile(tr):
            print("Bu GrelinTB'nin yardım sayfasıdır.\nGrelinTB bazı Linux dağıtımları için harika bir araç kutusudur.")
            print("Şimdiki sürüm:   "+version_current)
            print("Geliştirici:     MuKonqi (Muhammed S.)")
            print("Lisans:          GPLv3+")
            print("Krediler:        Lolcat (terminalde renkli komutlar için), wttr.in (hava durumu için), Google Material Symbols (uygulama ikonu için)")            
            print("GrelinTB için tüm parametrelerin listesi:")
            print("  yardım:        Bu sayfayı göster")
            print("  grelintb:      GrelinTB'nin GitHub deposunu aç")
            print("  sürüm:         "+version_current+" sürümünün değişik günlüğünü göster")
            print("  geliştirici:   GrelinTB geliştiricisinin internet sitesini aç")
            print("  lisans:        GPLv3 lisansının metnini göster")
            print("  sıfırla:       GrelinTB'yı sıfırla")
            print("  güncelle:      GrelinTB'yı güncelle")
            print("  kaldır:        GrelinTB'yı kaldır")
            exit("                 GrelinTB'yi normal olarak aç (varsayılan)")
    elif "grelintb" in sys.argv[1:]:
        subprocess.Popen("xdg-open https://github.com/mukonqi/grelintb", shell=True)
        exit()
    elif "version" in sys.argv[1:] or "sürüm" in sys.argv[1:]:
        if os.path.isfile(en):
            with open("/usr/local/bin/grelintb/changelog-en.txt", "r") as cc_file:
                cc_text = cc_file.read()
            exit("  Current version's ("+version_current+") changelog is below:\n"+cc_text)
        elif os.path.isfile(tr):
            with open("/usr/local/bin/grelintb/changelog-tr.txt", "r") as cc_file:
                cc_text = cc_file.read()
            exit("  Şimdiki sürümün ("+version_current+") değişiklik günlüğü aşağıdadır:\n"+cc_text)
    elif "developer" in sys.argv[1:] or "geliştirici" in sys.argv[1:]:
        subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True)
        exit()
    elif "license" in sys.argv[1:] or "lisans" in sys.argv[1:]:
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as l_file:
            l_text = l_file.read()
        exit(l_text)
    elif "reset" in sys.argv[1:] or "sıfırla" in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/update.sh")
        if os.path.isfile(en):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            exit("GrelinTB has been reset.")
        elif os.path.isfile(tr):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            exit("GrelinTB sıfırlandı.")
    elif "update" in sys.argv[1:] or "güncelle" in sys.argv[1:]:
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            if os.path.isfile(en):
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-en.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
                question = input("  New version's ("+version_latest+") changelog is below:\n"+cl_text+"\n\nDo you want update to "+version_latest+" version? [y/n]: ")
            elif os.path.isfile(tr):
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-tr.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
                question = input("  Yeni sürümün ("+version_latest+") değişiklik günlüğü aşağıdadır:\n"+cl_text+"\n\n"+version_latest+" sürümüne güncellemek ister misiniz? [e/h]: ")
            if question.lower() == "y" or question.lower() == "e":
                os.system("pkexec /usr/local/bin/grelintb/update.sh")
                if os.path.isfile(en):
                    exit("GrelinTB has been updated.")
                elif os.path.isfile(tr):
                    exit("GrelinTB güncellendi.")
        else:
            if os.path.isfile(en):
                exit("GrelinTB is up to date.")
            elif os.path.isfile(tr):
                exit("GrelinTB güncel.")
    elif "uninstall" in sys.argv[1:] or "kaldır" in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        os.system("cd /home/"+username+" ; rm .*-grelintb*")
        if os.path.isfile(en):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            exit("See you! GrelinTB uninstalled from your system.")
        elif os.path.isfile(tr):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            exit("Görüşürüz! GrelinTB sisteminizden kaldırıldı.")
    else:
        root = Root(className="grelintb")
        root.mainloop()