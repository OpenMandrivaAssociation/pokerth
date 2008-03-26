%define name pokerth
%define oname PokerTH
%define version 0.6.1
%define release %mkrel 1

Name: %{name}
Summary: PokerTH - play Texas Holdem Poker alone or online
Version: %{version}
Release: %{release}
License: GPL
#v2
Group: Games/Cards
URL: http://www.pokerth.net/
Source: http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.src.tar.bz2
BuildRequires: qt4-devel
BuildRequires: openssl-devel
BuildRequires: boost-devel
BuildRequires: SDL_mixer1.2-devel
BuildRequires: desktop-file-utils
%if %mdkversion < 200800
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%endif

%package -n %{name}-server
Summary: PokerTH server
License: GPL
Group: Games/Cards

%description
PokerTH is a multi-platform poker game.
It allows you to play the popular "Texas Hold'em" poker variant against up to 
six computer-opponents or play network games with people all over the world.

%description -n %{name}-server
PokerTH server.

%prep
%setup -n %{oname}-%{version}-src -q
perl -pi -e "s|.png||" %{name}.desktop
perl -pi -e "s|\r\n|\n|" ChangeLog

%build
export QTDIR=/usr/lib/qt4
$QTDIR/bin/qmake pokerth_lib.pro -o Makefile_lib
make -f Makefile_lib
$QTDIR/bin/qmake pokerth_game.pro -o Makefile_game
make -f Makefile_game
$QTDIR/bin/qmake pokerth_server.pro -o Makefile_server
make -f Makefile_server

%install
rm -rf %{buildroot}
#data
make -f Makefile_game install INSTALL_ROOT=%{buildroot}
#binaries
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 755 bin/%{name}_server %{buildroot}%{_bindir}/
#man page
install -d -m 755 %{buildroot}%{_mandir}/1
install -m 644 docs/%{name}.1 %{buildroot}%{_mandir}/1/
#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
#menu
install -d -m 755 %{buildroot}%{_datadir}/applications/
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/


mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor="" \
  --remove-key="Version" \
  --remove-category="Application" \
  --add-category="Qt" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Cards" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%post
%{update_menus}
 
%postun
%{clean_menus} 

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog docs/net_protocol.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%files -n %{name}-server
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING docs/net_protocol.txt
%attr(0755,root,root) %{_bindir}/%{name}_server

