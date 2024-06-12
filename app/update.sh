#!/bin/bash

# GrelinTB's updater is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GrelinTB's updater is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GrelinTB's updater.  If not, see <https://www.gnu.org/licenses/>.

echo -e "\n| --------------------------------------- GrelinTB Updater --------------------------------------- |"
echo -e "| ------------------------------------------------------------------------------------------------ |"
echo -e "|                                                                                                  |"
echo -e "| Copyright (C) 2024 MuKonqi (Muhammed S.)                                                         |"
echo -e "|                                                                                                  |"
echo -e "| GrelinTB and it's updater are free software: you can redistribute it and/or modify               |"
echo -e "| it under the terms of the GNU General Public License as published by                             |"
echo -e "| the Free Software Foundation, either version 3 of the License, or                                |"
echo -e "| (at your option) any later version.                                                              |"
echo -e "|                                                                                                  |"
echo -e "| GrelinTB and it's updater are distributed in the hope that they will be useful,                  |"
echo -e "| but WITHOUT ANY WARRANTY; without even the implied warranty of                                   |"
echo -e "| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                    |"
echo -e "| GNU General Public License for more details.                                                     |"
echo -e "|                                                                                                  |"
echo -e "| You should have received a copy of the GNU General Public License                                |"
echo -e "| along with GrelinTB and it's updater.  If not, see <https://www.gnu.org/licenses/>.              |"
echo -e "|                                                                                                  |"
echo -e "| ------------------------------------------------------------------------------------------------ |\n"
if (( $EUID != 0 )); then
    echo -e "Error: Please run as root. (1)"
    exit 1
fi
function update {
    if ! [ -d /usr/local/ ]; then
        mkdir /usr/local/
    fi
    if ! [ -d /usr/local/bin/ ]; then
        mkdir /usr/local/bin/
    fi
    rm /usr/bin/grelintb
    rm /usr/share/applications/grelintb.desktop
    rm -rf /usr/local/bin/grelintb/
    mkdir /usr/local/bin/grelintb
    cd /tmp
    git clone https://github.com/mukonqi/grelintb.git
    chmod +x grelintb/app/*
    cp grelintb/app/grelintb.py /usr/bin/grelintb
    cp grelintb/app/grelintb.desktop /usr/share/applications/
    cp grelintb/app/* /usr/local/bin/grelintb/
    rm -rf grelintb
    exit 0
}
if [ -f /etc/debian_version ]; then
    apt -y install python3 python3-tk python3-pip git curl xdg-utils
    update
elif [ -f /etc/fedora-release ]; then
    cd /tmp
    wget https://github.com/mukonqi/grelintb/releases/latest/download/grelintb.rpm
    dnf5 -y --nogpgcheck update grelintb.rpm
    dnf5 -y --nogpgcheck reinstall grelintb.rpm
    rm grelintb.rpm
    exit 0
elif [ -f /etc/solus-release ]; then
    eopkg -y install python3 python3-tkinter pip git curl xdg-utils
    update
elif [ -f /etc/arch-release ]; then
    pacman  --noconfirm -S python tk python-pip git curl xdg-utils
    update
else
    echo -e 'Error: The distribution you are using is not supported from GrelinTB. (2)'
    exit 2
fi