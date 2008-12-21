Summary:	Multi-target portable assembler
Summary(pl.UTF-8):	Przenośny asembler dla wielu rodzin procesorów
Name:		asl
Version:	1.41r8
Release:	8
License:	GPL-like
Group:		Development/Languages
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.gz
# Source0-md5:	f8b34f1acb48663243402b43f6070fd3
Source1:	%{name}-Makefile.def
Patch0:		%{name}-morearchs.patch
URL:		http://john.ccac.rwth-aachen.de:8000/as/index.html
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-latex
BuildRequires:	tetex-makeindex
BuildRequires:	tetex-tex-german
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A general purpose multi-target macro assembler with supporting tools.
This assembler supports many targets including some PIC's and DSP's.

%description -l pl.UTF-8
Makroasembler ogólnego przeznaczenia wraz z narzędziami. Potrafi
generować kod dla wielu rodzin układów, także dla procesorów
sygnałowych.

%prep
%setup -q
%patch0 -p1

install %{SOURCE1} Makefile.def

%build
%{__make} all docs \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} -Wall" \
	LIBDIR="%{_libdir}/asl"

%install
rm -rf $RPM_BUILD_ROOT
# asl's make install requires mkdirhier (from XFree) and always strips binaries
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name},%{_mandir}/man1,%{_libdir}/asl} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install asl pbind plist p2bin p2hex $RPM_BUILD_ROOT%{_bindir}
install asl.1 pbind.1 plist.1 p2bin.1 p2hex.1 $RPM_BUILD_ROOT%{_mandir}/man1
install include/* $RPM_BUILD_ROOT%{_includedir}/%{name}

install *.msg $RPM_BUILD_ROOT%{_libdir}/asl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc_EN/as.doc
%lang(de) %doc doc_DE/as.doc
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_includedir}/asl
%{_libdir}/asl
