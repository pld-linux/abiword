# TODO:
#	- use external wv library
Summary:	Multi-platform word processor
Summary(pl):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	1.99.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e96b50aea36ebf935d001b436b2bc582
URL:		http://www.abisource.com/
BuildRequires:	bzip2-devel
BuildRequires:	fontconfig-devel
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	gal-devel >= 1.99
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libbonobo-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgsf-devel
BuildRequires:	libjpeg-devel
BuildRequires:	librsvg-devel
BuildRequires:	libwmf-devel
BuildRequires:	libxml2-devel >= 2.4.2
BuildRequires:	pspell-devel >= 0.11.1
BuildRequires:	gucharmap-devel >= 0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AbiWord is a multi-platform word processor with a GTK+ interface on
the UNIX platform.

%description -l pl
AbiWord jest wieloplatformowym procesorem tekstu z interfejsem GTK+ na platformie UNIX.

%package clipart
Summary: 	AbiWord Clipart
Group: 		Applications/Productivity
                                                                                                                                                    
%description clipart
This is the clipart portfolio used by AbiWord.

%prep
%setup -q

%build
cd abi
./autogen.sh
%configure \
	--enable-gnome \
	--enable-xft \
	--with-pspell
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd abi
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Manual fixes to Abi package
#Desktop file and icon
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
install $RPM_BUILD_ROOT%{_datadir}/AbiSuite-2.0/icons/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}
install src/pkg/linux/rpm/data/abiword.desktop $RPM_BUILD_ROOT%{_desktopdir}
perl -p -i -e "s|Exec=abiword|Exec=AbiWord-2.0|" $RPM_BUILD_ROOT%{_desktopdir}/abiword.desktop

#Bonobo stuff
install -d $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
mv $RPM_BUILD_ROOT%{_datadir}/AbiSuite-2.0/GNOME_AbiWord_Control_2_0.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc abi/docs/*.abw abi/CREDITS.TXT
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/AbiSuite-2.0
%dir %{_datadir}/AbiSuite-2.0/AbiWord
%dir %{_datadir}/AbiSuite-2.0/AbiWord/scripts
%{_datadir}/AbiSuite-2.0/AbiWord/glade
%{_datadir}/AbiSuite-2.0/AbiWord/scripts/*
%{_datadir}/AbiSuite-2.0/AbiWord/strings
%{_datadir}/AbiSuite-2.0/AbiWord/system.profile*
%{_datadir}/AbiSuite-2.0/icons
%{_datadir}/AbiSuite-2.0/templates
%{_datadir}/AbiSuite-2.0/abi-nautilus-view-file.xml
%{_libdir}/bonobo/servers/*
%{_desktopdir}/*
%{_pixmapsdir}/*.png
%{_datadir}/AbiSuite-2.0/AbiWord.exe.MANIFEST
%{_datadir}/AbiSuite-2.0/AbiWord/readme.txt
%{_datadir}/AbiSuite-2.0/README

%files clipart
%defattr(644,root,root,755)
%{_datadir}/AbiSuite-2.0/clipart
