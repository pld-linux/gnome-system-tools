Summary:	GNOME System Tools
Summary(pl.UTF-8):	GNOME System Tools - narzędzia systemowe GNOME
Name:		gnome-system-tools
Version:	2.20.0
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-system-tools/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	382ed1f5ad4cb6ce7b88985611e2be18
Patch0:		%{name}-more-groups.patch
Patch1:		%{name}-more-services.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.11.2
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libiw-devel
BuildRequires:	liboobs-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	/etc/pld-release
Requires:	gtk+2 >= 2:2.12.0
Requires:	libgnomeui >= 2.20.0
Requires:	liboobs >= 2.20.0
Requires:	nautilus-libs >= 2.20.0
Requires:	shadow-extras
Requires:	system-tools-backends
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
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
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

rm -r $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/libnautilus-gst-shares.la

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so
%{_pkgconfigdir}/*.pc
%{_sysconfdir}/gconf/schemas/gnome-system-tools.schemas
%{_iconsdir}/hicolor/*/*/*.png
