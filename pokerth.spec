Name:		pokerth
Summary:	PokerTH - play Texas Holdem Poker alone or online
Version:	0.9.5
Release:	1
License:	GPLv2+
Group:		Games/Cards
URL:		http://www.pokerth.net/
Source0:	http://downloads.sourceforge.net/pokerth/PokerTH-%{version}-src.tar.bz2
Patch0:		PokerTH-0.9.1-libircclient-dir.patch
Patch1:		PokerTH-0.9.1-link.patch
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	qt4-devel
BuildRequires:	gnutls-devel
# Boost version in 2010.2 is too old so no backport to 2010.2
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libgsasl-devel
BuildRequires:	tinyxml-devel
BuildRequires:	libircclient-static-devel

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
%patch0 -p0
%patch1 -p0

%build
%qmake_qt4 pokerth.pro QMAKE_CXXFLAGS="%{optflags} -DBOOST_FILESYSTEM_VERSION=2"
%make

%install
%__rm -rf %{buildroot}
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

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc ChangeLog docs/gui_styling_howto.txt
%attr(0755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png

%files server
%defattr(0644,root,root,0755)
%doc ChangeLog COPYING docs/server_setup_howto.txt
%attr(0755,root,root) %{_bindir}/%{name}_server
