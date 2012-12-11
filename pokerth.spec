Name:		pokerth
Summary:		PokerTH - play Texas Holdem Poker alone or online
Version:		0.9.5
Release:		1
License:		GPLv2+
Group:		Games/Cards
URL:		http://www.pokerth.net/
Source0:		http://downloads.sourceforge.net/pokerth/PokerTH-%{version}-src.tar.bz2
Patch0:		PokerTH-0.9.1-libircclient-dir.patch
Patch1:		PokerTH-0.9.1-link.patch
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:	qt4-devel
BuildRequires:	gnutls-devel
# Boost version in 2010.2 is too old so no backport to 2010.2
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(libgsasl)
BuildRequires:	tinyxml-devel
BuildRequires:	libircclient-static-devel
BuildRequires:	libgcrypt-devel

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
%qmake_qt4 pokerth.pro 
%make

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


%changelog
* Tue Jul 03 2012 Crispin Boylan <crisb@mandriva.org> 0.9.5-1
+ Revision: 807897
- Use filesystem 3 now that it is the only version in boost
- New release

* Tue Apr 03 2012 Crispin Boylan <crisb@mandriva.org> 0.9.1-2
+ Revision: 789035
- Rebuild for new boost

* Tue Jan 31 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.1-1
+ Revision: 770059
- Add patch1 to fix linkage
- Add patch for new libircclient include dir (changed in 1.5)
- New version 0.9.1

* Thu Jan 05 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9-1
+ Revision: 757902
- New version 0.9

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 0.8.3-3
+ Revision: 650200
- rebuild for new gnutls

* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 0.8.3-2
+ Revision: 645775
- force boost filesystem v2 component
- rebuild

* Tue Feb 08 2011 John Balcaen <mikala@mandriva.org> 0.8.3-1
+ Revision: 636920
- Update to 0.8.3

* Thu Oct 14 2010 John Balcaen <mikala@mandriva.org> 0.8.1-1mdv2011.0
+ Revision: 585594
- Update to 0.8.1

* Mon Sep 27 2010 John Balcaen <mikala@mandriva.org> 0.8-1mdv2011.0
+ Revision: 581409
- Update to 0.8
- add buildrequires for libgsasl-devel

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.7.1-4mdv2011.0
+ Revision: 565997
- rebuild for new boost

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.7.1-3mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 0.7.1-2mdv2010.0
+ Revision: 418866
- rebuild for new libboost

* Fri Jun 26 2009 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 389335
- New version 0.7.1

* Mon May 04 2009 Funda Wang <fwang@mandriva.org> 0.7-1mdv2010.0
+ Revision: 371745
- New version 0.7

* Thu Mar 12 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.3-2mdv2009.1
+ Revision: 354300
- rebuild for new boost

* Sun Jan 04 2009 Guillaume Bedot <littletux@mandriva.org> 0.6.3-1mdv2009.1
+ Revision: 324392
- New release 0.6.3.

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 0.6.2-6mdv2009.1
+ Revision: 316561
- rebuild for new boost

* Tue Aug 19 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.2-5mdv2009.0
+ Revision: 273511
- rebuild against new boost

* Mon Aug 18 2008 Funda Wang <fwang@mandriva.org> 0.6.2-4mdv2009.0
+ Revision: 273426
- BR new boost

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.6.2-3mdv2009.0
+ Revision: 263958
- build server with server opts

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 0.6.2-2mdv2009.0
+ Revision: 263949
- specify qtdir using macro
- compile with new compile flags

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu May 29 2008 David Walluck <walluck@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 212877
- BuildRequires: curl-devel
- no need for n flag on subpackage
- 0.6.2
- remove overloaded macros
- fix License
- BuildRequires: gnutls-devel now instead of openssl-devel
- remove rpath from binaries
- fix manpage location
- call update-desktop-database
- fix eol in net_protocol.txt

* Wed Mar 26 2008 Guillaume Bedot <littletux@mandriva.org> 0.6.1-1mdv2009.0
+ Revision: 190340
- 0.6.1
- dropped obsolete patch
- added an icon

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

* Thu Dec 20 2007 Guillaume Bedot <littletux@mandriva.org> 0.6-2mdv2008.1
+ Revision: 135889
- Fix perms
- Allow license to be displayed

* Tue Dec 18 2007 Guillaume Bedot <littletux@mandriva.org> 0.6-1mdv2008.1
+ Revision: 131979
- import pokerth

