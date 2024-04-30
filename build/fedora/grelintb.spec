Name:           grelintb
Version:        1.4.3
Release:        3
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
/usr/share/applications/grelintb.desktop
/usr/bin/grelintb

%changelog
* Tue Apr 30 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Improve note saving experience in "Notes and Documents".
- Change exit()'s to sys.exit()'s.
- Fix some errors in "Store" for Debian GNU/Linux based distributions.
- Fix some grammer errors.