# TODO: wordperfect support with libwpd 0.10, libwp[gs] 0.3
#
%bcond_without	evolution	# Evolution Data Server for contacts and calendar
%bcond_without	champlain	# champlain maps display support
%bcond_with	gda		# libgda (1.x) support
%bcond_without	goffice		# goffice plugin
%bcond_with	gnomevfs	# gnome-vfs support (GTK+ 2.x only)
%bcond_with	gtk2		# GTK+ 2.x instead of 3.x
%bcond_without	introspection	# GObject introspection
%bcond_without	ots		# Open Text Summarizer plugin
%bcond_without	redland		# redland/raptor libraries
%bcond_with	psiconv		# psiconv / psion plugin
%bcond_with	wordperfect	# wordperfect plugin
#
%define		mver	3.0
#
%if %{without gtk2}
%undefine	with_gnomevfs
%endif
Summary:	Multi-platform word processor
Summary(pl.UTF-8):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	3.0.5
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	a8f218b711450e4ccae43a0522e0e806
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-mht.patch
Patch2:		%{name}-librevenge.patch
Patch6:		%{name}-tidy.patch
Patch7:		%{name}-asio.patch
URL:		http://www.abisource.com/
BuildRequires:	aiksaurus-gtk-devel >= 1.2.1
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	boost-devel >= 1.40.0
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	eps-devel
%{?with_evolution:BuildRequires:	evolution-data-server-devel >= 3.6}
BuildRequires:	fontconfig-devel >= 1:2.3.95
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gnutls-devel
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.0.0}
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 2:2.12.0
%else
BuildRequires:	gtk+3-devel >= 3.0.8
%endif
BuildRequires:	gtkmathview-devel >= 0.7.6
# libchamplain-gtk compiler with matching GTK+ version
%{?with_champlain:BuildRequires:	libchamplain-devel >= 0.12}
%if %{with gda}
BuildRequires:	libgda-devel >= 1:1.2.4-16
BuildRequires:	libgnomedb-devel >= 1:1.2.0
%endif
%{?with_goffice:BuildRequires:	libgoffice-devel >= 0.10.2}
BuildRequires:	libgcrypt-devel >= 1.4.5
BuildRequires:	libgsf-devel >= 1.14.18
BuildRequires:	libical-devel >= 0.46
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librevenge-devel
BuildRequires:	librsvg-devel >= 1:2.16.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libwmf-devel >= 2:0.2.8.4
%{?with_wordperfect:BuildRequires:	libwpd-devel >= 0.9.0}
%{?with_wordperfect:BuildRequires:	libwpg-devel >= 0.2.0}
%{?with_wordperfect:BuildRequires:	libwps-devel >= 0.2.0}
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel
BuildRequires:	link-grammar-devel >= 5.1.0
BuildRequires:	loudmouth-devel >= 1.3.2
%{?with_ots:BuildRequires:	ots-devel >= 0.5.0}
BuildRequires:	pango-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	popt-devel
%{?with_psiconv:BuildRequires:	psiconv-devel >= 0.9.6}
%{?with_introspection:BuildRequires:	python >= 2}
%{?with_introspection:BuildRequires:	python-pygobject3 >= 3}
%{?with_redland:BuildRequires:	rasqal-devel >= 0.9.17}
BuildRequires:	readline-devel
%{?with_redland:BuildRequires:	redland-devel >= 1.0.10}
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
BuildRequires:	tidy-devel
BuildRequires:	telepathy-glib-devel >= 0.14.5
BuildRequires:	wv-devel >= 1.2.1
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires:	cairo >= 1.10
Requires:	enchant >= 1.2.6
%{?with_evolution:Requires:	evolution-data-server-libs >= 3.6}
Requires:	fontconfig >= 1:2.3.95
Requires:	fribidi >= 0.10.4
Requires:	glib2 >= 1:2.12.1
%if %{with gtk2}
Requires:	gtk+2 >= 2:2.12.0
%else
Requires:	gtk+3 >= 3.0.8
%endif
%{?with_champlain:Requires:	libchamplain >= 0.12}
Requires:	libgcrypt >= 1.4.5
%{?with_goffice:Requires:	libgoffice >= 0.10.2}
Requires:	libgsf >= 1.14.18
Requires:	libical >= 0.46
Requires:	librsvg >= 1:2.16.0
Requires:	libxml2 >= 1:2.6.26
%{?with_redland:Requires:	rasqal >= 0.9.17}
%{?with_redland:Requires:	redland >= 1.0.10}
Requires:	wv >= 1.2.1
Obsoletes:	abiword-plugin-applix
Obsoletes:	abiword-plugin-babelfish
Obsoletes:	abiword-plugin-bmp
Obsoletes:	abiword-plugin-bz2
Obsoletes:	abiword-plugin-capi
Obsoletes:	abiword-plugin-clarisworks
Obsoletes:	abiword-plugin-coquille
Obsoletes:	abiword-plugin-dash
Obsoletes:	abiword-plugin-docbook
Obsoletes:	abiword-plugin-eml
Obsoletes:	abiword-plugin-freetranslation
%{!?with_gda:Obsoletes:	abiword-plugin-gda}
Obsoletes:	abiword-plugin-gdict
Obsoletes:	abiword-plugin-gdkpixbuf
Obsoletes:	abiword-plugin-gimp
%{!?with_goffice:Obsoletes:	abiword-plugin-goffice}
Obsoletes:	abiword-plugin-google
Obsoletes:	abiword-plugin-gypsython
Obsoletes:	abiword-plugin-hancom
Obsoletes:	abiword-plugin-hrtext
Obsoletes:	abiword-plugin-iscii
Obsoletes:	abiword-plugin-jpeg
Obsoletes:	abiword-plugin-kword
Obsoletes:	abiword-plugin-magick
Obsoletes:	abiword-plugin-mif
Obsoletes:	abiword-plugin-mswrite
Obsoletes:	abiword-plugin-nroff
Obsoletes:	abiword-plugin-opendocument
Obsoletes:	abiword-plugin-openwritter
Obsoletes:	abiword-plugin-palmdoc
Obsoletes:	abiword-plugin-passepartout
Obsoletes:	abiword-plugin-pdf
Obsoletes:	abiword-plugin-referee
Obsoletes:	abiword-plugin-rsvg
Obsoletes:	abiword-plugin-scripthappy
Obsoletes:	abiword-plugin-sdw
Obsoletes:	abiword-plugin-t602
Obsoletes:	abiword-plugin-urldict
Obsoletes:	abiword-plugin-wikipedia
%{!?with_wordperfect:Obsoletes:	abiword-plugin-wordperfect}
Obsoletes:	abiword-plugin-wml
Obsoletes:	abiword-plugin-xhtml
Obsoletes:	abiword-plugin-xslfo
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

%package -n python-abiword
Summary:	Python GObject binding for AbiWord library
Summary(pl.UTF-8):	Wiązanie Pythona i GObject do biblioteki AbiWorda
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-pygobject3 >= 3

%description -n python-abiword
Python GObject binding for AbiWord library.

%description -n python-abiword -l pl.UTF-8
Wiązanie Pythona i GObject do biblioteki AbiWorda.

# plugins - tools
%package plugin-aiksaurus
Summary:	AbiWord Aiksaurus plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda Aiksaurus
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	aiksaurus-gtk >= 1.2.1

%description plugin-aiksaurus
Allows to use Aiksaurus thesaurus.

%description plugin-aiksaurus -l pl.UTF-8
Wtyczka ta pozwala na użycie Aiksaurusa - słownika wyrazów
bliskoznacznych.

%package plugin-collab
Summary:	Remote collaborate for AbiWord
Summary(pl.UTF-8):	Zdalna współpraca dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dbus-glib >= 0.70
Requires:	loudmouth >= 1.3.2
Requires:	telepathy-glib >= 0.14.5

%description plugin-collab
Allows to collaborate with a remote user.

%description plugin-collab -l pl.UTF-8
Wtyczka pozwalająca na współpracę z innym użytkownikiem przez sieć.

%package plugin-command
Summary:	AbiWord command line control
Summary(pl.UTF-8):	Konrolowanie AbiWorda z linii poleceń
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-command
Allows command line control of AbiWord.

%description plugin-command -l pl.UTF-8
Wtyczka ta pozwala na kontrolowanie AbiWorda z poziomu linii poleceń.

%package plugin-gda
Summary:	AbiWord GDA plugin
Summary(pl.UTF-8):	Wtyczka AbiWorda dla GDA
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gnome-database-access-properties >= 1:1.2.1
Requires:	libgda >= 1:1.2.4-16
Requires:	libgnomedb >= 1:1.2.0

%description plugin-gda
Allows access to any database provided by libgda.

%description plugin-gda -l pl.UTF-8
Wtyczka ta pozwala na połączenie z dowolną bazą danych dostarczaną za
pośrednictwem libgda.

%package plugin-goffice
Summary:	GNOME Office plugin
Summary(pl.UTF-8):	Wtyczka GNOME Office
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgoffice >= 0.10.2

%description plugin-goffice
Allows to share GNOME Office objects between GOffice appplications.

%description plugin-goffice -l pl.UTF-8
Pozwala na współdzielenie obiektów GNOME Office pomiędzy jego
aplikacjami.

%package plugin-mathview
Summary:	AbiWord MathView plugin
Summary(pl.UTF-8):	Wtyczka MAthView dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtkmathview-devel >= 0.7.6

%description plugin-mathview
MathML or LaTeX style equation inserting and editing.

%description plugin-mathview -l pl.UTF-8
Pozwala na wstawianie i edycję równań w stylu MathML lub LaTeX.

%package plugin-ots
Summary:	AbiWord OTS plugin
Summary(pl.UTF-8):	Wtyczka OTS dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	ots >= 0.5.0

%description plugin-ots
Create document summaries.

%description plugin-ots -l pl.UTF-8
Wtyczka ta służy do tworzenia podsumowania dokumentu.

# plugins import - export
%package plugin-latex
Summary:	AbiWord LaTeX plugin
Summary(pl.UTF-8):	Wtyczka LaTeX dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-latex
LaTeX export.

%description plugin-latex -l pl.UTF-8
Wtyczka ta służy do eksportu do LaTeXa.

%package plugin-link-grammar
Summary:	AbiWord Link Grammar plugin
Summary(pl.UTF-8):	Wtyczka Gramatyki dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	link-grammar >= 5.1.0

%description plugin-link-grammar
AbiWord Link Grammar plugin.

%description plugin-link-grammar -l pl.UTF-8
Wtyczka Gramatyki dla Abiworda.

%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl.UTF-8):	Wtyczka Psion dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	psiconv >= 0.9.6

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Psiona.

%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl.UTF-8):	Wtyczka WMF dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libwmf >= 2:0.2.8.4

%description plugin-wmf
View Windows Metafiles.

%description plugin-wmf -l pl.UTF-8
Wtyczka ta służy do wyświetlania plików typu Windows Metafile.

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch6 -p1
%patch7 -p1

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-clipart \
	%{?with_introspection:--enable-introspection} \
	--enable-plugins=auto \
	--enable-templates \
	--with-champlain%{!?with_champlain:=no} \
	--with-evolution-data-server%{!?with_evolution:=no} \
	--with-gnomevfs%{!?with_gnomevfs:=no} \
	--with-goffice%{!?with_goffice:=no} \
	%{?with_gtk2:--with-gtk2} \
	--with-redland%{!?with_redland:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove useless files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/abiword-%{mver}/plugins/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%if %{with introspection}
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abiword
%attr(755,root,root) %{_libdir}/libabiword-%{mver}.so
%if %{with introspection}
%{_libdir}/girepository-1.0/Abi-%{mver}.typelib
%endif
%dir %{_libdir}/abiword-%{mver}
%dir %{_libdir}/abiword-%{mver}/plugins
%dir %{_datadir}/abiword-%{mver}
%{_datadir}/abiword-%{mver}/Presentation.xml
%{_datadir}/abiword-%{mver}/readme.abw
%{_datadir}/abiword-%{mver}/readme.txt
%{_datadir}/abiword-%{mver}/system.profile*
%{_datadir}/abiword-%{mver}/certs
%{_datadir}/abiword-%{mver}/mime-info
%{_datadir}/abiword-%{mver}/omml_xslt
%{_datadir}/abiword-%{mver}/strings
%{_datadir}/abiword-%{mver}/templates
%{_datadir}/abiword-%{mver}/ui
%{_datadir}/abiword-%{mver}/xsltml
%{_datadir}/appdata/abiword.appdata.xml
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.AbiCollab.service
%{_desktopdir}/abiword.desktop
%{_iconsdir}/hicolor/*/apps/abiword.*
%{_mandir}/man1/abiword.1*
%{_datadir}/telepathy/clients/AbiCollab.client

# These don't add any additional dependencies so there's no reason to split
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/applix.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/babelfish.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/bmp.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/clarisworks.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/docbook.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/eml.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/epub.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/freetranslation.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/garble.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/gdict.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/gimp.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/google.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/hancom.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/hrtext.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/iscii.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/kword.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/loadbindings.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/mht.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/mif.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/mswrite.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/opml.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/opendocument.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/openwriter.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/openxml.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/paint.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/passepartout.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/pdb.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/pdf.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/presentation.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/s5.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/sdw.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/t602.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/urldict.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wikipedia.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wml.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/xslfo.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/abiword-%{mver}
%if %{with introspection}
%{_datadir}/gir-1.0/Abi-3.0.gir
%endif
%{_pkgconfigdir}/abiword-%{mver}.pc

%if %{with introspection}
%files -n python-abiword
%defattr(644,root,root,755)
%{py_sitedir}/gi/overrides/Abi.py[co]
%endif

%files plugin-aiksaurus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/aiksaurus.so
%attr(755,root,root) %{_libdir}/libAiksaurusGtk3--export-dynamic.so
%attr(755,root,root) %{_libdir}/libAiksaurusGtk3.so

%files plugin-collab
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/collab.so

%files plugin-command
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/command.so

%if %{with gda}
%files plugin-gda
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/gda.so
%endif

%if %{with goffice}
%files plugin-goffice
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/goffice.so
%endif

%files plugin-mathview
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/mathview.so

%if %{with ots}
%files plugin-ots
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/ots.so
%endif

%files plugin-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/latex.so

%files plugin-link-grammar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/grammar.so

%if %{with psiconv}
%files plugin-psion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/psion.so
%endif

%files plugin-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wmf.so

%if %{with wordperfect}
%files plugin-wordperfect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wordperfect.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wpg.so
%endif

%files clipart
%defattr(644,root,root,755)
%{_datadir}/abiword-%{mver}/clipart
