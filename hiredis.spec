%undefine _missing_build_ids_terminate_build
Summary: hiredis
Name: hiredis
Version: 1.0.0
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://github.com/antirez/hiredis
Source0: https://github.com/redis/hiredis/archive/refs/tags/v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make
Provides: hiredis

%description
Minimalistic C client for Redis 

%prep
%autosetup -p1 -n %{name}-%{version}/

%build
mkdir -p %{buildroot}%{_prefix} 
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}
make all

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}
%{__install} -Dp -m 0755 libhiredis.so %{buildroot}%{_libdir}/libhiredis.so
%{__install} -Dp -m 0755 hiredis.h %{buildroot}%{_includedir}/hiredis/hiredis.h
%{__install} -Dp -m 0755 sds.h %{buildroot}%{_includedir}/hiredis/sds.h
%{__install} -Dp -m 0755 read.h %{buildroot}%{_includedir}/hiredis/read.h
%{__install} -Dp -m 0755 async.h %{buildroot}%{_includedir}/hiredis/async.h
%{__install} -Dp -m 0755 alloc.h %{buildroot}%{_includedir}/hiredis/alloc.h
%{__install} -Dp -m 0755 adapters/ae.h %{buildroot}%{_includedir}/hiredis/adapters/ae.h
%{__install} -Dp -m 0755 adapters/qt.h %{buildroot}%{_includedir}/hiredis/adapters/qt.h
%{__install} -Dp -m 0755 adapters/glib.h %{buildroot}%{_includedir}/hiredis/adapters/glib.h
%{__install} -Dp -m 0755 adapters/libuv.h %{buildroot}%{_includedir}/hiredis/adapters/libuv.h
%{__install} -Dp -m 0755 adapters/libev.h %{buildroot}%{_includedir}/hiredis/adapters/libev.h
%{__install} -Dp -m 0755 adapters/macosx.h %{buildroot}%{_includedir}/hiredis/adapters/macosx.h
%{__install} -Dp -m 0755 adapters/ivykis.h %{buildroot}%{_includedir}/hiredis/adapters/ivykis.h
%{__install} -Dp -m 0755 adapters/libevent.h %{buildroot}%{_includedir}/hiredis/adapters/libevent.h

mkdir -p %{buildroot}%{_libdir}/pkgconfig
%{__install} -Dp -m 0755 hiredis.pc %{buildroot}%{_libdir}/pkgconfig/hiredis.pc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/libhiredis.so
%{_includedir}/hiredis/hiredis.h
%{_includedir}/hiredis/sds.h
%{_includedir}/hiredis/alloc.h
%{_includedir}/hiredis/async.h
%{_includedir}/hiredis/read.h
%{_includedir}/hiredis/adapters/ae.h
%{_includedir}/hiredis/adapters/qt.h
%{_includedir}/hiredis/adapters/glib.h
%{_includedir}/hiredis/adapters/libuv.h
%{_includedir}/hiredis/adapters/libev.h
%{_includedir}/hiredis/adapters/macosx.h
%{_includedir}/hiredis/adapters/ivykis.h
%{_includedir}/hiredis/adapters/libevent.h
%{_libdir}/pkgconfig/hiredis.pc

%changelog
* Wed Aug 18 2021 yongxu <yongxu@qiyi.com> - 1.0.0-1
- updated to upstream 1.0.0

* Wed Dec 22 2010 Sergio Rubio <srubio@abiquo.com> - 0.9.2-1
- updated to upstream 0.9.2

* Fri Dec 10 2010 Sergio Rubio <srubio@abiquo.com> - 0.9.1-1
- updated to hiredis 0.9.1

* Tue Oct 05 2010 - Sergio Rubio <srubio@abiquo.com> 0.0.20101005
- Initial release
