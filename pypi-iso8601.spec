#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-iso8601
Version  : 1.0.2
Release  : 73
URL      : https://files.pythonhosted.org/packages/28/97/d2d3d96952c77e7593e0f4a634656fb384f7282327f7fef74b726b3b4c1c/iso8601-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/28/97/d2d3d96952c77e7593e0f4a634656fb384f7282327f7fef74b726b3b4c1c/iso8601-1.0.2.tar.gz
Summary  : Simple module to parse ISO 8601 dates
Group    : Development/Tools
License  : MIT
Requires: pypi-iso8601-license = %{version}-%{release}
Requires: pypi-iso8601-python = %{version}-%{release}
Requires: pypi-iso8601-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
BuildRequires : pypi-py
BuildRequires : pypi-pytest

%description
Simple module to parse ISO 8601 dates
This module parses the most common forms of ISO 8601 date strings (e.g. 2007-01-14T20:34:22+00:00) into datetime objects.

%package license
Summary: license components for the pypi-iso8601 package.
Group: Default

%description license
license components for the pypi-iso8601 package.


%package python
Summary: python components for the pypi-iso8601 package.
Group: Default
Requires: pypi-iso8601-python3 = %{version}-%{release}

%description python
python components for the pypi-iso8601 package.


%package python3
Summary: python3 components for the pypi-iso8601 package.
Group: Default
Requires: python3-core
Provides: pypi(iso8601)

%description python3
python3 components for the pypi-iso8601 package.


%prep
%setup -q -n iso8601-1.0.2
cd %{_builddir}/iso8601-1.0.2
pushd ..
cp -a iso8601-1.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656399199
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-iso8601
cp %{_builddir}/iso8601-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-iso8601/604d3444602058d69df81bd0c30c6944517360db
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-iso8601/604d3444602058d69df81bd0c30c6944517360db

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
