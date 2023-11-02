%define major 1
%define api 0

%define libname %mklibname shumate %{api} %{major}
%define devname %mklibname -d shumate %{api}
%define girname %mklibname shumate-gir %{major}

Name:           libshumate
Version:        1.1.2
Release:        1
Summary:        C library providing a GtkWidget to display maps
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libshumate
Source:         https://gitlab.gnome.org/GNOME/libshumate/-/archive/%{version}/libshumate-%{version}.tar.bz2

BuildRequires:  gtk-doc >= 1.9
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.4
BuildRequires:  pkgconfig(gi-docgen) >= 2021.1
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.3
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0
BuildRequires:  pkgconfig(sqlite3) >= 1.12.0
BuildRequires:  pkgconfig(vapigen) >= 0.11.0
BuildRequires:	glibc-static-devel

%description
libshumate is a C library providing a GtkWidget to display maps.
It supports numerous free map sources such as OpenStreetMap,
OpenCycleMap, OpenAerialMap and Maps for free.

libshumate is named after Jessamine Shumate, an American artist,
historian, and cartographer (Wikipedia). libshumate is forked from,
and tries to follow similar principles in the API as libchamplain.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
C library providing a GtkWidget to display maps.
This package contains the shared library files.

%package -n %{girname}
Summary:        Introspection file for %{name}

%description -n %{girname}
C library providing a GtkWidget to display maps.
This package contains introspection file for %{name}.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
C library providing a GtkWidget to display maps.
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dlibsoup3=true
%meson_build

%install
%meson_install

%find_lang shumate1

%files -n %{libname} -f shumate1.lang
%license COPYING
%{_libdir}/libshumate-%{major}.%{api}.so.*

%files -n %{girname}
%{_libdir}/girepository-1.0/Shumate-%{major}.%{api}.typelib

%files -n %{devname}
%doc AUTHORS README.md
%{_datadir}/doc/libshumate-%{major}.%{api}/
%{_includedir}/shumate-%{major}.%{api}/
%{_libdir}/pkgconfig/shumate-%{major}.%{api}.pc
%{_libdir}/libshumate-%{major}.%{api}.so
%{_datadir}/gir-1.0/Shumate-%{major}.%{api}.gir
%{_datadir}/vala/vapi/shumate-%{major}.%{api}.deps
%{_datadir}/vala/vapi/shumate-%{major}.%{api}.vapi
