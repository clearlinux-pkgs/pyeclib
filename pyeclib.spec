#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyeclib
Version  : 1.2.0
Release  : 6
URL      : https://bitbucket.org/kmgreen2/pyeclib/get/v1.2.0.tar.bz2
Source0  : https://bitbucket.org/kmgreen2/pyeclib/get/v1.2.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pyeclib-python
BuildRequires : liberasurecode-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
This is v1.2 of PyECLib.  This library provides a simple Python interface for
implementing erasure codes and is known to work with Python v2.6, 2.7 and 3.x.

%package python
Summary: python components for the pyeclib package.
Group: Default

%description python
python components for the pyeclib package.


%prep
%setup -q -n kmgreen2-pyeclib-19c99357839b

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
