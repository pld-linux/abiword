#
# TODO:
# - check plugin-magick - causes AbiWord to segfault on startup
# - polish/complete descriptions
#
%bcond_without	gnome	# without GNOME libs
#
%define		mver	2.2
Summary:	Multi-platform word processor
Summary(pl):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	2.2.1
Release:	0.2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	1e70a9ee1daee1206fb873bdcd35bcb9
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-python24.patch
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
BuildRequires:	python-devel >= 1:2.4
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

# abiCommand plugin
%package plugin-command
Summary:	AbiWord command line control
Summary(pl):	Konrolowanie AbiWorda z linii poleceñ
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-command
Allows command line control of AbiWord.

%description plugin-command -l pl
Pozwala na kontrolowanie AbiWorda z poziomu linii poleceñ.

# abiDash - not documented
%package plugin-dash
Summary:	AbiWord Dash plugin
Summary(pl):	Wtyczka Dash dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dash
Dash plugin.

%description plugin-dash -l pl
Wtyczka Dash.

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

# abiGimp plugin
%package plugin-gimp
Summary:	AbiWord image editor plugin
Summary(pl):	Wtyczka AbiWorda dla edytorów obrazu
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gimp
Allows to edit embedded images with a paint program like Gimp.

%description plugin-gimp -l pl
Pozwala na edycje osadzonych obrazów programem do ich obróbki jak
Gimp.

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
Tworzy podsumowanie dokumentu.

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

%description plugin-scripthappy -l pl
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
Summary:	AbiWord Wikipedia plugin
Summary(pl):	Wtyczka Wikipedia dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wikipedia
Search Wikipedia for selected text.

%description plugin-wikipedia -l pl
Przeszukuje Wikipediê w poszukiwaniu zaznaczonego teksu.

# plugins import - export
# abiApplix
%package plugin-applix
Summary:	AbiWord Applix plugin
Summary(pl):	Wtyczka Applix dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-applix
Import/export Applix Word files.

%description plugin-applix -l pl
Importuje/eksportuje pliki Applix Word.

# abiBMP
%package plugin-bmp
Summary:	AbiWord BMP plugin
Summary(pl):	Wtyczka BMP dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bmp
View Bitmap Images.

%description plugin-bmp -l pl
Wy¶wietla bitmapy.

# abiBZ2
%package plugin-bz2
Summary:	AbiWord BZ2 plugin
Summary(pl):	Wtyczka BZ2 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bz2
Import/export bzip2 compressed AbiWord files.

%description plugin-bz2 -l pl
Importuje/eksportuje pliki Abiworda spakowane przy pomocy bzip2.

# abiClarisWorks
%package plugin-clarisworks
Summary:	AbiWord ClarisWorks plugin
Summary(pl):	Wtyczka ClarisWorks dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-clarisworks
Import/export Clarisworks files.

%description plugin-clarisworks -l pl
Importuje/eksportuje pliki Clarisworks.

# abiCoquille
%package plugin-coquille
Summary:	AbiWord Coquille plugin
Summary(pl):	Wtyczka Coquille dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-coquille
Docbook extensions.

%description plugin-coquille -l pl
Rozszerzenia Docbooka.

# abiDocBook
%package plugin-docbook
Summary:	AbiWord DocBook plugin
Summary(pl):	Wtyczka DocBook dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-docbook
Import/export Docbook files.

%description plugin-docbook -l pl
Importuje/eksportuje pliki zapisane w formacie Docbook.

# abiEML
%package plugin-eml
Summary:	AbiWord EML plugin
Summary(pl):	Wtyczka EML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-eml
Import/export as MS Outlook Email files.

%description plugin-eml -l pl
Importuje/eksportuje pliki poczty programu MS Outlook.

# abiGdkPixbuf
%package plugin-gdkpixbuf
Summary:	AbiWord GdkPixbuf plugin
Summary(pl):	Wtyczka GdkPixbuf dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdkpixbuf
View any image that GTK+ can.

%description plugin-gdkpixbuf -l pl
Wy¶wietla ka¿dy obraz mo¿liwy do pokazania przez GTK+.

# abiHRText
%package plugin-hrtext
Summary:	AbiWord HRText plugin
Summary(pl):	Wtyczka HRText dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hrtext
Export text with "newsgroup" markup.

%description plugin-hrtext -l pl
Eksportuje ze znacznikiem "grupa news".

# abiHancom
%package plugin-hancom
Summary:	AbiWord Hancom plugin
Summary(pl):	Wtyczka Hancom dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hancom
Hancom Word Importer.

%description plugin-hancom -l pl
Importer formatu Hancom Word.

# abiISCII
%package plugin-iscii
Summary:	AbiWord ISCII plugin
Summary(pl):	Wtyczka  dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-iscii
Import/export ISCII text files (Indic script).

%description plugin-iscii -l pl
Importuje/eksportuje tekstowe pliki formatu ISCII (Indic script).

# abiJPEG
%package plugin-jpeg
Summary:	AbiWord JPEG plugin
Summary(pl):	Wtyczka JPEG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-jpeg
View JPEG Images.

%description plugin-jpeg -l pl
Wy¶wietla obrazy formatu JPEG.

# abiKWord
%package plugin-kword
Summary:	AbiWord KWord plugin
Summary(pl):	Wtyczka KWord dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-kword
KWord import/export.

%description plugin-kword -l pl
Import/Eksport plików KWorda.

# abiLaTeX
%package plugin-latex
Summary:	AbiWord LaTeX plugin
Summary(pl):	Wtyczka LaTeX dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-latex
LaTeX export.

%description plugin-latex -l pl
Eksport do LaTeX.

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
Import MS Write files.

%description plugin-mswrite -l pl
Importuje pliki MS Write.

# abiMagick
%package plugin-magick
Summary:	AbiWord ImageMagick plugin
Summary(pl):	Wtyczka ImageMagick dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-magick
View and format images that ImageMagick supports.

%description plugin-magick -l pl
Wy¶wietla obrazy wszystkich typów wspieranych przez ImageMagick.

# abiNroff - lack of precise description (export?/import?)
%package plugin-nroff
Summary:	AbiWord Nroff plugin
Summary(pl):	Wtyczka Nroff dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-nroff
nroff/man file format.

%description plugin-nroff -l pl
Typy plików nroff/man.

# abiOpenWriter
%package plugin-openwritter
Summary:	AbiWord OpenWriter plugin
Summary(pl):	Wtyczka OpenWriter dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openwritter
Import/export OpenOffice files.

%description plugin-openwritter -l pl
Importuje/eksportuje pliki OpenOffice.

# abiPalmDoc - not documented
%package plugin-palmdoc
Summary:	AbiWord PalmDoc plugin
Summary(pl):	Wtyczka PalmDoc dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-palmdoc
PalmDoc plugin.

%description plugin-palmdoc -l pl
Wtyczka PalmDoc.

# abiPassepartout - not documented
%package plugin-passepartout
Summary:	AbiWord Passepartout plugin
Summary(pl):	Wtyczka Passepartout dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-passepartout
Passepartout plugin.

%description plugin-passepartout -l pl
Wtyczka Passepartout.

# abiPsion
%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl):	Wtyczka Psion dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl
Imporuje/eksportuje pliki Psiona.

# abiRSVG
%package plugin-rsvg
Summary:	AbiWord RSVG plugin
Summary(pl):	Wtyczka RSVG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-rsvg
View Scalable Vector Graphics.

%description plugin-rsvg -l pl
Wy¶wietla pliki SVG.

# abiSDW
%package plugin-sdw
Summary:	AbiWord SDW plugin
Summary(pl):	Wtyczka SDW dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sdw
Import StarOffice 5.x files.

%description plugin-sdw -l pl
Importuje pliki StarOffice 5.x.

# abiT602
%package plugin-t602
Summary:	AbiWord T602 plugin
Summary(pl):	Wtyczka T602 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-t602
Import T602 files.

%description plugin-t602 -l pl
Importuje pliki T602.

# abiWMF
%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl):	Wtyczka WMF dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wmf
View Windows Metafiles.

%description plugin-wmf -l pl
Wy¶wietla pliki typu Windows Metafiles.

# abiWML
%package plugin-wml
Summary:	AbiWord WML plugin
Summary(pl):	Wtyczka WML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wml
Import/export WML files.

%description plugin-wml -l pl
Importuje/eksportuje pliki WML.

# abiWordPerfect
%package plugin-wordperfect
Summary:	AbiWord WordPerfect plugin
Summary(pl):	Wtyczka WordPerfect dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wordperfect
Import/export Corel WordPerfect files.

%description plugin-wordperfect -l pl
Importuje/eksportuje pliki formatu Corel WordPerfect.

# abiXHTML
%package plugin-xhtml
Summary:	AbiWord XHTML plugin
Summary(pl):	Wtyczka XHTML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xhtml
Import HTML/multipart HTML.

%description plugin-xhtml -l pl
Importuje pliki HTML/wieloczê¶ciowy HTML.

# abiXSLFO 
%package plugin-xslfo
Summary:	AbiWord XSLFO plugin
Summary(pl):	Wtyczka XSLFO dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xslfo
Import/export XSL-FO.

%description plugin-xslfo -l pl
Importuje/eksportuje XSL-FO.

# no one knows category
# abiCAPI 
%package plugin-capi
Summary:	AbiWord CAPI plugin
Summary(pl):	Wtyczka CAPI dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-capi
CAPI plugin.

%description plugin-capi -l pl
Wtyczka CAPI.

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
%patch2 -p1

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
#%{__libtoolize}
#%{__aclocal} -I ac-helpers
#%{__automake}
#%{__autoconf}
./nextgen.sh
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
%{_libdir}/AbiWord-%{mver}/plugins/AbiWord

%files plugin-aiksaurus 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiAikSaurus.so

%files plugin-babelfish
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBabelfish.so

%files plugin-capi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCAPI.so

%files plugin-command
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCommand.so

%files plugin-dash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiDash.so

%files plugin-freetranslation
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiFreeTranslation.so

%files plugin-gda
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGDA.so

%files plugin-gdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGdict.so

%files plugin-gimp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGimp.so

%files plugin-google
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGoogle.so

%files plugin-gypsython
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGypsython.so

%files plugin-ots
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOTS.so

%files plugin-referee
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiReferee.so

%files plugin-scripthappy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiScriptHappy.so

%files plugin-urldict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiURLDict.so

%files plugin-wikipedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWikipedia.so

%files plugin-applix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiApplix.so

%files plugin-bmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBMP.so

%files plugin-bz2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiBZ2.so

%files plugin-clarisworks
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiClarisWorks.so

#%files plugin-coquille
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiCoquille.so

%files plugin-docbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiDocBook.so

%files plugin-eml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiEML.so

%files plugin-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGdkPixbuf.so

%files plugin-hrtext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiHRText.so

%files plugin-hancom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiHancom.so

%files plugin-iscii
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiISCII.so

%files plugin-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiJPEG.so

%files plugin-kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiKWord.so

%files plugin-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiLaTeX.so

%files plugin-mif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMIF.so

%files plugin-mswrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMSWrite.so

%files plugin-magick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMagick.so

%files plugin-nroff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiNroff.so

%files plugin-openwritter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOpenWriter.so

%files plugin-palmdoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPalmDoc.so

%files plugin-passepartout
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPassepartout.so

%files plugin-psion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPsion.so

%files plugin-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiRSVG.so

%files plugin-sdw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiSDW.so

%files plugin-t602
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiT602.so

%files plugin-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWMF.so

%files plugin-wml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWML.so

%files plugin-wordperfect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiWordPerfect.so

%files plugin-xhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiXHTML.so

%files plugin-xslfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiXSLFO.so

%files clipart
%defattr(644,root,root,755)
%{_datadir}/AbiSuite-%{mver}/clipart
