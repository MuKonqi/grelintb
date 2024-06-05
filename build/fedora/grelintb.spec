Name:           grelintb
Version:        1.4.7
Release:        2
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-1.tar.gz

Requires:       dnf5 python3 python3-tkinter python3-pip git curl xdg-utils

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
/usr/local/bin/grelintb/theme.json
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/reset.sh
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/grelintb.py
/usr/share/applications/grelintb.desktop
/usr/bin/grelintb

%changelog
* Thu Jun 06 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Renamed color as theme (this will reset your theme configuration)
- Renamed theme as appearance (this will reset your appearance configuration).
- Added a new theme.
- Added labels for theme, appearance and language.
- Removed backward compatibility for .bashrc/.zshrc backups.