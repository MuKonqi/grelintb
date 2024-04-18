Name:           grelintb
Version:        1.4.0
Release:        1
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-tkinter python3-pip git curl xdg-utils

%description
GrelinTB comes with various tools. Here are examples: Useful information about the system, a simple note editor, a simple store for applications and DEs and WMs, various scripts for applications, a simple configuration tool for Bash and Zsh, a tool to change the name of the computer, information about some distributions and a simple calculator.

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
/usr/local/bin/grelintb/primary-changelog.txt
/usr/local/bin/grelintb/major-changelog.txt
/usr/local/bin/grelintb/minor-changelog.txt
/usr/local/bin/grelintb/version.txt
/usr/local/bin/grelintb/grelintb.desktop
/usr/local/bin/grelintb/icon.png
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/reset.sh
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/grelintb.py
/usr/bin/grelintb

%changelog
* Thu Apr 18 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Removed the text for configuration in the sidebar and embedded it in the list elements.
- Renewed changelog screen.
- Renewed license screen.
- Separated license and credit.
- Added button for about credit.
- Minor improvements to the list of all transactions section.
- Fixed various bugs.
- Created a new file for reset: reset.sh
- Split changelogs into 3 and removed the Turkish changelog.
- Changed version naming system. From now on, major (radical changes) will be the 1st digit of the version number, major (new features) releases will be the 2nd digit of the version number, and minor (bug fixes and very minor innovations) will be the 3rd digit of the version number. Release number will probably always be 1. There was no such order in the past.