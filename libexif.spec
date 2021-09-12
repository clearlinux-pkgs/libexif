#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libexif
Version  : 0.6.23
Release  : 12
URL      : https://github.com/libexif/libexif/archive/libexif-0_6_23-release/libexif-0.6.23.tar.gz
Source0  : https://github.com/libexif/libexif/archive/libexif-0_6_23-release/libexif-0.6.23.tar.gz
Summary  : Library for easy access to EXIF data
Group    : Development/Tools
License  : LGPL-2.1
Requires: libexif-lib = %{version}-%{release}
Requires: libexif-license = %{version}-%{release}
Requires: libexif-locales = %{version}-%{release}

%description
libexif
-------
DESCRIPTION
-----------
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace lots of redundant implementations in command-line
utilities and programs with GUIs.

%package dev
Summary: dev components for the libexif package.
Group: Development
Requires: libexif-lib = %{version}-%{release}
Provides: libexif-devel = %{version}-%{release}
Requires: libexif = %{version}-%{release}

%description dev
dev components for the libexif package.


%package doc
Summary: doc components for the libexif package.
Group: Documentation

%description doc
doc components for the libexif package.


%package lib
Summary: lib components for the libexif package.
Group: Libraries
Requires: libexif-license = %{version}-%{release}

%description lib
lib components for the libexif package.


%package license
Summary: license components for the libexif package.
Group: Default

%description license
license components for the libexif package.


%package locales
Summary: locales components for the libexif package.
Group: Default

%description locales
locales components for the libexif package.


%prep
%setup -q -n libexif-libexif-0_6_23-release
cd %{_builddir}/libexif-libexif-0_6_23-release

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631474996
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1631474996
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libexif
cp %{_builddir}/libexif-libexif-0_6_23-release/COPYING %{buildroot}/usr/share/package-licenses/libexif/4df5d4b947cf4e63e675729dd3f168ba844483c7
%make_install
%find_lang libexif-12

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libexif/_stdint.h
/usr/include/libexif/exif-byte-order.h
/usr/include/libexif/exif-content.h
/usr/include/libexif/exif-data-type.h
/usr/include/libexif/exif-data.h
/usr/include/libexif/exif-entry.h
/usr/include/libexif/exif-format.h
/usr/include/libexif/exif-ifd.h
/usr/include/libexif/exif-loader.h
/usr/include/libexif/exif-log.h
/usr/include/libexif/exif-mem.h
/usr/include/libexif/exif-mnote-data.h
/usr/include/libexif/exif-tag.h
/usr/include/libexif/exif-utils.h
/usr/lib64/libexif.so
/usr/lib64/pkgconfig/libexif.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libexif/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexif.so.12
/usr/lib64/libexif.so.12.3.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libexif/4df5d4b947cf4e63e675729dd3f168ba844483c7

%files locales -f libexif-12.lang
%defattr(-,root,root,-)

