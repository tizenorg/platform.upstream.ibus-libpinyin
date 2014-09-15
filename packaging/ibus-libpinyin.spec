Name:       ibus-libpinyin
Version:    1.6.92
Release:    0
Summary:    Intelligent Pinyin engine based on libpinyin for IBus
License:    GPL-2.0+
Group:      System/Libraries
URL:        https://github.com/libpinyin/ibus-libpinyin
Source0:    http://downloads.sourceforge.net/libpinyin/ibus-libpinyin/%{name}-%{version}.tar.gz
Source1001: ibus-libpinyin.manifest

BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  lua-devel
BuildRequires:  ibus-devel >= 1.3
BuildRequires:  libpinyin-devel > 0.6.90
BuildRequires:  fdupes

# Requires(post): sqlite
Requires:   ibus >= 1.2.0
Requires:   libpinyin > 0.6.90

%description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) input method based on libpinyin for IBus.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --disable-static \
             --disable-boost

# make -C po update-gmo
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%find_lang %{name}
%fdupes %{buildroot}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS README
%{_datadir}/applications/*.desktop
%{_libexecdir}/ibus-engine-libpinyin
%{_libexecdir}/ibus-setup-libpinyin
%{_datadir}/ibus-libpinyin/phrases.txt
%{_datadir}/ibus-libpinyin/icons
%{_datadir}/ibus-libpinyin/setup
%{_datadir}/ibus-libpinyin/*.lua
%{_datadir}/ibus-libpinyin/db/*.db
%dir %{_datadir}/ibus-libpinyin
%dir %{_datadir}/ibus-libpinyin/db
%{_datadir}/ibus/component/*
