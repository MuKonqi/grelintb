Name:           grelintb
Version:        1.3.6.1
Release:        1
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-tkinter python3-pip git curl xdg-utils

%description
GrelinTB is a great (simple, useful, fast, modern) toolbox for some Linux distributions made in Python3 and CustomTkinter.
GrelinTB's features:
- Sidebar for customizing GrelinTB and other good things
- A ufeful startup page
- Note and document editor
- Store for basic operations and some related scripts
- Other useful tools
- And more

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
* Sun Apr 7 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Reduced the minimum window size from 1200x600 to 960x540.
- Added a button to refresh information in the "Start" section.
- Removed the "Open Some File Managers with Root Rights" feature due to both insecurity and lack of functionality.
- Changed the status text in the sidebar to a button: Now, if there are running processes, clicking the button opens a new window and lists them.
- Various changes (removing the status text, changing the range sizes, optimizing methods, sub-section headers) were made to almost all of the store section.
- Zsh support has been added to the "Configure Bash" section. The section is now called "Configure Bash and Zsh".
- Updated information and shortened subsection titles in the "About Some Distributions" section.
- Improvements were made to the range sizes of the elements of the "Configure Bash and Zsh", "Change Computer Name" and "Calculator" sections.
- Bug fixes have been made: Syntax fixes for grelintb.py under Python 3.12 and for update.sh and uninstall.sh.
- Various minor improvements.
- Improved spelling in various places.