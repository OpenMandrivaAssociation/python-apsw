%define sqlite_version 3.38.1
%define uprel 1
%define pkg_version %{sqlite_version}-r%{uprel}

Name:		python-apsw
Version:	%{sqlite_version}.r%{uprel}
Release:	1
Summary:	Another Python SQLite Wrapper
Source0:	https://github.com/rogerbinns/apsw/archive/%{pkg_version}/apsw-%{pkg_version}.tar.gz
URL:		https://rogerbinns.github.io/apsw/
Group:		Development/Python
License:	zlib/libpng License
BuildRequires:	pkgconfig(sqlite3) >= %{sqlite_version}
BuildRequires:	pkgconfig(python3)
Obsoletes:	python2-apsw < 3.36.0

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%autosetup -n "apsw-%{pkg_version}" -p1

%build
CFLAGS="%{optflags} -fno-strict-aliasing" \
python setup.py build --enable-all-extensions --enable=load_extension

%install
%py3_install

%files
%{py_platsitedir}/*
