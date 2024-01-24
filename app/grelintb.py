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

version_current = "v0.2.3.0 (Alpha)" # temporary
# version_file = open("/usr/local/bin/grelintb/version.txt", "r")
# version_current = version_file.readline()
# version_file.close()

import customtkinter as ui
from tkinter import messagebox as mb
import threading
import subprocess
import os
import getpass

username = getpass.getuser()
config = "/home/"+username+"/.config/grelintb/"
en = "/home/"+username+"/.config/grelintb/language/en.txt"
tr = "/home/"+username+"/.config/grelintb/language/tr.txt"
system = "/home/"+username+"/.config/grelintb/theme/system.txt"
light = "/home/"+username+"/.config/grelintb/theme/light.txt"
dark = "/home/"+username+"/.config/grelintb/theme/dark.txt"
s_true = "/home/"+username+"/.config/grelintb/startup/true.txt"
s_false = "/home/"+username+"/.config/grelintb/startup/false.txt"

if not os.path.isdir(config):
    os.system("cd /home/"+username+"/.config ; mkdir grelintb ; cd grelintb ; mkdir language ; mkdir theme ; mkdir startup")
    os.system("cd "+config+" ; cd language ; touch en.txt ; cd .. ; cd theme ; touch system.txt ; cd .. ; cd startup ; touch true.txt")
if not os.path.isdir(config+"language/"):
    os.system("cd "+config+" ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(config+"theme/"):
    os.system("cd "+config+" ; mkdir theme ; cd theme ; touch system.txt")
if not os.path.isdir(config+"startup/"):
    os.system("cd "+config+" ; mkdir startup ; cd startup ; touch true.txt")

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
arch1 = "/bin/pacman"
arch2 = "/usr/bin/pacman"

if os.path.isfile(system):
    ui.set_appearance_mode("System")
elif os.path.isfile(light):
    ui.set_appearance_mode("Light")
elif os.path.isfile(dark):
    ui.set_appearance_mode("Dark")

ui.set_default_color_theme("dark-blue")

if os.path.isfile(en):
    install_text = "Install"
    reinstall_text = "Reinstall"
    uninstall_text = "Uninstall"
    search_text = "Search"
    enter_pkg_text = "Enter package name..."
    source_text = "Source"
    repos_text = "Repositories"
elif os.path.isfile(tr):
    install_text = "Kur"
    reinstall_text = "Yeniden Kur"
    uninstall_text = "Kaldır"
    search_text = "Ara"
    enter_pkg_text = "Paket adı girin..."
    source_text = "Kaynak"
    repos_text = "Depolar"

class AboutWindow(ui.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global version_latest
        version_latest = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/version.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        if version_current != version_latest:
            self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.geometry("640x320")
        self.minsize(640, 320)
        self.button1 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="GrelinTB\nGreat Tool Box for Linux", command=self.grelintb, font=ui.CTkFont(size=20, weight="bold"))
        if os.path.isfile(en):
            self.title("About")
            self.button2 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="License: GNU General Public License, Version 3.0", command=self.gplv3, font=ui.CTkFont(size=16, weight="normal"))
            self.button3 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Developer: MuKonqi (Muhammed S.)", command=self.mukonqi, font=ui.CTkFont(size=16, weight="normal"))
            if version_current == version_latest:
                self.button4 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Version: "+version_current, command=self.changelog_current, font=ui.CTkFont(size=16, weight="normal"))
            elif version_current != version_latest:
                self.button4 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Version: "+version_current, command=self.changelog_current, font=ui.CTkFont(size=16, weight="normal"))        
                self.button5 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Latest Version: "+version_latest, command=self.changelog_latest, font=ui.CTkFont(size=16, weight="normal"))      
        elif os.path.isfile(tr):
            self.title("Hakkında")
            self.button2 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Lisans: GNU General Public License, Version 3.0", command=self.gplv3, font=ui.CTkFont(size=16, weight="normal"))
            self.button3 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Geliştirici: MuKonqi (Muhammed S.)", command=self.mukonqi, font=ui.CTkFont(size=16, weight="normal"))
            if version_current == version_latest:
                self.button4 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Sürüm: "+version_current, command=self.changelog_current, font=ui.CTkFont(size=16, weight="normal"))
            elif version_current != version_latest:
                self.button4 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Sürüm: "+version_current, command=self.changelog_current, font=ui.CTkFont(size=16, weight="normal"))
                self.button5 = ui.CTkButton(self, fg_color="transparent", text_color=("#2f2f2f", "#a9a9a9"), text="Son Sürüm: "+version_latest, command=self.changelog_latest, font=ui.CTkFont(size=16, weight="normal"))
        self.button1.grid(row=0, column=0, sticky="nsew", padx=20, pady=5)
        self.button2.grid(row=1, column=0, sticky="nsew", padx=20, pady=5)
        self.button3.grid(row=2, column=0, sticky="nsew", padx=20, pady=5)
        self.button4.grid(row=3, column=0, sticky="nsew", padx=20, pady=5)
        if version_current != version_latest:
            self.button5.grid(row=4, column=0, sticky="nsew", padx=20, pady=5)
    def grelintb(self):
        os.system("xdg-open https://github.com/mukonqi/grelintb")
    def changelog_current(self):
        self.ccw = ui.CTkToplevel()
        self.ccw.geometry("560x560")
        self.ccw.minsize(560, 560)
        self.ccw.grid_rowconfigure(0, weight=1)
        self.ccw.grid_columnconfigure(0, weight=1)
        # if os.path.isfile(en):
        #     self.ccw.title("Changelog For "+version_current)
        #     cc_file = open("/usr/local/bin/grelintb/changelog-en.txt", "r")
        # elif os.path.isfile(tr):
        #     self.ccw.title(version_current+" için Değişiklik Günlüğü")
        #     cc_file = open("/usr/local/bin/grelintb/changelog-tr.txt", "r")
        # cc_text = cc_file.read()
        # cc_file.close()
        # self.textbox = ui.CTkTextbox(self.ccw, fg_color="transparent")
        # self.textbox.insert("0.0", cc_text)
        # self.textbox.grid(row=0, column=0, sticky="nsew")
    def changelog_latest(self):
        self.clw = ui.CTkToplevel()
        self.clw.geometry("560x560")
        self.clw.minsize(560, 560)
        self.clw.grid_rowconfigure(0, weight=1)
        self.clw.grid_columnconfigure(0, weight=1)
        # if os.path.isfile(en):
        #     self.clw.title("Changelog For "+version_latest)
        #     cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-en.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        # elif os.path.isfile(tr):
        #     self.clw.title(version_latest+" için Değişiklik Günlüğü")
        #     cl_text = subprocess.Popen('curl https://raw.githubusercontent.com/MuKonqi/grelintb/main/app/changelog-tr.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        # self.textbox = ui.CTkTextbox(self.clw, fg_color="transparent")
        # self.textbox.insert("0.0", cl_text)
        # self.textbox.grid(row=0, column=0, sticky="nsew")
    def gplv3(self):
        self.lw = ui.CTkToplevel()
        self.lw.geometry("560x560")
        self.lw.minsize(560, 560)
        self.lw.grid_rowconfigure(0, weight=1)
        self.lw.grid_columnconfigure(0, weight=1)
        # if os.path.isfile(en):
        #     self.lw.title("GPLv3 License")
        # elif os.path.isfile(tr):
        #     self.lw.title("GPlv3 Lisansı")
        # license_file = open("/usr/local/bin/grelintb/LICENSE.txt", "r")
        # license_text = license_file.read()
        # license_file.close()
        # self.textbox = ui.CTkTextbox(self.lw, fg_color="transparent")
        # self.textbox.insert("0.0", license_text)
        # self.textbox.grid(row=0, column=0, sticky="nsew")
    def mukonqi(self):
        os.system("xdg-open https://mukonqi.github.io")

class Sidebar(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(5, weight=1)
        self.text = ui.CTkLabel(self, text="GrelinTB", font=ui.CTkFont(size=20, weight="bold"))
        self.language_menu = ui.CTkOptionMenu(self, values=["English", "Türkçe"], command=self.change_language)
        if os.path.isfile(s_true):
            self.startup_var = ui.StringVar(value="on")
        elif os.path.isfile(s_false):
            self.startup_var = ui.StringVar(value="off")
        if os.path.isfile(en):
            self.button_1 = ui.CTkButton(self, text="About", command=self.about)
            self.button_2 = ui.CTkButton(self, text="Update", command=self.update)
            self.button_3 = ui.CTkButton(self, text="Reset", command=self.reset)
            self.button_4 = ui.CTkButton(self, text=uninstall_text, command=self.uninstall)
            self.startup = ui.CTkCheckBox(self, text="Startup Informations", command=self.startup_option, variable=self.startup_var, onvalue="on", offvalue="off")
            self.appearance_label = ui.CTkLabel(self, text="Appearance:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Language:", anchor="w")
            self.language_menu.set("English")
            if os.path.isfile(system):
                self.appearance_menu.set("System")
            elif os.path.isfile(light):
                self.appearance_menu.set("Light")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Dark")
        elif os.path.isfile(tr):
            self.button_1 = ui.CTkButton(self, text="Hakkında", command=self.about)
            self.button_2 = ui.CTkButton(self, text="Güncelle", command=self.update)
            self.button_3 = ui.CTkButton(self, text="Sıfırla", command=self.reset)
            self.button_4 = ui.CTkButton(self, text="Kaldır", command=self.uninstall)
            self.startup = ui.CTkCheckBox(self, text="Başlangıç Bilgileri", command=self.startup_option, variable=self.startup_var, onvalue="on", offvalue="off")
            self.appearance_label = ui.CTkLabel(self, text="Görünüm:", anchor="w")
            self.appearance_menu = ui.CTkOptionMenu(self, values=["Sistem", "Açık", "Koyu"], command=self.change_appearance)
            self.language_label = ui.CTkLabel(self, text="Dil:", anchor="w")
            self.language_menu.set("Türkçe")
            if os.path.isfile(system):
                self.appearance_menu.set("Sistem")
            elif os.path.isfile(light):
                self.appearance_menu.set("Açık")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Koyu")
        self.text.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.button_1.grid(row=1, column=0, padx=10, pady=10)
        self.button_2.grid(row=2, column=0, padx=10, pady=10)
        self.button_3.grid(row=3, column=0, padx=10, pady=10)
        self.button_4.grid(row=4, column=0, padx=10, pady=10)
        self.startup.grid(row=6, column=0, padx=10, pady=10)
        self.appearance_label.grid(row=7, column=0, padx=10, pady=(10, 0))
        self.appearance_menu.grid(row=8, column=0, padx=10, pady=(0, 10))
        self.language_label.grid(row=9, column=0, padx=10, pady=(10, 0))
        self.language_menu.grid(row=10, column=0, padx=10, pady=(0, 10))
        self.about_window = None
    def about(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = AboutWindow(self)
        else:
            self.about_window.focus()
    def update(self):
        pass
    def reset(self):
        pass
    def uninstall(self):
        pass
    def startup_option(self):
        if self.startup_var.get() == "on":
            os.system("cd "+config+"startup/ ; rm * ; touch true.txt")
        elif self.startup_var.get() == "off":
            os.system("cd "+config+"startup/ ; rm * ; touch false.txt")
    def change_appearance(self, new_appearance: str):
        if new_appearance == "System" or new_appearance == "Sistem":
            os.system("cd "+config+"theme ; rm * ; touch system.txt")
            ui.set_appearance_mode("System")
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

class StartPage(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        if os.path.isfile(s_true):
            if os.path.isfile(en):
                self.label0 = ui.CTkLabel(self, text="Welcome "+username+"!", font=ui.CTkFont(size=25, weight="bold"))
                self.label1 = ui.CTkLabel(self, text="Weather Forecast According To wttr.in\nSystem Information Obtained Using Neofetch", font=ui.CTkFont(size=15, weight="normal"))
                weather = subprocess.Popen('curl -H "Accept-Language: en" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(tr):
                self.label0 = ui.CTkLabel(self, text="Merhabalar "+username+"!", font=ui.CTkFont(size=25, weight="bold"))
                self.label1 = ui.CTkLabel(self, text="wttr.in'e Göre Hava Durumu\nNeofetch Kullanılarak Elde Edilen Sistem Bilgileri", font=ui.CTkFont(size=15, weight="normal"))
                weather = subprocess.Popen('curl -H "Accept-Language: tr" wttr.in/?format="%l:+%C+%t+%w+%h+%M"', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.label0.grid(row=0, column=0, pady=(0, 10))
            self.label1.grid(row=1, column=0, pady=(0, 10))
            self.textbox1 = ui.CTkTextbox(self, width=940, height=25, fg_color="transparent")
            self.textbox1.grid(row=2, column=0, sticky="nsew")
            self.textbox2 = ui.CTkTextbox(self, width=940, height=400, fg_color="transparent")
            self.textbox2.grid(row=3, column=0, sticky="nsew")
            neofetch = subprocess.Popen('neofetch --stdout', shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.textbox1.insert("0.0", weather)
            self.textbox1.configure(state="disabled")
            self.textbox2.insert("0.0", neofetch)
            self.textbox2.configure(state="disabled")
        elif os.path.isfile(s_false):
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            if os.path.isfile(en):
                self.label0 = ui.CTkLabel(self, text="Welcome\n"+username, font=ui.CTkFont(size=80, weight="normal"))
            elif os.path.isfile(tr):
                self.label0 = ui.CTkLabel(self, text="Merhabalar\n"+username, font=ui.CTkFont(size=80, weight="normal"))
            self.label0.grid(row=0, column=0, sticky="nsew")


class AppStore(ui.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        app1 = self.add("Mukotes")    
        app2 = self.add("Firefox")
        app3 = self.add("Brave")
        app4 = self.add("VLC")
        app5 = self.add("LibreOffice")
        app6 = self.add("Cups")
        app7 = self.add("GParted")
        app8 = self.add("GIMP")
        app9 = self.add("Wine")
        app10 = self.add("VS Codium")
        app11 = self.add("Heroic")
        app12 = self.add("Steam")
        app13 = self.add("Discord")
        app1.grid_columnconfigure(0, weight=1)
        app1.grid_rowconfigure((0, 1, 2), weight=1)
        app2.grid_columnconfigure(0, weight=1)
        app2.grid_rowconfigure((0, 1, 2), weight=1)
        app3.grid_columnconfigure(0, weight=1)
        app3.grid_rowconfigure((0, 1, 2), weight=1)
        app4.grid_columnconfigure(0, weight=1)
        app4.grid_rowconfigure((0, 1, 2), weight=1)
        app5.grid_columnconfigure(0, weight=1)
        app5.grid_rowconfigure((0, 1, 2), weight=1)
        app6.grid_columnconfigure(0, weight=1)
        app6.grid_rowconfigure((0, 1, 2), weight=1)
        app7.grid_columnconfigure(0, weight=1)
        app7.grid_rowconfigure((0, 1, 2), weight=1)
        app8.grid_columnconfigure(0, weight=1)
        app8.grid_rowconfigure((0, 1, 2), weight=1)
        app9.grid_columnconfigure(0, weight=1)
        app9.grid_rowconfigure((0, 1, 2), weight=1)
        app10.grid_columnconfigure(0, weight=1)
        app10.grid_rowconfigure((0, 1, 2), weight=1)
        app11.grid_columnconfigure(0, weight=1)
        app11.grid_rowconfigure((0, 1, 2), weight=1)
        app12.grid_columnconfigure(0, weight=1)
        app12.grid_rowconfigure((0, 1, 2), weight=1)
        app13.grid_columnconfigure(0, weight=1)
        app13.grid_rowconfigure((0, 1, 2), weight=1)
        self.a1b1 = ui.CTkButton(app1, text=install_text, command=lambda:self.do("1"))
        self.a1b2 = ui.CTkButton(app1, text=reinstall_text, command=lambda:self.do("2"))
        self.a1b3 = ui.CTkButton(app1, text=uninstall_text, command=lambda:self.do("3"))
        self.a2b1 = ui.CTkButton(app2, text=install_text, command=lambda:self.do("4"))
        self.a2b2 = ui.CTkButton(app2, text=reinstall_text, command=lambda:self.do("5"))
        self.a2b3 = ui.CTkButton(app2, text=uninstall_text, command=lambda:self.do("6"))
        self.a3b1 = ui.CTkButton(app3, text=install_text, command=lambda:self.do("7"))
        self.a3b2 = ui.CTkButton(app3, text=reinstall_text, command=lambda:self.do("8"))
        self.a3b3 = ui.CTkButton(app3, text=uninstall_text, command=lambda:self.do("9"))
        self.a4b1 = ui.CTkButton(app4, text=install_text, command=lambda:self.do("10"))
        self.a4b2 = ui.CTkButton(app4, text=reinstall_text, command=lambda:self.do("11"))
        self.a4b3 = ui.CTkButton(app4, text=uninstall_text, command=lambda:self.do("12"))
        self.a5b1 = ui.CTkButton(app5, text=install_text, command=lambda:self.do("13"))
        self.a5b2 = ui.CTkButton(app5, text=reinstall_text, command=lambda:self.do("14"))
        self.a5b3 = ui.CTkButton(app5, text=uninstall_text, command=lambda:self.do("15"))
        self.a6b1 = ui.CTkButton(app6, text=install_text, command=lambda:self.do("16"))
        self.a6b2 = ui.CTkButton(app6, text=reinstall_text, command=lambda:self.do("17"))
        self.a6b3 = ui.CTkButton(app6, text=uninstall_text, command=lambda:self.do("18"))
        self.a7b1 = ui.CTkButton(app7, text=install_text, command=lambda:self.do("19"))
        self.a7b2 = ui.CTkButton(app7, text=reinstall_text, command=lambda:self.do("20"))
        self.a7b3 = ui.CTkButton(app7, text=uninstall_text, command=lambda:self.do("21"))
        self.a8b1 = ui.CTkButton(app8, text=install_text, command=lambda:self.do("22"))
        self.a8b2 = ui.CTkButton(app8, text=reinstall_text, command=lambda:self.do("23"))
        self.a8b3 = ui.CTkButton(app8, text=uninstall_text, command=lambda:self.do("24"))
        self.a9b1 = ui.CTkButton(app9, text=install_text, command=lambda:self.do("25"))
        self.a9b2 = ui.CTkButton(app9, text=reinstall_text, command=lambda:self.do("26"))
        self.a9b3 = ui.CTkButton(app9, text=uninstall_text, command=lambda:self.do("27"))
        self.a10b1 = ui.CTkButton(app10, text=install_text, command=lambda:self.do("28"))
        self.a10b2 = ui.CTkButton(app10, text=reinstall_text, command=lambda:self.do("29"))
        self.a10b3 = ui.CTkButton(app10, text=uninstall_text, command=lambda:self.do("30"))
        self.a11b1 = ui.CTkButton(app11, text=install_text, command=lambda:self.do("31"))
        self.a11b2 = ui.CTkButton(app11, text=reinstall_text, command=lambda:self.do("32"))
        self.a11b3 = ui.CTkButton(app11, text=uninstall_text, command=lambda:self.do("33"))
        self.a12b1 = ui.CTkButton(app12, text=install_text, command=lambda:self.do("34"))
        self.a12b2 = ui.CTkButton(app12, text=reinstall_text, command=lambda:self.do("35"))
        self.a12b3 = ui.CTkButton(app12, text=uninstall_text, command=lambda:self.do("36"))
        self.a13b1 = ui.CTkButton(app13, text=install_text, command=lambda:self.do("37"))
        self.a13b2 = ui.CTkButton(app13, text=reinstall_text, command=lambda:self.do("38"))
        self.a13b3 = ui.CTkButton(app13, text=uninstall_text, command=lambda:self.do("39"))
        self.a1b1.grid(row=0, column=0)
        self.a1b2.grid(row=1, column=0)
        self.a1b3.grid(row=2, column=0)
        self.a2b1.grid(row=0, column=0)
        self.a2b2.grid(row=1, column=0)
        self.a2b3.grid(row=2, column=0)
        self.a3b1.grid(row=0, column=0)
        self.a3b2.grid(row=1, column=0)
        self.a3b3.grid(row=2, column=0)
        self.a4b1.grid(row=0, column=0)
        self.a4b2.grid(row=1, column=0)
        self.a4b3.grid(row=2, column=0)
        self.a5b1.grid(row=0, column=0)
        self.a5b2.grid(row=1, column=0)
        self.a5b3.grid(row=2, column=0)
        self.a6b1.grid(row=0, column=0)
        self.a6b2.grid(row=1, column=0)
        self.a6b3.grid(row=2, column=0)
        self.a7b1.grid(row=0, column=0)
        self.a7b2.grid(row=1, column=0)
        self.a7b3.grid(row=2, column=0)
        self.a8b1.grid(row=0, column=0)
        self.a8b2.grid(row=1, column=0)
        self.a8b3.grid(row=2, column=0)
        self.a9b1.grid(row=0, column=0)
        self.a9b2.grid(row=1, column=0)
        self.a9b3.grid(row=2, column=0)
        self.a10b1.grid(row=0, column=0)
        self.a10b2.grid(row=1, column=0)
        self.a10b3.grid(row=2, column=0)
        self.a11b1.grid(row=0, column=0)
        self.a11b2.grid(row=1, column=0)
        self.a11b3.grid(row=2, column=0)
        self.a12b1.grid(row=0, column=0)
        self.a12b2.grid(row=1, column=0)
        self.a12b3.grid(row=2, column=0)
        self.a13b1.grid(row=0, column=0)
        self.a13b2.grid(row=1, column=0)
        self.a13b3.grid(row=2, column=0)
    def do(self, name: str):
        pass

class OtherStore(ui.CTkFrame):
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
        self.source = ui.CTkLabel(self.frame, text=source_text)
        self.repos = ui.CTkSwitch(self.frame, text=repos_text+"/Flathub", offvalue="repos", onvalue="flathub", variable=self.repos_var, command=self.repos_command)
        self.entry = ui.CTkEntry(self.frame, placeholder_text=enter_pkg_text)
        self.button1 = ui.CTkButton(self.frame, text=search_text, command=self.go_search)
        self.button2 = ui.CTkButton(self.frame, text=install_text, command=self.install)
        self.button3 = ui.CTkButton(self.frame, text=reinstall_text, command=self.reinstall)
        self.button4 = ui.CTkButton(self.frame, text=uninstall_text, command=self.uninstall)
        self.source.grid(row=0, column=0, sticky="nsew", pady=0, padx=(25, 0))
        self.repos.grid(row=1, column=0, sticky="nsew", pady=0, padx=(25, 0))
        self.entry.grid(row=2, column=0, sticky="nsew", pady=(20, 0), padx=(25, 0))
        self.button1.grid(row=3, column=0, sticky="nsew", pady=(20, 5), padx=(25, 0))
        self.button2.grid(row=4, column=0, sticky="nsew", pady=(0, 5), padx=(25, 0))
        self.button3.grid(row=5, column=0, sticky="nsew", pady=(0, 5), padx=(25, 0))
        self.button4.grid(row=6, column=0, sticky="nsew", padx=(25, 0))
    def install_flatpak(self):
        global ask_f
        if os.path.isfile(en):
            ask_f = mb.askyesno("Warning","Flatpak can't found on your system.\nWe can try installing Flatpak to your computer.\nDo you approve it?")
        elif os.path.isfile(tr):
            ask_f = mb.askyesno("Uyarı","Flatpak sisteminizde bulunamadı.\nBiz sisteminize Flatpak yüklemeyi deneyebiliriz.\nOnaylıyor musunuz?")
        if ask_f == True:
            pass
        elif ask_f == False:
            if os.path.isfile(en):
                mb.showinfo("Information","Flatpak installation and process cancelled.")
            elif os.path.isfile(tr):
                mb.showinfo("Bilgilendirme","Flatpak kurulumu ve işlem iptal edildi.")
    def repos_command(self):
        if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak") and self.repos_var.get() == "flathub":
            self.install_flatpak()
    def search_main(self):
        if self.repos_var.get() == "repos":
            if os.path.isfile(debian):
                cmd = subprocess.Popen('apt search '+self.entry.get(), shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(fedora):
                cmd = subprocess.Popen('dnf search '+self.entry.get(), shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            elif os.path.isfile(arch1) or os.path.isfile(arch2):
                cmd = subprocess.Popen('pacman -Ss '+self.entry.get(), shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
            self.textbox.configure(state="normal")
            self.textbox.insert("0.0", cmd)
            self.textbox.configure(state="disabled")
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                self.install_flatpak()
                if ask_f == False:
                    return
            pass
    def go_search(self):
        t = threading.Thread(target=self.search_main, daemon=False)
        t.start()
    def install(self):
        if self.repos_var.get() == "repos":
            pass
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                self.install_flatpak()
                if ask_f == False:
                    return
            pass
    def reinstall(self):
        if self.repos_var.get() == "repos":
            pass
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                self.install_flatpak()
                if ask_f == False:
                    return
            pass
    def uninstall(self):
        if self.repos_var.get() == "repos":
            pass
        elif self.repos_var.get() == "flathub":
            if not os.path.isfile("/usr/bin/flatpak") and not os.path.isfile("/bin/flatpak"):
                self.install_flatpak()
                if ask_f == False:
                    return
            pass

class DEWMStore(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

class Store(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tabview = ui.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=0, sticky="nsew")
        if os.path.isfile(en):
            tab1 = self.tabview.add("General Apps")
            tab2 = self.tabview.add("Other Apps")
            tab3 = self.tabview.add("Desktop Environments\nWindow Managers")
        elif os.path.isfile(tr):
            tab1 = self.tabview.add("Genel Uygulamalar")
            tab2 = self.tabview.add("Diğer Uygulamalar")
            tab3 = self.tabview.add("Masaüstü Ortamları\nPencere Yöneticileri")
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        self.store_frame=AppStore(tab1)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab2.grid_columnconfigure(0, weight=1)
        tab2.grid_rowconfigure(0, weight=1)
        self.store_frame=OtherStore(tab2)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab3.grid_columnconfigure(0, weight=1)
        tab3.grid_rowconfigure(0, weight=1)
        self.store_frame=DEWMStore(tab3)
        self.store_frame.grid(row=0, column=0, sticky="nsew")

class Main(ui.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        if os.path.isfile(en):
            tab0 = self.add("Start Page")
            tab1 = self.add("Store")
            tab2 = self.add("Configuring")
            tab3 = self.add("Other Graphical Tools")
            tab4 = self.add("Other Tools")
        elif os.path.isfile(tr):
            tab0 = self.add("Başlangıç Sayfası")
            tab1 = self.add("Mağaza")
            tab2 = self.add("Yapılandırma")
            tab3 = self.add("Diğer Grafiksel Araçlar")
            tab4 = self.add("Diğer Araçlar")
        tab0.grid_columnconfigure(0, weight=1)
        tab0.grid_rowconfigure(0, weight=1)
        self.home_frame=StartPage(tab0)
        self.home_frame.grid(row=0, column=0, sticky="nsew")       
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        self.store_frame=Store(tab1)
        self.store_frame.grid(row=0, column=0, sticky="nsew")


class Root(ui.CTk):
    def __init__(self):
        super().__init__()
        self.title("GrelinTB")
        self.geometry("1280x640")
        self.resizable(0, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.sidebar_frame = Sidebar(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.tabview = Main(self, corner_radius=50)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")


if __name__ == "__main__":
    root = Root()
    root.mainloop()