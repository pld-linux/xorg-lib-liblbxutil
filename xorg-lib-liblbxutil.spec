Summary:	lbxutil library
Summary(pl):	Biblioteka lbxutil
Name:		xorg-lib-liblbxutil
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/liblbxutil-%{version}.tar.bz2
# Source0-md5:	c5363c38765d82fa02bcd261c36c6152
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lbxutil library.

%description -l pl
Biblioteka lbxutil.

%package devel
Summary:	Header files for liblbxutil library
Summary(pl):	Pliki nag³ówkowe biblioteki liblbxutil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xextproto-devel
Requires:	zlib-devel

%description devel
lbxutil library.

This package contains the header files needed to develop programs that
use liblbxutil.

%description devel -l pl
Biblioteka lbxutil.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki liblbxutil.

%package static
Summary:	Static liblbxutil library
Summary(pl):	Biblioteka statyczna liblbxutil
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
lbxutil library.

This package contains the static liblbxutil library.

%description static -l pl
Biblioteka lbxutil.

Pakiet zawiera statyczna bibliotekê liblbxutil.

%prep
%setup -q -n liblbxutil-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/liblbxutil.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblbxutil.so
%{_libdir}/liblbxutil.la
%{_pkgconfigdir}/lbxutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblbxutil.a
