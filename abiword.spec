Summary:	AbiWord
Summary(pl):	AbiWord
Name:		abiword
Version:	0.9.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://prodownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.abisource.com/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description

%description -l pl

%prep
%setup -q

%build
cd abi
gettextize --copy --force

%configure \
	--enable-gnome
	
%{__make} -f GNUmakefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Office/Wordprocessors}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
cd abi
%{__make} -f GNUmakefile install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CREDITS.TXT

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc abi/docs/*.abw abi/*.gz
%attr(755,root,root) %{_bindir}/[At]*
%{_datadir}/AbiSuite
%{_applnkdir}/Office/Wordprocessors/*
