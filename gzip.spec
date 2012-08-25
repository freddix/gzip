Summary:	GNU gzip file compression
Name:		gzip
Version:	1.5
Release:	3
License:	GPL
Group:		Applications/Archiving
Source0:	http://ftp.gnu.org/gnu/gzip/%{name}-%{version}.tar.gz
# Source0-md5:	11b76536941ee1c0221fe6eefbcb32cb
Patch0:		%{name}-mktemp.patch
Patch1:		%{name}-stderr.patch
Patch2:		%{name}-noppid.patch
URL:		http://www.gnu.org/software/gzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
Requires:	coreutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the popular GNU file compression and decompression program,
gzip.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/pt/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/gzip.info*

