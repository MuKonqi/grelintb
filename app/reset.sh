#!/bin/bash

# GrelinTB's resetter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GrelinTB's resetter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GrelinTB's resetter.  If not, see <https://www.gnu.org/licenses/>.

echo -e "\n| -------------------------------------- GrelinTB Resetter -------------------------------------- |"
echo -e "| ----------------------------------------------------------------------------------------------- |"
echo -e "|                                                                                                 |"
echo -e "| Copyright (C) 2024 MuKonqi (Muhammed S.)                                                        |"
echo -e "|                                                                                                 |"
echo -e "| GrelinTB and it's resetter are free software: you can redistribute it and/or modify             |"
echo -e "| it under the terms of the GNU General Public License as published by                            |"
echo -e "| the Free Software Foundation, either version 3 of the License, or                               |"
echo -e "| (at your option) any later version.                                                             |"
echo -e "|                                                                                                 |"
echo -e "| GrelinTB and it's resetter are distributed in the hope that they will be useful,                |"
echo -e "| but WITHOUT ANY WARRANTY; without even the implied warranty of                                  |"
echo -e "| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                   |"
echo -e "| GNU General Public License for more details.                                                    |"
echo -e "|                                                                                                 |"
echo -e "| You should have received a copy of the GNU General Public License                               |"
echo -e "| along with GrelinTB and it's resetter.  If not, see <https://www.gnu.org/licenses/>.            |"
echo -e "|                                                                                                 |"
echo -e "| ----------------------------------------------------------------------------------------------- |\n"
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
        function install_git {
        if [ -f /etc/debian_version ]; then
            pkexec apt -y install git
        elif [ -f /etc/solus-release ]; then
            pkexec eopkg install git
        elif [ -f /etc/arch-release ]; then
            pkexec pacman --noconfirm -S git
        fi
    }
    if [[ ! -f /bin/git ]] && [[ ! -f /usr/bin/git ]]; then
        install_git
    fi
    function install_pip {
        if [ -f /etc/debian_version ]; then
            pkexec apt -y install pip
        elif [ -f /etc/solus-release ]; then
            pkexec eopkg install pip
        elif [ -f /etc/arch-release ]; then
            pkexec pacman --noconfirm -S pip
        fi
    }
    if [[ ! -f /bin/pip ]] && [[ ! -f /usr/bin/pip ]]; then
        install_pip
    fi
    function install_python3 {
        if [ -f /etc/debian_version ]; then
            pkexec apt -y install python3
        elif [ -f /etc/solus-release ]; then
            pkexec eopkg install python3
        elif [ -f /etc/arch-release ]; then
            pkexec pacman  --noconfirm -S python3
        fi
    }
    if [[ ! -f /bin/python3 ]] && [[ ! -f /usr/bin/python3 ]]; then
        install_python3
    fi
    mkdir /usr/local/bin/grelintb
    cd /tmp
    git clone https://github.com/mukonqi/grelintb.git
    chmod +x grelintb/app/*
    cp grelintb/app/grelintb.py /usr/bin/grelintb
    cp grelintb/app/grelintb.desktop /usr/share/applications/
    cp grelintb/app/* /usr/local/bin/grelintb/
    rm -rf grelintb
    echo -e "GrelinTB updated."
    exit 0
}
if [ -f /etc/debian_version ]; then
    apt -y install python3 python3-tk python3-pip git curl xdg-utils
    update
elif [ -f /etc/fedora-release ]; then
    cd /tmp
    wget https://github.com/mukonqi/grelintb/releases/latest/download/grelintb.rpm
    dnf -y --nogpgcheck update grelintb.rpm
    dnf -y --nogpgcheck reinstall grelintb.rpm
    rm grelintb.rpm
    echo -e "GrelinTB updated."
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