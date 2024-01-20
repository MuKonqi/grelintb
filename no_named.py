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
r_true = "/home/"+username+"/.config/no_named/restart/true.txt"
r_false = "/home/"+username+"/.config/no_named/restart/false.txt"

if not os.path.isdir(config):
    os.system("cd /home/"+username+"/.config ; mkdir no_named ; cd no_named ; mkdir language ; mkdir theme ; mkdir restart ; cd language ; touch en.txt ; cd .. ; cd theme; touch system.txt ; cd .. ; cd restart ; touch false.txt")
    os.system("cd "+config+" ; cd language ; touch en.txt ; cd .. ; cd theme; touch system.txt ; cd .. ; cd restart ; touch false.txt")
if not os.path.isdir(config+"language/"):
    os.system("cd "+config+" ; mkdir language ; cd language ; touch en.txt")
if not os.path.isdir(config+"theme/"):
    os.system("cd "+config+" ; mkdir theme ; cd theme ; touch system.txt")
if not os.path.isdir(config+"restart/"):
    os.system("cd "+config+" ; mkdir restart ; cd restart ; touch false.txt")

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
        self.grid_rowconfigure(5, weight=1)
        self.text = ui.CTkLabel(self, text="no_named_special", font=ui.CTkFont(size=20, weight="bold"))
        self.language_menu = ui.CTkOptionMenu(self, values=["English", "Türkçe"], command=self.change_language)
        if os.path.isfile(r_true):
            self.restart_var = ui.StringVar(value="on")
        elif os.path.isfile(r_false):
            self.restart_var = ui.StringVar(value="off")
        if os.path.isfile(en):
            self.button_1 = ui.CTkButton(self, text="About", command=self.about)
            self.button_2 = ui.CTkButton(self, text="Update", command=self.update)
            self.button_3 = ui.CTkButton(self, text="Reset", command=self.reset)
            self.button_4 = ui.CTkButton(self, text="Uninstall :(", command=self.uninstall)
            self.restart = ui.CTkCheckBox(self, text="Instant Restart For\nSome Operations", command=self.restart_option, variable=self.restart_var, onvalue="on", offvalue="off")
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
            self.button_4 = ui.CTkButton(self, text="Kaldır :(", command=self.uninstall)
            self.restart = ui.CTkCheckBox(self, text="Bazı İşlemler İçin\nAnında Yeniden Başlatma", command=self.restart_option, variable=self.restart_var, onvalue="on", offvalue="off")
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
        self.button_1.grid(row=1, column=0, padx=20, pady=10)
        self.button_2.grid(row=2, column=0, padx=20, pady=10)
        self.button_3.grid(row=3, column=0, padx=20, pady=10)
        self.button_4.grid(row=4, column=0, padx=20, pady=10)
        self.restart.grid(row=6, column=0)
        self.appearance_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_menu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.language_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.language_menu.grid(row=10, column=0, padx=20, pady=(10, 10))
    def about(self):
        pass
    def update(self):
        pass
    def reset(self):
        pass
    def uninstall(self):
        pass
    def restart_option(self):
        if self.restart_var.get() == "on":
            os.system("cd "+config+"restart/ ; rm * ; touch true.txt")
        elif self.restart_var.get() == "off":
            os.system("cd "+config+"restart/ ; rm * ; touch false.txt")
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

class AppStore(ui.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        app1 = self.add("Firefox")
        app2 = self.add("Brave")
        app3 = self.add("VLC")
        app4 = self.add("Steam")
        app5 = self.add("Discord")
        app6 = self.add("VS Code")
        app7 = self.add("LibreOffice")
        app8 = self.add("Cups")
        app9 = self.add("GParted")
        app10 = self.add("GIMP")
        app11 = self.add("Wine")
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
        if os.path.isfile(en):
            self.a1b1 = ui.CTkButton(app1, text="Install", command=self.a1c1)
            self.a1b2 = ui.CTkButton(app1, text="Reinstall", command=self.a1c2)
            self.a1b3 = ui.CTkButton(app1, text="Uninstall", command=self.a1c3)
            self.a2b1 = ui.CTkButton(app2, text="Install", command=self.a2c1)
            self.a2b2 = ui.CTkButton(app2, text="Reinstall", command=self.a2c2)
            self.a2b3 = ui.CTkButton(app2, text="Uninstall", command=self.a2c3)
            self.a3b1 = ui.CTkButton(app3, text="Install", command=self.a3c1)
            self.a3b2 = ui.CTkButton(app3, text="Reinstall", command=self.a3c2)
            self.a3b3 = ui.CTkButton(app3, text="Uninstall", command=self.a3c3)
            self.a4b1 = ui.CTkButton(app4, text="Install", command=self.a4c1)
            self.a4b2 = ui.CTkButton(app4, text="Reinstall", command=self.a4c2)
            self.a4b3 = ui.CTkButton(app4, text="Uninstall", command=self.a4c3)
            self.a5b1 = ui.CTkButton(app5, text="Install", command=self.a5c1)
            self.a5b2 = ui.CTkButton(app5, text="Reinstall", command=self.a5c2)
            self.a5b3 = ui.CTkButton(app5, text="Uninstall", command=self.a5c3)
            self.a6b1 = ui.CTkButton(app6, text="Install", command=self.a6c1)
            self.a6b2 = ui.CTkButton(app6, text="Reinstall", command=self.a6c2)
            self.a6b3 = ui.CTkButton(app6, text="Uninstall", command=self.a6c3)
            self.a7b1 = ui.CTkButton(app7, text="Install", command=self.a7c1)
            self.a7b2 = ui.CTkButton(app7, text="Reinstall", command=self.a7c2)
            self.a7b3 = ui.CTkButton(app7, text="Uninstall", command=self.a7c3)
            self.a8b1 = ui.CTkButton(app8, text="Install", command=self.a8c1)
            self.a8b2 = ui.CTkButton(app8, text="Reinstall", command=self.a8c2)
            self.a8b3 = ui.CTkButton(app8, text="Uninstall", command=self.a8c3)
            self.a9b1 = ui.CTkButton(app9, text="Install", command=self.a9c1)
            self.a9b2 = ui.CTkButton(app9, text="Reinstall", command=self.a9c2)
            self.a9b3 = ui.CTkButton(app9, text="Uninstall", command=self.a9c3)
            self.a10b1 = ui.CTkButton(app10, text="Install", command=self.a10c1)
            self.a10b2 = ui.CTkButton(app10, text="Reinstall", command=self.a10c2)
            self.a10b3 = ui.CTkButton(app10, text="Uninstall", command=self.a10c3)
            self.a11b1 = ui.CTkButton(app11, text="Install", command=self.a11c1)
            self.a11b2 = ui.CTkButton(app11, text="Reinstall", command=self.a11c2)
            self.a11b3 = ui.CTkButton(app11, text="Uninstall", command=self.a11c3)
        elif os.path.isfile(tr):
            self.a1b1 = ui.CTkButton(app1, text="Kur", command=self.a1c1)
            self.a1b2 = ui.CTkButton(app1, text="Yeniden Kur", command=self.a1c2)
            self.a1b3 = ui.CTkButton(app1, text="kaldır", command=self.a1c3)
            self.a2b1 = ui.CTkButton(app2, text="Kur", command=self.a2c1)
            self.a2b2 = ui.CTkButton(app2, text="Yeniden Kur", command=self.a2c2)
            self.a2b3 = ui.CTkButton(app2, text="kaldır", command=self.a2c3)
            self.a3b1 = ui.CTkButton(app3, text="Kur", command=self.a3c1)
            self.a3b2 = ui.CTkButton(app3, text="Yeniden Kur", command=self.a3c2)
            self.a3b3 = ui.CTkButton(app3, text="kaldır", command=self.a3c3)
            self.a4b1 = ui.CTkButton(app4, text="Kur", command=self.a4c1)
            self.a4b2 = ui.CTkButton(app4, text="Yeniden Kur", command=self.a4c2)
            self.a4b3 = ui.CTkButton(app4, text="kaldır", command=self.a4c3)
            self.a5b1 = ui.CTkButton(app5, text="Kur", command=self.a5c1)
            self.a5b2 = ui.CTkButton(app5, text="Yeniden Kur", command=self.a5c2)
            self.a5b3 = ui.CTkButton(app5, text="kaldır", command=self.a5c3)
            self.a6b1 = ui.CTkButton(app6, text="Kur", command=self.a6c1)
            self.a6b2 = ui.CTkButton(app6, text="Yeniden Kur", command=self.a6c2)
            self.a6b3 = ui.CTkButton(app6, text="kaldır", command=self.a6c3)
            self.a7b1 = ui.CTkButton(app7, text="Kur", command=self.a7c1)
            self.a7b2 = ui.CTkButton(app7, text="Yeniden Kur", command=self.a7c2)
            self.a7b3 = ui.CTkButton(app7, text="kaldır", command=self.a7c3)
            self.a8b1 = ui.CTkButton(app8, text="Kur", command=self.a8c1)
            self.a8b2 = ui.CTkButton(app8, text="Yeniden Kur", command=self.a8c2)
            self.a8b3 = ui.CTkButton(app8, text="kaldır", command=self.a8c3)
            self.a9b1 = ui.CTkButton(app9, text="Kur", command=self.a9c1)
            self.a9b2 = ui.CTkButton(app9, text="Yeniden Kur", command=self.a9c2)
            self.a9b3 = ui.CTkButton(app9, text="kaldır", command=self.a9c3)
            self.a10b1 = ui.CTkButton(app10, text="Kur", command=self.a10c1)
            self.a10b2 = ui.CTkButton(app10, text="Yeniden Kur", command=self.a10c2)
            self.a10b3 = ui.CTkButton(app10, text="kaldır", command=self.a10c3)
            self.a11b1 = ui.CTkButton(app11, text="Kur", command=self.a11c1)
            self.a11b2 = ui.CTkButton(app11, text="Yeniden Kur", command=self.a11c2)
            self.a11b3 = ui.CTkButton(app11, text="kaldır", command=self.a11c3)
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
    def a1c1(self):
        pass
    def a1c2(self):
        pass
    def a1c3(self):
        pass
    def a2c1(self):
        pass
    def a2c2(self):
        pass
    def a2c3(self):
        pass
    def a3c1(self):
        pass
    def a3c2(self):
        pass
    def a3c3(self):
        pass
    def a4c1(self):
        pass
    def a4c2(self):
        pass
    def a4c3(self):
        pass
    def a5c1(self):
        pass
    def a5c2(self):
        pass
    def a5c3(self):
        pass
    def a6c1(self):
        pass
    def a6c2(self):
        pass
    def a6c3(self):
        pass
    def a7c1(self):
        pass
    def a7c2(self):
        pass
    def a7c3(self):
        pass
    def a8c1(self):
        pass
    def a8c2(self):
        pass
    def a8c3(self):
        pass
    def a9c1(self):
        pass
    def a9c2(self):
        pass
    def a9c3(self):
        pass
    def a10c1(self):
        pass
    def a10c2(self):
        pass
    def a10c3(self):
        pass
    def a11c1(self):
        pass
    def a11c2(self):
        pass
    def a11c3(self):
        pass


class DEWMStore(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
class PkgMgrStore(ui.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
class OtherStore(ui.CTkFrame):
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
            tab1 = self.tabview.add("App")
            tab2 = self.tabview.add("Desktop Environment\nWindow Manager")
            tab3 = self.tabview.add("Package Manager")
            tab4 = self.tabview.add("Other")
        elif os.path.isfile(tr):
            tab1 = self.tabview.add("Uygulama")
            tab2 = self.tabview.add("Masaüstü Ortamı\nPencere Yöneticisi")
            tab3 = self.tabview.add("Paket Yöneticisi")
            tab4 = self.tabview.add("Diğer")
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        self.store_frame=AppStore(tab1)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab2.grid_columnconfigure(0, weight=1)
        tab2.grid_rowconfigure(0, weight=1)
        self.store_frame=DEWMStore(tab2)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab3.grid_columnconfigure(0, weight=1)
        tab3.grid_rowconfigure(0, weight=1)
        self.store_frame=PkgMgrStore(tab3)
        self.store_frame.grid(row=0, column=0, sticky="nsew")
        tab4.grid_columnconfigure(0, weight=1)
        tab4.grid_rowconfigure(0, weight=1)
        self.store_frame=OtherStore(tab4)
        self.store_frame.grid(row=0, column=0, sticky="nsew")

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
        tab1.grid_columnconfigure(0, weight=1)
        tab1.grid_rowconfigure(0, weight=1)
        self.store_frame=Store(tab1)
        self.store_frame.grid(row=0, column=0, sticky="nsew")


class Root(ui.CTk):
    def __init__(self):
        super().__init__()
        self.title("no_named_special")
        self.geometry("1280x640")
        self.resizable(0, 0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.sidebar_frame = no_named_specialFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.tabview = Main(self, corner_radius=50)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

root = Root()
root.mainloop()