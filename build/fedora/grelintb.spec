Name:           grelintb
Version:        1.3.6.2
Release:        5
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-tkinter python3-pip git curl xdg-utils

%description
GrelinTB's name stands for great toolbox for some Linux distributions because of these features:
- Sidebar
     - A button with hidden style for showing application's name for opening this repository.
     - A button with hidden style for showing version for opening current version's changelog.
     - A button with hidden style for opening developer's website.
     - A button with hidden style for opening a window which showing license and credit.
     - A button for controling updates. If new version available, get the changelog of the new version and update to new version.
     - A button for resetting GrelinTB.
     - A button for uninstalling GrelinTB.
     - A list for changing color theme (random, dark blue, blue, green).
     - A list for Changing appearance mode (system, light, dark).
     - A list for Changing language (English, Turkish).
     - A button for showing status. If some processes are working, it opens a new window for displaying all processes with time if not it shows a warning message.
- Startup
     - Showing warious informations (weather forecast, system, usages, fans, tempatures, battery).
     - Refreshing these informations.
- Notes and Documents
     - Creating, editing, renaming, deleting notes or any documents.
- Store
     - Traditional Applications: Searching, installing, reinstalling, uninstalling and updating predefined and desired applications.
     - Flatpak Applications: Searching, installing, reinstalling, uninstalling and updating desired applications.
     - Desktop Environments and Window Managers: Installing, reinstalling, uninstalling and updating some desktop environemtns and window managers.
     - Traditional Scripts: Updating all packages, making more complex updates, clearing package cache, removing unnecessary packages, fixing broken dependencies, showing history and listing installed packages.
     - Flatpak Scripts: Updating all packages, removing unnecessary packages, repairing Flatpak installation, showing history and listing installed packages.
     - Systemd Services: Getting the status of any service or enabling, disabling, starting and stopping it.
- Tools
     - Configuring Bash and Zsh.
     - Changing the name of the computer.
     - Showing some informations about some distributions.
     - Making simple math operations (basic calculator).
- Also
     - GrelinTB can auto detect tr_TR locale when there is no config related with language setting. If locale tr_TR, set GrelinTB's language Turkish. If not set GrelinTB's language English.
     - GrelinTB can synchronize with the system theme (dark or light) when appearance setted to system.
     - Check GrelinTB updates every Monday.
     - Some parameters for terminal. Tip: Help page for all parameters: grelintb help

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
%license /usr/local/bin/grelintb/LICENSE.txt
/usr/local/bin/grelintb/changelog-en.txt
/usr/local/bin/grelintb/changelog-tr.txt
/usr/local/bin/grelintb/grelintb.desktop
/usr/local/bin/grelintb/grelintb.py
/usr/local/bin/grelintb/icon.png
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/version.txt
/usr/share/applications/grelintb.desktop
/usr/bin/grelintb

%changelog
* Wed Apr 17 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Reduced the minimum window size from 1200x600 to 960x540.
- Added a button to refresh information in the "Start" section.
- Added real-time outputs to "Store" section.
- Removed the "Open Some File Managers with Root Rights" feature due to both insecurity and lack of functionality.
- Changed the status text in the sidebar to a button: Now, if there are running processes, clicking the button opens a new window and lists them.
- Various changes (removing the status text, changing the range sizes, optimizing methods, sub-section headers) were made to almost all of the store section.
- Zsh support has been added to the "Configure Bash" section. The section is now called "Configure Bash and Zsh".
- Updated information and shortened subsection titles in the "About Some Distributions" section.
- Improvements were made to the range sizes of the elements of the "Configure Bash and Zsh", "Change Computer Name" and "Calculator" sections.
- Fix minor and major errors.
- Make various minor improvements.
- Improved spelling in various places.