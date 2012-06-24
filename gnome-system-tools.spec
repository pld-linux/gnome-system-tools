#TODO
# think about split devel subpackage
Summary:	GNOME System Tools
Summary(pl):	GNOME System Tools - narz�dzia systemowe GNOME
Name:		gnome-system-tools
Version:	0.32.0
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.32/%{name}-%{version}.tar.bz2
# Source0-md5:	d916a4c03f7c922b5ec906bfdc1694ac
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	GConf2-devel >= 2.4.0.1
BuildRequires:	cracklib-devel
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0.1
BuildRequires:	libxml2-devel >= 2.5.11
Requires(post):	GConf2
Requires:	/etc/pld-release
Requires:	shadow-extras
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GST are a fully integrated set of tools aimed to make easy the job
that means the computer administration on an UNIX or Linux system.
They're thought to help from the new Linux or UNIX user to the system
administrators. The GNOME System Tools are free software, licensed
under the terms of the GNU General Public License.

%description -l pl
GST (GNOME System Tools) to w pe�ni zintegrowany zestaw narz�dzi,
kt�rych celem jest u�atwienie prac administracyjnych pod systemem
uniksowym lub linuksowym. S� pomy�lane tak, aby pom�c nowym
u�ytkownikom Linuksa lub Uniksa w administrowaniu systemem. GNOME
System Tools to wolnodost�pne oprogramowanie, licencjonowane na
warunkach Powszechnej Licencji Publicznej GNU.

%prep
%setup -q

%build
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS HACKING NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
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
