#!/bin/bash

# GrelinTB's uninstaller is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GrelinTB's uninstaller is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GrelinTB's uninstaller.  If not, see <https://www.gnu.org/licenses/>.

echo -e "\n| ------------------------------------- GrelinTB Uninstaller ------------------------------------- |"
echo -e "| ------------------------------------------------------------------------------------------------ |"
echo -e "|                                                                                                  |"
echo -e "| Copyright (C) 2024 MuKonqi (Muhammed S.)                                                         |"
echo -e "|                                                                                                  |"
echo -e "| GrelinTB and it's uninstaller are free software: you can redistribute it and/or modify           |"
echo -e "| it under the terms of the GNU General Public License as published by                             |"
echo -e "| the Free Software Foundation, either version 3 of the License, or                                |"
echo -e "| (at your option) any later version.                                                              |"
echo -e "|                                                                                                  |"
echo -e "| GrelinTB and it's uninstaller are distributed in the hope that they will be useful,              |"
echo -e "| but WITHOUT ANY WARRANTY; without even the implied warranty of                                   |"
echo -e "| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                    |"
echo -e "| GNU General Public License for more details.                                                     |"
echo -e "|                                                                                                  |"
echo -e "| You should have received a copy of the GNU General Public License                                |"
echo -e "| along with GrelinTB and it's uninstaller.  If not, see <https://www.gnu.org/licenses/>.          |"
echo -e "|                                                                                                  |"
echo -e "| ------------------------------------------------------------------------------------------------ |\n"
if (( $EUID != 0 )); then
    echo -e "Error: Please run as root. (1)"
    exit 1
fi
function uninstall {
    rm /usr/bin/grelintb
    rm /usr/share/applications/grelintb.desktop
    rm -rf /usr/local/bin/grelintb/
    echo -e "GrelinTB uninstalled."
    exit 0
}
if  [ -f /etc/debian_version ]; then
    uninstall
elif [ -f /etc/fedora-release ]; then
    dnf5 -y --nogpgcheck remove grelintb
    if [ -f /usr/bin/grelintb/ ] ; then
        rm /usr/bin/grelintb
    fi
    if [ -f /usr/share/applications/grelintb.desktop ] ; then
        rm /usr/share/applications/grelintb.desktop
    fi
    if [ -d /usr/local/bin/grelintb/ ] ; then
        rm -rf /usr/local/bin/grelintb/
    fi
    echo -e "GrelinTB uninstalled."
elif  [ -f /etc/solus-release ]; then
    uninstall
elif  [ -f /etc/arch-release ]; then
    uninstall
fi