Name:           grelintb
Version:        1.4.5
Release:        1
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

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
/usr/local/bin/grelintb/update.sh
/usr/local/bin/grelintb/reset.sh
/usr/local/bin/grelintb/uninstall.sh
/usr/local/bin/grelintb/grelintb.py
/usr/share/applications/grelintb.desktop
/usr/bin/grelintb

%changelog
* Sun May 5 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- Move .bashrc's and .zshrc's backups and calculation history from /home/<username> folder to /home/<username>/.local/share/grelintb folder. This keeps the user's home folder cleaner.
- Switch to DNF5. This allows GrelinTB to prepare for Fedora Linux 41 and experience the benefits of DNF5.
- Add Hyprland for Fedora Linux and Arch Linux baseds.
- Add "Listing Installed Leaves" for Fedora Linux baseds. According to DNF5's wiki, it's is useful because: The list gives you a nice overview of what is installed on your system without flooding you with anything required by the packages already shown.
- Change "Traditional" texts in Store to more meaningful expressions.
- Fix text of distribution synchronizing button.
- Remove group reinstalling for Fedora Linux baseds. Because DNF (both of DNF4 and DNF5) doesn't support it.
- Remove fixing broken dependencies for Fedora Linux baseds.
- Remove distribution synchronizing for Arch Linux baseds.
- Fix that things that some distributions do not support in the traditional scripts section are enabled after any operation.