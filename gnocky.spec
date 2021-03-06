Summary:	Application suite for mobile phones
Summary(pl.UTF-8):	Aplikacja do obsługi telefonów komórkowych
Name:		gnocky
Version:	0.0.7
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://gnokii.org/download/gnocky/%{name}-%{version}.tar.bz2
# Source0-md5:	13767421ae807a753a66dd49772a48f8
Source1:	%{name}.desktop
URL:		http://gnocky.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libgnokii-devel
BuildRequires:	pkgconfig
Requires:	libgnokii >= 1:0.5.7
Requires:	gnokii >= 1:0.5.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnocky is an application that will allow you to use many features of
your mobile phone (setting logos, sending SMS, addressbook
management). It uses user-space mobile driver provided by gnokii
project.

%description -l pl.UTF-8
Gnocky jest aplikacją pozwalającą na zarządzanie telefonem (ustawianie
logo, wysyłanie SMS, zarządzanie książką adresową). Używa sterowników
dostarczanych przez projekt gnokii.

%prep
%setup -q

%build
rm -rf autom4te.cache
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/glade
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/glade/*
%{_datadir}/%{name}/pixmaps/*
%{_desktopdir}/gnocky.desktop
