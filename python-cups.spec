Summary:	Python bindings for CUPS
Name:		python-cups
Version:	1.9.60
Release:	1
URL:		http://cyberelk.net/tim/software/pycups/
Source0:	http://cyberelk.net/tim/data/pycups/pycups-%{version}.tar.bz2
# Source0-md5:	083f3dd657df986e712a6fae36427457
License:	GPL v2+
Group:		Development/Languages/Python
BuildRequires:	cups-devel
BuildRequires:	epydoc
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Python bindings for the CUPS API, known as
pycups. It was written for use with system-config-printer, but can be
put to other uses as well.

%package doc
Summary:	Documentation for python-cups
Group:		Documentation

%description doc
Documentation for python-cups.

%prep
%setup -q -n pycups-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fno-strict-aliasing"
%{__make} doc

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README NEWS TODO
%attr(755,root,root) %{py_sitedir}/cups.so
%{py_sitedir}/pycups*.egg-info

%files doc
%defattr(644,root,root,755)
%doc examples html
