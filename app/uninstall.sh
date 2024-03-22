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

if (( $EUID != 0 )); then
    echo -e "Please run as root. Exiting with status 1..."
    exit 1
fi
echo -e "GrelinTB and it's uninstaller licensed under GPLv3."
echo -e "\nCopyright (C) 2024 MuKonqi (Muhammed S.)"
echo -e "\nGrelinTB and it's uninstaller are free software: you can redistribute it and/or modify"
echo -e "it under the terms of the GNU General Public License as published by"
echo -e "the Free Software Foundation, either version 3 of the License, or"
echo -e "(at your option) any later version."
echo -e "\nGrelinTB and it's uninstaller are distributed in the hope that they will be useful,"
echo -e "but WITHOUT ANY WARRANTY; without even the implied warranty of"
echo -e "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the"
echo -e "GNU General Public License for more details."
echo -e "\nYou should have received a copy of the GNU General Public License"
echo -e "along with GrelinTB and it's uninstaller.  If not, see <https://www.gnu.org/licenses/>."
if [ -f /etc/fedora-release ]; then
    dnf remove grelintb -y
elif  [ -f /etc/debian_version || -f /etc/solus-release || -f /etc/arch-release]; then
    rm /usr/bin/grelintb
    rm /usr/share/applications/grelintb.desktop
    rm -rf /usr/local/bin/grelintb/
fi
echo -e "GrelinTB was uninstalled from your system. Exiting with status 0..."
exit 0