%define sqlite_version 3.34.0
%define uprel 1
%define pkg_version %{sqlite_version}-r%{uprel}

%define __noautoprov 'apsw.so'

Name:           python-apsw
Version:        %{sqlite_version}.r%{uprel}
Release:        1
Summary:        Another Python SQLite Wrapper
Source0:        https://github.com/rogerbinns/apsw/archive/%{pkg_version}.tar.gz
URL:            https://rogerbinns.github.io/apsw/
Group:          Development/Python
License:        zlib/libpng License
BuildRequires:  sqlite3-devel >= %{sqlite_version}
BuildRequires:  pkgconfig(python3)
BuildRequires:	pkgconfig(python2)

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%package -n python2-apsw
Summary:	Another Python SQLite wrapper
Group:	Development/Python

%description -n python2-apsw
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Pytho

%prep
%setup -q -n "apsw-%{pkg_version}"
cp -a . %py2dir

%build
pushd %py2dir
CFLAGS="%{optflags} -fno-strict-aliasing" \
%__python2 ./setup.py build
popd

CFLAGS="%{optflags} -fno-strict-aliasing" \
%__python ./setup.py build

%install
pushd %py2dir
%__python2 ./setup.py install \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"
popd

%__python ./setup.py install \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"

%files
%{py_platsitedir}/*

%files -n python2-apsw
%{py2_platsitedir}/*
