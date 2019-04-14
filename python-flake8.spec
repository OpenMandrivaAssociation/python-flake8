# Created by pyp2rpm-1.0.1
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        3.7.7
Release:        1
Group:          Development/Python
Summary:        The modular source code checker: pep8, pyflakes and co
License:        MIT
URL:            https://pypi.python.org/pypi/flake8
Source0:        http://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Flake8 is a wrapper around these tools:
- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching
the single ``flake8`` script.
It displays the warnings in a per-file, merged
output.

%package -n python2-%{pypi_name}
Group:          Development/Python
Summary:        the modular source code checker: pep8, pyflakes and co
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2-nose
BuildRequires:  python2-mccabe
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Flake8 is a wrapper around these tools:
- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching
the single ``flake8`` script.
It displays the warnings in a per-file, merged
output.

This is version of the package running with Python 2.

%prep
%setup -q -n %{pypi_name}-%{version}

# remove bundled egg-info
rm -rf flake8.egg-info
sed -i -e "/setup_requires=\['pytest-runner'\],/d" setup.py

%build
%py2_build
%py3_build

%install
%py2_install
mv %{buildroot}%{_bindir}/flake8 %{buildroot}%{_bindir}/python2-flake8

%py3_install

%files -n python2-%{pypi_name}
%doc LICENSE
%{_bindir}/python2-flake8
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitelib}/%{pypi_name}/

%files -n python-%{pypi_name}
%doc LICENSE
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{pypi_name}/
