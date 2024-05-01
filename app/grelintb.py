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
import sys

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
solus = "/etc/solus-release"
arch = "/etc/arch-release"

if not os.path.isfile(debian) and not os.path.isfile(fedora) and not os.path.isfile(solus) and os.path.isfile(arch):
    print("The distribution you are using is not supported from GrelinTB.\nPlease use Debian GNU/Linux, Fedora Linux, Solus and Arch Linux based distributions for GrelinTB. (1)")
    sys.exit(1)

if "root" in sys.argv[1:]:
    if os.getuid() != 0:
        print("Root rights are required for this feature. (3)")
        sys.exit(3)
    if "pcrename" in sys.argv[2:]:
        with open("/etc/hostname", "w") as pcname:
            pcname.write(str(sys.argv[3]))
    sys.exit(0)
elif os.getuid() == 0:
    print("GrelinTB already asks you for root rights when the need arises. (2)")
    sys.exit(2)

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
        os.system("pkexec apt -y install python3-tk")
    elif os.path.isfile(fedora):
        os.system("pkexec dnf -y --nogpgcheck install python3-tkinter")
    elif os.path.isfile(solus):
        os.system("pkexec eopkg -y install python3-tkinter")
    elif os.path.isfile(arch):
        os.system("pkexec pacman --noconfirm -S tk")
    from tkinter import messagebox as mb
    from tkinter import filedialog as fd
    from tkinter import PhotoImage as pi
if not os.path.isfile("/bin/pip") and not os.path.isfile("/usr/bin/pip"):
    print("Installing Pip...")
    if os.path.isfile(debian):
        os.system("pkexec apt -y install python3-pip")
    elif os.path.isfile(fedora):
        os.system("pkexec dnf -y --nogpgcheck install python3-pip")
    elif os.path.isfile(solus):
        os.system("pkexec eopkg -y install pip")
    elif os.path.isfile(arch):
        os.system("pkexec pacman --noconfirm -S python-pip")
try:
    import customtkinter as ui
except:
    try:
        print("Installing CustomTkinter...")
        os.system("pip install customtkinter")
        import customtkinter as ui
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install customtkinter --break-system-packages ; grelintb")
        sys.exit(0)
try:
    import psutil
except:
    try:
        print("Installing psutil...")
        os.system("pip install psutil")
        import psutil
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install psutil --break-system-packages ; grelintb")
        sys.exit(0)
try:
    import distro
except:
    try:
        print("Installing distro...")
        os.system("pip install distro")
        import distro
    except:
        print("Installing CustomTkinter with --break-system-packages parameter...")
        os.system("pip install distro --break-system-packages ; grelintb")
        sys.exit(0)

username = getpass.getuser()
config = f"/home/{username}/.config/grelintb/"
notes = f"/home/{username}/Notes/"
en = f"/home/{username}/.config/grelintb/language/en.txt"
tr = f"/home/{username}/.config/grelintb/language/tr.txt"
system = f"/home/{username}/.config/grelintb/theme/system.txt"
light = f"/home/{username}/.config/grelintb/theme/light.txt"
dark = f"/home/{username}/.config/grelintb/theme/dark.txt"
random = f"/home/{username}/.config/grelintb/color/random.txt"
dark_blue = f"/home/{username}/.config/grelintb/color/dark_blue.txt"
blue = f"/home/{username}/.config/grelintb/color/blue.txt"
green = f"/home/{username}/.config/grelintb/color/green.txt"
process_number = 0
current_operations = []

if not os.path.isdir(config):
    os.system(f"cd /home/{username}/.config ; mkdir grelintb")
if not os.path.isdir(f"{config}language/") or (not os.path.isfile(en) and not os.path.isfile(tr)):
    if locale.getlocale()[0] == "tr_TR":
        os.system(f"cd {config} ; mkdir language ; cd language ; touch tr.txt")
    else:
        os.system(f"cd {config} ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(f"{config}theme/") or (not os.path.isfile(system) and not os.path.isfile(light) and not os.path.isfile(dark)):
    os.system(f"cd {config} ; mkdir theme ; cd theme ; touch system.txt")
if not os.path.isdir(f"{config}color/") or (not os.path.isfile(random) and not os.path.isfile(dark_blue) and not os.path.isfile(blue) and not os.path.isfile(green)):
    os.system(f"cd {config} ; mkdir color ; cd color ; touch random.txt")
if not os.path.isdir(notes):
    os.system(f"cd /home/{username} ; mkdir Notes")
if not os.path.isfile(f"/home/{username}/.bashrc"):
    os.system(f"cd /home/{username} ; touch .bashrc")
if not os.path.isfile(f"/home/{username}/.zshrc"):
    os.system(f"cd /home/{username} ; touch .zshrc")
if not os.path.isfile(f"/home/{username}/.bashrc-first-grelintb.bak"):
    os.system(f"cd /home/{username} ; cp .bashrc .bashrc-first-grelintb.bak")
if not os.path.isfile(f"/home/{username}/.zshrc-first-grelintb.bak"):
    os.system(f"cd /home/{username} ; cp .zshrc .zshrc-first-grelintb.bak")

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
if "set-version" in sys.argv[1:]:
    version_current = sys.argv[(sys.argv[1:].index("set-version") + 2)]

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
        ask_a = mb.askyesno("Warning", f"{appname} can't found on your system.\nWe can try installing {appname} to your computer.\nDo you approve it?")
    elif os.path.isfile(tr):
        ask_a = mb.askyesno("Uyarı", f"{appname} sisteminizde bulunamadı.\nBiz sisteminize {appname} yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
    if ask_a == True:
        time_process = str(time.strftime("%H:%M:%S", time.localtime()))
        if os.path.isfile(en):
            add_operation(f"Installing {appname}", time_process)
        elif os.path.isfile(tr):
            add_operation(f"{appname} Kuruluyor", time_process)
        if os.path.isfile(debian):
            cmd = os.system(f'fkexec apt -y install {packagename}')
        elif os.path.isfile(fedora):
            cmd = os.system(f'pkexec dnf -y --nogpgcheck install {packagename}')
        elif os.path.isfile(solus):
            cmd = os.system(f'pkexec eopkg -y install {packagename}')
        elif os.path.isfile(arch):
            cmd = os.system(f'pkexec pacman --noconfirm -S  {packagename}')
        if os.path.isfile(en):
            delete_operation(f"Installing {appname}", time_process)
        elif os.path.isfile(tr):
            delete_operation(f"{appname} Kuruluyor", time_process)
    elif ask_a == False:
        if os.path.isfile(en):
            mb.showerror("Error", f"{appname} installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", f"{appname} kurulumu ve işlem iptal edildi.")
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
        if os.path.isfile(debian):
            cmd1 = os.system('pkexec apt -y install flatpak')
            cmd2 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
            restart_system()
        elif os.path.isfile(fedora):
            cmd1 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
        elif os.path.isfile(solus):
            cmd1 = os.system('pkexec eopkg -y install flatpak')
            cmd2 = os.system('flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo')
            restart_system()
        elif os.path.isfile(arch):
            cmd1 = os.system('pkexec pacman --noconfirm -S flatpak')
            restart_system()
        if os.path.isfile(en):
            delete_operation(f"Installing Flatpak", time_process)
        elif os.path.isfile(tr):
            delete_operation(f"Flatpak Kuruluyor", time_process)
    elif ask_f == False:
        if os.path.isfile(en):
            mb.showerror("Error", "Flatpak package manager installation ve process cancelled.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", "Flatpak paket yöneticisi kurulumu ve işlem iptal edildi.")
def ask_restart_for_grelintb_ui(mode: str):
    global ask_g
    if os.path.isfile(en) or mode == "en":
        ask_g = mb.askyesno("Warning", "GrelinTB's user interface needs restarting.\nDo you want to restart the GrelinTB user interface?")
    elif os.path.isfile(tr) or mode == "tr":
        ask_g = mb.askyesno("Uyarı", "GrelinTB'nin kullanıcı arayüzü yeniden başlatılmaya ihtiyaç duyuyor.\nGrelinTB kullanıcı arayüzünü yeniden başlatmak istiyor musunuz?")
    if ask_g == True:
        root.destroy()
        os.system("grelintb")
def main_successful():
    if os.path.isfile(en):
        mb.showinfo("Information","Process completed.")
    elif os.path.isfile(tr):
        mb.showinfo("Bilgilendirme","İşlem tamamlandı.")
def main_error():
    if os.path.isfile(en):
        mb.showerror("Error", "Process completed with error.")
    elif os.path.isfile(tr):
        mb.showerror("Hata", "İşlem hatayla tamamlandı.")

class Sidebar(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        global status
        self.grid_rowconfigure((5, 9, 13), weight=1)
        self.text = ui.CTkButton(self, text="GrelinTB", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io/grelintb/index.html", shell=True), font=ui.CTkFont(size=20, weight="bold"), fg_color="transparent", text_color=("gray14", "gray84"))
        if os.path.isfile(en):
            self.version_b = ui.CTkButton(self, text=f"Version: {version_current}", command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Developer: MuKonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_b = ui.CTkButton(self, text="License: GPLv3+", command=self.license, fg_color="transparent", text_color=("gray14", "gray84"))
            self.credit_b = ui.CTkButton(self, text="Credit: G. M. Icons", command=self.credit, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Update", command=lambda:self.check_update("sidebar"))
            self.reset_b = ui.CTkButton(self, text="Reset", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Uninstall", command=self.uninstall)
            self.color_menu = ui.CTkOptionMenu(self, values=["Color: Random", "Color: Dark Blue", "Color: Blue", "Color: Green"], command=self.change_color)
            self.theme_menu = ui.CTkOptionMenu(self, values=["Theme: System", "Theme: Light", "Theme: Dark"], command=self.change_theme)
            self.language_menu = ui.CTkOptionMenu(self, values=["Language: English", "Language: Turkish"], command=self.change_language)
            status = ui.CTkButton(self, text="Status: Ready", command=self.show_operations, font=ui.CTkFont(size=12, weight="bold"))
            if os.path.isfile(random):
                self.color_menu.set("Color: Random")
            elif os.path.isfile(dark_blue):
                self.color_menu.set("Color: Dark Blue")
            elif os.path.isfile(blue):
                self.color_menu.set("Color: Blue")
            elif os.path.isfile(green):
                self.color_menu.set("Color: Green")
            if os.path.isfile(system):
                self.theme_menu.set("Theme: System")
            elif os.path.isfile(light):
                self.theme_menu.set("Theme: Light")
            elif os.path.isfile(dark):
                self.theme_menu.set("Theme: Dark")
            self.language_menu.set("Language: English")
        elif os.path.isfile(tr):
            self.version_b = ui.CTkButton(self, text=f"Sürüm: {version_current}", command=self.changelog, fg_color="transparent", text_color=("gray14", "gray84"))
            self.mukonqi_b = ui.CTkButton(self, text="Geliştirici: MuKonqi", command=lambda:subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True), fg_color="transparent", text_color=("gray14", "gray84"))
            self.license_b = ui.CTkButton(self, text="Lisans: GPLv3+", command=self.license, fg_color="transparent", text_color=("gray14", "gray84"))
            self.credit_b = ui.CTkButton(self, text="Kredi: G. M. Icons", command=self.credit, fg_color="transparent", text_color=("gray14", "gray84"))
            self.update_b = ui.CTkButton(self, text="Güncelle", command=lambda:self.check_update("sidebar"))
            self.reset_b = ui.CTkButton(self, text="Sıfırla", command=self.reset)
            self.uninstall_b = ui.CTkButton(self, text="Kaldır", command=self.uninstall)
            self.color_menu = ui.CTkOptionMenu(self, values=["Renk: Rastgele", "Renk: Koyu Mavi", "Renk: Mavi", "Renk: Yeşil"], command=self.change_color)
            self.theme_menu = ui.CTkOptionMenu(self, values=["Tema: Sistem", "Tema: Açık", "Tema: Koyu"], command=self.change_theme)
            self.language_menu = ui.CTkOptionMenu(self, values=["Dil: Türkçe", "Dil: İngilizce"], command=self.change_language)
            status = ui.CTkButton(self, text="Durum: Hazır", command=self.show_operations, font=ui.CTkFont(size=12, weight="bold"))
            if os.path.isfile(random):
                self.color_menu.set("Renk: Rastgele")
            elif os.path.isfile(dark_blue):
                self.color_menu.set("Renk: Koyu Mavi")
            elif os.path.isfile(blue):
                self.color_menu.set("Renk: Mavi")
            elif os.path.isfile(green):
                self.color_menu.set("Renk: Yeşil")
            if os.path.isfile(system):
                self.theme_menu.set("Tema: Sistem")
            elif os.path.isfile(light):
                self.theme_menu.set("Tema: Açık")
            elif os.path.isfile(dark):
                self.theme_menu.set("Tema: Koyu")
            self.language_menu.set("Dil: Türkçe")
        self.text.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        self.version_b.grid(row=1, column=0, sticky="nsew", padx=10, pady=0)
        self.mukonqi_b.grid(row=2, column=0, sticky="nsew", padx=10, pady=0)
        self.license_b.grid(row=3, column=0, sticky="nsew", padx=10, pady=0)
        self.credit_b.grid(row=4, column=0, sticky="nsew", padx=10, pady=0)
        self.update_b.grid(row=6, column=0, sticky="nsew", padx=10, pady=5)
        self.reset_b.grid(row=7, column=0, sticky="nsew", padx=10, pady=5)
        self.uninstall_b.grid(row=8, column=0, sticky="nsew", padx=10, pady=5)
        self.color_menu.grid(row=10, column=0, sticky="nsew", padx=10, pady=(0, 5))
        self.theme_menu.grid(row=11, column=0, sticky="nsew", padx=10, pady=(0, 5))
        self.language_menu.grid(row=12, column=0, sticky="nsew", padx=10, pady=(0, 5))
        status.grid(row=14, column=0, sticky="nsew", padx=10, pady=(0, 5))
    def changelog(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.frame = ui.CTkScrollableFrame(self.window, fg_color="transparent")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid(row=0, column=0, sticky="nsew")
        if os.path.isfile(en):
            self.window.title("Changelogs For "+version_current)
            self.label1 = ui.CTkLabel(self.frame, text=f"Primary Changelog For {version_current}", font=ui.CTkFont(size=14, weight="bold"))
            self.label2 = ui.CTkLabel(self.frame, text=f"Major Changelog For {version_current}", font=ui.CTkFont(size=14, weight="bold"))
            self.label3 = ui.CTkLabel(self.frame, text=f"Minor Changelog For {version_current}", font=ui.CTkFont(size=14, weight="bold"))
        elif os.path.isfile(tr):
            self.window.title(version_current+" için Değişiklik Günlükleri")
            self.label1 = ui.CTkLabel(self.frame, text=f"{version_current} İçin Birincil Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
            self.label2 = ui.CTkLabel(self.frame, text=f"{version_current} İçin Major Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
            self.label3 = ui.CTkLabel(self.frame, text=f"{version_current} İçin Minor Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
        with open("/usr/local/bin/grelintb/primary-changelog.txt", "r") as self.cl_primary_file:
            self.cl_primary_text = self.cl_primary_file.read()
        with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as self.cl_major_file:
            self.cl_major_text = self.cl_major_file.read()
        with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as self.cl_minor_file:
            self.cl_minor_text = self.cl_minor_file.read()
        self.textbox1 = ui.CTkTextbox(self.frame)
        self.textbox1.insert("0.0", self.cl_primary_text)
        self.textbox1.configure(state="disabled")
        self.textbox2 = ui.CTkTextbox(self.frame)
        self.textbox2.insert("0.0", self.cl_major_text)
        self.textbox2.configure(state="disabled")
        self.textbox3 = ui.CTkTextbox(self.frame)
        self.textbox3.insert("0.0", self.cl_minor_text)
        self.textbox3.configure(state="disabled")
        self.label1.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.textbox1.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.label2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
        self.textbox2.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.label3.grid(row=4, column=0, sticky="nsew", pady=(0, 5))
        self.textbox3.grid(row=5, column=0, sticky="nsew", padx=10, pady=(0, 10))
    def license(self):
        self.window = ui.CTkToplevel()
        self.window.geometry("540x540")
        self.window.minsize(540, 540)
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        if os.path.isfile(en):
            self.window.title("License")
            self.label = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Copyright (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB licensed under GPLv3 or later.")
        elif os.path.isfile(tr):
            self.window.title("Lisans")
            self.label = ui.CTkLabel(self.window, font=ui.CTkFont(size=16, weight="bold"), text="Telif Hakkı (C) 2024 MuKonqi (Muhammed S.)\nGrelinTB GPLv3 veya sonrası altında lisanslanmıştır.")
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as self.license_file:
            self.license_text = self.license_file.read()
        self.textbox = ui.CTkTextbox(self.window)
        self.textbox.insert("0.0", self.license_text)
        self.textbox.configure(state="disabled")
        self.label.grid(row=0, column=0, sticky="nsew", pady=10)
        self.textbox.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
    def credit(self):
        if os.path.isfile(en):
            self.credit_mb = mb.askyesno("About Credit", "The credit is Google Material Symbols for application icon.\nDo you want visit the credit's website?")
        elif os.path.isfile(tr):
            self.credit_mb = mb.askyesno("Kredi Hakkında", "Kredi, uygulama ikonu için Google Material Symbols idir.\nKredinin internet sitesini ziyaret etmek ister misiniz?")
        if self.credit_mb == True:
            subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048", shell=True)
    def update(self, string: str):
        if os.path.isfile(en):
            if string == "sidebar":
                self.update_b.configure(text="Updating", state="disabled")
            os.system("pkexec /usr/local/bin/grelintb/update.sh")
            mb.showinfo("Successful", "GrelinTB updated.")
            if string == "sidebar":
                self.update_b.configure(text="Updated", state="disabled")
        elif os.path.isfile(tr):
            if string == "sidebar":
                self.update_b.configure(text="Güncelleniyor", state="disabled")
            os.system("pkexec /usr/local/bin/grelintb/update.sh")
            mb.showinfo("Başarılı", "GrelinTB güncellendi.")
            if string == "sidebar":
                self.update_b.configure(text="Güncellendi", state="disabled")
        ask_restart_for_grelintb_ui("normal")
    def check_update(self, string: str):
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
            if os.path.isfile(en):
                self.window.title("Changelogs For "+version_latest)
                self.label1 = ui.CTkLabel(self.frame, text=f"Primary Changelog For {version_latest}", font=ui.CTkFont(size=14, weight="bold"))
                self.label2 = ui.CTkLabel(self.frame, text=f"Major Changelog For {version_latest}", font=ui.CTkFont(size=14, weight="bold"))
                self.label3 = ui.CTkLabel(self.frame, text=f"Minor Changelog For {version_latest}", font=ui.CTkFont(size=14, weight="bold"))
                if string == "sidebar":
                    self.button = ui.CTkButton(self.window, text="Update To "+version_latest, command=lambda:Sidebar.update(self, "sidebar"))
                elif string == "startup":
                    self.button = ui.CTkButton(self.window, text="Update To "+version_latest, command=lambda:Sidebar.update(self, "startup"))
            elif os.path.isfile(tr):
                self.window.title(version_latest+" için Değişiklik Günlükleri")
                self.label1 = ui.CTkLabel(self.frame, text=f"{version_latest} İçin Birincil Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
                self.label2 = ui.CTkLabel(self.frame, text=f"{version_latest} İçin Major Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
                self.label3 = ui.CTkLabel(self.frame, text=f"{version_latest} İçin Minor Değişik Günlüğü", font=ui.CTkFont(size=14, weight="bold"))
                if string == "sidebar": 
                    self.button = ui.CTkButton(self.window, text=version_latest+" Sürümüne Güncelle", command=lambda:Sidebar.update(self, "sidebar"))
                elif string == "startup":
                    self.button = ui.CTkButton(self.window, text=version_latest+" Sürümüne Güncelle", command=lambda:Sidebar.update(self, "startup"))
            with open("/usr/local/bin/grelintb/primary-changelog.txt", "r") as self.cl_primary_file:
                self.cl_primary_text = self.cl_primary_file.read()
            with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as self.cl_major_file:
                self.cl_major_text = self.cl_major_file.read()
            with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as self.cl_minor_file:
                self.cl_minor_text = self.cl_minor_file.read()
            self.textbox1 = ui.CTkTextbox(self.frame)
            self.textbox1.insert("0.0", str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/primary-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
            self.textbox1.configure(state="disabled")
            self.textbox2 = ui.CTkTextbox(self.frame)
            self.textbox2.insert("0.0", str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/major-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
            self.textbox2.configure(state="disabled")
            self.textbox3 = ui.CTkTextbox(self.frame)
            self.textbox3.insert("0.0", str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/minor-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
            self.textbox3.configure(state="disabled")
            self.label1.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
            self.textbox1.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
            self.label2.grid(row=2, column=0, sticky="nsew", pady=(0, 5))
            self.textbox2.grid(row=3, column=0, sticky="nsew", padx=10, pady=(0, 10))
            self.label3.grid(row=4, column=0, sticky="nsew", pady=(0, 5))
            self.textbox3.grid(row=5, column=0, sticky="nsew", padx=10, pady=(0, 10))
            self.button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        elif string != "startup":
            if os.path.isfile(en):
                mb.showinfo("Information","GrelinTB is up to date.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","GrelinTB güncel.")
    def reset(self):
        if os.path.isfile(en):
            self.reset_b.configure(text="Resetting", state="disabled")
            os.system("pkexec /usr/local/bin/grelintb/reset.sh")
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            mb.showinfo("Successful", "GrelinTB reset.")
            self.reset_b.configure(text="Reset", state="disabled")
            ask_restart_for_grelintb_ui("en")
        elif os.path.isfile(tr):
            self.reset_b.configure(text="Sıfırlanıyor", state="disabled")
            os.system("pkexec /usr/local/bin/grelintb/reset.sh")
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            mb.showinfo("Başarılı", "GrelinTB sıfırlandı.")
            self.reset_b.configure(text="Sıfırlandı", state="disabled")
            ask_restart_for_grelintb_ui("tr")
    def uninstall(self):
        root.destroy()
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        if os.path.isfile(en):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            mb.showinfo("Successful","GrelinTB uninstalled.")
        elif os.path.isfile(tr):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            mb.showinfo("Bilgilendirme","GrelinTB kaldırıldı.")
        sys.exit(0)
    def change_color(self, new_color: str):
        if new_color == "Color: Random" or new_color == "Renk: Rastgele":
            os.system(f"rm {config}color/* ; touch {config}color/random.txt")
        elif new_color == "Color: Dark Blue" or new_color == "Renk: Koyu Mavi":
            os.system(f"rm {config}color/* ; touch {config}color/dark_blue.txt")
        elif new_color == "Color: Blue" or new_color == "Renk: Mavi":
            os.system(f"rm {config}color/* ; touch {config}color/blue.txt")
        elif new_color == "Color: Green" or new_color == "Renk: Yeşil":
            os.system(f"rm {config}color/* ; touch {config}color/green.txt")
        ask_restart_for_grelintb_ui("normal")
    def change_theme(self, new_theme: str):
        if new_theme == "Theme: System" or new_theme == "Tema: Sistem":
            ui.set_appearance_mode("System")
            os.system(f"rm {config}theme/* ; touch {config}theme/system.txt")
        elif new_theme == "Theme: Light" or new_theme == "Tema: Açık":
            ui.set_appearance_mode("Light")
            os.system(f"rm {config}theme/* ; touch {config}theme/light.txt")
        elif new_theme == "Theme: Dark" or new_theme == "Tema: Koyu":
            ui.set_appearance_mode("Dark")
            os.system(f"rm {config}theme/* ; touch {config}theme/dark.txt")
    def change_language(self, new_language: str):
        if new_language == "Language: English" or new_language == "Dil: İngilizce":
            os.system(f"rm {config}language/* ; touch {config}language/en.txt")
        elif new_language == "Language: Turkish" or new_language == "Dil: Türkçe":
            os.system(f"rm {config}language/* ; touch {config}language/tr.txt")
        ask_restart_for_grelintb_ui("normal")
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
                    ui.CTkLabel(self.frame, fg_color=["gray100", "gray20"], corner_radius=20, text=f"{self.progress[0]} - {self.progress[1]}", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.number, column=0, pady=5, padx=10, sticky="nsew")
                elif os.path.isfile(tr):
                    ui.CTkLabel(self.frame, fg_color=["gray100", "gray20"], corner_radius=20, text=f"{self.progress[0]} - {self.progress[1]}", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.number, column=0, pady=5, padx=10, sticky="nsew")
        else:
            if os.path.isfile(en):
                mb.showwarning("Warning", "There are no processes running at the moment.")
            elif os.path.isfile(tr):
                mb.showwarning("Uyarı", "Şu anda çalışan hiçbir işlem yok.")

class Startup(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.scrollable = ui.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable.grid(row=0, column=0, sticky="nsew")
        self.scrollable.grid_columnconfigure((0, 1, 2, 3), weight=1)
        if os.path.isfile(en):
            self.scrollable.configure(label_text=f"Welcome {username}!", label_font=ui.CTkFont(size=16, weight="bold"))
            self.weather = ui.CTkLabel(self.scrollable, text=f"Weather Forecast: Getting", font=ui.CTkFont(size=13, weight="bold")) 
            self.system = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"System", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname = ui.CTkLabel(self.scrollable, text=f"Host: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro = ui.CTkLabel(self.scrollable, text=f"Distribution: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel = ui.CTkLabel(self.scrollable, text=f"Kernel: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime = ui.CTkLabel(self.scrollable, text=f"Uptime: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time = ui.CTkLabel(self.scrollable, text=f"Boot Time: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Usages", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage = ui.CTkLabel(self.scrollable, text=f"CPU: Getting", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage = ui.CTkLabel(self.scrollable, text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage = ui.CTkLabel(self.scrollable, text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage = ui.CTkLabel(self.scrollable, text=f"Swap: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.refresh_button = ui.CTkButton(self, text="Refresh", command=self.refresh, font=ui.CTkFont(size=15, weight="bold"))
        elif os.path.isfile(tr):
            self.scrollable.configure(label_text=f"Merhabalar {username}!", label_font=ui.CTkFont(size=16, weight="bold"))
            self.weather = ui.CTkLabel(self.scrollable, text=f"Hava Durumu: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))   
            self.system = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Sistem", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname = ui.CTkLabel(self.scrollable, text=f"Ana Bilgisayar Adı: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro = ui.CTkLabel(self.scrollable, text=f"Dağıtım: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel = ui.CTkLabel(self.scrollable, text=f"Çekirdek: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime = ui.CTkLabel(self.scrollable, text=f"Çalışma Süresi: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time = ui.CTkLabel(self.scrollable, text=f"Önyüklenme Vakti: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Kullanımlar", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage = ui.CTkLabel(self.scrollable, text=f"CPU: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage = ui.CTkLabel(self.scrollable, text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage = ui.CTkLabel(self.scrollable, text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage = ui.CTkLabel(self.scrollable, text=f"Takas: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.refresh_button = ui.CTkButton(self, text="Yenile", command=self.refresh, font=ui.CTkFont(size=15, weight="bold"))
        self.weather.grid(row=0, column=0, pady=(0, 10), columnspan=4)
        self.system.grid(row=1, column=0, pady=(0, 7.5), columnspan=4)
        self.hostname.grid(row=2, column=0, pady=(0, 7.5), columnspan=4)
        self.distro.grid(row=3, column=0, pady=(0, 7.5), columnspan=4)
        self.kernel.grid(row=4, column=0, pady=(0, 7.5), columnspan=4)
        self.uptime.grid(row=5, column=0, pady=(0, 7.5), columnspan=4)
        self.boot_time.grid(row=6, column=0, pady=(0, 10), columnspan=4)
        self.usages.grid(row=7, column=0, pady=(0, 7.5), columnspan=4)
        self.cpu_usage.grid(row=8, column=0, pady=(0, 10))
        self.disk_usage.grid(row=8, column=1, pady=(0, 10))
        self.ram_usage.grid(row=8, column=2, pady=(0, 10))
        self.swap_usage.grid(row=8, column=3, pady=(0, 10))
        self.refresh_button.grid(row=1, column=0, pady=(10, 0), sticky="nsew")
        self.weather_thread = threading.Thread(target=lambda:self.weather_def(), daemon=True)
        self.weather_thread.start()
        self.cpu_usage_thread = threading.Thread(target=lambda:self.cpu_usage_def(), daemon=True)
        self.cpu_usage_thread.start()
        self.other_def("startup")
    def weather_def(self):
        if os.path.isfile(en):
            self.weather.configure(text="Weather Forecast: "+str(subprocess.Popen('curl -H "Accept-Language: en" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
        elif os.path.isfile(tr):
            self.weather.configure(text="Hava Durumu: "+str(subprocess.Popen('curl -H "Accept-Language: tr" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]))
    def cpu_usage_def(self):
        self.cpu_usage.configure(text=f"CPU: %{str(psutil.cpu_percent(5))}")
    def other_def(self, mode: str):
        self.temps_ok = False
        self.fans_ok = False
        if hasattr (psutil, "sensors_temperatures") and psutil.sensors_temperatures():
            self.temps_ok = True
            self.temps_number = 9
            self.temps = psutil.sensors_temperatures()
            if os.path.isfile(en):
                self.temps_header = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Temperatures", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
            elif os.path.isfile(tr):
                self.temps_header= ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Sıcaklıklar", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
            for self.temps_name, self.temps_entries in self.temps.items():
                self.temps_number = self.temps_number + 1
                if os.path.isfile(en):
                    self.temps_label = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Hardware: {self.temps_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
                elif os.path.isfile(tr):
                    self.temps_label = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Donanım: {self.temps_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.temps_entry in self.temps_entries:
                    self.temps_number = self.temps_number + 1
                    if os.path.isfile(en): 
                        ui.CTkLabel(self.scrollable, text=f"{self.temps_entry.label or self.temps_name}: Current = {self.temps_entry.current} °C, High = {self.temps_entry.high} °C, Critical = {self.temps_entry.critical} °C", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 5), columnspan=4)
                    elif os.path.isfile(tr): 
                        ui.CTkLabel(self.scrollable, text=f"{self.temps_entry.label or self.temps_name}: Current = {self.temps_entry.current} °C, Yüksek = {self.temps_entry.high} °C, Kritik = {self.temps_entry.critical} °C", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.temps_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_fans") and psutil.sensors_fans():
            self.fans_ok = True
            if self.temps_ok == True:
                self.fans_number = self.temps_number + 1
            else:
                self.fans_number = 9
            if os.path.isfile(en):
                self.fans_header = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Fans", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.fans_number, column=0, pady=(5, 7.5), columnspan=4)
            elif os.path.isfile(tr):
                self.fans_header = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Fanlar", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.fans_number, column=0, pady=(5, 7.5), columnspan=4)
            self.fans = psutil.sensors_fans()
            for self.fans_name, self.fans_entries in self.fans.items():
                self.fans_number = self.fans_number + 1
                if os.path.isfile(en):
                    self.fans_label = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Hardware: {self.fans_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 7.5), columnspan=4)
                elif os.path.isfile(tr):
                    self.fans_label = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Donanım: {self.fans_name}", font=ui.CTkFont(size=14, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 7.5), columnspan=4)
                for self.fans_entry in self.fans_entries:
                    self.fans_number = self.fans_number + 1
                    ui.CTkLabel(self.scrollable, text=f"{self.fans_entry.label or self.fans_name}: {self.fans_entry.current} RPM", font=ui.CTkFont(size=13, weight="bold")).grid(row=self.fans_number, column=0, pady=(0, 5), columnspan=4)
        if hasattr (psutil, "sensors_battery") and psutil.sensors_battery():
            if self.fans_ok == True:
                self.batt_number = self.fans_number + 1
            elif self.temps_ok == True:
                self.batt_number = self.temps_number + 1
            else:
                self.batt_number = 9
            self.batt = psutil.sensors_battery()
            if mode == "startup":
                if os.path.isfile(en):
                    self.header_text = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Battery", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.batt_number, column=0, pady=(5, 7.5), columnspan=4)
                    self.charge_text = ui.CTkLabel(self.scrollable, text=f"Charge: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                elif os.path.isfile(tr):
                    self.header_text = ui.CTkLabel(self.scrollable, fg_color=["gray100", "gray20"], corner_radius=20, text=f"Batarya", font=ui.CTkFont(size=15, weight="bold")).grid(row=self.batt_number, column=0, pady=(5, 7.5), columnspan=4)
                    self.charge_text = ui.CTkLabel(self.scrollable, text=f"Şarj: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                if self.batt.power_plugged:
                    if os.path.isfile(en):
                        self.remaining_text = ui.CTkLabel(self.scrollable, text=f"Remaining: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text = ui.CTkLabel(self.scrollable, text=f"Status: {str('Charging' if self.batt.percent < 100 else 'Fully Charged')}", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text = ui.CTkLabel(self.scrollable, text=f"Plugged In: Yes", font=ui.CTkFont(size=13, weight="bold"))
                    elif os.path.isfile(tr):
                        self.remaining_text = ui.CTkLabel(self.scrollable, text=f"Kalan: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text = ui.CTkLabel(self.scrollable, text=f"Durum: {str('Şarj Oluyor' if self.batt.percent < 100 else 'Şarj Oldu')}", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text = ui.CTkLabel(self.scrollable, text=f"Şarja Takılı: Evet", font=ui.CTkFont(size=13, weight="bold"))
                else:
                    if os.path.isfile(en):
                        self.remaining_text = ui.CTkLabel(self.scrollable, text=f"Remaining: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text = ui.CTkLabel(self.scrollable, text=f"Status: Discharging", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text = ui.CTkLabel(self.scrollable, text=f"Plugged In: No", font=ui.CTkFont(size=13, weight="bold"))
                    elif os.path.isfile(tr):
                        self.remaining_text = ui.CTkLabel(self.scrollable, text=f"Kalan: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text = ui.CTkLabel(self.scrollable, text=f"Durum: Şarj Azalıyor", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text = ui.CTkLabel(self.scrollable, text=f"Şarja Takılı: Hayır", font=ui.CTkFont(size=13, weight="bold"))
                self.charge_text.grid(row=self.batt_number + 1, column=0, pady=(0, 5), columnspan=4)
                self.remaining_text.grid(row=self.batt_number + 2, column=0, pady=(0, 5), columnspan=4)
                self.status_text.grid(row=self.batt_number + 3, column=0, pady=(0, 5), columnspan=4)
                self.plugged_text.grid(row=self.batt_number + 4, column=0, pady=(0, 5), columnspan=4)
            elif mode == "refresh":
                if os.path.isfile(en):
                    self.charge_text.configure(text=f"Charge: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                elif os.path.isfile(tr):
                    self.charge_text.configure(text=f"Şarj: {str(round(self.batt.percent, 2))}", font=ui.CTkFont(size=13, weight="bold"))
                if self.batt.power_plugged:
                    if os.path.isfile(en):
                        self.remaining_text.configure(text=f"Remaining: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text.configure(text=f"Status: {str('Charging' if self.batt.percent < 100 else 'Fully Charged')}", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text.configure(text=f"Plugged In: Yes", font=ui.CTkFont(size=13, weight="bold"))
                    elif os.path.isfile(tr):
                        self.remaining_text.configure(text=f"Kalan: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text.configure(text=f"Durum: {str('Şarj Oluyor' if self.batt.percent < 100 else 'Şarj Oldu')}", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text.configure(text=f"Şarja Takılı: Evet", font=ui.CTkFont(size=13, weight="bold"))
                else:
                    if os.path.isfile(en):
                        self.remaining_text.configure(text=f"Remaining: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text.configure(text=f"Status: Discharging", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text.configure(text=f"Plugged In: No", font=ui.CTkFont(size=13, weight="bold"))
                    elif os.path.isfile(tr):
                        self.remaining_text.configure(text=f"Kalan: {str(dt.timedelta(seconds = self.batt.secsleft))}", font=ui.CTkFont(size=13, weight="bold"))
                        self.status_text.configure(text=f"Durum: Şarj Azalıyor", font=ui.CTkFont(size=13, weight="bold"))
                        self.plugged_text.configure(text=f"Şarja Takılı: Hayır", font=ui.CTkFont(size=13, weight="bold"))
    def refresh(self):
        if os.path.isfile(en):
            self.scrollable.configure(label_text=f"Welcome {username}!", label_font=ui.CTkFont(size=16, weight="bold"))
            self.weather.configure(text=f"Weather Forecast: Getting", font=ui.CTkFont(size=13, weight="bold")) 
            self.system.configure(fg_color=["gray100", "gray20"], corner_radius=20, text=f"System", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname.configure(text=f"Host: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro.configure(text=f"Distribution: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel.configure(text=f"Kernel: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime.configure(text=f"Uptime: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time.configure(text=f"Boot Time: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages.configure(fg_color=["gray100", "gray20"], corner_radius=20, text=f"Usages", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage.configure(text=f"CPU: Getting", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage.configure(text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage.configure(text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage.configure(text=f"Swap: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        elif os.path.isfile(tr):
            self.scrollable.configure(label_text=f"Merhabalar {username}!", label_font=ui.CTkFont(size=16, weight="bold"))
            self.weather.configure(text=f"Hava Durumu: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))   
            self.system.configure(fg_color=["gray100", "gray20"], corner_radius=20, text=f"Sistem", font=ui.CTkFont(size=15, weight="bold")) 
            self.hostname.configure(text=f"Ana Bilgisayar Adı: {str(socket.gethostname())}", font=ui.CTkFont(size=13, weight="bold"))
            self.distro.configure(text=f"Dağıtım: {distro.name(pretty=True)}", font=ui.CTkFont(size=13, weight="bold"))
            self.kernel.configure(text=f"Çekirdek: {platform.platform()}", font=ui.CTkFont(size=13, weight="bold"))
            self.uptime.configure(text=f"Çalışma Süresi: {os.popen('uptime -p').read()[:-1].replace('up ', '')}", font=ui.CTkFont(size=13, weight="bold"))
            self.boot_time.configure(text=f"Önyüklenme Vakti: {str(dt.datetime.fromtimestamp(psutil.boot_time()).strftime('%d.%m.%Y %H:%M:%S'))}", font=ui.CTkFont(size=13, weight="bold"))
            self.usages.configure(fg_color=["gray100", "gray20"], corner_radius=20, text=f"Kullanımlar", font=ui.CTkFont(size=15, weight="bold"))
            self.cpu_usage.configure(text=f"CPU: Alınıyor", font=ui.CTkFont(size=13, weight="bold"))
            self.disk_usage.configure(text=f"Disk: %{str(psutil.disk_usage('/')[3])}", font=ui.CTkFont(size=13, weight="bold"))
            self.ram_usage.configure(text=f"RAM: %{str(psutil.virtual_memory()[2])}", font=ui.CTkFont(size=13, weight="bold"))
            self.swap_usage.configure(text=f"Takas: %{str(psutil.swap_memory()[3])}", font=ui.CTkFont(size=13, weight="bold"))
        self.weather_thread = threading.Thread(target=lambda:self.weather_def(), daemon=True)
        self.weather_thread.start()
        self.cpu_usage_thread = threading.Thread(target=lambda:self.cpu_usage_def(), daemon=True)
        self.cpu_usage_thread.start()
        self.other_def("refresh")
        
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
            self.button1 = ui.CTkButton(self.options, text="Take A New Note", command=lambda:self.new_note("new-note"))
            self.button2 = ui.CTkButton(self.options, text="Open", command=self.open)
            self.button3 = ui.CTkButton(self.options, text="Rename", command=self.rename)
            self.button4 = ui.CTkButton(self.options, text="Save", command=self.save)
            self.button5 = ui.CTkButton(self.options, text="Delete", command=self.delete)
        elif os.path.isfile(tr):
            self.list = ui.CTkOptionMenu(self.options, values=["Notlarınızın Listesi"] + self.notes, command=self.option)
            self.entry = ui.CTkEntry(self.options, placeholder_text="Ad")
            self.button1 = ui.CTkButton(self.options, text="Yeni Bir Not Al", command=lambda:self.new_note("new-note"))
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
    def new_note(self, mode: str):
        if os.path.isfile(en):
            self.dialog = ui.CTkInputDialog(text=f"Type a new note name.", title="Type New Name")
        elif os.path.isfile(tr):
            self.dialog = ui.CTkInputDialog(text=f"Yeni bir not adı girin.", title="Yeni Ad Girin")
        self.new_name = self.dialog.get_input()
        if self.new_name == None:
            if os.path.isfile(en) and mode == "new-note":
                mb.showwarning("Warning", "Taking a new note canceled.")
            elif os.path.isfile(tr) and mode == "new-note":
                mb.showwarning("Uyarı", "Yeni bir not alma iptal edildi.")
            return
        os.system(f"touch {notes}{self.new_name}")
        if not os.path.isfile(f"{notes}{self.new_name}"):
            if os.path.isfile(en):
                mb.showerror("Error", "The note could not be created.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Not oluşturulamadı.")
            return
        self.entry.delete(0, "end")
        self.entry.insert(0, f"{notes}{self.new_name}")
        self.notes = os.listdir(notes)
        if os.path.isfile(en):
            if mode == "new-note":
                mb.showinfo("Information", f"The note created.")
            self.list.configure(values=["List Of Your Notes"] + self.notes)
        elif os.path.isfile(tr):
            if mode == "new-note":
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
            mb.showinfo("Information", f"The note or document renamed as {self.new_name}.")
            self.list.configure(values=["List Of Your Notes"] + self.notes)
        elif os.path.isfile(tr):
            mb.showinfo("Bilgilendirme", f"Not ya da belge {self.new_name} olarak yeniden adlandırıldı.")
            self.list.configure(values=["Notlarınızın Listesi"] + self.notes)
    def save(self):
        if self.entry.get() == "":
            self.new_note("save-note")
        try:
            with open(self.entry.get(), "w+") as self.file:
                self.file.write(self.content.get("0.0", 'end'))
        except:
            if os.path.isfile(en):
                mb.showerror("Error","The note or document could not be saved.")
            elif os.path.isfile(tr):
                mb.showerror("Hata","Not ya da belge kaydedilemedi.")
            return
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
            mb.showerror("Error", "Please select application from list or enter packages name.")
        elif os.path.isfile(tr):
            mb.showerror("Hata", "Lütfen listeden uygulama seçin ya da paket adları girin.")
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
                self.command = f"apt -y search {self.entry.get()}"
            elif operation == "install":
                self.command = f"pkexec apt -y install {self.entry.get()}"
            elif operation == "reinstall":
                self.command = f"pkexec apt -y install --reinstall {self.entry.get()}"
            elif operation == "uninstall":
                self.command = f"pkexec apt -y autoremove --purge {self.entry.get()}"
            elif operation == "update":
                self.command = f"pkexec apt -y upgrade {self.entry.get()}"
        elif os.path.isfile(fedora):
            if operation == "search":
                self.command = f"dnf -y --nogpgcheck search {self.entry.get()}"
            elif operation == "install":
                self.command = f"pkexec dnf -y --nogpgcheck install {self.entry.get()}"
            elif operation == "reinstall":
                self.command = f"pkexec dnf -y --nogpgcheck reinstall {self.entry.get()}"
            elif operation == "uninstall":
                self.command = f"pkexec dnf -y --nogpgcheck remove {self.entry.get()}"
            elif operation == "update":
                self.command = f"pkexec dnf -y --nogpgcheck update {self.entry.get()}"
        elif os.path.isfile(solus):
            if operation == "search":
                self.command = f"eopkg -y search {self.entry.get()}"
            elif operation == "install":
                self.command = f"pkexec eopkg -y install {self.entry.get()}"
            elif operation == "reinstall":
                self.command = f"pkexec eopkg -y install --reinstall {self.entry.get()}"
            elif operation == "uninstall":
                self.command = f"pkexec eopkg -y remove --purge {self.entry.get()}"
            elif operation == "update":
                self.command = f"pkexec eopkg -y upgrade {self.entry.get()}"
        elif os.path.isfile(arch):
            if operation == "search":
                self.command = f"pacman --noconfirm -Ss {self.entry.get()}"
            elif operation == "install" or operation == "reinstall":
                self.command = f"pkexec pacman --noconfirm -S {self.entry.get()}"
            elif operation == "uninstall":
                self.command = f"pkexec pacman --noconfirm -Rns {self.entry.get()}"
            elif operation == "update":
                self.command = f"pkexec pacman --noconfirm -Syu {self.entry.get()}"
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(self.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
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
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
                mb.showerror("Error", "Please enter packages name.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Lütfen paket adları girin.")
            return
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
            install_flatpak()
            if ask_f == False:
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
        if operation == "search":
            self.command = f"flatpak search {self.entry.get()}"
        elif operation == "install":
            self.command = f"flatpak install {self.entry.get()}"
        elif operation == "reinstall":
            self.command = f"flatpak install --reinstall '{self.entry.get()}"
        elif operation == "uninstall":
            self.command = f"flatpak uninstall {self.entry.get()}"
        elif operation == "update":
            self.command = f"flatpak update '{self.entry.get()}"
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(self.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
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
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
                    self.command = f"pkexec apt -y install {self.dewm.get().lower()}"
                elif operation == "reinstall":
                    self.command = f"pkexec apt -y install --reinstall {self.dewm.get().lower()}"
                elif operation == "uninstall":
                    self.command = f"pkexec apt -y autoremove --purge {self.dewm.get().lower()}"
                elif operation == "update":
                    self.command = f"pkexec apt -y upgrade {self.dewm.get().lower()}"
            elif self.dewm.get().lower() == "mate":
                if operation == "install":
                    self.command = f"pkexec apt -y install mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == "reinstall":
                    self.command = f"pkexec apt -y install --reinstall mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == "uninstall":
                    self.command = f"pkexec apt -y autoremove --purge mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
                elif operation == "update":
                    self.command = f"pkexec apt -y upgrade mate-desktop-environment mate-desktop-environment-core mate-desktop-environment-extra"
        elif os.path.isfile(fedora):
            if self.dewm.get() in ["KDE", "Xfce", "Phosh", "LXDE", "LXQt", "Cinnamon", "Mate", "Sugar", "Deepin", "Budgie", "Basic", "Sway", "Deepin", "i3"]:
                if operation == "install":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck install @{self.dewm.get().lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "reinstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck reinstall @{self.dewm.get().lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "uninstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck remove @{self.dewm.get().lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "uodate":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck upgrade @{self.dewm.get().lower()}-desktop-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
            elif self.dewm.get() in ["Openbox", "Fluxbox", "Blackbox", "bspwm"]:
                if operation == "install":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck install {self.dewm.get().lower()}-desktop ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "reinstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck reinstall {self.dewm.get().lower()}-desktop ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "uninstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck remove {self.dewm.get().lower()}-desktop ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "update":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck upgrade {self.dewm.get().lower()}-desktop ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
            elif self.dewm.get() == "GNOME":
                if operation == "install":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck install @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "reinstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck reinstall @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "uninstall":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck remove @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"
                elif operation == "update":
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck upgrade @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"             
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck upgrade @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"             
        elif os.path.isfile(solus):
            if self.dewm.get().lower() not in ["openbox", "fluxbox", "bspwm"]:
                if operation == "install":
                    self.command = f"pkexec eopkg -y install -c desktop.{self.dewm.get().lower()}"
                elif operation == "reinstall":
                    self.command = f"pkexec eopkg -y install --reinstall -c desktop.{self.dewm.get().lower()}"
                elif operation == "uninstall":
                    self.command = f"pkexec eopkg -y remove --purge -c desktop.{self.dewm.get().lower()}"
                elif operation == "update":
                    self.command = f"pkexec eopkg -y upgrade -c desktop.{self.dewm.get().lower()}"
            else:
                if operation == "install":
                    self.command = f"pkexec eopkg -y install {self.dewm.get().lower()}"
                elif operation == "reinstall":
                    self.command = f"pkexec eopkg -y install --reinstall {self.dewm.get().lower()}"
                elif operation == "uninstall":
                    self.command = f"pkexec eopkg -y remove --purge {self.dewm.get().lower()}"
                elif operation == "update":
                    self.command = f"pkexec eopkg -y upgrade {self.dewm.get().lower()}"        
                    self.command = f"pkexec bash -c 'dnf -y --nogpgcheck upgrade @workstation-product-environment ; SYSTEMD_COLORS=0 systemctl set-default graphical.target'"              
        elif os.path.isfile(solus):
            if self.dewm.get().lower() not in ["openbox", "fluxbox", "bspwm"]:
                if operation == "install":
                    self.command = f"pkexec eopkg -y install -c desktop.{self.dewm.get().lower()}"
                elif operation == "reinstall":
                    self.command = f"pkexec eopkg -y install --reinstall -c desktop.{self.dewm.get().lower()}"
                elif operation == "uninstall":
                    self.command = f"pkexec eopkg -y remove --purge -c desktop.{self.dewm.get().lower()}"
                elif operation == "update":
                    self.command = f"pkexec eopkg -y upgrade -c desktop.{self.dewm.get().lower()}"
            else:
                if operation == "install":
                    self.command = f"pkexec eopkg -y install {self.dewm.get().lower()}"
                elif operation == "reinstall":
                    self.command = f"pkexec eopkg -y install --reinstall {self.dewm.get().lower()}"
                elif operation == "uninstall":
                    self.command = f"pkexec eopkg -y remove --purge {self.dewm.get().lower()}"
                elif operation == "update":
                    self.command = f"pkexec eopkg -y upgrade {self.dewm.get().lower()}"        
        elif os.path.isfile(arch):
            if operation == "install":
                self.command = f"pkexec pacman --noconfirm -S {self.dewm.get().lower()}"
            elif operation == "reinstall":
                self.command = f"pkexec pacman --noconfirm -S {self.dewm.get().lower()}"
            elif operation == "uninstall":
                self.command = f"pkexec pacman --noconfirm -Rns {self.dewm.get().lower()}"
            elif operation == "update":
                self.command = f"pkexec pacman --noconfirm -Syu {self.dewm.get().lower()}"
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(self.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
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
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
                self.command = 'pkexec apt -y upgrade'
            elif operation == "dist_update":
                self.command = 'pkexec apt -y dist-upgrade'
            elif operation == "clean":
                self.command = 'pkexec apt-get -y- autoclean'
            elif operation == "remove":
                self.command = 'pkexec apt -y autoremove'
            elif operation == "fix":
                self.command = 'pkexec bash -c "apt-get -y install -f ; dpkg --configure -a ; aptitude -y install"'
            elif operation == "history":
                self.command = 'cat /var/log/dpkg.log'
            elif operation == "list":
                self.command = 'dpkg --list | grep ^i'
        elif os.path.isfile(fedora):
            if operation == "update":
                self.command = 'pkexec dnf -y --nogpgcheck upgrade'
            elif operation == "dist_update":
                self.command = 'pkexec dnf -y --nogpgcheck distro-sync'
            elif operation == "clean":
                self.command = 'pkexec dnf -y --nogpgcheck clean all'
            elif operation == "remove":
                self.command = 'pkexec dnf -y --nogpgcheck autoremove'
            elif operation == "fix":
                self.command = 'pkexec dnf -y --nogpgcheck repoquery --unsatisfied'
            elif operation == "history":
                self.command = 'dnf -y --nogpgcheck history'
            elif operation == "list":
                self.command = 'dnf -y --nogpgcheck list installed'
        elif os.path.isfile(solus):
            if operation == "update":
                self.command = 'pkexec eopkg -y upgrade'
            elif operation == "clean":
                self.command = 'pkexec eopkg -y dc'
            elif operation == "remove":
                self.command = 'pkexec eopkg -y rmf'
            elif operation == "history":
                self.command = 'eopkg -y history'
            elif operation == "list":
                self.command = 'eopkg -y list-installed'
        elif os.path.isfile(arch):
            if operation == "update":
                self.command = 'pkexec pacman --noconfirm -Syu'
            elif operation == "dist_update":
                self.command = 'pkexec pacman --noconfirm -Syu'
            elif operation == "clean":
                self.command = 'pkexec pacman --noconfirm -Scc'
            elif operation == "remove":
                self.command = 'pacman --noconfirm -Qdtq | pacman --noconfirm -Rs -'
            elif operation == "fix":
                self.command = 'pacman --noconfirm -Dk'
            elif operation == "history":
                self.command = 'cat /var/log/pacman.log'
            elif operation == "list":
                self.command = 'pacman --noconfirm -Q'
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(self.command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
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
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
            install_flatpak()
            if ask_f == False:
                return
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
            if operation == "update -y":
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
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(f"flatpak {operation}", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
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
            if operation == "update -y":
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
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
            self.button1 = ui.CTkButton(self.frame, text="Status", command=lambda:self.go_main(["", "status"]))
            self.button2 = ui.CTkButton(self.frame, text="Enable", command=lambda:self.go_main(["pkexec", "enable"]))
            self.button3 = ui.CTkButton(self.frame, text="Disable", command=lambda:self.go_main(["pkexec", "disable"]))
            self.button4 = ui.CTkButton(self.frame, text="Start", command=lambda:self.go_main(["pkexec", "start"]))
            self.button5 = ui.CTkButton(self.frame, text="Stop", command=lambda:self.go_main(["pkexec", "start"]))
        elif os.path.isfile(tr):
            self.entry = ui.CTkEntry(self.frame, placeholder_text="Servis Adı")
            self.button1 = ui.CTkButton(self.frame, text="Durum", command=lambda:self.go_main(["", "status"]))
            self.button2 = ui.CTkButton(self.frame, text="Aktifleştir", command=lambda:self.go_main(["pkexec", "enable"]))
            self.button3 = ui.CTkButton(self.frame, text="Devre Dışı Bırak", command=lambda:self.go_main(["pkexec", "disable"]))
            self.button4 = ui.CTkButton(self.frame, text="Başlat", command=lambda:self.go_main(["pkexec", "start"]))
            self.button5 = ui.CTkButton(self.frame, text="Durdur", command=lambda:self.go_main(["pkexec", "start"]))
        self.entry.grid(row=0, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button1.grid(row=1, column=0, sticky="nsew", pady=5, padx=(10, 0))
        self.button2.grid(row=2, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button3.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button4.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(10, 0))
        self.button5.grid(row=5, column=0, sticky="nsew", padx=(10, 0))
    def do_main(self, operation: str):
        if self.entry.get() == "":
            if os.path.isfile(en):
                mb.showerror("Error", "Please enter service name.")
            elif os.path.isfile(tr):
                mb.showerror("Hata", "Lütfen servis adı girin.")
            return
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", 'end')
        self.textbox.configure(state="disabled")
        with subprocess.Popen(f"{operation[0]} bash -c 'SYSTEMD_COLORS=0 systemctl {operation[1]} {self.entry.get()}'", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=1) as self.run_command:
            for self.out in self.run_command.stdout:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.out)
                self.textbox.configure(state="disabled")
            for self.err in self.run_command.stderr:
                self.textbox.configure(state="normal")
                self.textbox.insert("end", self.err)
                self.textbox.configure(state="disabled")
        if self.run_command.returncode == 0:
            main_successful()
        else:
            main_error()
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
        with open(f"/home/{username}/.bashrc", "r") as self.bashrc:
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
            with open(f"/home/{username}/.bashrc", "r") as self.bashrc:
                self.content = self.bashrc.read()
        elif self.var.get() == "zsh":
            if not os.path.isfile("/usr/bin/zsh") and not os.path.isfile("/bin/zsh"):
                install_app("Zsh", "zsh")
            with open(f"/home/{username}/.zshrc", "r") as self.zshrc:
                self.content = self.zshrc.read()
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", self.content)
    def save(self):
        if self.var.get() == "bash":
            os.system(f"cp /home/{username}/.bashrc /home/{username}/.bashrc-grelintb.bak")
            with open(f"/home/{username}/.bashrc", "w+") as self.file:
                self.file.write(self.textbox.get("0.0", 'end'))
            with open(f"/home/{username}/.bashrc") as self.file:
                self.output = self.file.read()
        elif self.var.get() == "zsh":
            os.system(f"cp /home/{username}/.zshrc /home/{username}/.zshrc-grelintb.bak")
            with open(f"/home/{username}/.zshrc", "w+") as self.file:
                self.file.write(self.textbox.get("0.0", 'end'))
            with open(f"/home/{username}/.zshrc") as self.file:
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
            os.system(f"cd /home/{username} ; cp .bashrc .bashrc-session-grelintb.bak")
        if os.path.isfile(f"/home/{username}/.zshrc"):
            os.system(f"cd /home/{username} ; cp .zshrc .zshrc-session-grelintb.bak")
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
            self.entry = ui.CTkEntry(self, placeholder_text="New Name For Computer")
            self.button = ui.CTkButton(self, text="Apply", command=self.apply)
        elif os.path.isfile(tr):
            self.label = ui.CTkLabel(self, text="Bilgisayarın mevcut ismi: "+computername)
            self.entry = ui.CTkEntry(self, placeholder_text="Bilgisayar İçin Yeni Ad")
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
                "\n\nNote from GrelinTB developer: For Arch base, I suggest you look for other alternatives.")
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
                "\n\nGrelinTB geliştiricisinin notu: Arch tabanı için başka alternatiflere yönelmenizi öneririm.")
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
        if os.path.isfile(f"/home/{username}/.calc-history-grelintb.txt"):
            with open(f"/home/{username}/.calc-history-grelintb.txt", "r") as self.file:
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
            with open(f"/home/{username}/.calc-history-grelintb.txt", "a+") as self.file:
                self.file.write(self.process+"="+self.result+"\n")
            with open(f"/home/{username}/.calc-history-grelintb.txt", "r") as self.file:
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
        subprocess.Popen(f"rm /home/{username}/.calc-history-grelintb.txt", shell=True)
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
                self.title(f"GrelinTB says at {str(dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}: Today is developer's (MuKonqi) birthday!")
            elif os.path.isfile(tr):
                self.title(f'Vakit {str(dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}, GrelinTB söyler: Bugün geliştiricinin (MuKonqi) doğum günü!')
        if dt.datetime.now().weekday() == 2:
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
            print(" Copyright (C) 2024 MuKonqi (Muhammed S.)")
            print("This is GrelinTB's help page.")
            print("Current version: "+version_current)
            print("Developer:       MuKonqi (Muhammed S.)")
            print("License:         GPLv3 or later")
            print("Credit:          Google Material Symbols (for application icon)")
            print("List of all parameters for GrelinTB:")
            print("  help:          Show this page")
            print("  grelintb:      Open website of GrelinTB's GitHub repository")
            print("  version:       Show changelog of "+version_current)
            print("  developer:     Open website of GrelinTB developer")
            print("  license:       Show license text of GPLv3")
            print("  credit:        Open website of the credit")
            print("  update:        Update GrelinTB")
            print("  reset:         Reset GrelinTB")
            print("  uninstall:     Uninstall GrelinTB")  
            print("                 Start GrelinTB normally (default)")
        elif os.path.isfile(tr):
            print(" Telif Hakkı (C) 2024 MuKonqi (Muhammed S.)")
            print("Bu GrelinTB'nin yardım sayfasıdır.")
            print("Şimdiki sürüm:   "+version_current)
            print("Geliştirici:     MuKonqi (Muhammed S.)")
            print("Lisans:          GPLv3 veya daha sonrası")
            print("Kredi:           Google Material Symbols (uygulama ikonu için)")            
            print("GrelinTB için tüm parametrelerin listesi:")
            print("  yardım:        Bu sayfayı göster")
            print("  grelintb:      GrelinTB'nin GitHub deposunu aç")
            print("  sürüm:         "+version_current+" sürümünün değişik günlüğünü göster")
            print("  geliştirici:   GrelinTB geliştiricisinin internet sitesini aç")
            print("  lisans:        GPLv3 lisansının metnini göster")
            print("  kredi:         Kredinin internet sitesini aç")
            print("  güncelle:      GrelinTB'yı güncelle")
            print("  sıfırla:       GrelinTB'yı sıfırla")
            print("  kaldır:        GrelinTB'yı kaldır")
            print("                 GrelinTB'yi normal olarak aç (varsayılan)")
        sys.exit(0)
    elif "grelintb" in sys.argv[1:]:
        subprocess.Popen("xdg-open https://mukonqi.github.io/grelintb/index.html", shell=True)
        sys.exit(0)
    elif "version" in sys.argv[1:] or "sürüm" in sys.argv[1:]:
        with open("/usr/local/bin/grelintb/primary-changelog.txt", "r") as cl_primary_file:
            cl_primary_text = cl_primary_file.read()
        with open("/usr/local/bin/grelintb/major-changelog.txt", "r") as cl_major_file:
            cl_major_text = cl_major_file.read()
        with open("/usr/local/bin/grelintb/minor-changelog.txt", "r") as cl_minor_file:
            cl_minor_text = cl_minor_file.read()
        if os.path.isfile(en):
            print(f" Primary Changelog For {version_current}\n{cl_primary_text}\n\n Major Changelog For {version_current}\n{cl_major_text}\n\n Minor Changelog For {version_current}\n{cl_minor_text}")
        elif os.path.isfile(tr):
            print(f" {version_current} İçin Birincil Değişiklik Günlüğü\n{cl_primary_text}\n\n {version_current} İçin Major Değişiklik Günlüğü\n{cl_major_text}\n\n {version_current} İçin Minor Değişiklik Günlüğü\n{cl_minor_text}")
        sys.exit(0)
    elif "developer" in sys.argv[1:] or "geliştirici" in sys.argv[1:]:
        subprocess.Popen("xdg-open https://mukonqi.github.io", shell=True)
        sys.exit(0)
    elif "license" in sys.argv[1:] or "lisans" in sys.argv[1:]:
        with open("/usr/local/bin/grelintb/LICENSE.txt", "r") as l_file:
            l_text = l_file.read()
        print(f"\n{l_text}")
        sys.exit(0)
    elif "credit" in sys.argv[1:] or "kredi" in sys.argv[1:]:
        subprocess.Popen(f"xdg-open https://fonts.google.com/icons?selected=Material%20Symbols%20Outlined%3Aconstruction%3AFILL%400%3Bwght%40700%3BGRAD%40200%3Bopsz%4048")
        sys.exit(0)
    elif "update" in sys.argv[1:] or "güncelle" in sys.argv[1:]:
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        if version_latest != version_current:
            if os.path.isfile(en):
                print(f" Primary Changelog For {version_latest}\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/primary-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n\n Major Changelog For {version_latest}\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/major-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n\n Minor Changelog For {version_latest}\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/minor-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n")
                question = input(f"Do you want to update {version_latest} version? [y/n or e/h]: ")
            elif os.path.isfile(tr):
                print(f" {version_latest} İçin Birincil Değişiklik Günlüğü\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/primary-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n\n {version_latest} İçin Major Değişiklik Günlüğü\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/major-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n\n {version_latest} İçin Minor Değişiklik Günlüğü\n{str(subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/minor-changelog.txt', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0])}\n")
                question = input(f"{version_latest} sürümüne güncellemek ister misiniz? [e/h veya y/n]: ")
            if question.lower() == "y" or question.lower() == "e":
                os.system("pkexec /usr/local/bin/grelintb/update.sh")
                if os.path.isfile(en):
                    print("GrelinTB updated.")
                elif os.path.isfile(tr):
                    print("GrelinTB güncellendi.")
            elif question.lower() == "n" or question.lower() == "h":
                if os.path.isfile(en):
                    print("Update cancelled.")
                elif os.path.isfile(tr):
                    print("Güncelleme iptal edildi.")                
        else:
            if os.path.isfile(en):
                print("GrelinTB is up to date.")
            elif os.path.isfile(tr):
                print("GrelinTB güncel.")
        sys.exit(0)
    elif "reset" in sys.argv[1:] or "sıfırla" in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/reset.sh")
        if os.path.isfile(en):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            print("GrelinTB reset.")
        elif os.path.isfile(tr):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            print("GrelinTB sıfırlandı.")
        sys.exit(0)
    elif "uninstall" in sys.argv[1:] or "kaldır" in sys.argv[1:]:
        os.system("pkexec /usr/local/bin/grelintb/uninstall.sh")
        if os.path.isfile(en):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            print("GrelinTB uninstalled.")
        elif os.path.isfile(tr):
            os.system(f"rm -rf /home/{username}/.config/grelintb")
            print("GrelinTB kaldırıldı.")
        sys.exit(0)
    else:
        root = Root(className="grelintb")
        root.mainloop()