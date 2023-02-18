Name:		fonts-ttf-cousine
Version:	1.0
Release:	1
Summary:	Cousine ttf fonts
License:	Apache License v2.00
Group:		System/Fonts/True type
Url:		https://www.ascenderfonts.com/
Source0:	%{name}-%version.tar.gz
BuildArch:	noarch

%description
Cousine is a typeface which is metrics compatible with Courier New.

%files
%dir %{_datadir}/fonts/TTF/cousine/
%{_datadir}/fonts/TTF/cousine/*

%prep
%setup -qn %{name}-%{version}/fonts/TTF/cousine/

%build
#

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/cousine
install -Dm 644  *.ttf  %{buildroot}%{_datadir}/fonts/TTF/cousine/
