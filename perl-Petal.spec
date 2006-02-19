#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Petal
Summary:	Petal - Perl Template Attribute Language - TAL for Perl!
Summary(pl):	Petal - Perl Template Attribute Language - TAL dla Perla!
Name:		perl-Petal
Version:	2.18
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BP/BPOSTLE/%{pnam}-%{version}.tar.gz
# Source0-md5:	40fc181e53122705570102695ae9240c
URL:		http://search.cpan.org/~bpostle/Petal-2.18/lib/Petal.pm
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Lingua-31337
BuildRequires:	perl-MKDoc-XML
BuildRequires:	perl-Locale-Maketext-Gettext
%endif
Requires:	perl-Lingua-31337
Requires:	perl-MKDoc-XML
Requires:	perl-Locale-Maketext-Gettext
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Petal is a XML based templating engine that is able to process any
kind of XML, XHTML and HTML.

Petal borrows a lot of good ideas from the Zope Page Templates TAL
specification, it is very well suited for the creation of WYSIWYG
XHTML editable templates.

The idea is to further enforce the separation of logic from
presentation. With Petal, graphic designers can use their favorite
WYSIWYG editor to easily edit templates without having to worry about
the loops and ifs which happen behind the scene.

%description -l pl
Petal to silnik szablonów oparty na XML-u, potrafi±cy przetwarzaæ
dowolny rodzaj XML-a, XHTML-a i HTML-a.

Petal zapo¿ycza wiele dobrych pomys³ów ze specyfikacji TAL Zope Page
Templates i jest bardzo dobrze dopasowany do tworzenia modyfikowalnych
szablonów WYSIWYG XHTML.

Ide± jest dalsze wymuszenie oddzielenia logiki od prezentacji. Przy
u¿yciu Petala projektanci grafiki mog± u¿ywaæ swojego ulubionego
edytora WYSIWYG do ³atwego modyfikowania szablonów bez potrzeby
martwienia siê o pêtle i warunki ukryte za scen±.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Petal.pm
%dir %{perl_vendorlib}/Petal
%dir %{perl_vendorlib}/Petal/Cache
%{perl_vendorlib}/Petal/Cache/Disk.pm
%{perl_vendorlib}/Petal/Cache/Memory.pm
%dir %{perl_vendorlib}/Petal/Canonicalizer
%{perl_vendorlib}/Petal/Canonicalizer/XHTML.pm
%{perl_vendorlib}/Petal/Canonicalizer/XML.pm
%{perl_vendorlib}/Petal/CodeGenerator.pm
%{perl_vendorlib}/Petal/Cookbook.pod
%{perl_vendorlib}/Petal/Deprecated.pm
%{perl_vendorlib}/Petal/Entities.pm
%{perl_vendorlib}/Petal/Functions.pm
%{perl_vendorlib}/Petal/Hash.pm
%{perl_vendorlib}/Petal/Hash/String.pm
%{perl_vendorlib}/Petal/Hash/Test.pm
%{perl_vendorlib}/Petal/Hash/Var.pm
%{perl_vendorlib}/Petal/I18N.pm
%{perl_vendorlib}/Petal/Parser.pm
%dir %{perl_vendorlib}/Petal/TranslationService
%{perl_vendorlib}/Petal/TranslationService/Gettext.pm
%{perl_vendorlib}/Petal/TranslationService/MOFile.pm
%{perl_vendorlib}/Petal/TranslationService/Noop.pm
%{perl_vendorlib}/Petal/TranslationService/h4x0r.pm
%{_mandir}/man3/*
