%define module	apsw
%define sqlite_version 3.38.1
%define uprel 1
%define pkg_version %{sqlite_version}-r%{uprel}

Name:		python-%{module}
Version:	3.39.3.0
Release:	1
Summary:	Another Python SQLite Wrapper
Source0:	https://github.com/rogerbinns/apsw/archive/%{pkg_version}/apsw-%{pkg_version}.tar.gz
# (upstream)
# https://github.com/rogerbinns/apsw/commit/bea8b11f3057600082b89c17ada8ccee316cdd36
Patch0:		port-to-python3.11.patch
URL:		https://rogerbinns.github.io/python-%{module}/
Group:		Development/Python
License:	zlib/libpng License
BuildRequires:	pkgconfig(sqlite3) 
#>= %{sqlite_version}
BuildRequires:	pkgconfig(python3)
#Obsoletes:	python2-python-%{module} < 3.36.0

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%files
%{py_platsitedir}/%{module}.pyi
%{py_platsitedir}/%{module}*.so
%{py_platsitedir}/%{module}-*-py%{python_version}.egg-info

#----------------------------------------------------------------------------

%prep
%autosetup -n "%{module}-%{pkg_version}" -p1

%build
%py_build -- --enable-all-extensions --enable=load_extension

%install
%py_install

# fix path
mv %{buildroot}%{_prefix}/%{module}.pyi %{buildroot}%{python3_sitearch}

