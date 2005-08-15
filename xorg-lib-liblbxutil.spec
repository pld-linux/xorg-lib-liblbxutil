# $Rev: 3331 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	lbxutil library
Summary(pl):	Biblioteka lbxutil
Name:		xorg-lib-liblbxutil
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/liblbxutil-%{version}.tar.bz2
# Source0-md5:	be6cb45d6341a8bfc142621606c81372
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libz-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xextproto-devel
BuildRoot:	%{tmpdir}/liblbxutil-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
lbxutil library.

%description -l pl
Biblioteka lbxutil.


%package devel
Summary:	Header files liblbxutil development
Summary(pl):	Pliki nag³ówkowe do biblioteki liblbxutil
Group:		X11/Development/Libraries
Requires:	xorg-lib-liblbxutil = %{version}-%{release}
Requires:	libz-devel
Requires:	xorg-proto-xextproto-devel

%description devel
lbxutil library.

This package contains the header files needed to develop programs that
use these liblbxutil.

%description devel -l pl
Biblioteka lbxutil.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki liblbxutil.


%package static
Summary:	Static liblbxutil libraries
Summary(pl):	Biblioteki statyczne liblbxutil
Group:		Development/Libraries
Requires:	xorg-lib-liblbxutil-devel = %{version}-%{release}

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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/liblbxutil.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/liblbxutil.la
%attr(755,root,wheel) %{_libdir}/liblbxutil.so
%{_pkgconfigdir}/lbxutil.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/liblbxutil.a
