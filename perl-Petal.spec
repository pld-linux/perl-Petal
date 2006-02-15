#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
#%define		pdir	-
%define		pnam	Petal
Summary:	Petal - Perl Template Attribute Language - TAL for Perl!
Summary(pl):	Petal - Perl Template Attribute Language - TAL dla Perla!
Name:		perl-Petal
Version:	2.18
Release:	0.1
# note if it is "same as perl"
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BP/BPOSTLE/%{pnam}-%{version}.tar.gz
#Patch0:		%{name}
URL:		http://search.cpan.org/~bpostle/Petal-2.18/lib/Petal.pm
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
#BuildRequires:	-
%if %{with tests}
BuildRequires:	perl
BuildRequires:	perl
%endif
#Requires:	-
#Provides:	-
#Obsoletes:	-
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
Petal is a XML based templating engine that is able to process any kind 
of XML, XHTML and HTML.

Petal borrows a lot of good ideas from the Zope Page Templates TAL 
specification, it is very well suited for the creation of WYSIWYG 
XHTML editable templates.

The idea is to further enforce the separation of logic from presentation. 
With Petal, graphic designers can use their favorite WYSIWYG editor 
to easily edit templates without having to worry about the loops 
and ifs which happen behind the scene.

%prep
%setup -q -n %{pnam}-%{version}
#%patch0 -p1

%build
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
# note it's mostly easier to copy unpackaged filelist here, and run adapter over the spec.
# use macros:
#%%{perl_vendorlib}/...
#%%{perl_vendorarch}/...
#%%{perl_vendorlib}/
%{perl_vendorarch}/auto/Petal/.packlist
%{perl_vendorlib}/Petal.pm
%{perl_vendorlib}/Petal/Cache/Disk.pm
%{perl_vendorlib}/Petal/Cache/Memory.pm
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
%{perl_vendorlib}/Petal/TranslationService/Gettext.pm
%{perl_vendorlib}/Petal/TranslationService/MOFile.pm
%{perl_vendorlib}/Petal/TranslationService/Noop.pm
%{perl_vendorlib}/Petal/TranslationService/h4x0r.pm
%{_mandir}/man3/*
