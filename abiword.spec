#
# TODO:
# - check impexp-plugins, loading them on starup causes AbiWord to segfault
# - make "light" version without gnome dependencies 
# - split plugins into subpackages (yeah, we can do it) (started! :)
# - check BRs/Rs
# - use our auto macros not ./autogen stuff
#
%bcond_without	gnome 	# without GNOME libs
#
%define		mver	2.2
Summary:	Multi-platform word processor
Summary(pl):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	2.2.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	1e70a9ee1daee1206fb873bdcd35bcb9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
URL:		http://www.abisource.com/i
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ImageMagick-c++-devel >= 5.4.0
BuildRequires:	aiksaurus-gtk-devel >= 1.0
BuildRequires:	aspell-devel >= 0.50.0
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	enchant-devel >= 1.1.5
BuildRequires:	eps-devel >= 1.2
BuildRequires:	fontconfig-devel >= 1.0
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gucharmap-devel >= 1.4.0
BuildRequires:	libbonobo-devel >= 2.2.0
BuildRequires:	libgda-devel >= 0.90.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomedb-devel >= 0.90.0
BuildRequires:	libgnomeprintui-devel >= 2.2.1.3-2
BuildRequires:	libgnomeprint-devel >= 2.2.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libgsf-devel >= 1.4.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	libwpd-devel >= 0.7.1
BuildRequires:	libxml2-devel >= 2.4.20
BuildRequires:	nautilus-devel >= 2.0
BuildRequires:	ots-devel >= 0.4.1
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	popt-devel
BuildRequires:	psiconv-devel >= 0.9.6
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	wv-devel >= 1.0.3
BuildRequires:	xft-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AbiWord is a multi-platform word processor with a GTK+ interface on
the UNIX platform.

%description -l pl
AbiWord jest wieloplatformowym procesorem tekstu z interfejsem GTK+ na
platformie UNIX.

# abiCommand plugin
%package plugin-abicommand
Summary:	AbiWord command line control
Summary(pl):	Konrolowanie AbiWorda z linii poleceñ
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-abicommand
Allows command line control of AbiWord.

%description plugin-abicommand -l pl
Pozwala na kontrolowanie AbiWorda z poziomu linii poleceñ.

# abiGimp plugin
%package plugin-abigimp
Summary:	AbiWord image editor plugin
Summary(pl):	Wtyczka AbiWorda dla edytorów obrazu
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-abigimp
Allows to edit embedded images with a paint program like Gimp.

%description plugin-abigimp -l pl
Pozwala na edycje osadzonych obrazów programem do ich obróbki jak
Gimp.

# abiAiksaurus
%package plugin-aiksaurus
Summary:	AbiWord Aiksaurus plugin
Summary(pl):	Wtyczka AbiWorda Aiksaurus
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-aiksaurus
Allows to use Aiksaurus thesaurus.

%description plugin-aiksaurus -l pl
Pozwala na u¿ycie Aiksaurusa - s³ownika wyrazów bliskoznacznych.

# abiBabelfish
%package plugin-babelfish
Summary:	AbiWord Babelfish plugin
Summary(pl):	Wtyczka AbiWorda Babelfish
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-babelfish
Allows to translate selected text.

%description plugin-babelfish -l pl
Pozwala na przet³umaczenie wybranego tekstu.

# abiFreeTranslation
%package plugin-freetranslation
Summary:	AbiWord freetranslation.com plugin
Summary(pl):	Wtyczka AbiWorda dla freetranslation.com
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-freetranslation
Allows to translate selected text.

%description plugin-freetranslation -l pl
Pozwala na przet³umaczenie wybranego tekstu.

# abiGDA
%package plugin-gda
Summary:	AbiWord GDA plugin
Summary(pl):	Wtyczka AbiWorda dla GDA
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gda
Allows access to any database provided by libgda.

%description plugin-gda -l pl
Pozwala na po³±czenie z dowoln± baz± danych dostarczan± za
po¶rednictwem libgda.

# abiDash
# abiGdict
# abiGoogle
# abiGypsython
# abiOTS
# abiReferee
# abiScriptHappy
# abiURLDict
# abiWikipedia

# abiApplix
# abiBMP
# abiBZ2
# abiClarisWorks
# abiCoquille
# abiDocBook
# abiEML
# abiGdkPixbuf
# abiHRText
# abiHancom
# abiISCII
# abiJPEG
# abiKWord
# abiLaTeX
# abiMIF
# abiMSWrite
# abiMagick
# abiNroff
# abiOpenWriter
# abiPalmDoc
# abiPassepartout
# abiPsion
# abiRSVG
# abiSDW
# abiT602
# abiWMF
# abiWML
# abiWordPerfect
# abiXHTML
# abiXSLFO
 
%package clipart
Summary:	AbiWord Clipart
Summary(pl):	Cliparty dla AbiWorda
Group:		Applications/Productivity

%description clipart
This is the clipart portfolio used by AbiWord.

%description clipart -l pl
Jest to teczka clipartów u¿ywanych przez AbiWorda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd abi
%{__aclocal} -I ac-helpers
%{__automake}
%{__autoconf}
%configure \
	--%{!?with_gnome:dis}%{?with_gnome:en}able-gnome \
	--with-pspell \
	--with-sys-wv \
	--enable-threads \
	--with-libxml2

%{__make}

cd ../abiword-plugins
./nextgen.sh
%configure \
	--with-psiconv=/usr
# --with-psiconv=dir is workaround to avoid -Lyes/lib which libtool doesn't like

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd abiword-plugins
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd ../abi
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Manual fixes to Abi package
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_iconsdir}/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}

#Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/AbiWord-%{mver}/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/AbiWord-%{mver}/plugins/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/AbiSuite-%{mver}
%dir %{_datadir}/AbiSuite-%{mver}/AbiWord
%dir %{_datadir}/AbiSuite-%{mver}/AbiWord/scripts
%dir %{_libdir}/AbiWord-%{mver}
%dir %{_libdir}/AbiWord-%{mver}/plugins
%{_datadir}/AbiSuite-%{mver}/AbiWord/glade
%{_datadir}/AbiSuite-%{mver}/AbiWord/scripts/*
%{_datadir}/AbiSuite-%{mver}/AbiWord/strings
%{_datadir}/AbiSuite-%{mver}/AbiWord/system.profile*
%{_datadir}/AbiSuite-%{mver}/icons
%{_datadir}/AbiSuite-%{mver}/templates
#%{_datadir}/AbiSuite-%{mver}/abi-nautilus-view-file.xml
#%{_libdir}/bonobo/servers/*
%{_desktopdir}/*
%{_pixmapsdir}/*.png
#%{_datadir}/AbiSuite-%{mver}/AbiWord.exe.MANIFEST
%{_datadir}/AbiSuite-%{mver}/AbiWord/readme.txt
#%{_datadir}/AbiSuite-%{mver}/README

%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiAikSaurus.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBabelfish.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCAPI.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCommand.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiDash.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiFreeTranslation.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGDA.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGdict.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGimp.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGoogle.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGypsython.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOTS.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiReferee.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiScriptHappy.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiURLDict.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWikipedia.so

%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiApplix.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBMP.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBZ2.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiClarisWorks.so
#%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCoquille.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiDocBook.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiEML.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGdkPixbuf.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiHRText.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiHancom.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiISCII.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiJPEG.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiKWord.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiLaTeX.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMIF.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMSWrite.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMagick.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiNroff.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOpenWriter.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPalmDoc.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPassepartout.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPsion.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiRSVG.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiSDW.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiT602.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWMF.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWML.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWordPerfect.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiXHTML.so
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiXSLFO.so
%{_libdir}/AbiWord-%{mver}/plugins/AbiWord

%files clipart
%defattr(644,root,root,755)
%{_datadir}/AbiSuite-%{mver}/clipart
