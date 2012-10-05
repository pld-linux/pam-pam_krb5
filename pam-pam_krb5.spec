%define 	modulename pam_krb5
Summary:	Kerberos V5 Pluggable Authentication Module
Summary(pl.UTF-8):	Moduł PAM do uwierzytelniania z użyciem Kerberos V5
Name:		pam-%{modulename}
Version:	4.6
Release:	1
Epoch:		1
License:	BSD v2 / GPL v2
Group:		Base
URL:		http://www.eyrie.org/~eagle/software/pam-krb5/
Source0:	http://archives.eyrie.org/software/kerberos/pam-krb5-%{version}.tar.gz
# Source0-md5:	296e9c8281419ce1fc41d537d18f74b8
BuildRequires:	automake
BuildRequires:	heimdal-devel
BuildRequires:	pam-devel
Obsoletes:	pam_krb5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
This is pam_krb5, a pluggable authentication module that can be used
with Linux-PAM and Kerberos V5. This module supports password
checking, ticket creation, and optional TGT verification and
conversion to Kerberos IV tickets if Kerberos V5 was built with
support for Kerberos IV.

%description -l pl.UTF-8
To jest pam_krb5, wymienny moduł uwierzytelniania, który może być
użyty z Linux-PAM i Kerberos V5. Moduł ten wspiera zmienianie haseł,
tworzenie biletów oraz opcjonalną weryfikację i konwersję TGT do
biletów Kerberos IV, w przypadku gdy Kerberos V5 został zbudowany ze
wsparciem dla Kerberos IV.

%prep
%setup -q -n pam-krb5-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_libdir}/security/pam_krb5.so
%{_mandir}/man5/pam_krb5.5*
