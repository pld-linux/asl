Summary:	Multi-target portable assembler
Summary(pl):	Przeno¶ny asembler dla wielu rodzin procesorów
Name:		asl
Version:	1.41r8
Release:	4
License:	GPL-like
Group:		Development/Languages
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.gz
# Source0-md5:	f8b34f1acb48663243402b43f6070fd3
Source1:	%{name}-Makefile.def
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	alpha %{ix86} sparc m68k

%description
A general purpose multi-target macro assembler with supporting tools.
This assembler supports many targets including some PIC's and DSP's.

%description -l pl
Makroasembler ogólnego przeznaczenia wraz z narzêdziami. Potrafi
generowaæ kod dla wielu rodzin uk³adów, tak¿e dla procesorów
sygna³owych.

%prep
%setup -q
install %{SOURCE1} Makefile.def

%build
%ifarch alpha axp
ARCH=__alpha
%endif

%ifarch %{ix86}
ARCH=__i386
%endif

%ifarch sparc
ARCH=__sparc
%endif

%ifarch m68k
ARCH=__68k
%endif

%{__make} all docs ARCH=$ARCH \
	OPTFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"

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
