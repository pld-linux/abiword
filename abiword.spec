# TODO:
#    - split into subpackages (plugins)
#    - use external wv library
Summary:	AbiWord - advanced wordprocessor
Summary(pl):	AbiWord - zaawansowany procesor tekstu
Name:		abiword
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/abiword/%{name}-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/abiword/abiword-plugins.tar.gz
Source2:	%{name}.desktop
URL:		http://www.abisource.com/
BuildRequires:	Aiksaurus-devel
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake >= 1.5-8
BuildRequires:	bonobo-devel
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel >= 1.2.7
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:  libltdl-devel
BuildRequires:	pspell-devel
BuildRequires:	readline-devel
BuildRequires:	zipios++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
AbiWord is a free word processing program similar to Microsoft Word.
It is suitable for typing papers, letters, reports, memos, and so
forth.

%description -l pl
AbiWord jest darmowym procesorem tekstu podobnym do Microsoft Word.
Jest idealnym narz�dziem do pisania dokument�w, list�w, raport�w itp.

%prep
%setup -q -a1

%build
cd abi
./autogen.sh
gettextize --copy --force
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
%configure CPPFLAGS="$CPPFLAGS" \
	--enable-gnome \
	--enable-bidi \
	--with-pspell \
	--with-libjpeg \
	--with-libxml2 \
	--with-expat
%{__make} -f GNUmakefile

cd ../abiword-plugins/abiword-plugins
find . -name autogen.sh -type f -exec /bin/sh -c "echo \"libtoolize --copy --force\" >> {}" ";"
./autogen.sh; ./autogen.sh
%configure CPPFLAGS="$CPPFLAGS `%{_bindir}/gtk-config --cflags`" \
	--prefix=%{_libdir}/AbiSuite \
	--enable-gnome \
	--with-bzip2 \
	--with-ImageMagick \
	--with-abiword=$PWD/../../abi/
%{__make} -f GNUmakefile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Office/Wordprocessors,%{_pixmapsdir}}

%{__make} -C abi -f GNUmakefile install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C abiword-plugins/abiword-plugins -f GNUmakefile install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{_libdir}/AbiSuite/AbiWord/plugins  $RPM_BUILD_ROOT%{_datadir}/AbiSuite/AbiWord/plugins
ln -sf %{_bindir}/AbiWord $RPM_BUILD_ROOT%{_bindir}/abiword

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Office/Wordprocessors
install $RPM_BUILD_ROOT%{_datadir}/AbiSuite/icons/abiword_48.png $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf abi/CREDITS.TXT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc abi/docs/*.abw abi/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/AbiSuite
%dir %{_libdir}/AbiSuite
%dir %{_libdir}/AbiSuite/AbiWord
%dir %{_libdir}/AbiSuite/AbiWord/plugins
%attr(755,root,root) %{_libdir}/AbiSuite/AbiWord/plugins/*.so
%attr(755,root,root) %{_libdir}/AbiSuite/AbiWord/plugins/*.la
%{_applnkdir}/Office/Wordprocessors/*
%{_pixmapsdir}/*.png
