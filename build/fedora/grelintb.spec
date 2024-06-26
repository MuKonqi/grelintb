Name:           grelintb
Version:        1.5.0
Release:        21
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-1.tar.gz

Requires:       dnf5 python3 python3-tkinter python3-pip git curl coreutils xdg-utils

%description
GrelinTB comes with various tools. Here are examples: Useful informations about the system etc., a note and document editor and manager, a store for packages and DEs and WMs and Compotisors, various scripts for package managers, a simple configuration tool for Bashrc and Zshrc, a tool to change the name of the computer, information about some distributions and a simple calcer.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp grelintb.py $RPM_BUILD_ROOT/usr/bin/grelintb
chmod +x $RPM_BUILD_ROOT/usr/bin/grelintb
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
cp grelintb.desktop $RPM_BUILD_ROOT/usr/share/applications/grelintb.desktop
chmod +x $RPM_BUILD_ROOT/usr/share/applications/grelintb.desktop
mkdir -p $RPM_BUILD_ROOT/usr/local/bin/grelintb
cp * $RPM_BUILD_ROOT/usr/local/bin/grelintb

%files
/usr/bin/grelintb
/usr/share/applications/grelintb.desktop
/usr/local/bin/grelintb/grelintb.desktop
/usr/local/bin/grelintb/grelintb.py
/usr/local/bin/grelintb/icon.png
/usr/local/bin/grelintb/language.json
%license /usr/local/bin/grelintb/LICENSE.txt
/usr/local/bin/grelintb/major-changelog.txt
/usr/local/bin/grelintb/minor-changelog.txt
/usr/local/bin/grelintb/requirements.txt
/usr/local/bin/grelintb/theme.json
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/version.txt

%changelog
* Thu Jun 13 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
--- General
- The language system has completely changed: Now the language texts are pulled from a json file. This made the code cleaner.
- Optimization has been done: All features now run as a separate thread. Also, the number of lines of code has been reduced from 2595 to 1970, although the interface has been greatly refreshed and beautified because of using dynamic variables, loops etc.
- Unnecessary message boxes etc. have been removed.
- Fixed various bugs (e.g. incorrect detection for Arch Linux base).
- Removed reset.sh file.
- Removed the primary changelog.
--- Sidebar
- The change logs windows have been overhauled.
- Changed “Ready” to “Idle” in the status text.
- Changed “List of All Operations” to “Running Processes” and changed the text style about the running process.
--- Startup
- Added number of packs.
- Minor improvements to the text.
--- Notes and Documents
- Remaded.
- Now 8 notes or documents can be opened and edited at the same time. The reason for not 8 is that if there are no other files with that name, the first 4 letters are the name of that tab. More than 8 creates a bad image when all slots are used.
- Backup system for notes has been added. A backup is now created for every change.
- New interface style: In this style, selections are listed in a big way on the right, while operations are on the left.
--- Store
- All sub-features remaded.
- Merged traditional packages/features with Flatpak packages/features.
- Increased to 14 the ability to perform 1 operation and show 1 operation output at the same time.
- New interface style: In this style, selections are listed in a big way on the right, while operations are on the left.
-- Packages
- Added recommended Flatpak packages.
- Added detection if the package(s) entered is an automatic Flatpak package: If “.” in the name of the package(s) it is considered as a Flatpak package. Also added a button if the user wants to search without using .
-- Desktop Environments, Windows Managers & Compotisors
- Added “Compotisors”, a missing concept.
-- Scripts
- Thanks to the new interface, operations have been moved to selections and the left side has been canceled.
| Systemd Services
- Now running and active services are listed in the selections.
--- Tools
- All sub-features reworked or revisited.
-- Configure Bashrc and Zshrc
- Put options and file in the same class.
- Switch to a single function to add.
- Changed to a single function for undo.
- Moved Bashrc / Zshrc mode switcher to the bottom.
-- Change Computer's Name
- Texts have been improved.
-- About Some Distributions
- Some distributions have been changed.
- Updated information about distributions.
- The background was made from scratch: 150 lines, now 16 lines.
-- Calcer
- Improved history file creation process.
--- CLI
- Reworked
- Texts and parameters have been changed.
