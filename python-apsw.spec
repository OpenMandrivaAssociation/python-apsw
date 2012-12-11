%define sqlite_version 3.7.13
%define uprel 1
%define pkg_version %{sqlite_version}-r%{uprel}

%if %_use_internal_dependency_generator
%define __noautoprov 'apsw.so'
%else
%define __noautoprov apsw.so
%endif

Name:           python-apsw
Version:        %{sqlite_version}.r%{uprel}
Release:        1
Summary:        Another Python SQLite Wrapper
Source0:        http://apsw.googlecode.com/files/apsw-3.7.13-r1.zip
URL:            http://code.google.com/p/apsw/
Group:          Development/Python
License:        zlib/libpng License
BuildRequires:  sqlite3-devel >= %{sqlite_version}
%py_requires -d

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
%{python_sitearch}/*

%files doc
%doc doc/*


%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.7.13.r1-1
+ Revision: 806804
- version update 3.7.13-r1

* Wed May 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.7.11.r1-1
+ Revision: 795024
- update to 3.7.11-r1

* Sat Feb 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.7.10.r1-1
+ Revision: 780712
- new version 3.7.10-r1

* Tue Nov 29 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.7.9.r1-1
+ Revision: 735354
- imported package python-apsw

