#!/bin/bash

# GrelinTB's installer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GrelinTB's installer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GrelinTB's installer.  If not, see <https://www.gnu.org/licenses/>.

if (( $EUID != 0 )); then
    echo -e "Please run as root. Exiting with status 1..."
    exit 1
fi
printf "Welcome to GrelinTB installer!\nGrelinTB and it's installer licensed under GPLv3. Do you agree them? [y/n]: "
read choice
if ! [ $choice = y ] ; then
    echo -e "You didn't agree license or you entered something invalid. Exiting with status 1..."
    exit 1
fi
echo -e "\nCopyright (C) 2024 MuKonqi (Muhammed S.)"
echo -e "\nGrelinTB and it's installer are free software: you can redistribute it and/or modify"
echo -e "it under the terms of the GNU General Public License as published by"
echo -e "the Free Software Foundation, either version 3 of the License, or"
echo -e "(at your option) any later version."
echo -e "\nGrelinTB and it's installer are distributed in the hope that they will be useful,"
echo -e "but WITHOUT ANY WARRANTY; without even the implied warranty of"
echo -e "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
echo -e "GNU General Public License for more details."
echo -e "\nYou should have received a copy of the GNU General Public License"
echo -e "along with GrelinTB and it's installer.  If not, see <https://www.gnu.org/licenses/>."
function install {
    if ! [ -d /usr/local/ ]; then
        mkdir /usr/local/
    fi
    if ! [ -d /usr/local/bin/ ]; then
        mkdir /usr/local/bin/
    fi
    mkdir /usr/local/bin/grelintb
    git clone https://github.com/mukonqi/grelintb.git
    chmod +x grelintb/app/*
    cp grelintb/app/grelintb.py /usr/bin/grelintb
    cp grelintb/app/grelintb.desktop /usr/share/applications/
    cp grelintb/app/* /usr/local/bin/grelintb/
    rm -rf grelintb
    echo -e "Installation completed. Exiting with status 0..."
    exit 0
}
if [ -f /etc/debian_version ]; then
    apt install python3 python3-tk python3-pip git curl lolcat neofetch xdg-utils -y
    install
elif [ -f /etc/fedora-release ]; then
    dnf install python3 python3-tkinter python3-pip git curl lolcat neofetch xdg-utils -y
    install
elif [ -f /etc/solus-release ]; then
    eopkg install python3 python3-tkinter pip git curl lolcat neofetch xdg-utils -y
    install
elif [ -f /usr/bin/pacman] || [ -f /bin/pacman]; then
    pacman -S python tk python-pip git curl neofetch lolcat xdg-utils --noconfirm
    install
else
    echo 'The distribution you are using is not supported from GrelinTB. Exiting with status 1...'
    exit 1
fi