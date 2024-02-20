# GrelinTB
## Great toolbox for some Linux distros.
- [Bu dökümantasyonun devamını Türkçe dilinde görüntelemek için bu cümleye tıklayın.](#turkish)
## Features
### Sidebar:
- Show app's name, when clicked open this GitHub repository.
- Show version, when clicked open current versions's changelog.
- Show developer's name when clicked open developer's website.
- A button for license and credits.
- Control updates. If new version available, get the changelog of the new version and update to the new version.
- Reset GrelinTB.
- Uninstall GrelinTB.
- Enable/disable startup informations.
- Change color theme.
- Change appearance mode.
- Change language.
- Status text.
### Starting:
- A nice welcome text or weather forecast and system information.
### Notes:
- Create, edit, delete notes and documents.
### Store: 
- General: Search, install, reinstall and uninstall for some applications.
- Other: Search, install, reinstall and uninstall any package.
### Tools:
- Configure Bash.
- Change the name of the computer.
- Open file managers with root rights.
- About some distributions.
- Calculator.
### Scripts:
- Open Cups configuration page.
- Open Wine configuration app.
- Open Grub Customizer.
- Update packages.
- Clear package cache.
- Remove unnecessary packages.
- Update Flatpak packages.
- Remove unnecessary Flatpak packages.
- Only for Debian GNU/Linux base: Resolve package errors.
### Also:
- Auto detect tr_TR locale. If locale tr_TR, set GrelinTB's language Turkish. If not set GrelinTB's language English.
- Auto detect system appearance.
- Check GrelinTB updates every Monday.
- Some parameters for terminal. Note: Help page for all parameters: `grelintb help`
- Maybe more...
## Installation
- Please install wget package.
- Open terminal.
- Type this: ```wget https://raw.githubusercontent.com/MuKonqi/grelintb/main/install-grelintb.sh ; chmod +x install-grelintb.sh ; pkexec ./install-grelintb.sh ; rm install-grelintb.sh```
## Dependencies
- A distribution based on Debian GNU/Linux (apt) or Fedora Linux (dnf) or Solus (eopkg) or Arch Linux (pacman)
- Minimum screen resolution of 1200x600 for best efficiency
- curl (it usually comes installed, also package name: `curl`)
- xdg-utils (it usually comes installed, also package name: `xdg-utils`)
- pkexec (it usually comes installed, also package name: `pkexec`)
- A pkexec agent (it usually comes installed with DE's, if not please install a agent)
- neofetch (package name: `neofetch`)
- lolcat (package name: `lolcat`)
- python3 (package name: `python3`)
- pip (package name: usually `pip`)
- CustomTkinter (after installing pip, run this command: `pip install customtkinter`)
- Tkinter (package name: `python3-tk` (Debian GNU/Linux based) or `python3-tkinter` (Fedora Linux and Solus based) or `tk` (Arch Linux based))
## Why was GrelinTB made?
### Pros
+ GrelinTB's UI good and simpler. MetterXP has very bad UI and it buggy.
+ GrelinTB's codes are really more optimize because OOB. MetterXP doesn't have OOB, it has bloat file-moduling system.
+ GrelinTB doesn't have theme system but it has appearance system.
+ GrelinTB can detect system theme and tr_TR locale.
+ GrelinTB supports Arch Linux based distributions.
+ GrelinTB's window's size isn't fixed, it can flow any value greater than 1200x600.
### Cons
- GrelinTB doesn't provide options for DE/WM and default applications (Firefox etc.). So as the developer of both projects (by the way MetterXP based on BetterXP, BetterXP based on Terminalden kurtulun), I think GrelinTB is better. DE/WM is usually installed several times, not always DE/WM is installed, if needed it can be easily looked up on the internet. Also the default applications are already installed in most distributions.
### Result
+ GrelinTB is coded from scratch with OOB. But MetterXP is based on BetterXP. BetterXP is based on Terminalden kurtulun (not my project). So MetterXP is based on a long process and there are many remnants.
## Copyright Notification, License, Credits
- Copyright (C) 2024 MuKonqi (Muhammed S.)
- GNU General Public License, Version 3.0 or later
- [Neofetch](https://github.com/dylanaraps/neofetch) (for system information)
- [Lolcat](https://github.com/busyloop/lolcat) (for colorful commands in terminal)
- [wttr.in](https://github.com/chubin/wttr.in) (for weather forecast)
# GrelinTB
## Bazı Linux dağıtımları için harika bir araç kutusu.
- [Click on this sentence to view the rest of this documentation in English.](#english)
## Özellikler
### Kenar Çubuğu:
- Uygulamanın adını göster, tıklandığında bu GitHub deposunu aç.
- Sürümü göster, tıklandığında mevcut sürümlerin değişiklik günlüğünü aç.
- Tıklandığında geliştiricinin adını göster geliştiricinin internet sitesini aç.
- Lisans ve krediler için bir buton.
- Güncellemeleri kontrol edin. Yeni sürüm mevcutsa, yeni sürümün değişiklik günlüğünü alın ve yeni sürüme güncelleyin.
- GrelinTB'yi sıfırlayın.
- GrelinTB'yi kaldırın.
- Başlangıç bilgilerini etkinleştirin/devre dışı bırakın.
- Renk temasını değiştirin.
- Görünüm modunu değiştirin.
- Dili değiştirin.
- Durum metni.
### Başlangıç:
- Güzel bir karşılama metni veya hava durumu tahmini ve sistem bilgileri.
### Notlar:
- Notlar ve belgeler oluşturun, düzenleyin, silin.
### Mağaza: 
- Genel: Bazı uygulamalar için arama, yükleme, yeniden yükleme ve kaldırma.
- Diğer: Herhangi bir paketi arayın, yükleyin, yeniden yükleyin ve kaldırın.
### Araçlar:
- Bash'ı yapılandırın.
- Bilgisayarın adını değiştirin.
- Kök hakları ile dosya yöneticilerini açın.
- Bazı dağıtımlar hakkında.
- Hesap makinesi.
### Betikler:
- Cups yapılandırma sayfasını açın.
- Wine yapılandırma uygulamasını açın.
- Grub Özelleştirici'yi açın.
- Paketleri güncelleyin.
- Paket önbelleğini temizleyin.
- Gereksiz paketleri kaldırın.
- Flatpak paketlerini güncelleyin.
- Gereksiz Flatpak paketlerini kaldırın.
- Sadece Debian GNU/Linux tabanı için: Paket hatalarını çözün.
### Ayrıca:
- tr_TR yerel ayarını otomatik algıla. Eğer yerel ayar tr_TR ise, GrelinTB'nin dilini Türkçe olarak ayarlayın. Değilse GrelinTB'nin dilini İngilizce olarak ayarlayın.
- Sistem görünümünü otomatik algıla.
- Her pazartesi GrelinTB güncellemelerini kontrol et.
- Terminal için bazı parametreler. Not: Tüm parametreler için yardım sayfası: `grelintb yardım`
- Belki daha fazlası...
## Kurulum
- Lütfen wget paketini yükleyin.
- Terminali açın.
- Bunu yazın: ```wget https://raw.githubusercontent.com/MuKonqi/grelintb/main/install-grelintb.sh ; chmod +x install-grelintb.sh ; pkexec ./install-grelintb.sh ; rm install-grelintb.sh```
## Bağımlılıklar
- Debian GNU/Linux (apt) veya Fedora Linux (dnf) veya Solus (eopkg) veya Arch Linux (pacman) tabanlı bir dağıtım
- En iyi verim için minimum 1200x600 ekran çözünürlüğü
- curl (genellikle yüklü olarak gelir, ayrıca paket adı: `curl`)
- xdg-utils (genellikle yüklü olarak gelir, ayrıca paket adı: `xdg-utils`)
- pkexec (genellikle yüklü olarak gelir, ayrıca paket adı: `pkexec`)
- Bir pkexec ajanı (genellikle DE'lerle birlikte yüklü olarak gelir, değilse lütfen bir ajan yükleyin)
- neofetch (paket adı: `neofetch`)
- lolcat (paket adı: `lolcat`)
- python3 (paket adı: `python3`)
- pip (paket adı: genellikle `pip`)
- CustomTkinter (pip yükledikten sonra şu komutu çalıştırın: `pip install customtkinter`)
- Tkinter (paket adı: `python3-tk` (Debian GNU/Linux tabanlı) veya `python3-tkinter` (Fedora Linux ve Solus tabanlı) veya `tk` (Arch Linux tabanlı))
## Neden GrelinTB yapıldı?
### Artılar
+ GrelinTB'nin kullanıcı arayüzü iyi ve daha basit. MetterXP çok kötü bir kullanıcı arayüzüne sahip ve hatalı.
+ GrelinTB'nin kodları gerçekten daha optimize çünkü OOB. MetterXP'de OOB yok, bloat dosya modülleme sistemi var.
+ GrelinTB'nin tema sistemi yok ama görünüm sistemi var.
+ GrelinTB sistem temasını ve tr_TR yerel ayarını algılayabilir.
+ GrelinTB Arch Linux tabanlı dağıtımları destekler.
+ GrelinTB'nin pencere boyutu sabit değildir, 1200x600'den daha büyük herhangi bir değeri akıtabilir.
### Eksiler
- GrelinTB, DE/WM ve varsayılan uygulamalar (Firefox vb.) için seçenekler sunmuyor. Her iki projenin de geliştiricisi olarak (bu arada MetterXP BetterXP'ye, BetterXP Terminalden kurtulun'a dayanıyor) GrelinTB'nin daha iyi olduğunu düşünüyorum. DE/WM genellikle birkaç kez kurulur, her zaman DE/WM kurulmaz, gerekirse internetten kolayca bakılabilir. Ayrıca varsayılan uygulamalar çoğu dağıtımda zaten yüklüdür.
### Sonuç
+ GrelinTB sıfırdan OOB ile kodlanmıştır. Fakat MetterXP, BetterXP tabanlı. BetterXP ise Terminalden kurtulun tabanlı (benim projem değil). Yani MetterXP'ın temeli uzun bir sürece dayanır ve kalıntıları çoktur.
## Telif Hakkı Bildirimi, Lisans, Krediler
- Telif Hakkı (C) 2024 MuKonqi (Muhammed S.)
- GNU General Public License, Version 3.0 veya sonrası
- [Neofetch](https://github.com/dylanaraps/neofetch) (sistem bilgisi için)
- [Lolcat](https://github.com/busyloop/lolcat) (terminalde renkli komutlar için)
- [wttr.in](https://github.com/chubin/wttr.in) (hava durumun için)