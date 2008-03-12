Summary:	GNOME System Tools
Summary(pl.UTF-8):	GNOME System Tools - narzędzia systemowe GNOME
Name:		gnome-system-tools
Version:	2.22.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-tools/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	6559bb97fc75bc28b559dc530571d527
Patch0:		%{name}-more-groups.patch
Patch1:		%{name}-more-services.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	PolicyKit-devel >= 0.5
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.1.2
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	libiw-devel
BuildRequires:	liboobs-devel >= 2.22.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	/etc/pld-release
Requires:	PolicyKit-gnome
Requires:	gtk+2 >= 2:2.12.5
Requires:	libgnomeui >= 2.22.0
Requires:	liboobs >= 2.22.0
Requires:	nautilus-libs >= 2.22.0
Requires:	shadow-extras
Requires:	system-tools-backends >= 2.5.8
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
%patch1 -p1

%build
%{__gnome_doc_common}
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--enable-gnome \
	--disable-static \
	--enable-network \
	--enable-services \
	--enable-time \
	--enable-users \
	--enable-nautilus \
	--enable-shares
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/libnautilus-gst-shares.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-system-tools.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnome-system-tools.schemas

%postun
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
%{_datadir}/%{name}
%{_desktopdir}/network.desktop
%{_desktopdir}/services.desktop
%{_desktopdir}/shares.desktop
%{_desktopdir}/time.desktop
%{_desktopdir}/users.desktop
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-gst-shares.so
%{_pkgconfigdir}/gnome-system-tools.pc
%{_sysconfdir}/gconf/schemas/gnome-system-tools.schemas
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
