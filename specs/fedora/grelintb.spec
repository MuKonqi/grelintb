Name:           grelintb
Version:        1.3.5.0
Release:        1
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-tkinter python3-pip git curl lolcat xdg-utils

%description
GrelinTB is a great (simple, useful, fast, modern) toolbox for some Linux distributions made in Python3 and CustomTkinter.
GrelinTB's features:
- Sidebar
- A beatiful startup page
- Note and document editor
- Basic store and some related tools
- Other tools
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
* Fri Mar 22 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- %{version}
-   Startup page made from scratch.
-   Various improvements have been made to the "Notes and Documents" section.
-   Removed the option for startup information in the sidebar.
-   The automatic update check on Monday is done in the background so as not to prolong startup.
-   Weather and CPU utilization percentage are taken in the background so as not to prolong startup.