# TODO:
# - update to 4.0+
# - SECURITY: http://securitytracker.com/alerts/2004/Jun/1010579.html
Summary:	A bug tracking system
Summary(pl.UTF-8):   System śledzenia błędów
Name:		gnats
Version:	3.113.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://sources.redhat.com/pub/gnats/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	7a3fac7196a3179c69d7d348b1ac4dcc
URL:		http://www.gnu.org/software/gnats/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}

%description
GNATS (GNU Problem Report Management System) is a bug-tracking tool
designed for use at a central support site. Users with problems report
them to the support site via email. GNATS partially automates the
tracking of the problem reports (PRs) in the following ways: by
organizing problem reports into a database and notifying responsible
parties of suspected bugs, by allowing support personnel and their
managers to edit and query accumulated bugs, and by providing a
reliable archive of problems for a given program (and their subsequent
solutions). If you're installing GNATS, you'll need to install both
the gnats and the gnats-db packages.

%description -l pl.UTF-8
GNATS (GNU Problem Report Management System) - System GNU Zarządzania
Raportami o Błędach. Użytkownicy przesyłają informacje o problemach za
pomocą poczty elektronicznej. GNATS częściowo automatyzuje śledzenie
raportów o błędach (PR
- Problem Report) w następujące sposoby: organizując raporty w bazę
  danych oraz informując ludzi odpowiedzialnych o podejrzewanych błędach;
  pozwalając na edycję i odpytywanie bazy oraz dostarczając informację o
  archiwalnych błędach dla danego problemu. Jeśli instalujesz GNATS
  będziesz potrzebował zarówno tego pakietu jak i pakietu gnats-db.

%package db
Summary:	The database skeleton for the GNATS bug tracking system
Summary(pl.UTF-8):   Szkielet bazy dla systemu śledzenia błędów GNATS
Group:		Development/Tools

%description db
GNATS (GNU Problem Report Management System) - database skeleton.

%description db -l pl.UTF-8
GNATS (GNU Problem Report Management System) - System GNU Zarządzania
Raportami o Błędach - szkielet bazy.

%prep
%setup -q

%build
%configure \
	--with-full-gnats \
	--with-gnats-root=%{_var}/lib/gnats

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{xemacs/lisp,emacs}
ln -s $RPM_BUILD_ROOT%{_datadir}/xemacs/lisp $RPM_BUILD_ROOT%{_datadir}/emacs/lisp

%{makeinstall} -k \
	GNATS_ROOT=$RPM_BUILD_ROOT%{_datadir}/gnats/gnats-db \
	install-info

%{makeinstall} -C gnats \
	GNATS_ROOT=$RPM_BUILD_ROOT%{_datadir}/gnats/gnats-db \
	install-gnats-arch-indep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{BETA,PROBLEMS,README,TODO,UPGRADE}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

%files db
%defattr(644,root,root,755)
