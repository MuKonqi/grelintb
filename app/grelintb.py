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

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
solus = "/etc/solus-release"
arch1 = "/bin/pacman"
arch2 = "/usr/bin/pacman"

if os.getuid() == 0:
    exit("GrelinTB already asks you for root rights when the need arises. Exiting...")
if not os.path.isfile(debian) and not os.path.isfile(fedora) and not os.path.isfile(solus) and not os.path.isfile(arch1) and not os.path.isfile(arch2):
    exit("The distribution you are using is not supported from GrelinTB. Exiting...")

import sys
import locale
import getpass
import threading
import subprocess
import datetime as dt
from tkinter import messagebox as mb
from tkinter import filedialog as fd

try:
    import customtkinter as ui
except:
    try:
        try:
            print("Installing CustomTkinter...")
            os.system("pip install customtkinter")
            import customtkinter as ui 
        except:
            print("Installing CustomTkinter with --break-system-packages parameter...")
            os.system("pip install customtkinter --break-system-packages")
            import customtkinter as ui
    except Exception as e:
        print("Error: "+str(e)+". So opening the Issues page and then exiting...")
        os.system("xdg-open https://github.com/MuKonqi/grelintb/issues")
        exit(1)

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
s_true = "/home/"+username+"/.config/grelintb/startup/true.txt"
s_false = "/home/"+username+"/.config/grelintb/startup/false.txt"

with open("/usr/local/bin/grelintb/version.txt", "r") as version_file:
    version_current = version_file.readline()

if not os.path.isdir(config):
    os.system("cd /home/"+username+"/.config ; mkdir grelintb")
if not os.path.isdir(config+"language/"):
    if locale.getlocale()[0] == "tr_TR":
        os.system("cd "+config+" ; mkdir language ; cd language ; touch tr.txt")
    else:
        os.system("cd "+config+" ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(config+"theme/"):
    os.system("cd "+config+" ; mkdir theme ; cd theme ; touch system.txt")
if not os.path.isdir(config+"color/"):
    os.system("cd "+config+" ; mkdir color ; cd color ; touch dark-blue.txt")
if not os.path.isdir(config+"startup/"):
    os.system("cd "+config+" ; mkdir startup ; cd startup ; touch false.txt")
if not os.path.isdir(notes):
    os.system("cd /home/"+username+" ; mkdir Notes")
if not os.path.isfile("/home/"+username+"/.bashrc-first-grelintb.bak"):
    os.system("cd /home/"+username+" ; cp .bashrc .bashrc-first-grelintb.bak")

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

def running(process: str):
    if os.path.isfile(en):
        status.configure(text="Status:\n"+process+" Package(s)")
    elif os.path.isfile(tr):
        status.configure(text="Durum:\nPaket(ler) "+process)
def normal():
    if os.path.isfile(en):
        status.configure(text="Status: Ready")
    elif os.path.isfile(tr):
        status.configure(text="Durum: Hazır")

def restart_system():
    global ask_r
    if os.path.isfile(en):
        ask_r = mb.askyesno("Warning", "Your system needs to be restarted for the changes to be completed.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_r = mb.askyesno("Uyarı", "Değişikliklerin tamamlanması için sisteminizin yeniden başlatılması gerekiyor.\nOnaylıyor musunuz?")
    if ask_r == True:
        os.system("pkexec reboot")

def install_app(appname: str, packagename: str):
    global ask_a
    if os.path.isfile(en):
        ask_a = mb.askyesno("Warning", appname+" can't found on your system.\nWe can try installing "+appname+" to your computer.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_a = mb.askyesno("Uyarı", appname+" sisteminizde bulunamadı.\nBiz sisteminize "+appname+" yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
    if ask_a == True:
        running(installing)
        if os.path.isfile(debian):
            cmd = os.system('pkexec apt install '+packagename+" -y")
        elif os.path.isfile(fedora):
            cmd = os.system('pkexec dnf install '+packagename+" -y")
        elif os.path.isfile(solus):
            cmd = os.system('pkexec eopkg install '+packagename+" -y")
        elif os.path.isfile(arch1) or os.path.isfile(arch2):
            cmd = os.system('pkexec pacman -S '+packagename+" --noconfirm")
        normal()
    elif ask_a == False:
        if os.path.isfile(en):
            mb.showerror("Error", appname+" installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", appname+" kurulumu ve işlem iptal edildi.")
def install_flatpak():
    global ask_f
    if os.path.isfile(en):
        ask_f = mb.askyesno("Warning", "Flatpak package manager can't found on your system.\nWe can try installing Flatpak package manager to your computer.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_f = mb.askyesno("Uyarı", "Flatpak paket yöneticisi sisteminizde bulunamadı.\nBiz sisteminize Flatpak paket yöneticisi yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
    if ask_f == True:
        running(installing)
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
        elif os.path.isfile(arch1) or os.path.isfile(arch2):
            cmd1 = os.system('pkexec pacman -S flatpak --noconfirm')
            restart_system()
        if ask_r == False:
            ask_f = False
            if os.path.isfile(en):
                mb.showinfo("Information", "Flatpak package manager installation could not be completed, process cancelled.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme", "Flatpak paket yöneticisi kurulumu tamamlanamadı, işlem iptal edildi.")
        normal()
    elif ask_f == False:
        if os.path.isfile(en):
            mb.showerror("Error", "Flatpak package manager installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", "Flatpak paket yöneticisi kurulumu ve işlem iptal edildi.")

def main_successful():
    if os.path.isfile(en):
        mb.showinfo("Information","Process completed.")
    elif os.path.isfile(tr):
        mb.showinfo("Bilgilendirme","İşlem tamamlandı.")

class Sidebar(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global status
        self.grid_rowconfigure((4, 8), weight=1)
        self.text = ui.CTkButton(self, text="GrelinTB", command=lambda:subprocess.Popen("xdg-open https://github.com/mukonqi/grelintb", shell=True), font=ui.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color=("gray14", "gray84"))
        self.language_menu = ui.CTkOptionMenu(self, values=["English", "Türkçe"], command=self.change_language)
        if os.path.isfile(s_true):
            self.startup_var = ui.StringVar(value="on")
        elif os.path.isfile(s_false):
            self.startup_var = ui.StringVar(value="off")
        if os.path.isfile(en):
            self.version_b = ui.CTkButton(self, text="Version: "+version_current, command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Developer: MuKonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_and_credits_b = ui.CTkButton(self, text="License and Credits", command=self.license_and_credits, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Update", command=self.check_update)
            self.reset_b = ui.CTkButton(self, text="Reset", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Uninstall", command=self.uninstall)
            self.startup = ui.CTkCheckBox(self, text="Startup Informations\n(Increases Time)", command=self.startup_option, variable=self.startup_var, onvalue="on", offvalue="off")
            self.color_label = ui.CTkLabel(self, text="Color Theme:", anchor="w")
            self.color_menu = ui.CTkOptionMenu(self, values=["Dark Blue", "Blue", "Green"], command=self.change_color)                
            self.appearance_label = ui.CTkLabel(self, text="Appearance:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Language:", anchor="w")
            status = ui.CTkLabel(self, text="Status: Ready", font=ui.CTkFont(size=12, weight="bold"))
            self.language_menu.set("English")
            if os.path.isfile(system):
                self.appearance_menu.set("System")
            elif os.path.isfile(light):
                self.appearance_menu.set("Light")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Dark")
            if os.path.isfile(dark_blue):
                self.color_menu.set("Dark Blue")
            elif os.path.isfile(blue):
                self.color_menu.set("Blue")
            elif os.path.isfile(green):
                self.color_menu.set("Green")
        elif os.path.isfile(tr):
            self.version_b = ui.CTkButton(self, text="Sürüm: "+version_current, command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Geliştirici: MuKonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_and_credits_b = ui.CTkButton(self, text="Lisans ve Krediler", command=self.license_and_credits, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Güncelle", command=self.check_update)
            self.reset_b = ui.CTkButton(self, text="Sıfırla", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Kaldır", command=self.uninstall)
            self.startup = ui.CTkCheckBox(self, text="Başlangıç Bilgileri\n(Süreyi Arttırır)", command=self.startup_option, variable=self.startup_var, onvalue="on", offvalue="off")
            self.color_label = ui.CTkLabel(self, text="Renk Teması:", anchor="w")
            self.color_menu = ui.CTkOptionMenu(self, values=["Koyu Mavi", "Mavi", "Yeşil"], command=self.change_color)            
            self.appearance_label = ui.CTkLabel(self, text="Görünüm:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["Sistem", "Açık", "Koyu"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Dil:", anchor="w")
            status = ui.CTkLabel(self, text="Durum: Hazır", font=ui.CTkFont(size=12, weight="bold"))
            self.language_menu.set("Türkçe")
            if os.path.isfile(system):
                self.appearance_menu.set("Sistem")
            elif os.path.isfile(light):
                self.appearance_menu.set("Açık")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Koyu")
            if os.path.isfile(dark_blue):
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
        self.startup.grid(row=9, column=0, padx=10, pady=(0, 5))
        self.color_label.grid(row=10, column=0, padx=10, pady=(5, 0))
        self.color_menu.grid(row=11, column=0, padx=10, pady=(0, 5))
        self.appearance_label.grid(row=12, column=0, padx=10, pady=(5, 0))
        self.appearance_menu.grid(row=13, column=0, padx=10, pady=(0, 5))
        self.language_label.grid(row=14, column=0, padx=10, pady=(5, 0))
        self.language_menu.grid(row=15, column=0, padx=10, pady=(0, 5))
        status.grid(row=16, column=0, padx=10, pady=(0, 5))
    def changelog(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("600x600")
        self.window.minsize(600, 600)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.window.title("Changelog For "+version_current)
            self.label = ui.CTkLabel(self.window, text="Current version: "+version_current+"\nThe changelog for the "+version_current+" version is below:", font=ui.CTkFont(size=16, weight="bold"))
            with open("/usr/local/bin/grelintb/changelog-en.txt", "r") as cc_file:
                cc_text = cc_file.read()
        elif os.path.isfile(tr):
            self.window.title(version_current+" için Değişiklik Günlüğü")
            self.label = ui.CTkLabel(self.window, text="Şuanki sürüm: "+version_current+"\n\n"+version_current+" sürümünün değişiklik günlüğü aşağıdadır:", font=ui.CTkFont(size=16, weight="bold"))
            with open("/usr/local/bin/grelintb/changelog-tr.txt", "r") as cc_file:
                cc_text = cc_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", cc_text)
        self.textbox.configure(state="disabled")
        self.label.grid(row=0, column=0, sticky="nsew", pady=10)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    def license_and_credits(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("600x600")
        self.window.minsize(600, 600)
        self.window.grid_rowconfigure((1), weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.window.title("License And Credits")
            self.label1 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Copyright (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB licensed under GPLv3 or later.")
            self.label2 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Credits")
        elif os.path.isfile(tr):
            self.window.title("Lisans Ve Krediler")
            self.label1 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Telif Hakkı (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB GPLv3 veya sonrası altında lisanslanmıştır.")
            self.label2 = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Krediler")
        self.button1 = ui.CTkButton(self.window, text="Neofetch", command=lambda:subprocess.Popen("xdg-open https://github.com/dylanaraps/neofetch", shell=True))
        self.button2 = ui.CTkButton(self.window, text="Lolcat", command=lambda:subprocess.Popen("xdg-open https://github.com/busyloop/lolcat", shell=True))
        self.button3 = ui.CTkButton(self.window, text="wttr.in", command=lambda:subprocess.Popen("xdg-open https://github.com/chubin/wttr.in", shell=True))
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as license_file:
            license_text = license_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", license_text)
        self.textbox.configure(state="disabled")
        self.label1.grid(row=0, column=0, sticky="nsew", pady=10)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=20)
        self.label2.grid(row=2, column=0, sticky="nsew", pady=10)
        self.button1.grid(row=3, column=0, sticky="nsew", padx=50, pady=5)
        self.button2.grid(row=4, column=0, sticky="nsew", padx=50, pady=5)
        self.button3.grid(row=5, column=0, sticky="nsew", padx=50, pady=(5, 10))
    def uninstall(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        os.system("cd /home/"+username+" ; rm .bashrc*-grelintb.bak")
        if os.path.isfile(en):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("See you!","GrelinTB uninstalled from your system.")
        elif os.path.isfile(tr):
            os.system("cd /home/"+username+"/.config ; rm -rf grelintb")
            mb.showinfo("Görüşürüz!","GrelinTB sisteminizden kaldırıldı.")
        exit()
    def update(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/update.sh")
        if os.path.isfile(en):
            mb.showinfo("Successful", "GrelinTB updated.")
        elif os.path.isfile(tr):
            mb.showinfo("Başarılı", "GrelinTB güncellendi.")
        os.system("grelintb")
        exit()
    def check_update(self):
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            self.window = ui.CTkToplevel()
            self.window.geometry("600x600")
            self.window.minsize(600, 600)
            self.window.grid_rowconfigure(1, weight=1)
            self.window.grid_columnconfigure(0, weight=1)
            if os.path.isfile(en):
                self.window.title("Changelog For "+version_latest)
                self.label = ui.CTkLabel(self.window, text="New version found: "+version_latest+"\n\nThe changelog for the "+version_latest+" version is below:", font=ui.CTkFont(size=16, weight="bold"))
                self.button = ui.CTkButton(self.window, text="Update To\n"+version_latest, command=self.update)
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-en.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(tr):
                self.window.title(version_latest+" için Değişiklik Günlüğü")
                self.label = ui.CTkLabel(self.window, text="Yeni sürüm bulundu: "+version_latest+"\n\n"+version_latest+" sürümünün değişiklik günlüğü aşağıdadır:", font=ui.CTkFont(size=16, weight="bold"))
                self.button = ui.CTkButton(self.window, text=version_latest+" Sürümüne Güncelle", command=self.update) 
                cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-tr.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.textbox = ui.CTkTextbox(self.window)
            self.textbox.insert("0.0", cl_text)
            self.label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
            self.textbox.grid(row=1, column=0, sticky="nsew", padx=50, pady=10)
            self.button.grid(row=2, column=0, sticky="nsew", padx=100, pady=10)
            self.textbox.configure(state="disabled")
        else:
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
    def startup_option(self):
        if self.startup_var.get() == "on":
            os.system("cd "+config+"startup/ ; rm * ; touch true.txt")
        elif self.startup_var.get() == "off":
            os.system("cd "+config+"startup/ ; rm * ; touch false.txt")
    def change_color(self, new_color: str):
        if new_color == "Dark Blue" or new_color == "Koyu Mavi":
            os.system("cd "+config+"color ; rm * ; touch dark-blue.txt")
        elif new_color == "Blue" or new_color == "Mavi":
            os.system("cd "+config+"color ; rm * ; touch blue.txt")
        elif new_color == "Green" or new_color == "Yeşil":
            os.system("cd "+config+"color ; rm * ; touch green.txt")
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

class Starting(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        if os.path.isfile(s_true):
            self.grid_rowconfigure(3, weight=1)
            self.grid_columnconfigure(0, weight=1)
            if os.path.isfile(en):
                self.label0 = ui.CTkLabel(self, text="Welcome "+username+"!", font=ui.CTkFont(size=25, weight="bold"))
                self.label1 = ui.CTkLabel(self, text="Weather Forecast\nSystem Information", font=ui.CTkFont(size=15, weight="normal"))
                self.weather = subprocess.Popen('curl -H "Accept-Language: en" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(tr):
                self.label0 = ui.CTkLabel(self, text="Merhabalar "+username+"!", font=ui.CTkFont(size=25, weight="bold"))
                self.label1 = ui.CTkLabel(self, text="Hava Durumu\nSistem Bilgileri", font=ui.CTkFont(size=15, weight="normal"))
                self.weather = subprocess.Popen('curl -H "Accept-Language: tr" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.label0.grid(row=0, column=0, pady=(0, 10))
            self.label1.grid(row=1, column=0, pady=(0, 10))
            self.textbox1 = ui.CTkTextbox(self, fg_color="transparent", height=25)
            self.textbox1.grid(row=2, column=0, sticky="nsew")
            self.textbox2 = ui.CTkTextbox(self, fg_color="transparent")
            self.textbox2.grid(row=3, column=0, sticky="nsew")
            self.system = subprocess.Popen('neofetch --stdout', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.textbox1.insert("0.0", self.weather)
            self.textbox1.configure(state="disabled")
            self.textbox2.insert("0.0", self.system)
            self.textbox2.configure(state="disabled")
        elif os.path.isfile(s_false):
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            if os.path.isfile(en):
                self.label0 = ui.CTkLabel(self, text="Welcome\n"+username, font=ui.CTkFont(size=80, weight="normal"))
            elif os.path.isfile(tr):
                self.label0 = ui.CTkLabel(self, text="Merhabalar\n"+username, font=ui.CTkFont(size=80, weight="normal"))
            self.label0.grid(row=0, column=0, sticky="nsew")

class Notes(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.file_a = None
        self.file_l = None
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.content = ui.CTkTextbox(self)
        self.content.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.tabview = ui.CTkTabview(self, fg_color="transparent")
        self.tabview.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        if os.path.isfile(en):
            self.from_list = self.tabview.add("From List")
            self.any = self.tabview.add("Any")
        elif os.path.isfile(tr):
            self.from_list = self.tabview.add("Listeden")
            self.any = self.tabview.add("Herhangi")
        self.from_list.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.from_list.grid_columnconfigure(0, weight=1),
        self.any.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.any.grid_columnconfigure(0, weight=1)
        self.command = subprocess.Popen('ls '+notes, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        self.list = ui.CTkTextbox(self.from_list, fg_color="transparent")
        self.list.insert("0.0", self.command)
        self.list.configure(state="disabled")
        if os.path.isfile(en):
            self.label1 = ui.CTkLabel(self.from_list, text="If you have taken notes, they are listed below:")
            self.entry1 = ui.CTkEntry(self.from_list, placeholder_text="Please enter note name.")
            self.button11 = ui.CTkButton(self.from_list, text="Open", command=self.open_list)
            self.button12 = ui.CTkButton(self.from_list, text="Delete", command=self.delete_list)
            self.button13 = ui.CTkButton(self.from_list, text="Save", command=self.save_list)
            self.label2 = ui.CTkLabel(self.any, text="- You can enter the note name yourself.\n- Do not enter it to select it with the file dialog.")
            self.entry2 = ui.CTkEntry(self.any, placeholder_text="Act according to the instructions above.")
            self.button21 = ui.CTkButton(self.any, text="Open", command=self.open_any)
            self.button22 = ui.CTkButton(self.any, text="Delete", command=self.delete_any)
            self.button23 = ui.CTkButton(self.any, text="Save", command=self.save_any)
        elif os.path.isfile(tr):
            self.label1 = ui.CTkLabel(self.from_list, text="Notlar aldıysanız aşağıda listelenmiştir:")
            self.entry1 = ui.CTkEntry(self.from_list, placeholder_text="Lütfen not adı girin.")
            self.button11 = ui.CTkButton(self.from_list, text="Aç", command=self.open_list)
            self.button12 = ui.CTkButton(self.from_list, text="Sil", command=self.delete_list)
            self.button13 = ui.CTkButton(self.from_list, text="Kaydet", command=self.save_list)
            self.label2 = ui.CTkLabel(self.any, text="- Kendiniz not adı girebilirsiniz.\n- Dosya diyoloğu ile seçmek için girmeyin.")
            self.entry2 = ui.CTkEntry(self.any, placeholder_text="Üstteki yönergeye göre davranın.")
            self.button21 = ui.CTkButton(self.any, text="Aç", command=self.open_any)
            self.button22 = ui.CTkButton(self.any, text="Sil", command=self.delete_any)
            self.button23 = ui.CTkButton(self.any, text="Kaydet", command=self.save_any)
        self.label1.grid(row=0, column=0, sticky="nsew", pady=0, padx=(15, 0))
        self.list.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.entry1.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button11.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button12.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button13.grid(row=5, column=0, sticky="nsew", pady=(0, 0), padx=(15, 0))
        self.label2.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.entry2.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button21.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button22.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(15, 0))
        self.button23.grid(row=4, column=0, sticky="nsew", pady=0, padx=(15, 0))
    def open_error(self):
        if os.path.isfile(en):
            mb.showerror("Error","The note could not be opened.")
        elif os.path.isfile(tr):
            mb.showerror("Hata","Not açılamadı.")
    def no_note_error(self):
        if os.path.isfile(en):
            mb.showerror("Error","There is no such note.")
        elif os.path.isfile(tr):
            mb.showerror("Hata","Öyle bir not yok.")
    def delete_error(self):
        if os.path.isfile(en):
            mb.showerror("Error","The note could not be deleted.")
        elif os.path.isfile(tr):
            mb.showerror("Hata","Not silinemedi.")
    def delete_successful(self):
        if os.path.isfile(en):
            mb.showinfo("Information","The note deleted.")
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme","Not silindi.")
    def save_successful(self):
        if os.path.isfile(en):
            mb.showinfo("Information","The note saved.")
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme","Not kaydedildi.")
    def save_error(self):
        if os.path.isfile(en):
            mb.showerror("Error","The note could not be saved.")
        elif os.path.isfile(tr):
            mb.showerror("Hata","Not kaydedilemedi.")
    def open_list(self):
        try:
            with open(notes+self.entry1.get(), "r") as self.file_l:
                self.text = self.file_l.read()
        except:
            self.open_error()
            return
        self.content.delete("0.0", 'end')
        self.content.insert("0.0", self.text)
    def delete_list(self):
        if not os.path.isfile(notes+self.entry1.get()):
            self.no_note_error()
            return
        os.system("cd "+notes+" ; rm '"+self.entry1.get()+"'")
        if os.path.isfile(notes+self.entry1.get()):
            self.delete_error()
        else:
            self.delete_successful()
        self.list.configure(state="normal")
        self.list.delete("0.0", 'end')
        self.command = subprocess.Popen('ls '+notes, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        self.list.insert("0.0", self.command)
        self.list.configure(state="disabled")
    def save_list(self):
        if self.entry1.get() == None:
            if os.path.isfile(en):
                mb.showerror("Error","You did not enter a note name.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Not adı girmediniz.")
            return
        with open(notes+self.entry1.get(), "w+") as self.file:
            self.file.write(self.content.get("0.0", 'end'))
        with open(notes+self.entry1.get()) as self.file:
            self.output = self.file.read()
        self.list.configure(state="normal")
        self.list.delete("0.0", 'end')
        self.command = subprocess.Popen('ls '+notes, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        self.list.insert("0.0", self.command)
        self.list.configure(state="disabled")
        if self.output == self.content.get("0.0", 'end'):
            self.save_successful()
        else:
            self.save_error()
    def open_any(self):
        if self.entry2.get() == "":
            try:
                self.file_a = fd.askopenfilename()
                with open(self.file_a, "r") as self.file_ao:
                    self.text = self.file_ao.read()
                self.entry2.insert(0, self.file_a)
            except:
                self.open_error()
                return
        else:
            try:
                with open(self.entry2.get(), "r") as self.file_a:
                    self.text = self.file_a.read()
            except:
                self.open_error()
                return
        self.content.delete("0.0", 'end')
        self.content.insert("0.0", self.text)
    def delete_any(self):
        if not os.path.isfile(self.entry2.get()):
            self.no_note_error()
            return
        os.system("rm '"+self.entry2.get()+"'")
        if os.path.isfile(self.entry2.get()):
            self.delete_error()
        else:
            self.delete_successful()
    def save_any(self):
        with open(self.entry2.get(), "w+") as self.file:
            self.file.write(self.content.get("0.0", 'end'))
        with open(self.entry2.get()) as self.file:
            self.output = self.file.read()
        if self.output == self.content.get("0.0", 'end'):
            self.save_successful()
        else:
            self.save_error()

class Store(ui.CTkFrame):
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
        self.frame.grid_rowconfigure((3, 4, 5, 6), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.repos_var = ui.StringVar(value = "repos")
        if os.path.isfile(en):
            self.source = ui.CTkLabel(self.frame, text="Source")
            self.repos = ui.CTkSwitch(self.frame, text="Repositories/Flathub", offvalue="repos", onvalue="flathub", variable=self.repos_var, command=self.repos_go)
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Please enter package name.")
            self.button1 = ui.CTkButton(self.frame, text="Search", command=self.go_search)
            self.button2 = ui.CTkButton(self.frame, text="Install", command=self.go_install)
            self.button3 = ui.CTkButton(self.frame, text="Reinstall", command=self.go_reinstall)
            self.button4 = ui.CTkButton(self.frame, text="Uninstall", command=self.go_uninstall)
        elif os.path.isfile(tr):
            self.source = ui.CTkLabel(self.frame, text="Kaynak")
            self.repos = ui.CTkSwitch(self.frame, text="Depolar/Flathub", offvalue="repos", onvalue="flathub", variable=self.repos_var, command=self.repos_go)
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Lütfen paket adı girin.")
            self.button1 = ui.CTkButton(self.frame, text="Ara", command=self.go_search)
            self.button2 = ui.CTkButton(self.frame, text="Kur", command=self.go_install)
            self.button3 = ui.CTkButton(self.frame, text="Yeniden Kur", command=self.go_reinstall)
            self.button4 = ui.CTkButton(self.frame, text="Kaldır", command=self.go_uninstall)
        self.source.grid(row=0, column=0, sticky="nsew", pady=0, padx=(25, 0))
        self.repos.grid(row=1, column=0, sticky="nsew", pady=0, padx=(25, 0))
        self.entry.grid(row=2, column=0, sticky="nsew", pady=(20, 0), padx=(25, 0))
        self.button1.grid(row=3, column=0, sticky="nsew", pady=(20, 5), padx=(25, 0))
        self.button2.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(25, 0))
        self.button3.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(25, 0))
        self.button4.grid(row=6, column=0, sticky="nsew", padx=(25, 0))
    def repos_main(self):
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak") and self.repos_var.get() == "flathub":
            install_flatpak()
    def repos_go(self):
        t = threading.Thread(target=self.repos_main, daemon=False)
        t.start()
    def search_main(self):
        running(searching)
        if self.repos_var.get() == "repos":
            if os.path.isfile(debian):
                cmd = subprocess.Popen('apt search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(fedora):
                cmd = subprocess.Popen('dnf search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(solus):
                cmd = subprocess.Popen('eopkg search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(arch1) or os.path.isfile(arch2):
                cmd = subprocess.Popen('pacman -Ss '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                install_flatpak()
                if ask_f == False:
                    return
            cmd = subprocess.Popen('flatpak search '+self.entry.get(), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        normal()
        main_successful()
    def go_search(self):
        t = threading.Thread(target=self.search_main, daemon=False)
        t.start()
    def install_main(self):
        running(installing)
        if self.repos_var.get() == "repos":
            if os.path.isfile(debian):
                cmd = subprocess.Popen('pkexec apt install '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(fedora):
                cmd = subprocess.Popen('pkexec dnf install '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(solus):
                cmd = subprocess.Popen('pkexec eopkg install '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(arch1) or os.path.isfile(arch2):
                cmd = subprocess.Popen('pkexec pacman -S '+self.entry.get()+" --noconfirm", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                install_flatpak()
                if ask_f == False:
                    return
            cmd = subprocess.Popen('flatpak install '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()   
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        normal()
        main_successful()
    def go_install(self):
        t = threading.Thread(target=self.install_main, daemon=False)
        t.start()
    def reinstall_main(self):
        running(reinstalling)
        if self.repos_var.get() == "repos":
            if os.path.isfile(debian):
                cmd = subprocess.Popen('pkexec apt install --reinstall '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(fedora):
                cmd = subprocess.Popen('pkexec dnf reinstall '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(solus):
                cmd = subprocess.Popen('pkexec eopkg install --reinstall '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(arch1) or os.path.isfile(arch2):
                cmd = subprocess.Popen('pkexec pacman -S '+self.entry.get()+" --noconfirm", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                install_flatpak()
                if ask_f == False:
                    return
            cmd = subprocess.Popen('flatpak install '+self.entry.get()+' -y --reinstall', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        normal()
        main_successful()
    def go_reinstall(self):
        t = threading.Thread(target=self.reinstall_main, daemon=False)
        t.start()
    def uninstall_main(self):
        running(uninstalling)
        if self.repos_var.get() == "repos":
            if os.path.isfile(debian):
                cmd = subprocess.Popen('pkexec apt remove '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(fedora):
                cmd = subprocess.Popen('pkexec dnf remove '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(solus):
                cmd = subprocess.Popen('pkexec eopkg remove '+self.entry.get()+" -y", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
            elif os.path.isfile(arch1) or os.path.isfile(arch2):
                cmd = subprocess.Popen('pkexec pacman -Rs '+self.entry.get()+" --noconfirm", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                install_flatpak()
                if ask_f == False:
                    return
            cmd = subprocess.Popen('flatpak uninstall '+self.entry.get()+' -y', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        (out, err) = cmd.communicate()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", (out+err))
        self.textbox.configure(state="disabled")
        normal()
        main_successful()
    def go_uninstall(self):
        t = threading.Thread(target=self.uninstall_main, daemon=False)
        t.start()

class Bashrc(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        os.system("cd /home/"+username+" ; cp .bashrc .bashrc-session-grelintb.bak")
        if os.path.isfile(en):
            self.label1 = ui.CTkLabel(self, text="Without Colors")
            self.button1 = ui.CTkButton(self, text="Add My Username", command=self.username1)
            self.button2 = ui.CTkButton(self, text="Add System Info", command=self.systeminfo1)
            self.button3 = ui.CTkButton(self, text="Add Memory Consumption", command=self.memory1)
            self.label2 = ui.CTkLabel(self, text="With Colors")
            self.button4 = ui.CTkButton(self, text="Add My Username ", command=self.username2)
            self.button5 = ui.CTkButton(self, text="Add System Info", command=self.systeminfo2)
            self.button6 = ui.CTkButton(self, text="Add Memory Consumption", command=self.memory2)
            self.label3 = ui.CTkLabel(self, text="Undo Options")
            self.button7 = ui.CTkButton(self, text="Undo Last Change", command=self.undo1)
            self.button8 = ui.CTkButton(self, text="Undo Changes In This Session", command=self.undo2)
            self.button9 = ui.CTkButton(self, text="Undo Changes Mate So Far", command=self.undo3)
        elif os.path.isfile(tr):
            self.label1 = ui.CTkLabel(self, text="Renkler Olmadan")
            self.button1 = ui.CTkButton(self, text="Kullanıcı Adımı Ekle", command=self.username1)
            self.button2 = ui.CTkButton(self, text="Sistem Bilgisini", command=self.systeminfo1)
            self.button3 = ui.CTkButton(self, text="RAM Tüketimini Ekle", command=self.memory1)
            self.label2 = ui.CTkLabel(self, text="Renklerle")
            self.button4 = ui.CTkButton(self, text="Kullanıcı Adımı Ekle", command=self.username2)
            self.button5 = ui.CTkButton(self, text="Sistem Bilgisini Ekle", command=self.systeminfo2)
            self.button6 = ui.CTkButton(self, text="RAM Tüketimini Ekle", command=self.memory2)
            self.label3 = ui.CTkLabel(self, text="Geri Alma Seçenekleri")
            self.button7 = ui.CTkButton(self, text="Son Değişikliği Geri Al", command=self.undo1)
            self.button8 = ui.CTkButton(self, text="Bu Oturumdaki Değişiklikleri Geri Al", command=self.undo2)
            self.button9 = ui.CTkButton(self, text="Bugüne Kadar Yapılan Değişiklikleri Geri Al", command=self.undo3)
        self.label1.grid(row=0, column=0, sticky="nsew", pady=20, padx=10)
        self.button1.grid(row=1, column=0, sticky="nsew", pady=20, padx=10)
        self.button2.grid(row=2, column=0, sticky="nsew", pady=20, padx=10)
        self.button3.grid(row=3, column=0, sticky="nsew", pady=20, padx=10)
        self.label2.grid(row=0, column=1, sticky="nsew", pady=20, padx=10)
        self.button4.grid(row=1, column=1, sticky="nsew", pady=20, padx=10)
        self.button5.grid(row=2, column=1, sticky="nsew", pady=20, padx=10)
        self.button6.grid(row=3, column=1, sticky="nsew", pady=20, padx=10)
        self.label3.grid(row=0, column=2, sticky="nsew", pady=20, padx=10)
        self.button7.grid(row=1, column=2, sticky="nsew", pady=20, padx=10)
        self.button8.grid(row=2, column=2, sticky="nsew", pady=20, padx=10)
        self.button9.grid(row=3, column=2, sticky="nsew", pady=20, padx=10)
    def successful(self):
        if os.path.isfile(en):
            mb.showinfo("Information",".bashrc configuration completed.")
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme",".bashrc yapılandırması tamamlandı.")
    def username1(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        if os.path.isfile(en):
            os.system("echo 'echo Hello "+username+"!' >> /home/"+username+"/.bashrc")
        elif os.path.isfile(tr):
            os.system("echo 'echo Merhabalar "+username+"!' >> /home/"+username+"/.bashrc")
        self.successful()
    def username2(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        if os.path.isfile(en):
            os.system("echo 'echo Hello "+username+"! | lolcat' >> /home/"+username+"/.bashrc")
        elif os.path.isfile(tr):
            os.system("echo 'echo Merhabalar "+username+"! | lolcat' >> /home/"+username+"/.bashrc")
        self.successful()
    def systeminfo1(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        os.system("echo 'neofetch' >> /home/"+username+"/.bashrc")
        self.successful()
    def systeminfo2(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        os.system("echo 'neofetch | lolcat' >> /home/"+username+"/.bashrc")
        self.successful()
    def memory1(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        os.system("echo 'free -h' >> /home/"+username+"/.bashrc")
        self.successful()
    def memory2(self):
        os.system("cp /home/"+username+"/.bashrc /home/"+username+"/.bashrc-grelintb.bak")
        os.system("echo 'free -h | lolcat' >> /home/"+username+"/.bashrc")
        self.successful()
    def undo1(self):
        os.system("cp /home/"+username+"/.bashrc-grelintb.bak /home/"+username+"/.bashrc")
        self.successful()
    def undo2(self):
        os.system("cp /home/"+username+"/.bashrc-session-grelintb.bak /home/"+username+"/.bashrc")
        self.successful()
    def undo3(self):
        os.system("cp /home/"+username+"/.bashrc-first-grelintb.bak /home/"+username+"/.bashrc")
        self.successful()

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
        self.label.grid(row=0, column=0, sticky="nsew", padx=80, pady=(20, 0))
        self.entry.grid(row=1, column=0, sticky="nsew", padx=80, pady=40)
        self.button.grid(row=2, column=0, sticky="nsew", padx=80, pady=40)
    def apply(self):
        subprocess.Popen("pkexec grelintb pcrename "+self.entry.get(), shell=True)

class OpenFM(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.button1 = ui.CTkButton(self, text="Nautilus", command=self.go_nautilus)
        self.button2 = ui.CTkButton(self, text="Nemo", command=self.go_nemo)
        self.button3 = ui.CTkButton(self, text="Caja", command=self.go_caja)
        self.button4 = ui.CTkButton(self, text="Thunar", command=self.go_thunar)
        self.button5 = ui.CTkButton(self, text="PCManFM", command=self.go_pcmanfm)
        self.button6 = ui.CTkButton(self, text="PCManFM-Qt", command=self.go_pcmanfmqt)
        self.button1.grid(row=0, column=0, sticky="nsew", padx=50, pady=10)
        self.button2.grid(row=1, column=0, sticky="nsew", padx=50, pady=10)
        self.button3.grid(row=2, column=0, sticky="nsew", padx=50, pady=10)
        self.button4.grid(row=3, column=0, sticky="nsew", padx=50, pady=10)
        self.button5.grid(row=4, column=0, sticky="nsew", padx=50, pady=10)
        self.button6.grid(row=5, column=0, sticky="nsew", padx=50, pady=10)
    def main_nautilus(self):
        if not os.path.isfile("/usr/bin/nautilus") and not os.path.isfile("/bin/nautilus"):
            install_app("Nautilus", "nautilus")
            if ask_a == False:
                return
        subprocess.Popen("pkexec nautilus", shell=True)
    def go_nautilus(self):
        t = threading.Thread(target=self.main_nautilus, daemon=False)
        t.start()
    def main_nemo(self):
        if not os.path.isfile("/usr/bin/nemo") and not os.path.isfile("/bin/nemo"):
            install_app("Nemo", "nemo")
            if ask_a == False:
                return
        subprocess.Popen("pkexec nemo", shell=True)
    def go_nemo(self):
        t = threading.Thread(target=self.main_nemo, daemon=False)
        t.start()
    def main_caja(self):
        if not os.path.isfile("/usr/bin/caja") and not os.path.isfile("/bin/caja"):
            install_app("Caja", "caja")
            if ask_a == False:
                return
        subprocess.Popen("pkexec caja", shell=True)
    def go_caja(self):
        t = threading.Thread(target=self.main_caja, daemon=False)
        t.start()
    def main_thunar(self):
        if not os.path.isfile("/usr/bin/thunar") and not os.path.isfile("/bin/thunar"):
            install_app("Thunar", "thunar")
            if ask_a == False:
                return
        subprocess.Popen("pkexec thunar", shell=True)
    def go_thunar(self):
        t = threading.Thread(target=self.main_thunar, daemon=False)
        t.start()
    def main_pcmanfm(self):
        if not os.path.isfile("/usr/bin/pcmanfm") and not os.path.isfile("/bin/pcmanfm"):
            install_app("PCManFM", "pcmanfm")
            if ask_a == False:
                return
        subprocess.Popen("pkexec pcmanfm", shell=True)
    def go_pcmanfm(self):
        t = threading.Thread(target=self.main_pcmanfm, daemon=False)
        t.start()
    def main_pcmanfmqt(self):
        if not os.path.isfile("/usr/bin/pcmanfm-qt") and not os.path.isfile("/bin/pcmanfm-qt"):
            install_app("PcMANFM-Qt", "pcmanfm-qt")
            if ask_a == False:
                return
        subprocess.Popen("pkexec pcmanfm-qt", shell=True)
    def go_pcmanfmqt(self):
        t = threading.Thread(target=self.main_pcmanfmqt, daemon=False)
        t.start()

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
        distro1 = self.tabview.add("MX Linux")
        distro2 = self.tabview.add("Linux Mint")
        distro3 = self.tabview.add("Endeavour OS")
        distro4 = self.tabview.add("Debian GNU/Linux")
        distro5 = self.tabview.add("Manjaro")
        distro6 = self.tabview.add("Ubuntu")
        distro7 = self.tabview.add("Fedora Linux")
        distro8 = self.tabview.add("Pop!_OS by System76")
        distro9 = self.tabview.add("Zorin OS")
        distro10 = self.tabview.add("OpenSUSE")
        distro1.grid_columnconfigure(0, weight=1)
        distro1.grid_rowconfigure(0, weight=1)
        distro2.grid_columnconfigure(0, weight=1)
        distro2.grid_rowconfigure(0, weight=1)
        distro3.grid_columnconfigure(0, weight=1)
        distro3.grid_rowconfigure(0, weight=1)
        distro4.grid_columnconfigure(0, weight=1)
        distro4.grid_rowconfigure(0, weight=1)
        distro5.grid_columnconfigure(0, weight=1)
        distro5.grid_rowconfigure(0, weight=1)
        distro6.grid_columnconfigure(0, weight=1)
        distro6.grid_rowconfigure(0, weight=1)
        distro7.grid_columnconfigure(0, weight=1)
        distro7.grid_rowconfigure(0, weight=1)
        distro8.grid_columnconfigure(0, weight=1)
        distro8.grid_rowconfigure(0, weight=1)
        distro9.grid_columnconfigure(0, weight=1)
        distro9.grid_rowconfigure(0, weight=1)
        distro10.grid_columnconfigure(0, weight=1)
        distro10.grid_rowconfigure(0, weight=1)
        if os.path.isfile(en):
            self.text1 = ui.CTkLabel(distro1, text="MX Linux is a cooperative venture between the antiX and MX Linux communities."+
                "\nIt is a family of operating systems that are designed to combine elegant and efficient desktops with high stability and solid performance."+
                "\nMX's graphical tools and tools from antiX make it easy to use.")
            self.button1 = ui.CTkButton(distro1, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))
            self.text2 = ui.CTkLabel(distro2, text="Linux Mint is an operating system for desktop and laptop computers."+
                "\nIt is designed to work 'out of the box' and comes fully equipped with the apps most people need."+
                "\n\nNote from GrelinTB developer: I highly recommend Linux Mint for first time Linux users. It is really easy to use.")
            self.button2 = ui.CTkButton(distro2, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
            self.text3 = ui.CTkLabel(distro3, text="EndeavourOS is an Arch-based distro that provides an Arch experience"+
                "\nwithout the hassle of installing it manually for both x86_64 and ARM systems."+
                "\nAfter installation, you’re provided with good environment and guide.")
            self.button3 = ui.CTkButton(distro3, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
            self.text4 = ui.CTkLabel(distro4, text="Debian GNU/Linux, although very old, is still supported."+
                "\nToday, a considerable number of distributions are based on it."+
                "\nDebian GNU/Linux offers a very stable experience, but can lag a bit behind if Testing etc. versions are not used.")
            self.button4 = ui.CTkButton(distro4, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
            self.text5 = ui.CTkLabel(distro5, text="Manjaro is a distribution based on Arch Linux. It is aimed at the end user."+
                "\n\nNote from GrelinTB developer: If you are going to use an Arch Linux base, I suggest you look for other alternatives.")
            self.button5 = ui.CTkButton(distro5, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
            self.text6 = ui.CTkLabel(distro6, text="Ubuntu is aimed at many user groups. There are many flavors of Ubuntu."+
                "\n\nNote from GrelinTB developer: Ubuntu comes by default with open telemetry that can be turned off."+
                "\nAlso forces you to use Snap, which is not very good.")
            self.button6 = ui.CTkButton(distro6, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
            self.text7 = ui.CTkLabel(distro7, text="Fedora Linux is sponsered by Red Hat. Packages come to Fedora Linux before they come to RHEL."+
                "\nFedora Linux has many versions for different desktop environments."+
                "\n\nNote from GrelinTB developer: Fedora Linux is really suitable for users who want stability, simplicity, and up to date."+
                "\nFedora Linux is one of the distributions I recommend.")
            self.button7 = ui.CTkButton(distro7, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
            self.text8 = ui.CTkLabel(distro8, text="Pop!_OS is an operating system for those who use their computer as a tool to discover and create."+
                "\nIt offers a separate download option for Nvidia users."+
                "\nIt only supports UEFI because it uses systemd-boot.")
            self.button8 = ui.CTkButton(distro8, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
            self.text9 = ui.CTkLabel(distro9, text="It is a distribution targeted at users migrating from Windows and Mac and wants to provide ease of use."+
                "\n\nGrelinTB developer note: I used it for a while, but I don't recommend it because I think the logic of the Pro version is ridiculous.")
            self.button9 = ui.CTkButton(distro9, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
            self.text10 = ui.CTkLabel(distro10, text="It is the only distribution on this list that GrelinTB does not support. It targets many audiences and has its own tools."+
                "\nIt is divided into Tumbleweed (more up-to-date), Leap (more stable)."+
                "\n\nNote from GrelinTB developer: I read from various sources that it is better to use Tumbleweed.")
            self.button10 = ui.CTkButton(distro10, text="Open Website", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True))
        elif os.path.isfile(tr):
            self.text1 = ui.CTkLabel(distro1, text="MX Linux, antiX ve MX Linux toplulukları arasında bir işbirliği girişimidir."+
                "\nZarif ve verimli masaüstlerini yüksek kararlılık ve sağlam performansla birleştirmek için tasarlanmış bir işletim sistemi ailesidir."+
                "\nMX'in grafiksel araçları ve antiX'in araçları kullanımı kolaylaştırır.")
            self.button1 = ui.CTkButton(distro1, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://mxlinux.org/", shell=True))  
            self.text2 = ui.CTkLabel(distro2, text="Linux Mint masaüstü ve dizüstü bilgisayarlar için bir işletim sistemidir."+
                "\nKutudan çıktığı gibi' çalışmak üzere tasarlanmıştır ve çoğu insanın ihtiyaç duyduğu uygulamalarla tam donanımlı olarak gelir."+
                "\n\nGrelinTB geliştiricisinin notu: İlk kez Linux kullanacaklar için Linux Mint'i şiddetle tavsiye ederim. Kullanımı gerçekten çok kolay.")
            self.button2 = ui.CTkButton(distro2, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://linuxmint.com/", shell=True))
            self.text3 = ui.CTkLabel(distro3, text="EndeavourOS, hem x86_64 hem de ARM sistemleri için manuel olarak yükleme zahmetine girmeden"+
                "\nArch deneyimi sağlayan Arch tabanlı bir dağıtımdır."+
                "\nKurulumdan sonra, size iyi bir ortam ve rehber sağlanır.")
            self.button3 = ui.CTkButton(distro3, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://endeavouros.com/", shell=True))
            self.text4 = ui.CTkLabel(distro4, text="Debian GNU/Linux, çok eski olmasına rağmen halen desteklenmektedir."+
                "\nBugün azımsanmayacak kadar dağıtım, onu taban alır."+
                "\nDebian GNU/Linux oldukça stabil bir deneyim sunar fakat Testing vs. sürümler kullanılmazsa biraz geriden gelebilir.")
            self.button4 = ui.CTkButton(distro4, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://debian.org/", shell=True))
            self.text5 = ui.CTkLabel(distro5, text="Manjaro, Arch Linux tabanlı bir dağıtımdır. Son kullanıcıyı hedef alır."+
                "\n\nGrelinTB geliştiricisinin notu: İlla ki Arch Linux tabanı kullanacaksanız başka alternatiflere yönelmenizi öneririm.")
            self.button5 = ui.CTkButton(distro5, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://manjaro.org/", shell=True))
            self.text6 = ui.CTkLabel(distro6, text="Ubuntu birçok kullanıcı kitlesini hedeflemektedir. Birçok Ubuntu çeşidi vardır."+
                "\n\nGrelinTB geliştiricisinin notu: Ubuntu varsayılan olarak kapatılması mümkün olan açık telemetrilerle gelir."+
                "\nAyrıca sizi çok iyi olmayan Snap kullanmaya zorlar.")
            self.button6 = ui.CTkButton(distro6, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://ubuntu.com/", shell=True))
            self.text7 = ui.CTkLabel(distro7, text="Fedora Linux Red Hat tarafından desteklenmektedir. Paketler RHEL'e gelmeden önce Fedora Linux'a gelir."+
                "\nFedora Linux'un farklı masaüstü ortamları için birçok sürümü vardır."+
                "\n\nGrelinTB geliştiricisinin notu: Fedora Linux gerçekten hem stabillik hem kolaylık hem de güncellik isteyen kullanıcılar için uygun."+
                "\nFedora Linux, önerdiğim dağıtımlardan bir tanesi.")
            self.button7 = ui.CTkButton(distro7, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://fedoraproject.org/", shell=True))
            self.text8 = ui.CTkLabel(distro8, text="Pop!_OS, bilgisayarlarını keşfetmek ve yaratmak için bir araç olarak kullananlar için bir işletim sistemidir."+
                "\nNvidia kullanıcıları için ayrı bir indirme seçeneği sunar."+
                "\nSystemd-boot kullandığı için sadece UEFI destekler.")
            self.button8 = ui.CTkButton(distro8, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://pop.system76.com/", shell=True))
            self.text9 = ui.CTkLabel(distro9, text="Hedef kitlesi Windows'tan ve Mac'ten geçen kullanıcılar olan ve kullanım kolaylığı sağlamak isteyen bir dağıtım."+
                "\n\nGrelinTB geliştiricisinin notu: Bir ara ben de kullandım fakat pek tavsiye etmiyorum çünkü Pro sürümü mantığı bence saçma.")
            self.button9 = ui.CTkButton(distro9, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://zorin.com/", shell=True))
            self.text10 = ui.CTkLabel(distro10, text="Bu listede GrelinTB'nin desteklemediği tek dağıtımdır kendisi. Birçok kitleyi hedef alır ve kendi araçlarına sahiptir."+
                "\nTumbleweed (daha güncel olan), Leap (daha stabil olan) olarak ikiye ayrılır."+
                "\n\nGrelinTB geliştiricisinin notu: Çeşitli kaynaklardan okuduğum kadarıyla Tumbleweed kullanmak daha iyiymiş.")
            self.button10 = ui.CTkButton(distro10, text="İnternet Sitesini Aç", command=lambda:subprocess.Popen("xdg-open https://opensuse.org/", shell=True)) 
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

class Tools(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        if os.path.isfile(en):
            tab1 = self.tabview.add("Configure .bashrc File")
            tab2 = self.tabview.add("Change Computer's Name")
            tab3 = self.tabview.add("Open File Managers With Root Rights")
            tab4 = self.tabview.add("Informations About Some Distributions")
        elif os.path.isfile(tr):
            tab1 = self.tabview.add(".bashrc Dosyasını Yapılandır")
            tab2 = self.tabview.add("Bilgisayarın Adını Değiştir")
            tab3 = self.tabview.add("Dosya Yöneticilerini Kök Haklarıyla Aç")
            tab4 = self.tabview.add("Bazı Dağıtımlar Hakkında Bilgiler")
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        self.bashrc_frame=Bashrc(tab1, fg_color="transparent")
        self.bashrc_frame.grid(row=0, column=0, sticky="nsew")
        tab2.grid_columnconfigure(0, weight=1)
        tab2.grid_rowconfigure(0, weight=1)
        self.computername_frame=ComputerName(tab2, fg_color="transparent")
        self.computername_frame.grid(row=0, column=0, sticky="nsew")
        tab3.grid_columnconfigure(0, weight=1)
        tab3.grid_rowconfigure(0, weight=1)
        self.openfm_frame=OpenFM(tab3, fg_color="transparent")
        self.openfm_frame.grid(row=0, column=0, sticky="nsew")        
        tab4.grid_columnconfigure(0, weight=1)
        tab4.grid_rowconfigure(0, weight=1)
        self.distros_frame=Distros(tab4)
        self.distros_frame.grid(row=0, column=0, sticky="nsew")


class Scripts(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.button1 = ui.CTkButton(self, command=self.cups, text="Open Cups Configuration Page")
            self.button2 = ui.CTkButton(self, command=self.go_wine, text="Open Wine Configuration App")
            self.button3 = ui.CTkButton(self, command=self.go_grub, text="Open Grub Customizer")
            self.button4 = ui.CTkButton(self, command=self.go_update, text="Update Packages")
            self.button5 = ui.CTkButton(self, command=self.go_clear, text="Clear Package Cache")
            self.button6 = ui.CTkButton(self, command=self.go_remove, text="Remove Unnecessary Packages")
        elif os.path.isfile(tr):
            self.button1 = ui.CTkButton(self, command=self.cups, text="Cups Yapılandırma Sayfasını Aç")
            self.button2 = ui.CTkButton(self, command=self.go_wine, text="Wine Yapılandırma Uygulamasını Aç")
            self.button3 = ui.CTkButton(self, command=self.go_grub, text="Grub Customizer Uygulamasını Aç")
            self.button4 = ui.CTkButton(self, command=self.go_update, text="Paketleri Güncelle")
            self.button5 = ui.CTkButton(self, command=self.go_clear, text="Paket Önbelleğini Temizle")
            self.button6 = ui.CTkButton(self, command=self.go_remove, text="Gereksiz Paketleri Kaldır")
        self.button1.grid(row=0, column=0, sticky="nsew", pady=(0, 25), padx=50)
        self.button2.grid(row=1, column=0, sticky="nsew", pady=(0, 25), padx=50)
        self.button3.grid(row=2, column=0, sticky="nsew", pady=(0, 25), padx=50)
        self.button4.grid(row=3, column=0, sticky="nsew", pady=(0, 25), padx=50)
        self.button5.grid(row=4, column=0, sticky="nsew", pady=(0, 25), padx=50)
        self.button6.grid(row=5, column=0, sticky="nsew", padx=50)
        if not os.path.isfile("/usr/bin/winecfg") and not os.path.isfile("/bin/winecfg"):
            if os.path.isfile(en):
                self.button2.configure(text="Open Wine Configuration App\nError: Wine Not Installed", state="disabled")
            elif os.path.isfile(tr):
                self.button2.configure(text="Wine Yapılandırma Uygulamasını Aç\nHata: Wine Kurulu Değil", state="disabled")
    def cups(self):
        subprocess.Popen('xdg-open localhost:631', shell=True)
    def wine_main(self):
        subprocess.Popen('winecfg', shell=True)
    def go_wine(self):
        t = threading.Thread(target=self.wine_main, daemon=False)
        t.start()
    def grub_main(self):
        if not os.path.isfile("/usr/bin/grub-customizer") and not os.path.isfile("/bin/grub-customizer"):
            install_app("Grub Customizer", "grub-customizer")
            if ask_a == False:
                return
        subprocess.Popen('grub-customizer', shell=True)
    def go_grub(self):
        t = threading.Thread(target=self.grub_main, daemon=False)
        t.start()
    def update_main(self):
        if os.path.isfile(en):
            status.configure(text="Status:\nUpdating Package(s)")
        elif os.path.isfile(tr):
            status.configure(text="Durum:\nPaket(ler) Güncelleniyor")
        if os.path.isfile(debian):
            os.system("pkexec apt upgrade -y")
        elif os.path.isfile(fedora):
            os.system("pkexec dnf update -y")
        elif os.path.isfile(solus):
            os.system("pkexec eopkg upgrade -y")
        elif os.path.isifle(arch1) or os.path.isfile(arch2):
            os.system("pkexec pacman -Syu --noconfirm")
        normal()
        main_successful()
    def go_update(self):
        t = threading.Thread(target=self.update_main, daemon=False)
        t.start()
    def clear_main(self):
        if os.path.isfile(en):
            status.configure(text="Status:\nClearing Package Cache")
        elif os.path.isfile(tr):
            status.configure(text="Durum:\nPaket Önbelleği Temizleniyor")
        if os.path.isfile(debian):
            os.system("pkexec apt-get autoclean -y")
        elif os.path.isfile(fedora):
            os.system("pkexec dnf clean all -y")
        elif os.path.isfile(solus):
            os.system("pkexec eopkg dc -y")
        elif os.path.isifle(arch1) or os.path.isfile(arch2):
            os.system("pkexec pacman -Scc --noconfirm")
        normal()
        main_successful()
    def go_clear(self):
        t = threading.Thread(target=self.clear_main, daemon=False)
        t.start()
    def remove_main(self):
        if os.path.isfile(en):
            status.configure(text="Status:\nRemoving Unnecessary Package(s)")
        elif os.path.isfile(tr):
            status.configure(text="Durum:\nGereksiz Paketler Kaldırılıyor")
        if os.path.isfile(debian):
            os.system("pkexec apt-get autoremove -y")
        elif os.path.isfile(fedora):
            os.system("pkexec dnf autoremove -y")
        elif os.path.isfile(solus):
            os.system("pkexec eopkg rmf -y")
        elif os.path.isifle(arch1) or os.path.isfile(arch2):
            os.system("pacman -Qdtq | pkexec pacman -Rs - --noconfirm")
        normal()
        main_successful()
    def go_remove(self):
        t = threading.Thread(target=self.remove_main, daemon=False)
        t.start()

class Root(ui.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("GrelinTB")
        self.geometry("1200x600")
        self.minsize(1200, 600)
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
            Sidebar.check_update(self)
        if os.path.isfile(en):
            tab_starting = self.tabview.add("Starting")
            tab_notes = self.tabview.add("Notes")
            tab_store = self.tabview.add("Store")
            tab_tools = self.tabview.add("Tools")
            tab_scripts = self.tabview.add("Scripts")
        elif os.path.isfile(tr):
            tab_starting = self.tabview.add("Başlangıç")
            tab_notes = self.tabview.add("Notlar")
            tab_store = self.tabview.add("Mağaza")
            tab_tools = self.tabview.add("Araçlar")
            tab_scripts = self.tabview.add("Betikler")
        tab_starting.grid_columnconfigure(0, weight=1)
        tab_starting.grid_rowconfigure(0, weight=1)
        self.starting_frame=Starting(tab_starting)
        self.starting_frame.grid(row=0, column=0, sticky="nsew")
        tab_notes.grid_columnconfigure(0, weight=1)
        tab_notes.grid_rowconfigure(0, weight=1)
        self.notes_frame=Notes(tab_notes)
        self.notes_frame.grid(row=0, column=0, sticky="nsew")
        tab_store.grid_columnconfigure(0, weight=1)
        tab_store.grid_rowconfigure(0, weight=1)
        self.store_frame=Store(tab_store)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab_tools.grid_columnconfigure(0, weight=1)
        tab_tools.grid_rowconfigure(0, weight=1)
        self.tools_frame=Tools(tab_tools)
        self.tools_frame.grid(row=0, column=0, sticky="nsew")
        tab_scripts.grid_columnconfigure(0, weight=1)
        tab_scripts.grid_rowconfigure(0, weight=1)
        self.scripts_frame=Scripts(tab_scripts)
        self.scripts_frame.grid(row=0, column=0, sticky="nsew")

if "pcrename" in sys.argv[1:]:
    with open("/etc/hostname", "w") as pcname:
        pcname.write(str(sys.argv[2]))
elif __name__ == "__main__":
    root = Root(className="grelintb")
    root.mainloop()