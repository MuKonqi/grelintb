#!/usr/bin/env python3

# Copyright (C) 2021-2024 MuKonqi (Muhammed S. / Muhammed Abdurrahman)

# no_named_special is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# no_named_special is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with no_named_special.  If not, see <https://www.gnu.org/licenses/>.

# no_named_special: New name's true writing (etc. MetterXP)
# no_named: New name's writing in lowercase (etc. metterxp)
# nn: New name's short writing in lowercase (etc. mxp)

import customtkinter as ui
from tkinter import messagebox as mb
import subprocess
import os
import sys
import getpass

username = getpass.getuser()

config = "/home/"+username+"/.config/no_named/"
en = "/home/"+username+"/.config/no_named/language/en.txt"
tr = "/home/"+username+"/.config/no_named/language/tr.txt"
system = "/home/"+username+"/.config/no_named/theme/system.txt"
light = "/home/"+username+"/.config/no_named/theme/light.txt"
dark = "/home/"+username+"/.config/no_named/theme/dark.txt"

def set_defaults():
    os.system("cd "+config+" ; cd language ; touch en.txt ; cd .. ; cd theme; touch system.txt")
if not os.path.isdir(config):
    os.system("cd /home/"+username+"/.config ; mkdir no_named ; cd no_named ; mkdir language ; mkdir theme")
    set_defaults()
if not os.path.isdir(config+"theme/"):
    os.system("cd "+config+" ; mkdir theme")
    set_defaults()
if not os.path.isdir(config+"language/"):
    os.system("cd "+config+" ; mkdir language")
    set_defaults()

debian = "/etc/debian_version"
fedora = "/etc/fedora-release"
solus = "/etc/solus-release"
arch1 = "/bin/pacman"
arch2 = "/usr/bin/pacman"

args = sys.argv[1:]

if os.path.isfile(system):
    ui.set_appearance_mode("System")
elif os.path.isfile(light):
    ui.set_appearance_mode("Light")
elif os.path.isfile(dark):
    ui.set_appearance_mode("Dark")

ui.set_default_color_theme("dark-blue") 

class no_named_specialFrame(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(6, weight=1)
        self.text = ui.CTkLabel(self, text="no_named_special", font=ui.CTkFont(size=20, weight="bold"))
        self.text.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.button_1 = ui.CTkButton(self)
        self.button_1.grid(row=1, column=0, padx=20, pady=10)
        self.button_2 = ui.CTkButton(self)
        self.button_2.grid(row=2, column=0, padx=20, pady=10)
        self.button_3 = ui.CTkButton(self)
        self.button_3.grid(row=3, column=0, padx=20, pady=10)
        self.button_4 = ui.CTkButton(self)
        self.button_4.grid(row=4, column=0, padx=20, pady=10)
        self.button_5 = ui.CTkButton(self)
        self.button_5.grid(row=5, column=0, padx=20, pady=10)
        if os.path.isfile(en):
            self.appearance_label = ui.CTkLabel(self, text="Appearance:", anchor="w")
        elif os.path.isfile(tr):
            self.appearance_label = ui.CTkLabel(self, text="Görünüm:", anchor="w")
        self.appearance_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        if os.path.isfile(en):
            self.appearance_menu = ui.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance)
        elif os.path.isfile(tr):
            self.appearance_menu = ui.CTkOptionMenu(self, values=["Sistem", "Açık", "Koyu"], command=self.change_appearance)
        self.appearance_menu.grid(row=8, column=0, padx=20, pady=(10, 10))
        if os.path.isfile(en):
            self.language_label = ui.CTkLabel(self, text="Language:", anchor="w")
        elif os.path.isfile(tr):
            self.language_label = ui.CTkLabel(self, text="Dil:", anchor="w")
        self.language_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.language_menu = ui.CTkOptionMenu(self, values=["English", "Türkçe"], command=self.change_language)
        self.language_menu.grid(row=10, column=0, padx=20, pady=(10, 10))
        if os.path.isfile(en):
            self.language_menu.set("English")
            if os.path.isfile(system):
                self.appearance_menu.set("System")
            elif os.path.isfile(light):
                self.appearance_menu.set("Light")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Dark")
        elif os.path.isfile(tr):
            self.language_menu.set("Türkçe")
            if os.path.isfile(system):
                self.appearance_menu.set("Sistem")
            elif os.path.isfile(light):
                self.appearance_menu.set("Açık")
            elif os.path.isfile(dark):
                self.appearance_menu.set("Koyu")
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
            mb.showinfo("Information","Language changing has been applied. Please restart the application.")
        elif new_language == "Türkçe":
            os.system("cd "+config+"language ; rm * ; touch tr.txt")
            mb.showinfo("Bilgilendirme","Dil değişikliği uygulandı. Lütfen uygulamayı yeniden başlatın.")

class Main(ui.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        if os.path.isfile(en):
            tab1 = self.add("Store")
            tab2 = self.add("Configuring")
            tab3 = self.add("Other Graphical Tools")
            tab4 = self.add("Other Tools")
        elif os.path.isfile(tr):
            tab1 = self.add("Mağaza")
            tab2 = self.add("Yapılandırma")
            tab3 = self.add("Diğer Grafiksel Araçlar")
            tab4 = self.add("Diğer Araçlar")

class Root(ui.CTk):
    def __init__(self):
        super().__init__()
        self.title("no_named_special")
        self.geometry("1280x720")
        self.resizable(0, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.sidebar_frame = no_named_specialFrame(self)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.tabview = Main(self, corner_radius=50)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

root = Root()
root.mainloop()