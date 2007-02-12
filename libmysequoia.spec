Summary:	Alternative libmysqlclient library
Summary(pl.UTF-8):   Alternatywna biblioteka libmysqlclient
Name:		libmysequoia
Version:	0.9.3
Release:	0.1
License:	Apache License 2.0
Group:		Libraries
Source0:	https://forge.continuent.org/frs/download.php/181/%{name}-%{version}.tar.gz
# Source0-md5:	633a929e994e55e08ab865060e42259a
URL:		http://carob.continuent.org/LibMySequoia
BuildRequires:	autoconf
BuildRequires:	carob-devel
BuildRequires:	libstdc++-devel
BuildRequires:	log4cxx-devel
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reimplementation of libmysqlclient library, using Carob to benefit
from clustering. So, native MySQL client programs can use the Sequoia
clustering solution without changing any line of code in the
application.

%description -l pl.UTF-8
Reimplementacja biblioteki libmysqlclient z użyciem Caroba dla zysków
z klastrowania. W ten sposób natywne programy klienckie MySQL-a mogą
używać rozwiązania klastrowego Sequoia bez zmiany ani jednej linii
kodu w aplikacji.

# XXX: where are "header files"???
%package devel
Summary:	Header files for libmysequoia library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libmysequoia
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libmysequoia
library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libmysequoia.

%package static
Summary:	Static libmysequoia library
Summary(pl.UTF-8):   Statyczna biblioteka libmysequoia
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmysequoia library.

%description static -l pl.UTF-8
Statyczna biblioteka libmysequoia.

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libmysequoia.so.*.*.*
%{_sysconfdir}/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmysequoia.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libmysequoia.a
