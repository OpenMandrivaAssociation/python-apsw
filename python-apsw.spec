%define module	apsw
# Keep OMIT_* flags in sync with sqlite
%global optflags %{optflags} -DSQLITE_OMIT_SHARED_CACHE

Name:		python-%{module}
Version:	3.51.2.0
Release:	1
Summary:	Another Python SQLite Wrapper
URL:		https://pypi.org/project/apsw
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch0:		apsw-3.43.0.0-fix-sqlite-with-omitted-misfeatures.patch
Group:		Development/Python
License:	any-OSI
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	pkgconfig(sqlite3) 
BuildRequires:	pkgconfig(python3)

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep -a
# Don't download a custom sqlite
sed -i -e 's,^fetch = True,fetch = False,' setup.apsw
# And allow building the ICU extension
sed -i -e 's,^omit =,# omit =,' setup.apsw

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{_bindir}/apsw
%{py_platsitedir}/%{module}
%{py_platsitedir}/%{module}-%{version}.dist-info
