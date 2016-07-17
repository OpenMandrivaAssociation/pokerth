%define _disable_lto 1

Name:		pokerth
Summary:	PokerTH - play Texas Holdem Poker alone or online
Version:	1.1.1
Release:	3
License:	GPLv2+
Group:		Games/Cards
URL:		http://www.pokerth.net/
Source0:	http://downloads.sourceforge.net/pokerth/PokerTH-%{version}-src.tar.bz2
Patch0:		PokerTH-1.0.1-libircclient-dir.patch
Patch1:		PokerTH-0.9.1-link.patch
Patch2:		pokerth-1.1.1-fstream-ambiguity.patch
Patch3:		pokerth-1.1.1-ownerless.patch
Patch4:		pokerth-1.1.1-cxx11-build.patch
Patch5:		pokerth-1.1.1-cxx11-fixes.patch
BuildRequires:	qt4-devel
BuildRequires:	gnutls-devel
BuildRequires:	boost-devel
BuildRequires:	tinyxml-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgsasl)
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(SDL_mixer)

%description
PokerTH is a multi-platform poker game.
It allows you to play the popular "Texas Hold'em" poker variant against up to 
six computer-opponents or play network games with people all over the world.

%package	server
Summary:	PokerTH server
Group:		Games/Cards

%description server
PokerTH server.

%prep
%setup -q -n PokerTH-%{version}-src
%apply_patches

%build
%qmake_qt4 pokerth.pro QMAKE_CXXFLAGS_RELEASE= 
%make CC=gcc CXX=g++

%install
#data
%make INSTALL_ROOT=%{buildroot} install
#binaries
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 755 bin/%{name}_server %{buildroot}%{_bindir}/
#man page
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/
#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{name}.png %{buildroot}%{_iconsdir}/%{name}.png
#menu
install -d -m 755 %{buildroot}%{_datadir}/applications/
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/


%files
%doc ChangeLog docs/gui_styling_howto.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%files server
%doc ChangeLog COPYING docs/server_setup_howto.txt
%attr(0755,root,root) %{_bindir}/%{name}_server

