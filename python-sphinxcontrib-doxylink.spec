#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
#
Summary:	Sphinx extension to link to external Doxygen API documentation
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z Doxygena
Name:		python-sphinxcontrib-doxylink
Version:	1.3
Release:	5
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/s/sphinxcontrib-doxylink/sphinxcontrib-doxylink-%{version}.tar.gz
# Source0-md5:	f6800726c2d31bcd6b4a65d40852881f
URL:		http://packages.python.org/sphinxcontrib-doxylink/
%if %{with python2}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-Sphinx >= 0.6
Requires:	python-pyparsing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx extension to link to external Doxygen API documentation.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z
Doxygena.

%package -n python3-sphinxcontrib-doxylink
Summary:	Sphinx extension to link to external Doxygen API documentation
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z Doxygena
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-Sphinx >= 0.6
Requires:	python3-pyparsing

%description -n python3-sphinxcontrib-doxylink
Sphinx extension to link to external Doxygen API documentation.

%description -n python3-sphinxcontrib-doxylink -l pl.UTF-8
Rozszerzenie Sphinksa do łączenia z zewnętrzną dokumentacją API z
Doxygena.

%prep
%setup -q -n sphinxcontrib-doxylink-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python2}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/tests
%endif

%if %{with python2}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py_sitescriptdir}/sphinxcontrib
%{py_sitescriptdir}/sphinxcontrib/doxylink
%{py_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-doxylink
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%dir %{py3_sitescriptdir}/sphinxcontrib
%{py3_sitescriptdir}/sphinxcontrib/doxylink
%{py3_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_doxylink-%{version}-py*-nspkg.pth
%endif
