%define apiver 0.1

%define build_plf 0
%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif

Name:		scim-python
Version:	%{apiver}.11
Release:	%mkrel 1
Summary:	Python wrapper for Smart Common Input Method platform
License:	LGPLv2+
Group:		System/Internationalization
URL:		http://code.google.com/p/scim-python/
Source0:	http://scim-python.googlecode.com/files/%{name}-%{version}.tar.gz
%if %build_plf
Source1:	http://scim-python.googlecode.com/files/pinyin-database-0.1.10.5.tar.bz2
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	scim-devel gettext-devel
BuildRequires:	pygtk2.0-devel python-enchant
Requires:	scim-client = %{scim_api}
Requires:	%name-l10n = %version

%description
Python wrapper for Smart Common Input Method platform.

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{python_sitearch}/scim-%{apiver}
%{python_sitearch}/scim.pth
%{scim_plugins_dir}/*/*.so
%dir %{_datadir}/scim-python
%dir %{_datadir}/scim-python/engine
%{_datadir}/scim-python/engine/__init__.*
%dir %{_datadir}/scim-python/setupui
%{_datadir}/scim-python/setupui/__init__.*
%dir %{_datadir}/scim-python/helper
%{_datadir}/scim-python/helper/__init__.*
%{_datadir}/scim/icons/*

#-----------------------------------------------------------
%package en
Summary:	Python english IM engine 
Group:		System/Internationalization
Requires:	%{name} = %{version}
Requires:	python-enchant
Requires:	locales-en
Provides:	%name-l10n = %version
Conflicts:	%name < 0.1.9

%description en
This package contains a python english IM engine.

%files en
%defattr(-,root,root,-)
%{_datadir}/scim-python/engine/EnglishWriter
%{_datadir}/scim-python/setupui/EnglishWriter
#-----------------------------------------------------------

%package zh_CN
Summary:        Python chinese IM engine
Group:          System/Internationalization
Requires:       %{name} = %{version}
Requires:       locales-zh
Provides:       %name-l10n = %version
Conflicts:      %name < 0.1.9

%description zh_CN
This package contains a python chinese IM engine.
%if %build_plf
This package is in Plf because the data file used by PinYin
is not free to redistribute. Check here (mainly term 3.3):
	http://www.sogou.com/labs/dl/license.html
%endif

%files zh_CN
%defattr(-,root,root,-)
%if %build_plf
%{_datadir}/scim-python/engine/PinYin
%{_datadir}/scim-python/helper/PinYinSetup
%{_datadir}/scim-python/helper/ZhengJuSetup
%endif
%_bindir/XMCreateDB
%{_datadir}/scim-python/engine/XingMa
%{_datadir}/scim-python/data/pinyin_table.txt

#-----------------------------------------------------------

%prep
%setup -q
%if %build_plf
cd python/engine/PinYin
tar jxvf %{SOURCE1}
cd -
%endif

%build
%configure2_5x --disable-static \
%if %build_plf
	--enable-pinyin
%else
	--disable-pinyin
%endif
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{python_sitearch}/scim-%{apiver}/scim/_scim.la
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT
