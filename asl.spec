Summary:	Multi-target portable assembler
Name:		asl
Version:	1.41r8
Release:	1
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Source0:	ftp://sunsite.unc.edu/pub/Linux/lang/assemblers/%{name}-%{version}.tar.gz
Source1:	%{name}-Makefile.def
License:	GPL-like (but not GPL)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips

%description
A general purpose multi-target macro assembler with supporting tools.
This assembler supports many targets including some PIC's and DSP's.

%prep
%setup -q
install %{SOURCE1} Makefile.def

%build
%ifarch alpha axp
ARCH=__alpha
%endif

%ifarch %ix86
ARCH=__i386
%endif

%ifarch sparc
ARCH=__sparc
%endif

%ifarch 68k
ARCH=__68k
%endif

%{__make} all docs ARCH=$ARCH \
	OPTFLAGS="%{?debug:-g -O}%{!?debug:$RPM_OPT_FLAGS -fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
# asl's make install requires mkdirhier (from XFree) and always strips binaries
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name},%{_mandir}/man1,%{_libdir}/asl}
install asl pbind plist p2bin p2hex $RPM_BUILD_ROOT%{_bindir}
install asl.1 pbind.1 plist.1 p2bin.1 p2hex.1 $RPM_BUILD_ROOT%{_mandir}/man1
install include/* $RPM_BUILD_ROOT%{_includedir}/%{name}

for i in *.msg ; do
  install $i $RPM_BUILD_ROOT%{_libdir}/asl
done

#cp -f doc_EN/as.doc as-en.doc
#cp -f doc_DE/as.doc as-de.doc
#gzip -9nf README as-en.doc as-de.doc
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install doc_EN/as.doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/as-en.doc
install doc_DE/as.doc $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/as-de.doc
install README $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
gzip -9nf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/*

%files
%defattr(644,root,root,755)
#%doc README.gz
#%lang(en) %doc as-en.doc.gz
#%lang(de) %doc as-de.doc.gz
%docdir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/README*
%lang(en) %{_docdir}/%{name}-%{version}/as-en.doc*
%lang(de) %{_docdir}/%{name}-%{version}/as-de.doc*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_includedir}/asl
%{_libdir}/asl

%clean
rm -rf $RPM_BUILD_ROOT
