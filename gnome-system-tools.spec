#TODO
# think about split devel subpackage
Summary:	GNOME System Tools
Summary(pl):	GNOME System Tools - narzêdzia systemowe GNOME
Name:		gnome-system-tools
Version:	1.1.90
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	c68597f9b85525b4719d16409849b734
Patch0:		%{name}-CommonMakefile.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.9.2
BuildRequires:	cracklib-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.5.0
BuildRequires:	libgnomeui-devel >= 2.9.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.11
BuildRequires:	nautilus-devel >= 2.9.90
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	/etc/pld-release
Requires:	gtk+2 >= 2:2.6.2
Requires:	shadow-extras
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
%patch1 -p1
%patch2 -p1

%build
cd backends
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

%{__libtoolize}
gnome-doc-common
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-platform-gnome-2 \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS HACKING NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so
%attr(755,root,root) %{_datadir}/setup-tool-backends/scripts/*
%attr(755,root,root) %{_datadir}/setup-tool-backends/files/*
%dir %{_datadir}/setup-tool-backends
%dir %{_datadir}/setup-tool-backends/files
%dir %{_datadir}/setup-tool-backends/scripts
%{_desktopdir}/*.desktop
%{_sysconfdir}/X11/sysconfig/*.desktop
%{_datadir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.*
%{_pkgconfigdir}/*.pc
%{_omf_dest_dir}/%{name}
%{_aclocaldir}/*.m4
