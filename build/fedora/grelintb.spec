Name:           grelintb
Version:        1.5.0
Release:        4
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-1.tar.gz

Requires:       dnf5 python3 python3-tkinter python3-pip git curl coreutils xdg-utils

%description
GrelinTB comes with various tools. Here are examples: Useful informations about the system etc., a simple note and document editor, a simple store for packages and DEs and WMs, various scripts for packages, a simple configuration tool for Bashrc and Zshrc, a tool to change the name of the computer, information about some distributions and a simple calcer.

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
/usr/local/bin/grelintb/reset.sh
/usr/local/bin/grelintb/theme.json
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/version.txt

%changelog
* Sat Jun 08 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Started developing 1.5.0 version.