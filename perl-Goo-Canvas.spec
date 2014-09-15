#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Goo
%define		pnam	Canvas
%include	/usr/lib/rpm/macros.perl
Summary:	Goo::Canvas - Perl interface to the GooCanvas
Name:		perl-Goo-Canvas
Version:	0.06
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YE/YEWENBIN/Goo-Canvas-%{version}.tar.gz
# Source0-md5:	7dfe0be8c17bfd641d18384d4fd8fb23
URL:		http://search.cpan.org/dist/Goo-Canvas/
BuildRequires:	goocanvas-devel >= 0.9
BuildRequires:	perl(ExtUtils::Depends) >= 0.2
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.0
BuildRequires:	perl-Cairo >= 1.00
BuildRequires:	perl-Glib >= 1.103
BuildRequires:	perl-Gtk2-devel >= 1.100
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ does't has an buildin canvas widget. GooCanvas is wonderful. It
is easy to use and has powerful and extensible way to create items in
canvas. Just try it.

For more documents, please read GooCanvas Manual and the demo programs
provided in the source distribution in both perl-Goo::Canvas and
GooCanvas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%dir %{perl_vendorarch}/Goo
%{perl_vendorarch}/Goo/*.pm
%dir %{perl_vendorarch}/auto/Goo
%dir %{perl_vendorarch}/auto/Goo/Canvas
%attr(755,root,root) %{perl_vendorarch}/auto/Goo/Canvas/*.so
%{_mandir}/man3/*
