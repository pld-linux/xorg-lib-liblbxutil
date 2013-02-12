Summary:	lbxutil library - Low Bandwidth X extension (LBX) utility routines
Summary(pl.UTF-8):	Biblioteka lbxutil z funkcjami rozszerzenia LBX (Low Bandwidth X)
Name:		xorg-lib-liblbxutil
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/liblbxutil-%{version}.tar.bz2
# Source0-md5:	273329a78c2e9ea189ac416c7fde94a1
Patch0:		%{name}-am.patch
Patch1:		%{name}-xorg.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lbxutil library contains Low Bandwidth X extension (LBX) utility
routines.

%description -l pl.UTF-8
Biblioteka lbxutil zawiera funkcje narzędziowe rozszerzenia LBX (Low
Bandwidth X - X o niskim wykorzystaniu pasma).

%package devel
Summary:	Header files for liblbxutil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblbxutil
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-xextproto-devel >= 7.0.99.1
Requires:	zlib-devel
Conflicts:	xorg-lib-libXext-devel < 1.1.1-3

%description devel
lbxutil library contains Low Bandwidth X extension (LBX) utility
routines.

This package contains the header files needed to develop programs that
use liblbxutil.

%description devel -l pl.UTF-8
Biblioteka lbxutil zawiera funkcje narzędziowe rozszerzenia LBX (Low
Bandwidth X - X o niskim wykorzystaniu pasma).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki liblbxutil.

%package static
Summary:	Static liblbxutil library
Summary(pl.UTF-8):	Biblioteka statyczna liblbxutil
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static liblbxutil library.

%description static -l pl.UTF-8
Pakiet zawiera statyczna bibliotekę liblbxutil.

%prep
%setup -q -n liblbxutil-%{version}
%patch0 -p1
%patch1 -p1

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/liblbxutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblbxutil.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblbxutil.so
%{_libdir}/liblbxutil.la
%{_includedir}/X11/extensions/lbx*.h
%{_pkgconfigdir}/lbxutil.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblbxutil.a
