#
# TODO:
# - installed, but unpackaged files
#	   /usr/share/mime-info/abiword.keys
#
%bcond_without	gda		# libgda support
%bcond_with	goffice		# without plugin-goffice
%bcond_without	gnome		# without GNOME libs
%bcond_with	gnomevfs	# gnome-vfs support
%bcond_with	ots		# try build plugin-ots (requires ots >= 0.5.0)
#
%define		mver	2.8
#
Summary:	Multi-platform word processor
Summary(pl.UTF-8):	Wieloplatformowy procesor tekstu
Name:		abiword
Version:	2.8.6
Release:	16
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://www.abisource.com/downloads/abiword/%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	f883b0a7f26229a9c66fd6a1a94381aa
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-mht.patch
Patch2:		%{name}-libwpd.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-libpng15.patch
Patch5:		glib.patch
Patch6:		%{name}-format-security.patch
URL:		http://www.abisource.com/
BuildRequires:	aiksaurus-gtk-devel >= 1.2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	enchant-devel >= 1.2.6
BuildRequires:	eps-devel
BuildRequires:	fontconfig-devel >= 1:2.3.95
BuildRequires:	fribidi-devel >= 0.10.4
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtkmathview-devel >= 0.7.6
BuildRequires:	gucharmap-devel >= 1.7.0
%if %{with gda}
BuildRequires:	libgda-devel >= 1:1.2.4-16
BuildRequires:	libgnomedb-devel >= 1:1.2.0
%else
Obsoletes:	abiword-plugin-gda
%endif
BuildRequires:	libgnomeui-devel >= 2.15.91
%if %{with goffice}
BuildRequires:	libgoffice-devel >= 0.8.0
%else
Obsoletes:	abiword-plugin-goffice
%endif
BuildRequires:	libgsf-devel >= 1.14.9
#%{?with_gnomevfs:BuildRequires:	libgsf-gnome-devel >= 1.14.1}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.16.0
BuildRequires:	libtool
BuildRequires:	libwmf-devel >= 2:0.2.8.4
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel >= 0.2.0
BuildRequires:	libwps-devel >= 0.2.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	link-grammar-devel >= 4.2.1
BuildRequires:	loudmouth-devel >= 1.0.1
%{?with_ots:BuildRequires:	ots-devel >= 0.5.0}
BuildRequires:	pango-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	popt-devel
BuildRequires:	psiconv-devel >= 0.9.6
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	t1lib-devel
BuildRequires:	wv-devel >= 1.2.1
Requires(post,postun):	desktop-file-utils
Obsoletes:	abiword-plugin-applix
Obsoletes:	abiword-plugin-babelfish
Obsoletes:	abiword-plugin-bmp
Obsoletes:	abiword-plugin-bz2
Obsoletes:	abiword-plugin-capi
Obsoletes:	abiword-plugin-clarisworks
Obsoletes:	abiword-plugin-dash
Obsoletes:	abiword-plugin-docbook
Obsoletes:	abiword-plugin-eml
Obsoletes:	abiword-plugin-freetranslation
Obsoletes:	abiword-plugin-gdict
Obsoletes:	abiword-plugin-gdkpixbuf
Obsoletes:	abiword-plugin-gimp
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

# plugins - tools
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

%package plugin-collab
Summary:	Remote collaborate for AbiWord
Summary(pl.UTF-8):	Zdalna współpraca dla AbiWorda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%description plugin-mathview
MathML or LaTeX style equation inserting and editing.

%description plugin-mathview -l pl.UTF-8
Pozwala na wstawianie i edycję równań w stylu MathML lub LaTeX.

%package plugin-ots
Summary:	AbiWord OTS plugin
Summary(pl.UTF-8):	Wtyczka OTS dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-ots
Create document summaries.

%description plugin-ots -l pl.UTF-8
Wtyczka ta służy do tworzenia podsumowania dokumentu.

# plugins import - export
%package plugin-coquille
Summary:	AbiWord Coquille plugin
Summary(pl.UTF-8):	Wtyczka Coquille dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-coquille
Docbook extensions.

%description plugin-coquille -l pl.UTF-8
Rozszerzenia Docbooka.

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

%description plugin-link-grammar
AbiWord Link Grammar plugin.

%description plugin-link-grammar -l pl.UTF-8
Wtyczka Gramatyki dla Abiworda.

%package plugin-psion
Summary:	AbiWord Psion plugin
Summary(pl.UTF-8):	Wtyczka Psion dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description plugin-psion
Import/export Psion files.

%description plugin-psion -l pl.UTF-8
Wtyczka ta służy do importu/eksportu plików Psiona.

%package plugin-wmf
Summary:	AbiWord WMF plugin
Summary(pl.UTF-8):	Wtyczka WMF dla Abiworda
Group:		X11/Applications/Editors
Requires:	%{name} = %{epoch}:%{version}-%{release}

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# use generic icon name
%{__sed} -i -e 's|abiword_48.png|abiword.png|' Makefile.am
%{__sed} -i -e 's|abiword_48|abiword|' src/wp/ap/gtk/ap_UnixFrameImpl.cpp
mv abiword_48.png abiword.png

%build
%{__aclocal} -I .
%{__automake}
%{__autoconf}
%configure \
	--with-gnomevfs=%{?with_gnomevfs:yes}%{!?with_gnomevfs:no} \
	--with-goffice=%{?with_goffice:yes}%{!?with_goffice:no} \
	--disable-static \
	--enable-clipart \
	--enable-plugins=auto \
	--enable-printing \
	--enable-scripting \
	--enable-templates \
	--enable-threads \
	--with-libxml2 \
	--with-pspell \
	--with-sys-wv

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

# Remove useless files
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/abiword-%{mver}/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libabiword-%{mver}.so
%dir %{_libdir}/abiword-%{mver}
%dir %{_libdir}/abiword-%{mver}/plugins
%dir %{_datadir}/abiword-%{mver}
%{_datadir}/abiword-%{mver}/Presentation.xml
%{_datadir}/abiword-%{mver}/readme.abw
%{_datadir}/abiword-%{mver}/readme.txt
%{_datadir}/abiword-%{mver}/strings
%{_datadir}/abiword-%{mver}/system.profile*
%{_datadir}/abiword-%{mver}/templates
%{_datadir}/abiword-%{mver}/ui
%{_datadir}/abiword-%{mver}/xsltml
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/abiword.1*

# These don't add any additional dependencies so there's no reason to split
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/applix.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/babelfish.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/bmp.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/clarisworks.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/docbook.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/eml.so
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
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wpg.so
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/xslfo.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libabiword-%{mver}.la
%{_includedir}/abiword-%{mver}
%{_pkgconfigdir}/abiword-%{mver}.pc

%files plugin-aiksaurus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/aiksaurus.so

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

%files plugin-psion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/psion.so

%files plugin-wmf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wmf.so

%files plugin-wordperfect
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/abiword-%{mver}/plugins/wordperfect.so

%files clipart
%defattr(644,root,root,755)
%{_datadir}/abiword-%{mver}/clipart
