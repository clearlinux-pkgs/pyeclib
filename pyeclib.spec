#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyeclib
Version  : 1.5.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/e3/02/2814399e18c10f0ea6912bf7e7ce5e20c9482b4b5fae9f756c72c97cc144/pyeclib-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e3/02/2814399e18c10f0ea6912bf7e7ce5e20c9482b4b5fae9f756c72c97cc144/pyeclib-1.5.0.tar.gz
Summary  : This library provides a simple Python interface for                    implementing erasure codes.  To obtain the best possible                    performance, the underlying erasure code algorithms are                    written in C.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pyeclib-python3
Requires: pyeclib-python
BuildRequires : buildreq-distutils3
BuildRequires : liberasurecode-dev
BuildRequires : six

%description
PyEClib
-------
This library provides a simple Python interface for implementing erasure codes
and is known to work with Python v2.6, 2.7 and 3.x.

%package python
Summary: python components for the pyeclib package.
Group: Default
Requires: pyeclib-python3

%description python
python components for the pyeclib package.


%package python3
Summary: python3 components for the pyeclib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyeclib package.


%prep
%setup -q -n pyeclib-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533876325
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
