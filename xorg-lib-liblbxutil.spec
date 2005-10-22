Summary:	lbxutil library
Summary(pl):	Biblioteka lbxutil
Name:		xorg-lib-liblbxutil
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/liblbxutil-%{version}.tar.bz2
# Source0-md5:	4adf922ead2e6c9d8c53b77e28fc5f7c
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
Summary:	Header files liblbxutil development
Summary(pl):	Pliki nag³ówkowe do biblioteki liblbxutil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xextproto-devel
Requires:	zlib-devel

%description devel
lbxutil library.

This package contains the header files needed to develop programs that
use these liblbxutil.

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
