%define sqlite_version 3.7.17
%define uprel 1
%define pkg_version %{sqlite_version}-r%{uprel}

%define __noautoprov 'apsw.so'

Name:           python-apsw
Version:        3.7.17.r1
Release:        1
Summary:        Another Python SQLite Wrapper
Source0:        http://apsw.googlecode.com/files/apsw-3.7.17-r1.zip
URL:            http://code.google.com/p/apsw/
Group:          Development/Python
License:        zlib/libpng License
BuildRequires:  sqlite3-devel >= %{sqlite_version}
BuildRequires:  python-devel

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%package doc
Summary:        Another Python SQLite Wrapper - Documentation
Group:          Development/Python
License:        zlib/libpng License
BuildArch:      noarch

%description doc
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%setup -q -n "apsw-%{pkg_version}"

%build
CFLAGS="%{optflags} -fno-strict-aliasing" \
%__python ./setup.py build

%install
%__python ./setup.py install \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"

%__rm doc/.buildinfo

%files
%{py_platsitedir}/*

%files doc
%doc doc/*
