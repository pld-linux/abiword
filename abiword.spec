# TODO:
#	- use external wv library
Summary:	Multi-platform word processor
Summary(pl):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	1.99.1
Release:	0.2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	e96b50aea36ebf935d001b436b2bc582
Source1:	http://dl.sourceforge.net/%{name}/%{name}-plugins-%{version}.tar.gz
# Source1-md5:	c7b7bc8f1c875b31209e24b0d51f2e63
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

%package plugins-tools
Summary:	Various tools that can be used to extend AbiWord's capabilities.
Summary(pl):	Ró¿ne narzêdzia powiêkszaj±ce mo¿liwo¶ci AbiWord.
Group: 		Applications/Productivity
Requires: 	%{name} = %{epoch}:%{version}

%description plugins-tools
This is a set of plugins for AbiWord.  It includes
        eml: Use mathematical notation in AbiWord.
 abicommand: Perform AbiWord operations from the command prompt.
    abigimp: Process images in AbiWord using the Gimp.
  abimagick: Process images in AbiWord using ImageMagick.
  wikipedia: Access the Wikipedia reference from AbiWord.
    urldict: Cross-platform url dictionary plugin.
      gdict: Use the gnome dictionary application from within AbiWord.
  aiksaurus: Use the Aiksaurus thesaurus in AbiWord.
  babelfish: Translate text online using Babelfish.
ScriptHappy: Run other programs in a shell and direct the output to AbiWord.

%package plugins-impexp
Summary: 	Plugins to import and export otherwise unsupported formats.
Summary(pl):	Wtyczki importuj±ce i eksportuj±ce do róznych formatów dokumentów.
Group: 		Applications/Productivity
Requires: 	%{name} = %{epoch}:%{version}

%description plugins-impexp
This is a set of plugins for AbiWord.  It includes support for OpenWriter,
bzipped AbiWord, and (x)html document formats.  Additionally, it adds support
for certain image types to AbiWord builds that were not gnome-enabled.

%package clipart
Summary: 	AbiWord Clipart
Group: 		Applications/Productivity
                                                                                                                                                    
%description clipart
This is the clipart portfolio used by AbiWord.

%prep
%setup -q -a 1

#Shorten paths for easier build
mv %{name}-plugins-%{version}/%{name}-plugins %{name}-plugins

%build
cd abi
./autogen.sh
%configure \
	--enable-gnome \
	--enable-xft \
	--with-pspell
%{__make}

cd ../abiword-plugins
./nextgen.sh
%configure \
	--disable-eg \
	--disable-gda \
	--enable-abicommand \
	--enable-abigimp \
	--enable-aiksaurus \
	--enable-babelfish \
	--enable-freetranslation \
	--enable-gdict \
	--enable-referee \
	--enable-urldict \
	--enable-wikipedia \
	--disable-magick \
	--enable-shell \
	--enable-gdkpixbuf \
	--enable-bmp \
	--enable-jpeg \
	--enable-wmf \
	--enable-applix \
	--enable-bz2abw \
	--enable-clarisworks \
	--enable-eml \
	--enable-hancom \
	--enable-hrtext \
	--enable-html \
	--enable-iscii-text \
	--enable-kword \
	--enable-latex \
	--enable-mif \
	--enable-mswrite \
	--disable-nroff \
	--enable-OpenWriter \
	--enable-pdb \
	--enable-psion \
	--enable-pw \
	--enable-sdw \
	--enable-t602 \
	--enable-wml \
	--enable-wordperfect \
	--enable-xhtml \
	--enable-xsl-fo \
	--enable-librsvg \
	--enable-docbook
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
#Desktop file and icon
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
install $RPM_BUILD_ROOT%{_datadir}/AbiSuite-2.0/icons/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}
install src/pkg/linux/rpm/data/abiword.desktop $RPM_BUILD_ROOT%{_desktopdir}
perl -p -i -e "s|Exec=abiword|Exec=AbiWord-2.0|" $RPM_BUILD_ROOT%{_desktopdir}/abiword.desktop

#Bonobo stuff
install -d $RPM_BUILD_ROOT%{_libdir}/bonobo/servers
mv $RPM_BUILD_ROOT%{_datadir}/AbiSuite-2.0/GNOME_AbiWord_Control_2_0.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers

#Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/AbiWord-2.0/plugins/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/AbiWord-2.0/plugins/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc abi/docs/*.abw abi/CREDITS.TXT
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/AbiSuite-2.0
%dir %{_datadir}/AbiSuite-2.0/AbiWord
%dir %{_datadir}/AbiSuite-2.0/AbiWord/scripts
%dir %{_libdir}/AbiWord-2.0
%dir %{_libdir}/AbiWord-2.0/plugins
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

%files plugins-tools
%defattr(644,root,root,755)
%{_libdir}/AbiWord-2.0/plugins/libAbiCommand.so
%{_libdir}/AbiWord-2.0/plugins/libAbiBabelfish.so
%{_libdir}/AbiWord-2.0/plugins/libAbiFreeTranslation.so
%{_libdir}/AbiWord-2.0/plugins/libAbiGdict.so
%{_libdir}/AbiWord-2.0/plugins/libAbiGimp.so
%{_libdir}/AbiWord-2.0/plugins/libAbiGoogle.so
%{_libdir}/AbiWord-2.0/plugins/libAbiGypsython.so
%{_libdir}/AbiWord-2.0/plugins/libAbiURLDict.so
%{_libdir}/AbiWord-2.0/plugins/libAbiWikipedia.so
%{_libdir}/AbiWord-2.0/plugins/libAbiReferee.so
%{_libdir}/AbiWord-2.0/plugins/libAbiScriptHappy.so

%files plugins-impexp
%defattr(644,root,root,755)
%{_libdir}/AbiWord-2.0/plugins/libAbiApplix.so
%{_libdir}/AbiWord-2.0/plugins/libAbiBMP.so
%{_libdir}/AbiWord-2.0/plugins/libAbiBZ2.so
%{_libdir}/AbiWord-2.0/plugins/libAbiClarisWorks.so
%{_libdir}/AbiWord-2.0/plugins/libAbiCoquille.so
%{_libdir}/AbiWord-2.0/plugins/libAbiDocBook.so
%{_libdir}/AbiWord-2.0/plugins/libAbiEML.so
%{_libdir}/AbiWord-2.0/plugins/libAbiGdkPixbuf.so
%{_libdir}/AbiWord-2.0/plugins/libAbiHancom.so
%{_libdir}/AbiWord-2.0/plugins/libAbiHRText.so
%{_libdir}/AbiWord-2.0/plugins/libAbiISCII.so
%{_libdir}/AbiWord-2.0/plugins/libAbiJPEG.so
%{_libdir}/AbiWord-2.0/plugins/libAbiKWord.so
%{_libdir}/AbiWord-2.0/plugins/libAbiLaTeX.so
%{_libdir}/AbiWord-2.0/plugins/libAbiMIF.so
%{_libdir}/AbiWord-2.0/plugins/libAbiMSWrite.so
%{_libdir}/AbiWord-2.0/plugins/libAbiOpenWriter.so
%{_libdir}/AbiWord-2.0/plugins/libAbiPW.so
%{_libdir}/AbiWord-2.0/plugins/libAbiPalmDoc.so
%{_libdir}/AbiWord-2.0/plugins/libAbiRSVG.so
%{_libdir}/AbiWord-2.0/plugins/libAbiSDW.so
%{_libdir}/AbiWord-2.0/plugins/libAbiT602.so
%{_libdir}/AbiWord-2.0/plugins/libAbiWMF.so
%{_libdir}/AbiWord-2.0/plugins/libAbiWML.so
%{_libdir}/AbiWord-2.0/plugins/libAbiXHTML.so
%{_libdir}/AbiWord-2.0/plugins/libAbiXSLFO.so

%files clipart
%defattr(644,root,root,755)
%{_datadir}/AbiSuite-2.0/clipart
