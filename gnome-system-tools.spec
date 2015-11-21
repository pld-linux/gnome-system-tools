Summary:	GNOME System Tools
Summary(pl.UTF-8):	GNOME System Tools - narzędzia systemowe GNOME
Name:		gnome-system-tools
Version:	3.0.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-tools/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	5dc48086cec964d146c9c446a54a8d39
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	GConf2
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool
BuildRequires:	libiw-devel
BuildRequires:	liboobs-devel >= 3.0.0
BuildRequires:	libxml2-progs
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	system-tools-backends >= 2.10.0
BuildRequires:	system-tools-backends-devel >= 2.10.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	/etc/pld-release
Requires:	gtk+3 >= 3.0.0
Requires:	liboobs >= 2.30.0
Requires:	nautilus-libs >= 3.0.0
Requires:	polkit-gnome >= 0.94
Requires:	setup >= 2.6.1-1
Requires:	shadow-extras
Requires:	system-tools-backends >= 2.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GST are a fully integrated set of tools aimed to make easy the job
that means the computer administration on an UNIX or Linux system.
They're thought to help from the new Linux or UNIX user to the system
administrators. The GNOME System Tools are free software, licensed
under the terms of the GNU General Public License.

%description -l pl.UTF-8
GST (GNOME System Tools) to w pełni zintegrowany zestaw narzędzi,
których celem jest ułatwienie prac administracyjnych pod systemem
uniksowym lub linuksowym. Są pomyślane tak, aby pomóc nowym
użytkownikom Linuksa lub Uniksa w administrowaniu systemem. GNOME
System Tools to wolnodostępne oprogramowanie, licencjonowane na
warunkach Powszechnej Licencji Publicznej GNU.

%prep
%setup -q
%patch0 -p1

%build
mkdir m4
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static \
	--enable-nautilus \
	--enable-network \
	--enable-polkit-gtk \
	--enable-services \
	--enable-shares \
	--enable-time \
	--enable-users
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/libnautilus-gst-shares.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS HACKING NEWS ChangeLog
%attr(755,root,root) %{_bindir}/network-admin
%attr(755,root,root) %{_bindir}/services-admin
%attr(755,root,root) %{_bindir}/shares-admin
%attr(755,root,root) %{_bindir}/time-admin
%attr(755,root,root) %{_bindir}/users-admin
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-gst-shares.so
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.system-tools.gschema.xml
%dir %{_sysconfdir}/gnome-system-tools
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnome-system-tools/user-profiles.conf
%{_desktopdir}/network.desktop
%{_desktopdir}/services.desktop
%{_desktopdir}/shares.desktop
%{_desktopdir}/time.desktop
%{_desktopdir}/users.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_pkgconfigdir}/gnome-system-tools.pc
