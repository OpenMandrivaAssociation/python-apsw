%define module	apsw

Name:		python-%{module}
Version:	3.46.1.0
Release:	1
Summary:	Another Python SQLite Wrapper
Source0:	https://github.com/rogerbinns/apsw/archive/refs/tags/%{version}.tar.gz
Patch0:		apsw-3.43.0.0-fix-sqlite-with-omitted-misfeatures.patch
URL:		https://rogerbinns.github.io/python-%{module}/
Group:		Development/Python
License:	zlib/libpng License
BuildRequires:	pkgconfig(sqlite3) 
BuildRequires:	pkgconfig(python3)

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%files
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-*.*-info

#----------------------------------------------------------------------------

%prep
%autosetup -n "%{module}-%{version}" -p1

%build
%py_build -- --enable-all-extensions --use-system-sqlite-config --enable=load_extension

%install
%py_install
