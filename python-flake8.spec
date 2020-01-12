# Created by pyp2rpm-1.0.1
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        3.7.9
Release:        1
Group:          Development/Python
Summary:        The modular source code checker: pep8, pyflakes and co
License:        MIT
URL:            https://pypi.python.org/pypi/flake8
Source0:        http://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python-nose
BuildRequires:  python-mccabe

%description
Flake8 is a wrapper around these tools:
- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching
the single ``flake8`` script.
It displays the warnings in a per-file, merged
output.

%prep
%setup -q -n %{pypi_name}-%{version}

# remove bundled egg-info
rm -rf flake8.egg-info
sed -i -e "/setup_requires=\['pytest-runner'\],/d" setup.py

%build
%py3_build

%install
%py3_install

%files
%doc LICENSE
%{_bindir}/flake8
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelib}/%{pypi_name}/
