Summary:	Fullscreen ftp client
Summary(pl):	Pełnoekranowy klient ftp
Name:		cftp
Version:	0.11.2
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.giga.or.at/pub/nih/cftp/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_libnsl.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
CFTP is used to transfer files from one computer to another via the
FTP protocol. It's advantages over most standard ftp clients is its
fullscreen representation of the remote directory tree, providing a
compact overview of the remote server's contents.

%description -l pl
CFTP jest używany do przesyłania plików z jednego komputera na inny
poprzez protokół FTP. Jego zalety ponad innymi klientami ftp to
pełnoekranowa reprezentacja drzewa katalogów zdalnego komputera,
wsparcie dla IPv6 i inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
