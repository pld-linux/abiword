Summary:	AbiWord - advanced wordprocessor
Summary(pl):	AbiWord - zaawansowany procesor tekstu
Name:		abiword
Version:	0.9.6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://prodownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.abisource.com/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
AbiWord is a free word processing program similar to Microsoft Word. 
It is suitable for typing papers, letters, reports, memos, and so forth.

%description -l pl
AbiWord jest darmowym procesorem tekstu podobnym do Microsoft Word.
Jest idealnym narzêdziem do pisania dokumentów, listów, raportów itp.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Office/Wordprocessors,%{_pixmapsdir}}

cd abi
%{__make} -f GNUmakefile install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install $RPM_BUILD_ROOT%{_datadir}/AbiSuite/icons/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf CREDITS.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc abi/docs/*.abw abi/*.gz
%attr(755,root,root) %{_bindir}/[At]*
%{_datadir}/AbiSuite
%{_applnkdir}/Office/Wordprocessors/*
%{_pixmapsdir}/*.png
