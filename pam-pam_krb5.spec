#
# Conditional build:
%bcond_with	mit	# build with Kerberos V5 from MIT
%bcond_with	parser	# build with krb5.conf parser
#
%define		ver	1.3-rc7
%define 	modulename pam_krb5
Summary:	Kerberos V5 Pluggable Authentication Module
Summary(pl):	Modu³ PAM do uwierzytelniania z u¿yciem Kerberos V5
Name:		pam-%{modulename}
Version:	%(echo %{ver} | tr -d - )
Release:	1
Epoch:		1
Vendor:		Balazs Gal <balsa@rit.bme.hu>
License:	LGPL
Group:		Base
Source0:	http://dl.sourceforge.net/pam-krb5/%{modulename}-%{ver}.tar.gz
# Source0-md5:	2c7c8974604e5c325bb2e62d0066cdce
Patch0:		%{name}-paths.patch
%{?with_parser:BuildRequires:	byacc}
%{?with_parser:BuildRequires:	flex}
%{!?with_mit:BuildRequires:	heimdal-devel}
%{?with_mit:BuildRequires:	krb5-devel >= 1.3.1-0.1}
BuildRequires:	pam-devel
Obsoletes:	pam_krb5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
This is pam_krb5, a pluggable authentication module that can be used
with Linux-PAM and Kerberos V5. This module supports password checking,
ticket creation, and optional TGT verification and conversion to
Kerberos IV tickets if Kerberos V5 was built with support for Kerberos
IV.

%description -l pl
To jest pam_krb5, wymienny modu³ uwierzytelniania, który mo¿e byæ
u¿yty z Linux-PAM i Kerberos V5. Modu³ ten wspiera zmienianie hase³,
tworzenie biletów oraz opcjonaln± weryfikacjê i konwersjê TGT do
biletów Kerberos IV, w przypadku gdy Kerberos V5 zosta³ zbudowany
ze wsparciem dla Kerberos IV.

%prep
%setup -q -n %{modulename}-%{ver}
%{!?with_mit:%patch0 -p1}

%build
%configure \
	--with-krb5=%{_prefix} \
	%{?with_parser:--enable-confparser} \
	--enable-default-ccache-dir=/tmp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f pam.d/Makefile*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.heimdal ChangeLog ChangeLog.orig pam.d
%attr(755,root,root) %{_libdir}/security/pam_krb5.so

%{_mandir}/man5/*
%{_mandir}/man8/*
