Summary:	GNOME System Tools
Name:		gnome-system-tools
Version:	0.23.0
Release:	1
License:	LGPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.23/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/projects/gst/
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libglade2-devel 
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	vte-devel >= 0.10.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%description
The GST are a fully integrated set of tools aimed to make easy the job
that means the computer administration on an UNIX or Linux system.
They're thought to help from the new Linux or UNIX user to the system
administrators. The GNOME System Tools are free software, licensed
under the terms of the GNU General Public License.

%prep
%setup -q

%build
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
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_sysconfdir}/X11/sysconfig/*.desktop
%{_datadir}/%{name}
%{_datadir}/setup-tool-backends
%{_sysconfdir}/gconf/schemas/%{name}.*
