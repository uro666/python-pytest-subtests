%define module pytest-subtests
%define oname pytest_subtests
# disable tests for abf
%bcond_with test

Name:		python-pytest-subtests
Version:	0.14.1
Release:	1
Summary:	unittest subTest() support and subtests fixture
URL:		https://pypi.org/project/pytest-subtests/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-subtests/%{oname}-%{version}.tar.gz
# see https://github.com/pytest-dev/pytest-subtests/issues/181
Patch0:		https://github.com/sysfce2/python-pytest-subtests/commit/aa3f96bfb5dfa45c95e0158dc2b76c29157453db.patch
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(attrs)
%if %{with test}
BuildRequires:	python%{pyver}dist(attrs)
BuildRequires:	python%{pyver}dist(iniconfig)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
unittest subTest() support and subtests fixture

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
pytest -v tests/
%endif

%files
%{py_sitedir}/%{oname}.py
%{py_sitedir}/__pycache__/%{oname}*.pyc
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
%doc README.md
