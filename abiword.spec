#
# TODO:
# - complete descriptions
# - fix broken bconds
#
#%bcond_without	gnome	# without GNOME libs
#%bcond_without	gda	# libgda support
#
%define		mver	2.4
#
Summary:	Multi-platform word processor
Summary(pl):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	2.4.6
Release:	0.2
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.bz2
# Source0-md5:	8ed5fb282b9741aca75b9e47500d39a1
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-mailmerge.patch
Patch3:		%{name}-poppler05x.patch
Patch4:		%{name}-goffice03.patch
Patch5:		%{name}-eps15.patch
URL:		http://www.abisource.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	aiksaurus-gtk-devel >= 1.2.1
BuildRequires:	aspell-devel >= 0.60.4
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	eps-devel >= 1.5
BuildRequires:	fontconfig-devel >= 1:2.3.95
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	gtkmathview-devel >= 0.7.6
BuildRequires:	gucharmap-devel >= 1.7.0
BuildRequires:	libgda-devel >= 1:1.2.3
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomedb-devel >= 1:1.2.2
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libgoffice-devel >= 0.3.1
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.15.90
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 2:0.2.8.4
BuildRequires:	libwpd-devel >= 0.8.5
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	link-grammar-devel >= 4.2.1
BuildRequires:	ots-devel >= 0.4.1
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	poppler-glib-devel >= 0.5.3
BuildRequires:	popt-devel
BuildRequires:	psiconv-devel >= 0.9.6
BuildRequires:	t1lib-devel
BuildRequires:	wv-devel >= 1.2.1
Obsoletes:	abiword-plugin-collab
Obsoletes:	abiword-plugin-gdkpixbuf
Obsoletes:	abiword-plugin-gypsython
Obsoletes:	abiword-plugin-magick
Obsoletes:	abiword-plugin-referee
Obsoletes:	abiword-plugins-impexp
Obsoletes:	abiword-plugins-tools
Requires(post,postun):	desktop-file-utils
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
Wtyczka ta pozwala na u¿ycie Aiksaurusa - s³ownika wyrazów
bliskoznacznych.

# abiBabelfish
%package plugin-babelfish
Summary:	AbiWord Babelfish plugin
Summary(pl):	Wtyczka AbiWorda Babelfish
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-babelfish
Allows to translate selected text.

%description plugin-babelfish -l pl
Wtyczka ta pozwala na przet³umaczenie wybranego tekstu.

# abiCommand plugin
%package plugin-command
Summary:	AbiWord command line control
Summary(pl):	Konrolowanie AbiWorda z linii poleceñ
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-command
Allows command line control of AbiWord.

%description plugin-command -l pl
Wtyczka ta pozwala na kontrolowanie AbiWorda z poziomu linii poleceñ.

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
Wtyczka ta pozwala przet³umaczyæ wybrany tekst.

# abiGDA
%package plugin-gda
Summary:	AbiWord GDA plugin
Summary(pl):	Wtyczka AbiWorda dla GDA
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-database-access-properties >= 1:1.2.1

%description plugin-gda
Allows access to any database provided by libgda.

%description plugin-gda -l pl
Wtyczka ta pozwala na po³±czenie z dowoln± baz± danych dostarczan± za
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
Wtyczka ta s³u¿y do wyszukiwania definicji w zaznaczonym fragmencie
tekstu.

# abiGimp plugin
%package plugin-gimp
Summary:	AbiWord image editor plugin
Summary(pl):	Wtyczka AbiWorda dla edytorów obrazu
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gimp
Allows to edit embedded images with a paint program like Gimp.

%description plugin-gimp -l pl
Wtyczka ta pozwala na edycjê osadzonych obrazów programem do ich
obróbki, takim jak Gimp.

# abiGOChart plugin
%package plugin-goffice
Summary:	GNOME Office plugin
Summary(pl):	Wtyczka GNOME Office
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-goffice
Allows to share GNOME Office objects between GOffice
appplications.

%description plugin-goffice -l pl
Pozwala na wspó³dzielenie obiektów GNOME Office pomiêdzy jego
aplikacjami.

# abiGoogle
%package plugin-google
Summary:	AbiWord Google plugin
Summary(pl):	Wtyczka Google dla AbiWorda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-google
Search Google for selected text.

%description plugin-google -l pl
Wtyczka ta s³u¿y do przeszukiwania Google w poszukiwaniu zaznaczonego
tekstu.

# abiMathView
%package plugin-mathview
Summary:	AbiWord MathView plugin
Summary(pl):	Wtyczka MAthView dla AbiWorda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mathview
MathML or LaTeX style equation inserting and editing.

%description plugin-mathview -l pl
Pozwala na wstawianie i edycjê równañ w stylu MathML lub LaTeX.

# abiOTS
%package plugin-ots
Summary:	AbiWord OTS plugin
Summary(pl):	Wtyczka OTS dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ots
Create document summaries.

%description plugin-ots -l pl
Wtyczka ta s³u¿y do tworzenia podsumowania dokumentu.

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
Wtyczka ta s³u¿y do przeszukiwania Wikipedii w poszukiwaniu
zaznaczonego tekstu.

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
Wtyczka ta s³u¿y do importu/eksportu plików Applix Worda.

# abiBMP
%package plugin-bmp
Summary:	AbiWord BMP plugin
Summary(pl):	Wtyczka BMP dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bmp
View Bitmap Images.

%description plugin-bmp -l pl
Wtyczka ta s³u¿y do wy¶wietlania bitmap.

# abiBZ2
%package plugin-bz2
Summary:	AbiWord BZ2 plugin
Summary(pl):	Wtyczka BZ2 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bz2
Import/export bzip2 compressed AbiWord files.

%description plugin-bz2 -l pl
Wtyczka ta s³u¿y do importu/eksportu plików Abiworda spakowanych przy
pomocy bzip2.

# abiClarisWorks
%package plugin-clarisworks
Summary:	AbiWord ClarisWorks plugin
Summary(pl):	Wtyczka ClarisWorks dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-clarisworks
Import/export Clarisworks files.

%description plugin-clarisworks -l pl
Wtyczka ta s³u¿y do importu/eksportu plików Clarisworks.

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
Wtyczka ta s³u¿y do importu/eksportu plików zapisanych w formacie
Docbook.

# abiEML
%package plugin-eml
Summary:	AbiWord EML plugin
Summary(pl):	Wtyczka EML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-eml
Import/export as MS Outlook Email files.

%description plugin-eml -l pl
Wtyczka ta s³u¿y do importu/eksportu plików poczty programu MS
Outlook.

# abiHRText
%package plugin-hrtext
Summary:	AbiWord HRText plugin
Summary(pl):	Wtyczka HRText dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hrtext
Export text with "newsgroup" markup.

%description plugin-hrtext -l pl
Wtyczka ta s³u¿y do eksportu ze znacznikiem "grupa news".

# abiHancom
%package plugin-hancom
Summary:	AbiWord Hancom plugin
Summary(pl):	Wtyczka Hancom dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hancom
Hancom Word Importer.

%description plugin-hancom -l pl
Wtyczka ta s³u¿y jest importerem formatu Hancom Word.

# abiISCII
%package plugin-iscii
Summary:	AbiWord ISCII plugin
Summary(pl):	Wtyczka dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-iscii
Import/export ISCII text files (Indic script).

%description plugin-iscii -l pl
Wtyczka ta s³u¿y do importu/eksportu plików tekstowych w kodowaniu
ISCII (Indic script).

# abiJPEG
%package plugin-jpeg
Summary:	AbiWord JPEG plugin
Summary(pl):	Wtyczka JPEG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-jpeg
View JPEG Images.

%description plugin-jpeg -l pl
Wtyczka ta s³u¿y do wy¶wietlania obrazów w formacie JPEG.

# abiKWord
%package plugin-kword
Summary:	AbiWord KWord plugin
Summary(pl):	Wtyczka KWord dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-kword
KWord import/export.

%description plugin-kword -l pl
Wtyczka ta s³u¿y do importu/eksportu plików KWorda.

# abiLaTeX
%package plugin-latex
Summary:	AbiWord LaTeX plugin
Summary(pl):	Wtyczka LaTeX dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-latex
LaTeX export.

%description plugin-latex -l pl
Wtyczka ta s³u¿y do eksportu do LaTeXa.

# AbiGrammar
%package plugin-link-grammar
Summary:	AbiWord Link Grammar plugin
Summary(pl):	Wtyczka Gramatyki dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-link-grammar
AbiWord Link Grammar plugin.

%description plugin-link-grammar -l pl
Wtyczka Gramatyki dla Abiworda.

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
Wtyczka ta s³u¿y do importu plików MS Write'a.

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

# abiOpenDocument
%package plugin-opendocument
Summary:	AbiWord OpenDocument plugin
Summary(pl):	Wtyczka OpenDocument dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-opendocument
Import/export OpenDocument files.

%description plugin-opendocument -l pl
Wtyczka ta s³u¿y do importu/eksportu plików OpenDocument.

# abiOpenWriter
%package plugin-openwritter
Summary:	AbiWord OpenWriter plugin
Summary(pl):	Wtyczka OpenWriter dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openwritter
Import/export OpenOffice files.

%description plugin-openwritter -l pl
Wtyczka ta s³u¿y do importu/eksportu plików OpenOffice'a.

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

# abiPDF
%package plugin-pdf
Summary:	AbiWord PDF plugin
Summary(pl):	Wtyczka PDF dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-pdf
Exports documents to PDF format.

%description plugin-pdf -l pl
Eksportuje dokumenty do formatu PDF.

# abiPsion
%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl):	Wtyczka Psion dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl
Wtyczka ta s³u¿y do importu/eksportu plików Psiona.

# abiRSVG
%package plugin-rsvg
Summary:	AbiWord RSVG plugin
Summary(pl):	Wtyczka RSVG dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-rsvg
View Scalable Vector Graphics.

%description plugin-rsvg -l pl
Wtyczka ta s³u¿y do wy¶wietlania plików SVG.

# abiSDW
%package plugin-sdw
Summary:	AbiWord SDW plugin
Summary(pl):	Wtyczka SDW dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sdw
Import StarOffice 5.x files.

%description plugin-sdw -l pl
Wtyczka ta s³u¿y do importu plików StarOffice'a 5.x.

# abiT602
%package plugin-t602
Summary:	AbiWord T602 plugin
Summary(pl):	Wtyczka T602 dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-t602
Import T602 files.

%description plugin-t602 -l pl
Wtyczka ta s³u¿y do importu plików T602.

# abiWMF
%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl):	Wtyczka WMF dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wmf
View Windows Metafiles.

%description plugin-wmf -l pl
Wtyczka ta s³u¿y do wy¶wietlania plików typu Windows Metafile.

# abiWML
%package plugin-wml
Summary:	AbiWord WML plugin
Summary(pl):	Wtyczka WML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wml
Import/export WML files.

%description plugin-wml -l pl
Wtyczka ta s³u¿y do importu/eksportu plików WML.

# abiWordPerfect
%package plugin-wordperfect
Summary:	AbiWord WordPerfect plugin
Summary(pl):	Wtyczka WordPerfect dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wordperfect
Import/export Corel WordPerfect files.

%description plugin-wordperfect -l pl
Wtyczka ta s³u¿y do importu/eksportu plików w formacie Corel
WordPerfect.

# abiXHTML
%package plugin-xhtml
Summary:	AbiWord XHTML plugin
Summary(pl):	Wtyczka XHTML dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xhtml
Import HTML/multipart HTML.

%description plugin-xhtml -l pl
Wtyczka ta s³u¿y do importu plików HTML/wieloczê¶ciowego HTML.

# abiXSLFO 
%package plugin-xslfo
Summary:	AbiWord XSLFO plugin
Summary(pl):	Wtyczka XSLFO dla Abiworda
Group:		Applications/Productivity
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xslfo
Import/export XSL-FO.

%description plugin-xslfo -l pl
Wtyczka ta s³u¿y do importu/eksportu XSL-FO.

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
%patch3 -p1
%patch5 -p1
%patch4 -p0

# use generic icon name
sed -i -e 's|abiword_48.png|abiword.png|' abi/GNUmakefile.am
mv abi/abiword_48.png abi/abiword.png

%build
cd abi
%{__aclocal} -I ac-helpers
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--enable-threads \
	--with-libxml2 \
	--with-pspell \
	--with-sys-wv

# see TODO	
#	--%{!?with_gnome:dis}%{?with_gnome:en}able-gnome \

%{__make}

cd ../abiword-plugins
./nextgen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C abiword-plugins install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C abi install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

# Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/AbiWord-%{mver}/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

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
%{_desktopdir}/*.desktop
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

%if %{with gda}
%files plugin-gda
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGDA.so
%endif

%files plugin-gdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGdict.so

%files plugin-gimp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGimp.so

%files plugin-goffice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGOChart.so

%files plugin-google
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGoogle.so

%files plugin-mathview
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMathView.so

%files plugin-ots
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOTS.so

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

%files plugin-docbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiDocBook.so

%files plugin-eml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiEML.so

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

%files plugin-link-grammar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiGrammar.so

%files plugin-mif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMIF.so

%files plugin-mswrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiMSWrite.so

%files plugin-nroff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiNroff.so

%files plugin-opendocument
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOpenDocument.so

%files plugin-openwritter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiOpenWriter.so

%files plugin-palmdoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPalmDoc.so

%files plugin-passepartout
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPassepartout.so

%files plugin-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/AbiWord-%{mver}/plugins/libAbiPDF.so

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
