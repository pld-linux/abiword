#
# TODO:
# - package new plugins
# - complete descriptions
# - fix broken bconds
# - consider subpackage for helps
# - installed, but unpackaged files
#	   /usr/share/mime-info/abiword.keys
#
%bcond_with	capi		# AbiCAPI plugin (disappeared)
%bcond_without	gda		# libgda support
%bcond_without	gnome		# without GNOME libs
%bcond_with	gnomevfs	# gnome-vfs support
%bcond_with	goffice		# try build plugin-goffice (requires goffice < 0.6.0)
%bcond_with	xhtml		# try build plugin-xhtml (compile error)
%bcond_with	ots		# try build plugin-ots (requires ots >= 0.5.0)
%bcond_with	dash		# try build plugin-dash (absolutly no idea)
%bcond_with	bz2		# try build plugin-bz2 (disappeared)
#
%define		mver	2.6
#
Summary:	Multi-platform word processor
Summary(pl.UTF-8):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	2.6.6
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	b9de84f03f555d4490b63e5b7f53e2f1
Source1:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-plugins-%{version}.tar.gz
# Source1-md5:	45dabc491976e3f21d943817e61b9d89
Source2:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-extras-%{version}.tar.gz
# Source2-md5:	15db5e3ffa5429d2ce773351fc6fdb72
Source3:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-docs-%{version}.tar.gz
# Source3-md5:	833129f266e699b3cf0f3774e005a312
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-home_etc.patch
Patch4:		%{name}-goffice05.patch
URL:		http://www.abisource.com/
BuildRequires:	aiksaurus-gtk-devel >= 1.2.1
BuildRequires:	aspell-devel >= 0.60.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	fontconfig-devel >= 1:2.3.95
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 1:2.12.1
#BuildRequires:	gnome-scan-devel < 0.6
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	gtkmathview-devel >= 0.7.6
BuildRequires:	gucharmap-devel >= 1.7.0
BuildRequires:	libgda-devel >= 1:1.2.3
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomedb-devel >= 1:1.2.2
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.15.91
%{?with_goffice:BuildRequires:	libgoffice-devel >= 0.6.0}
%{?with_gnomevfs:BuildRequires:	libgsf-gnome-devel >= 1.14.1}
BuildRequires:	libgsf-devel >= 1.14.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.15.90
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 2:0.2.8.4
BuildRequires:	libwpd-devel >= 0.8.5
BuildRequires:	libwpg-devel >= 0.1.0
BuildRequires:	libwps-devel >= 0.1.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	link-grammar-devel >= 4.2.1
BuildRequires:	loudmouth-devel >= 1.0.1
%{?with_ots:BuildRequires:	ots-devel >= 0.5.0}
BuildRequires:	perl-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	popt-devel
BuildRequires:	psiconv-devel >= 0.9.6
BuildRequires:	readline-devel
BuildRequires:	t1lib-devel
BuildRequires:	wv-devel >= 1.2.1
Requires(post,postun):	desktop-file-utils
Obsoletes:	abiword-plugin-gdkpixbuf
Obsoletes:	abiword-plugin-gypsython
Obsoletes:	abiword-plugin-magick
Obsoletes:	abiword-plugin-referee
Obsoletes:	abiword-plugins-impexp
Obsoletes:	abiword-plugins-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AbiWord is a multi-platform word processor with a GTK+ interface on
the UNIX platform.

%description -l pl.UTF-8
AbiWord jest wieloplatformowym procesorem tekstu z interfejsem GTK+ na
platformie UNIX.

%package devel
Summary:	Files for AbiWord plugins development
Summary(pl.UTF-8):	Pliki do tworzenia wtyczek dla AbiWorda
Group:		Development/Libraries
# doesn't require base

%description devel
Files for AbiWord plugins development.

%description devel -l pl.UTF-8
Pliki do tworzenia wtyczek dla AbiWorda.

# plugins - tools
# abiAiksaurus
%package plugin-aiksaurus
Summary:	AbiWord Aiksaurus plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda Aiksaurus
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-aiksaurus
Allows to use Aiksaurus thesaurus.

%description plugin-aiksaurus -l pl.UTF-8
Wtyczka ta pozwala na użycie Aiksaurusa - słownika wyrazów
bliskoznacznych.

# abiBabelfish
%package plugin-babelfish
Summary:	AbiWord Babelfish plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda Babelfish
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-babelfish
Allows to translate selected text.

%description plugin-babelfish -l pl.UTF-8
Wtyczka ta pozwala na przetłumaczenie wybranego tekstu.

# abiCollab plugin
%package plugin-collab
Summary:	Remote collaborate for AbiWord
Summary(pl):	Zdalna współpraca dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-collab
Allows to collaborate with a remote user.

%description plugin-collab -l pl
Wtyczka pozwalająca na współpracę z innym użytkownikiem przez sieć.

# abiCommand plugin
%package plugin-command
Summary:	AbiWord command line control
Summary(pl.UTF-8):	Konrolowanie AbiWorda z linii poleceń
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-command
Allows command line control of AbiWord.

%description plugin-command -l pl.UTF-8
Wtyczka ta pozwala na kontrolowanie AbiWorda z poziomu linii poleceń.

# abiDash - not documented
%package plugin-dash
Summary:	AbiWord Dash plugin
Summary(pl.UTF-8):	Wtyczka Dash dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-dash
Dash plugin.

%description plugin-dash -l pl.UTF-8
Wtyczka Dash.

# abiFreeTranslation
%package plugin-freetranslation
Summary:	AbiWord freetranslation.com plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda dla freetranslation.com
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-freetranslation
Allows to translate selected text.

%description plugin-freetranslation -l pl.UTF-8
Wtyczka ta pozwala przetłumaczyć wybrany tekst.

# abiGDA
%package plugin-gda
Summary:	AbiWord GDA plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda dla GDA
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-database-access-properties >= 1:1.2.1

%description plugin-gda
Allows access to any database provided by libgda.

%description plugin-gda -l pl.UTF-8
Wtyczka ta pozwala na połączenie z dowolną bazą danych dostarczaną za
pośrednictwem libgda.

# abiGdict
%package plugin-gdict
Summary:	AbiWord gDict plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda gDict
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gdict
Look up definitions of selected text.

%description plugin-gdict -l pl.UTF-8
Wtyczka ta służy do wyszukiwania definicji w zaznaczonym fragmencie
tekstu.

# abiGimp plugin
%package plugin-gimp
Summary:	AbiWord image editor plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda dla edytorów obrazu
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-gimp
Allows to edit embedded images with a paint program like Gimp.

%description plugin-gimp -l pl.UTF-8
Wtyczka ta pozwala na edycję osadzonych obrazów programem do ich
obróbki, takim jak Gimp.

# abiGOChart plugin
%package plugin-goffice
Summary:	GNOME Office plugin
Summary(pl.UTF-8):	Wtyczka GNOME Office
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-goffice
Allows to share GNOME Office objects between GOffice appplications.

%description plugin-goffice -l pl.UTF-8
Pozwala na współdzielenie obiektów GNOME Office pomiędzy jego
aplikacjami.

# abiGoogle
%package plugin-google
Summary:	AbiWord Google plugin
Summary(pl.UTF-8):	Wtyczka Google dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-google
Search Google for selected text.

%description plugin-google -l pl.UTF-8
Wtyczka ta służy do przeszukiwania Google w poszukiwaniu zaznaczonego
tekstu.

# abiMathView
%package plugin-mathview
Summary:	AbiWord MathView plugin
Summary(pl.UTF-8):	Wtyczka MAthView dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mathview
MathML or LaTeX style equation inserting and editing.

%description plugin-mathview -l pl.UTF-8
Pozwala na wstawianie i edycję równań w stylu MathML lub LaTeX.

# abiOTS
%package plugin-ots
Summary:	AbiWord OTS plugin
Summary(pl.UTF-8):	Wtyczka OTS dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ots
Create document summaries.

%description plugin-ots -l pl.UTF-8
Wtyczka ta służy do tworzenia podsumowania dokumentu.

# abiScriptHappy - not documented
%package plugin-scripthappy
Summary:	AbiWord ScriptHappy plugin
Summary(pl.UTF-8):	Wtyczka ScriptHappy dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-scripthappy
Plugin ScriptHappy.

%description plugin-scripthappy -l pl.UTF-8
Wtyczka ScriptHappy.

# abiURLDict
%package plugin-urldict
Summary:	AbiWord URLDict plugin
Summary(pl.UTF-8):	Wtyczka URLDict dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-urldict
Internet dictionary.

%description plugin-urldict -l pl.UTF-8
Słownik internetowy.

# abiWikipedia
%package plugin-wikipedia
Summary:	AbiWord Wikipedia plugin
Summary(pl.UTF-8):	Wtyczka Wikipedia dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wikipedia
Search Wikipedia for selected text.

%description plugin-wikipedia -l pl.UTF-8
Wtyczka ta służy do przeszukiwania Wikipedii w poszukiwaniu
zaznaczonego tekstu.

# plugins import - export
# abiApplix
%package plugin-applix
Summary:	AbiWord Applix plugin
Summary(pl.UTF-8):	Wtyczka Applix dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-applix
Import/export Applix Word files.

%description plugin-applix -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Applix Worda.

# abiBMP
%package plugin-bmp
Summary:	AbiWord BMP plugin
Summary(pl.UTF-8):	Wtyczka BMP dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bmp
View Bitmap Images.

%description plugin-bmp -l pl.UTF-8
Wtyczka ta służy do wyświetlania bitmap.

# abiBZ2
%package plugin-bz2
Summary:	AbiWord BZ2 plugin
Summary(pl.UTF-8):	Wtyczka BZ2 dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-bz2
Import/export bzip2 compressed AbiWord files.

%description plugin-bz2 -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Abiworda spakowanych przy
pomocy bzip2.

# abiClarisWorks
%package plugin-clarisworks
Summary:	AbiWord ClarisWorks plugin
Summary(pl.UTF-8):	Wtyczka ClarisWorks dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-clarisworks
Import/export Clarisworks files.

%description plugin-clarisworks -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Clarisworks.

# abiCoquille
%package plugin-coquille
Summary:	AbiWord Coquille plugin
Summary(pl.UTF-8):	Wtyczka Coquille dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-coquille
Docbook extensions.

%description plugin-coquille -l pl.UTF-8
Rozszerzenia Docbooka.

# abiDocBook
%package plugin-docbook
Summary:	AbiWord DocBook plugin
Summary(pl.UTF-8):	Wtyczka DocBook dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-docbook
Import/export Docbook files.

%description plugin-docbook -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików zapisanych w formacie
Docbook.

# abiEML
%package plugin-eml
Summary:	AbiWord EML plugin
Summary(pl.UTF-8):	Wtyczka EML dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-eml
Import/export as MS Outlook Email files.

%description plugin-eml -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików poczty programu MS
Outlook.

# abiHRText
%package plugin-hrtext
Summary:	AbiWord HRText plugin
Summary(pl.UTF-8):	Wtyczka HRText dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hrtext
Export text with "newsgroup" markup.

%description plugin-hrtext -l pl.UTF-8
Wtyczka ta służy do eksportu ze znacznikiem "grupa news".

# abiHancom
%package plugin-hancom
Summary:	AbiWord Hancom plugin
Summary(pl.UTF-8):	Wtyczka Hancom dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-hancom
Hancom Word Importer.

%description plugin-hancom -l pl.UTF-8
Wtyczka ta służy jest importerem formatu Hancom Word.

# abiISCII
%package plugin-iscii
Summary:	AbiWord ISCII plugin
Summary(pl.UTF-8):	Wtyczka dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-iscii
Import/export ISCII text files (Indic script).

%description plugin-iscii -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików tekstowych w kodowaniu
ISCII (Indic script).

# abiJPEG
%package plugin-jpeg
Summary:	AbiWord JPEG plugin
Summary(pl.UTF-8):	Wtyczka JPEG dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-jpeg
View JPEG Images.

%description plugin-jpeg -l pl.UTF-8
Wtyczka ta służy do wyświetlania obrazów w formacie JPEG.

# abiKWord
%package plugin-kword
Summary:	AbiWord KWord plugin
Summary(pl.UTF-8):	Wtyczka KWord dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-kword
KWord import/export.

%description plugin-kword -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików KWorda.

# abiLaTeX
%package plugin-latex
Summary:	AbiWord LaTeX plugin
Summary(pl.UTF-8):	Wtyczka LaTeX dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-latex
LaTeX export.

%description plugin-latex -l pl.UTF-8
Wtyczka ta służy do eksportu do LaTeXa.

# AbiGrammar
%package plugin-link-grammar
Summary:	AbiWord Link Grammar plugin
Summary(pl.UTF-8):	Wtyczka Gramatyki dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-link-grammar
AbiWord Link Grammar plugin.

%description plugin-link-grammar -l pl.UTF-8
Wtyczka Gramatyki dla Abiworda.

# abiMIF - not documented
%package plugin-mif
Summary:	AbiWord MIF plugin
Summary(pl.UTF-8):	Wtyczka MIF dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mif
MIF plugin.

%description plugin-mif -l pl.UTF-8
Wtyczka MIF.

# abiMSWrite
%package plugin-mswrite
Summary:	AbiWord MSWrite plugin
Summary(pl.UTF-8):	Wtyczka MSWrite dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-mswrite
Import MS Write files.

%description plugin-mswrite -l pl.UTF-8
Wtyczka ta służy do importu plików MS Write'a.

# abiNroff - lack of precise description (export?/import?)
%package plugin-nroff
Summary:	AbiWord Nroff plugin
Summary(pl.UTF-8):	Wtyczka Nroff dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-nroff
nroff/man file format.

%description plugin-nroff -l pl.UTF-8
Typy plików nroff/man.

# abiOpenDocument
%package plugin-opendocument
Summary:	AbiWord OpenDocument plugin
Summary(pl.UTF-8):	Wtyczka OpenDocument dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-opendocument
Import/export OpenDocument files.

%description plugin-opendocument -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików OpenDocument.

# abiOpenWriter
%package plugin-openwritter
Summary:	AbiWord OpenWriter plugin
Summary(pl.UTF-8):	Wtyczka OpenWriter dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-openwritter
Import/export OpenOffice files.

%description plugin-openwritter -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików OpenOffice'a.

# abiPalmDoc - not documented
%package plugin-palmdoc
Summary:	AbiWord PalmDoc plugin
Summary(pl.UTF-8):	Wtyczka PalmDoc dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-palmdoc
PalmDoc plugin.

%description plugin-palmdoc -l pl.UTF-8
Wtyczka PalmDoc.

# abiPassepartout - not documented
%package plugin-passepartout
Summary:	AbiWord Passepartout plugin
Summary(pl.UTF-8):	Wtyczka Passepartout dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-passepartout
Passepartout plugin.

%description plugin-passepartout -l pl.UTF-8
Wtyczka Passepartout.

# abiPDF
%package plugin-pdf
Summary:	AbiWord PDF plugin
Summary(pl.UTF-8):	Wtyczka PDF dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-pdf
Exports documents to PDF format.

%description plugin-pdf -l pl.UTF-8
Eksportuje dokumenty do formatu PDF.

# abiPsion
%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl.UTF-8):	Wtyczka Psion dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Psiona.

# abiRSVG
%package plugin-rsvg
Summary:	AbiWord RSVG plugin
Summary(pl.UTF-8):	Wtyczka RSVG dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-rsvg
View Scalable Vector Graphics.

%description plugin-rsvg -l pl.UTF-8
Wtyczka ta służy do wyświetlania plików SVG.

# abiSDW
%package plugin-sdw
Summary:	AbiWord SDW plugin
Summary(pl.UTF-8):	Wtyczka SDW dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-sdw
Import StarOffice 5.x files.

%description plugin-sdw -l pl.UTF-8
Wtyczka ta służy do importu plików StarOffice'a 5.x.

# abiT602
%package plugin-t602
Summary:	AbiWord T602 plugin
Summary(pl.UTF-8):	Wtyczka T602 dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-t602
Import T602 files.

%description plugin-t602 -l pl.UTF-8
Wtyczka ta służy do importu plików T602.

# abiWMF
%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl.UTF-8):	Wtyczka WMF dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wmf
View Windows Metafiles.

%description plugin-wmf -l pl.UTF-8
Wtyczka ta służy do wyświetlania plików typu Windows Metafile.

# abiWML
%package plugin-wml
Summary:	AbiWord WML plugin
Summary(pl.UTF-8):	Wtyczka WML dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wml
Import/export WML files.

%description plugin-wml -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików WML.

# abiWordPerfect
%package plugin-wordperfect
Summary:	AbiWord WordPerfect plugin
Summary(pl.UTF-8):	Wtyczka WordPerfect dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-wordperfect
Import/export Corel WordPerfect files.

%description plugin-wordperfect -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików w formacie Corel
WordPerfect.

# abiXHTML
%package plugin-xhtml
Summary:	AbiWord XHTML plugin
Summary(pl.UTF-8):	Wtyczka XHTML dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xhtml
Import HTML/multipart HTML.

%description plugin-xhtml -l pl.UTF-8
Wtyczka ta służy do importu plików HTML/wieloczęściowego HTML.

# abiXSLFO
%package plugin-xslfo
Summary:	AbiWord XSLFO plugin
Summary(pl.UTF-8):	Wtyczka XSLFO dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-xslfo
Import/export XSL-FO.

%description plugin-xslfo -l pl.UTF-8
Wtyczka ta służy do importu/eksportu XSL-FO.

# no one knows category
# abiCAPI
%package plugin-capi
Summary:	AbiWord CAPI plugin
Summary(pl.UTF-8):	Wtyczka CAPI dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-capi
CAPI plugin.

%description plugin-capi -l pl.UTF-8
Wtyczka CAPI.

%package clipart
Summary:	AbiWord Clipart
Summary(pl.UTF-8):	Cliparty dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description clipart
This is the clipart portfolio used by AbiWord.

%description clipart -l pl.UTF-8
Jest to teczka clipartów używanych przez AbiWorda.

%prep
%setup -q -a1 -a2 -a3
%patch0 -p1
# needs some work
#patch1 -p1

#patch4 -p0

# use generic icon name
sed -i -e 's|abiword_48.png|abiword.png|' GNUmakefile.am
mv abiword_48.png abiword.png

%build
%{__aclocal} -I ac-helpers
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--%{!?with_gnome:dis}%{?with_gnome:en}able-gnomeui \
	--%{!?with_gnomevfs:dis}%{?with_gnomevfs:en}able-gnomevfs \
	--enable-printing \
	--enable-scripting \
	--enable-threads \
	--with-libxml2 \
	--with-pspell \
	--with-sys-wv

%{__make}

cd abiword-plugins-%{version}
%{__libtoolize}
%{__aclocal} -I ac-helpers
%{__automake}
%{__autoconf}
%configure \
	--with-abiword=.. \
	%{!?with_goffice:--disable-abigoffice} \
	%{!?with_xhtml:--disable-xhtml}
%{__make}
cd ..

export PKG_CONFIG_PATH=`pwd`
cd abiword-extras-%{version}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}
cd ..

export PATH="$PATH:`pwd`/src/wp/main/unix"
cd abiword-docs-%{version}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C abiword-plugins-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

%{__make} -C abiword-extras-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C abiword-docs-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/abiword-%{mver}/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/abiword-%{mver}
%dir %{_libdir}/abiword-%{mver}/plugins
%dir %{_datadir}/abiword-%{mver}
%{_datadir}/abiword-%{mver}/Presentation.xml
%{_datadir}/abiword-%{mver}/dictionary
%{_datadir}/abiword-%{mver}/glade
%dir %{_datadir}/abiword-%{mver}/help
%{_datadir}/abiword-%{mver}/help/en-US
%lang(fr) %{_datadir}/abiword-%{mver}/help/fr-FR
%lang(pl) %{_datadir}/abiword-%{mver}/help/pl-PL
%{_datadir}/abiword-%{mver}/readme.abw
%{_datadir}/abiword-%{mver}/readme.txt
%{_datadir}/abiword-%{mver}/strings
%{_datadir}/abiword-%{mver}/system.profile*
%{_datadir}/abiword-%{mver}/templates
%{_datadir}/abiword-%{mver}/xsltml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

# XXX TODO: move to subpackages?
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiOPML.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiOpenXML.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiWPG.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libLoadBindings.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libPresentation.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/abiword-%{mver}
%{_pkgconfigdir}/abiword-%{mver}.pc

%files plugin-aiksaurus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiAikSaurus.so

%files plugin-babelfish
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiBabelfish.so

%if %{with capi}
%files plugin-capi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiCAPI.so
%endif

%files plugin-collab
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiCollab.so

%files plugin-command
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiCommand.so

%if %{with dash}
%files plugin-dash
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiDash.so
%endif

%files plugin-freetranslation
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiFreeTranslation.so

%if %{with gda}
%files plugin-gda
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGDA.so
%endif

%files plugin-gdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGdict.so

%files plugin-gimp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGimp.so

%if %{with goffice}
%files plugin-goffice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGOChart.so
%endif

%files plugin-google
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGoogle.so

%files plugin-mathview
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiMathView.so

%if %{with ots}
%files plugin-ots
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiOTS.so
%endif

%files plugin-scripthappy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiScriptHappy.so

%files plugin-urldict
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiURLDict.so

%files plugin-wikipedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiWikipedia.so

%files plugin-applix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiApplix.so

%files plugin-bmp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiBMP.so

%if %{with bz2}
%files plugin-bz2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiBZ2.so
%endif

%files plugin-clarisworks
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiClarisWorks.so

%files plugin-docbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiDocBook.so

%files plugin-eml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiEML.so

%files plugin-hrtext
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiHRText.so

%files plugin-hancom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiHancom.so

%files plugin-iscii
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiISCII.so

%files plugin-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiJPEG.so

%files plugin-kword
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiKWord.so

%files plugin-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiLaTeX.so

%files plugin-link-grammar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiGrammar.so

%files plugin-mif
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiMIF.so

%files plugin-mswrite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiMSWrite.so

%files plugin-nroff
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiNroff.so

%files plugin-opendocument
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiOpenDocument.so

%files plugin-openwritter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiOpenWriter.so

%files plugin-palmdoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiPalmDoc.so

%files plugin-passepartout
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiPassepartout.so

%files plugin-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiPDF.so

%files plugin-psion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiPsion.so

%files plugin-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiRSVG.so

%files plugin-sdw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiSDW.so

%files plugin-t602
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiT602.so

%files plugin-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiWMF.so

%files plugin-wml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiWML.so

%files plugin-wordperfect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiWordPerfect.so

%if %{with xhtml}
%files plugin-xhtml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiXHTML.so
%endif

%files plugin-xslfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/libAbiXSLFO.so

%files clipart
%defattr(644,root,root,755)
%{_datadir}/abiword-%{mver}/clipart
