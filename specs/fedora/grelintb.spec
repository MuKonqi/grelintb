Name:           grelintb
Version:        1.3.6.0
Release:        1
Summary:        Great toolbox for some Linux distributions.
License:        GPLv3+
URL:            https://github.com/mukonqi/grelintb
Source0:        %{name}-%{version}.tar.gz

Requires:       python3 python3-tkinter python3-pip git curl xdg-utils

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
* Fri Apr 5 2024 MuKonqi (Muhammed S.) <mukonqi@gmail.com>
- %{version}
-   Reduced the minimum window size from 1200x600 to 960x540.
-   Removed the "Open Some File Managers with Root Rights" feature due to both lack of security and functionality.
-   Changed the status text in the sidebar to a button: Now, if there are running processes, clicking the button opens a new window and lists them.
-   Various changes were made to almost all of the store section (removing status text, changing spacing sizes, improving methods, sub-section headers).
-   Zsh support has been added to the "Configure Bash" section. The section is now called "Configure Bash and Zsh".
-   Updated information and shortened subsection titles in the "About Some Distributions" section.
-   Improvements were made to the range sizes of the elements of the "Configure Bash and Zsh", "Change Computer Name" and "Calculator" sections.
-   Bug fixes have been made: For example there were critical syntax issues in 3.11, because I was using an innovation in Python 3.12 without realizing it.
-   Various minor improvements were made.
-   Improved spelling in various places.