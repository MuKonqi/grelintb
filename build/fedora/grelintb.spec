Name:           grelintb
Version:        1.4.2
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
/usr/share/applications/grelintb.desktop
/usr/bin/grelintb

%changelog
* Sun Apr 28 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Disable writing in output in store when waiting for new line.
- Check the exit code of the processes in the store section. If it is 0, show a information messagebox if not, show a error messagebox.
- Increase f-strings instead of string with + operators.
- Revisit commands in the store section.
- Improve shell scripts.