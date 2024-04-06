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

if (( $EUID != 0 )); then
    echo -e "Please run as root. Exiting with status 1..."
    exit 1
fi
echo -e "GrelinTB and it's updater licensed under GPLv3."
echo -e "\nCopyright (C) 2024 MuKonqi (Muhammed S.)"
echo -e "\nGrelinTB and it's updater are free software: you can redistribute it and/or modify"
echo -e "it under the terms of the GNU General Public License as published by"
echo -e "the Free Software Foundation, either version 3 of the License, or"
echo -e "(at your option) any later version."
echo -e "\nGrelinTB and it's updater are distributed in the hope that they will be useful,"
echo -e "but WITHOUT ANY WARRANTY; without even the implied warranty of"
echo -e "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
echo -e "GNU General Public License for more details."
echo -e "\nYou should have received a copy of the GNU General Public License"
echo -e "along with GrelinTB and it's updater.  If not, see <https://www.gnu.org/licenses/>."
if [ -f /etc/fedora-release ]; then
    wget https://github.com/mukonqi/grelintb/releases/latest/download/grelintb.rpm
    dnf update grelintb.rpm -y
    rm grelintb.rpm
elif  [[ -f /etc/debian_version || -f /etc/solus-release || -f /etc/arch-release]]; then
    function install_git {
        if [ -f /etc/debian_version ]; then
            apt install git -y
        elif [ -f /etc/solus-release ]; then
            eopkg install git -y
        elif [ -f /etc/arch-release ]; then
            pacman -S git --noconfirm
        fi
    }
    if [[ ! -f /bin/git ]] && [[ ! -f /usr/bin/git ]]; then
        install_git
    fi
    function install_pip {
        if [ -f /etc/debian_version ]; then
            apt install pip -y
        elif [ -f /etc/solus-release ]; then
            eopkg install pip -y
        elif [ -f /etc/arch-release ]; then
            pacman -S pip --noconfirm
        fi
    }
    if [[ ! -f /bin/pip ]] && [[ ! -f /usr/bin/pip ]]; then
        install_pip
    fi
    function install_python3 {
        if [ -f /etc/debian_version ]; then
            apt install python3 -y
        elif [ -f /etc/solus-release ]; then
            eopkg install python3 -y
        elif [ -f /etc/arch-release ]; then
            pacman -S python3 --noconfirm
        fi
    }
    if [[ ! -f /bin/python3 ]] && [[ ! -f /usr/bin/python3 ]]; then
        install_python3
    fi
    rm /usr/bin/grelintb
    rm /usr/share/applications/grelintb.desktop
    rm -rf /usr/local/bin/grelintb/
    mkdir /usr/local/bin/grelintb
    git clone https://github.com/mukonqi/grelintb.git
    chmod +x grelintb/app/*
    cp grelintb/app/grelintb.py /usr/bin/grelintb
    cp grelintb/app/grelintb.desktop /usr/share/applications/
    cp grelintb/app/* /usr/local/bin/grelintb/
    rm -rf grelintb
fi
echo -e "GrelinTB updated. Exiting with status 0..."
exit 0