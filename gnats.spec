Summary:	A bug tracking system
Summary(pl):	System �ledzenia b��d�w
Name:		gnats
Version:	3.113.1
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://sources.redhat.com/pub/gnats/snapshots/%{name}-%{version}.tar.gz
URL:		http://sources.redhat.com/gnats/
BuildRequires:	awk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_libexecdir	%{_libdir}

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

%description -l pl
GNATS (GNU Problem Report Management System) - System GNU Zarz�dzania
Raportami o B��dach. U�ytkownicy przesy�aj� informacje o problemach za
pomoc� poczty elektronicznej. GNATS cz�ciowo automatyzuje �ledzenie
raport�w o b��dach (PR
- Problem Report) w nastepuj�ce sposoby: organizuj�c raporty w baz�
  danych oraz informuj�c ludzi odpowiedzialnych o podej�ewanych b��dach;
  pozwalaj�c na edycj� i odpytywanie bazy oraz dostarczaj�c informacj� o
  archiwalnych b��dach dla danego problemu. Je�li instalujesz GNATS
  bedziesz potrzebowa� zar�wno tego pakietu jak i pakietu gnats-db.

%package db
Summary:	The database skeleton for the GNATS bug tracking system
Summary(pl):	Szkielet bazy dla systemu �ledzenia b��d�w GNATS
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia

%description db
GNATS (GNU Problem Report Management System) - database skeleton.

%description db -l pl
GNATS (GNU Problem Report Management System) - System GNU Zarz�dzania
Raportami o B��dach - szkielet bazy.

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

gzip -9nf doc/{BETA,PROBLEMS,README,TODO,UPGRADE}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*

%files db
%defattr(644,root,root,755)
