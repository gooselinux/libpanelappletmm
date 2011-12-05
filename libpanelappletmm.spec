Name:           libpanelappletmm
Version:        2.26.0
Release:        3%{?dist}
Summary:        C++ interface for Gnome panel applets

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libpanelappletmm/2.26/libpanelappletmm-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gconfmm26-devel >= 2.6.0
BuildRequires: libgnomemm26-devel >= 2.6.0
BuildRequires: gnome-panel-devel >= 2.14.0
BuildRequires: doxygen, graphviz


%description
libpanelappletmm is part of the gnomemm project and provides a C++
interface for developing Gnome panel applets.


%package devel
Summary:  Headers for developing programs that will use %{name}
Group:    Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gconfmm26-devel
Requires: libgnomemm26-devel
Requires: gnome-panel-devel


%description devel
This package contains the static libraries and header files needed for
developing C++ gnome panel applets using libpanelappletmm.


%prep
%setup -q


%build
%configure %{!?_with_static: --disable-static}

# Take care of unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

# Build documentation
make -C docs/reference


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, -)
%doc ChangeLog docs/reference/html
%{_includedir}/libpanelappletmm-2.6
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%{_libdir}/libpanelappletmm-2.6
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu May 27 2010 Benjamin Otte <otte@redhat.com> - 2.26.0-3
- Fix source URL
Resolves: #rhbz596643

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.26.0-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0
- Removed upstreamed patch 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Denis Leroy <denis@poolshark.org> - 2.22.0-2
- Added patch to fix compiling with gnome ui flags

* Thu Mar 13 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to upstream 2.22.0

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.0-3
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Denis Leroy <denis@poolshark.org> - 2.6.0-2
- Review fixes

* Fri Aug 24 2007 Denis Leroy <denis@poolshark.org> - 2.6.0-1
- First version

