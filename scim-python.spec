%define apiver 0.1

Name:		scim-python
Version:	%{apiver}.9
Release:	%mkrel 1
Summary:	Python wrapper for Smart Common Input Method platform
License:	LGPLv2+
Group:		System/Internationalization
URL:		http://code.google.com/p/scim-python/
Source0:	http://scim-python.googlecode.com/files/%{name}-%{version}.tar.bz2
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
%{scim_plugins_dir}/IMEngine/scim-python-engine.so
%{scim_plugins_dir}/SetupUI/scim-python-setup.so
%dir %{_datadir}/scim-python
%dir %{_datadir}/scim-python/engine
%{_datadir}/scim-python/engine/__init__.*
%dir %{_datadir}/scim-python/setupui
%{_datadir}/scim-python/setupui/__init__.*
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

%files zh_CN
%defattr(-,root,root,-)
%{_datadir}/scim-python/engine/PinYin

%post zh_CN
cd /usr/share/scim-python/engine/PinYin
echo "Creating INDEX in phrases database."
python -c "import PYSQLiteDB; db = PYSQLiteDB.PYSQLiteDB (); db.create_indexes ();"
#-----------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{python_sitearch}/scim-%{apiver}/scim/_scim.la
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT
