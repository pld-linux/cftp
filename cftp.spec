Summary:	Fullscreen ftp client
Summary(pl):	Pe³noekranowy klient ftp
Name:		cftp
Version:	0.10
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://ftp.giga.or.at/pub/nih/cftp/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_libnsl.patch
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
CFTP is used to transfer files from one computer to another via the
FTP protocol.  It's advantages over most standard ftp clients is its
fullscreen representation of the remote directory tree, providing a
compact overview of the remote server's contents.

%description -l pl
CFTP jest u¿ywany do przesy³ania plików z jednego komputera na inny poprzez
protokó³ FTP. Jego zalety ponad innymi klientami ftp to pe³noekranowa
reprezentacja drzewa katalogów zdalnego komputera, wsparcie dla IPv6 i inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS THANKS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
%fix_info_dir

%postun
%fix_info_dir

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
