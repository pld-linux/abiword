#
# TODO:
# - check impexp-plugins, loading them on starup causes AbiWord to segfault
# - split plugins into subpackages (yeah, we can do it) (started! :)
# - check BRs/Rs
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
URL:		http://www.abisource.com/
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
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 0.2.8
BuildRequires:	libwpd-devel >= 0.7.1
BuildRequires:	libxml2-devel >= 2.4.20
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

# plugins - tools
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

# abiDash - not documented
%package plugin-dash
Summary:	AbiWord dash plugin
Summary(pl):	Wtyczka dash dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dash
Dash plugin.

%description plugin-dash -l pl
Wtyczka dash.

# abiGdict
%package plugin-gdict
Summary:	AbiWord gDict plugin
Summary(pl):	Wtyczka AbiWorda gDict
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdict
Look up definitions of selected text.

%description plugin-gdict -l pl
Wyszukuje definicje w zaznaczonym fragmencie tekstu.

# abiGoogle
%package plugin-google
Summary:	AbiWord Google plugin
Summary(pl):	Wtyczka Google dla AbiWorda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-google
Search Google for selected text.

%description plugin-google -l pl
Przeszukuje Google w poszukiwaniu zaznaczonego tekstu.

# abiGypsython - todo: pl translation 
%package plugin-gypsython
Summary:	AbiWord Gyspsython plugin
Summary(pl):	Wtyczka Gypsython dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gypsython
Python MailMerge.

%description plugin-gypsython -l pl
Python MailMerge.

# abiOTS
%package plugin-ots
Summary:	AbiWord OTS plugin
Summary(pl):	Wtyczka OTS dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ots
Create document summaries.

%description plugin-ots -l pl
Tworzy podumowanie dokumentu.

# abiReferee - not documented
%package plugin-referee
Summary:	AbiWord Referee plugin
Summary(pl):	Wtyczka Referee dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-referee
Referee plugin.

%description plugin-referee -l pl
Wtyczka Referee.

# abiScriptHappy - not documented
%package plugin-scripthappy
Summary:	AbiWord ScriptHappy plugin
Summary(pl):	Wtyczka ScriptHappy dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripthappy
Plugin ScriptHappy.

%description plugin- -l pl
Wtyczka ScriptHappy.

# abiURLDict
%package plugin-urldict
Summary:	AbiWord URLDict plugin
Summary(pl):	Wtyczka URLDict dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-urldict
Internet dictionary.

%description plugin-urldict -l pl
S³ownik internetowy.

# abiWikipedia
%package plugin-wikipedia
Summary:	AbiWord  plugin
Summary(pl):	Wtyczka  dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wikipedia
Search wikipedia for selected text.

%description plugin-wikipedia -l pl
Przeszukuje wikipedie w poszukiwaniu zaznaczonego teksu.

# plugins import - export
# abiApplix
%package plugin-applix
Summary:	AbiWord Applix plugin
Summary(pl):	Wtyczka Applix dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-applix
Import/Export Applix Word files.

%description plugin-applix -l pl
.

# abiBMP
%package plugin-bmp
Summary:	AbiWord BMP plugin
Summary(pl):	Wtyczka BMP dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bmp
View Bitmap Images.

%description plugin-bmp -l pl
.

# abiBZ2
%package plugin-bz2
Summary:	AbiWord BZ2 plugin
Summary(pl):	Wtyczka BZ2 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bz2
Import/Export BZ2 compressed AbiWord files.

%description plugin-bz2 -l pl
.

# abiClarisWorks
%package plugin-clarisworks
Summary:	AbiWord ClarisWorks plugin
Summary(pl):	Wtyczka ClarisWorks dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-clarisworks
Import/Export Clarisworks files.

%description plugin-clarisworks -l pl
.

# abiCoquille
%package plugin-coquille
Summary:	AbiWord Coquille plugin
Summary(pl):	Wtyczka Coquille dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-coquille
Docbook extensions.

%description plugin-coquille -l pl
.

# abiDocBook
%package plugin-docbook
Summary:	AbiWord DocBook plugin
Summary(pl):	Wtyczka DocBook dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-docbook
Import/export Docbook files.

%description plugin-docbook -l pl
.

# abiEML
%package plugin-eml
Summary:	AbiWord EML plugin
Summary(pl):	Wtyczka EML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-eml
Import/export as MS Outlook Email files.

%description plugin-eml -l pl
.

# abiGdkPixbuf
%package plugin-gdkpixbuf
Summary:	AbiWord GdkPixbuf plugin
Summary(pl):	Wtyczka GdkPixbuf dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdkpixbuf
View any Image that GTK+ Can.

%description plugin-gdkpixbuf -l pl
.

# abiHRText
%package plugin-hrtext
Summary:	AbiWord HRText plugin
Summary(pl):	Wtyczka HRText dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hrtext
Export text with "newsgroup" markup.

%description plugin-hrtext -l pl
.

# abiHancom
%package plugin-hancom
Summary:	AbiWord Hancom plugin
Summary(pl):	Wtyczka Hancom dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hancom
Hancom Word Importer.

%description plugin-hancom -l pl
.

# abiISCII
%package plugin-iscii
Summary:	AbiWord ISCII plugin
Summary(pl):	Wtyczka  dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-iscii
Import/export ISCII text files (Indic script).

%description plugin-iscii -l pl
.

# abiJPEG
%package plugin-jpeg
Summary:	AbiWord JPEG plugin
Summary(pl):	Wtyczka JPEG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-jpeg
View JPEG Images.

%description plugin-jpeg -l pl
.

# abiKWord
%package plugin-kword
Summary:	AbiWord KWord plugin
Summary(pl):	Wtyczka KWord dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-kword
KWord import/export.

%description plugin-kword -l pl
.

# abiLaTeX
%package plugin-latex
Summary:	AbiWord LaTeX plugin
Summary(pl):	Wtyczka LaTeX dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-latex
LaTeX export.

%description plugin-latex -l pl
.

# abiMIF - not documented
%package plugin-mif
Summary:	AbiWord MIF plugin
Summary(pl):	Wtyczka MIF dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mif
MIF plugin.

%description plugin-mif -l pl
Wtyczka MIF.

# abiMSWrite
%package plugin-mswrite
Summary:	AbiWord MSWrite plugin
Summary(pl):	Wtyczka MSWrite dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mswrite
Import MSWrite files.

%description plugin-mswrite -l pl
.

# abiMagick
%package plugin-magick
Summary:	AbiWord ImageMagick plugin
Summary(pl):	Wtyczka ImageMagick dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-magick
View and format images that ImageMagick supports.

%description plugin-magick -l pl
.

# abiNroff
%package plugin-nroff
Summary:	AbiWord Nroff plugin
Summary(pl):	Wtyczka Nroff dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-nroff
Nroff/Man file format.

%description plugin-nroff -l pl
.

# abiOpenWriter
%package plugin-openwritter
Summary:	AbiWord OpenWriter plugin
Summary(pl):	Wtyczka OpenWriter dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openwritter
Import/export OpenOffice files.

%description plugin-openwritter -l pl
.

# abiPalmDoc
%package plugin-palmdoc
Summary:	AbiWord PalmDoc plugin
Summary(pl):	Wtyczka PalmDoc dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-palmdoc
.

%description plugin-palmdoc -l pl
.

# abiPassepartout
%package plugin-passepartout
Summary:	AbiWord Passepartout plugin
Summary(pl):	Wtyczka Passepartout dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-passepartout
.

%description plugin-passepartout -l pl
.

# abiPsion
%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl):	Wtyczka Psion dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl
.

# abiRSVG
%package plugin-rsvg
Summary:	AbiWord RSVG plugin
Summary(pl):	Wtyczka RSVG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-rsvg
View Scalable Vector Graphics.

%description plugin-rsvg -l pl
.

# abiSDW
%package plugin-sdw
Summary:	AbiWord SDW plugin
Summary(pl):	Wtyczka SDW dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sdw
Import StarOffice 5.x files.

%description plugin-sdw -l pl
.

# abiT602
%package plugin-t602
Summary:	AbiWord T602 plugin
Summary(pl):	Wtyczka T602 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-t602
Import T602 files.

%description plugin-t602 -l pl
.

# abiWMF
%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl):	Wtyczka WMF dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wmf
View Windows Metafiles.

%description plugin-wmf -l pl
.

# abiWML
%package plugin-wml
Summary:	AbiWord WML plugin
Summary(pl):	Wtyczka WML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wml
Import/export WML files.

%description plugin-wml -l pl
.

# abiWordPerfect
%package plugin-wordperfect
Summary:	AbiWord WordPerfect plugin
Summary(pl):	Wtyczka WordPerfect dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wordperfect
Import/Export Wordperfect files.

%description plugin-wordperfect -l pl
.

# abiXHTML
%package plugin-xhtml
Summary:	AbiWord XHTML plugin
Summary(pl):	Wtyczka XHTML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xhtml
Import html/multipart html.

%description plugin-xhtml -l pl
.

# abiXSLFO
%package plugin-xslfo
Summary:	AbiWord XSLFO plugin
Summary(pl):	Wtyczka XSLFO dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xslfo
Import/export XSL-FO.

%description plugin-xslfo -l pl
.

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
%{__libtoolize}
%{__aclocal} -I ac-helpers
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C abiword-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C abi install \
	DESTDIR=$RPM_BUILD_ROOT

# Manual fixes to Abi package
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
mv $RPM_BUILD_ROOT%{_iconsdir}/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}

# Remove useless files
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
%{_desktopdir}/*
%{_pixmapsdir}/*.png
%{_datadir}/AbiSuite-%{mver}/AbiWord/readme.txt

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
