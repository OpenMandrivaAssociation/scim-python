%define apiver 0.1

Name:		scim-python
Version:	%{apiver}.4
Release:	%mkrel 1
Summary:	Python wrapper for Smart Common Input Method platform
License:	LGPLv2+
Group:		System/Internationalization
URL:		http://code.google.com/p/scim-python/
Source0:	http://scim-python.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	scim-devel gettext-devel
BuildRequires:	pygtk2.0-devel
Requires:	scim

%description
Python wrapper for Smart Common Input Method platform.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT%{python_sitearch}/scim-%{apiver}/scim/_scim.la
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{python_sitearch}/scim-%{apiver}
%{python_sitearch}/scim.pth
%{scim_pluginsdir}/IMEngine/scim-python-engine.so
%{scim_pluginsdir}/SetupUI/scim-python-setup.so
%{_datadir}/scim-python/
%{_datadir}/scim/icons/*
