Summary:	Multi-target portable assembler
Summary(pl):	Przeno¶ny asembler dla wielu rodzin procesorów
Name:		asl
Version:	1.41r8
Release:	3
License:	GPL-like (but not GPL)
Group:		Development/Languages
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.gz
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

#cp -f doc_EN/as.doc as-en.doc
#cp -f doc_DE/as.doc as-de.doc
#gzip -9nf README as-en.doc as-de.doc
install doc_EN/as.doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/as-en.doc
install doc_DE/as.doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/as-de.doc
install README $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README.gz
#%doc as-en.doc.gz
#%lang(de) %doc as-de.doc.gz
%docdir %{_docdir}/%{name}-%{version}
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/README*
%{_docdir}/%{name}-%{version}/as-en.doc*
%lang(de) %{_docdir}/%{name}-%{version}/as-de.doc*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_includedir}/asl
%{_libdir}/asl
