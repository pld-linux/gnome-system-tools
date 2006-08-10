Summary:	GNOME System Tools
Summary(pl):	GNOME System Tools - narzêdzia systemowe GNOME
Name:		gnome-system-tools
Version:	2.14.0
Release:	4
License:	GPL v2
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-system-tools/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	3aded3a37f4f5b4962bf253d25cebea1
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	cracklib-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.21
BuildRequires:	nautilus-devel >= 2.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	system-tools-backends >= 1.4.0
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	/etc/pld-release
Requires:	gtk+2 >= 2:2.8.3
Requires:	libgnomeui >= 2.14.0
Requires:	nautilus-libs >= 2.14
Requires:	shadow-extras
Requires:	system-tools-backends >= 1.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GST are a fully integrated set of tools aimed to make easy the job
that means the computer administration on an UNIX or Linux system.
They're thought to help from the new Linux or UNIX user to the system
administrators. The GNOME System Tools are free software, licensed
under the terms of the GNU General Public License.

%description -l pl
GST (GNOME System Tools) to w pe³ni zintegrowany zestaw narzêdzi,
których celem jest u³atwienie prac administracyjnych pod systemem
uniksowym lub linuksowym. S± pomy¶lane tak, aby pomóc nowym
u¿ytkownikom Linuksa lub Uniksa w administrowaniu systemem. GNOME
System Tools to wolnodostêpne oprogramowanie, licencjonowane na
warunkach Powszechnej Licencji Publicznej GNU.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__gnome_doc_common}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-platform-gnome-2 \
	--disable-static \
	--enable-boot \
	--enable-network \
	--enable-services \
	--enable-time \
	--enable-users \
	--enable-disks \
	--enable-share
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/libnautilus-gst-shares.la

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-system-tools.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall gnome-system-tools.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS HACKING NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so
%{_omf_dest_dir}/*
%{_pkgconfigdir}/*.pc
%{_sysconfdir}/gconf/schemas/gnome-system-tools.schemas
