Summary:	Sphinx extension to link to external Doxygen API documentation
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z Doxygena
Name:		python-sphinxcontrib-doxylink
Version:	1.3
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/s/sphinxcontrib-doxylink/sphinxcontrib-doxylink-%{version}.tar.gz
# Source0-md5:	f6800726c2d31bcd6b4a65d40852881f
URL:		http://packages.python.org/sphinxcontrib-doxylink/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-Sphinx >= 0.6
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to link to external Doxygen API documentation.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z
Doxygena.

%prep
%setup -q -n sphinxcontrib-doxylink-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/doxylink
%{py_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*-nspkg.pth
