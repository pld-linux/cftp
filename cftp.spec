Summary:	Fullscreen FTP client
Summary(pl):	Pe³noekranowy klient FTP
Name:		cftp
Version:	0.12
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.giga.or.at/pub/nih/cftp/%{name}-%{version}.tar.gz
# Source0-md5:	e497c2cf060a6906f48ac99f55bedc8a
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_libnsl.patch
Patch2:		%{name}-AC_LIBOBJ.patch
Patch3:		%{name}-ac_better_tgetent_detection.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CFTP is used to transfer files from one computer to another via the
FTP protocol. It's advantages over most standard FTP clients is its
fullscreen representation of the remote directory tree, providing a
compact overview of the remote server's contents.

%description -l pl
CFTP jest u¿ywany do przesy³ania plików z jednego komputera na inny
poprzez protokó³ FTP. Jego zalety ponad innymi klientami FTP to
pe³noekranowa reprezentacja drzewa katalogów zdalnego komputera,
wsparcie dla IPv6 i inne.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*.info*
