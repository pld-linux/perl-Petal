#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pnam	Petal
Summary:	Petal - Perl Template Attribute Language - TAL for Perl!
Summary(pl.UTF-8):	Petal - Perl Template Attribute Language - TAL dla Perla!
Name:		perl-Petal
Version:	2.19
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BP/BPOSTLE/%{pnam}-%{version}.tar.gz
# Source0-md5:	5be2cd6bba2be5d61aa82be5849e4a09
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

%description -l pl.UTF-8
Petal to silnik szablonów oparty na XML-u, potrafiący przetwarzać
dowolny rodzaj XML-a, XHTML-a i HTML-a.

Petal zapożycza wiele dobrych pomysłów ze specyfikacji TAL Zope Page
Templates i jest bardzo dobrze dopasowany do tworzenia modyfikowalnych
szablonów WYSIWYG XHTML.

Ideą jest dalsze wymuszenie oddzielenia logiki od prezentacji. Przy
użyciu Petala projektanci grafiki mogą używać swojego ulubionego
edytora WYSIWYG do łatwego modyfikowania szablonów bez potrzeby
martwienia się o pętle i warunki ukryte za sceną.

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
%{perl_vendorlib}/Petal/*.pm
%dir %{perl_vendorlib}/Petal/Cache
%{perl_vendorlib}/Petal/Cache/*.pm
%dir %{perl_vendorlib}/Petal/Canonicalizer
%{perl_vendorlib}/Petal/Canonicalizer/*.pm
%dir %{perl_vendorlib}/Petal/Hash
%{perl_vendorlib}/Petal/Hash/*.pm
%dir %{perl_vendorlib}/Petal/TranslationService
%{perl_vendorlib}/Petal/TranslationService/*.pm
%{_mandir}/man3/*
