Summary:	tavu
Name:		tavu
Version:	0.2.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://da.weeno.net/code/tavu/%{name}-%{version}.tar.gz
# Source0-md5:	4e15cac2f70865f834b3ff47938cc9ab
URL:		http://da.weeno.net/code/tavu/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tavu allows remote programs to use your local KDE notification system
(aka knotify). The network communication between the remote program
and knotify is done using the XMPP (Jabber) protocol.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/tavu/python

%{__make} install \
	COMPILE_DATA=: \
	PREFIX=$RPM_BUILD_ROOT \
	dest_conf_d=$RPM_BUILD_ROOT%{_sysconfdir}

%py_comp $RPM_BUILD_ROOT%{_datadir}/tavu/python
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/tavu/python
%py_postclean %{_datadir}/tavu/python

rm -rf $RPM_BUILD_ROOT%{_docdir}/tavu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{INSTALL,README}
%attr(755,root,root) %{_bindir}/tavu-listen
%{_sysconfdir}/tavurc
%{_datadir}/tavu/dotfile.skel
%dir %{_datadir}/tavu/python
%{_datadir}/tavu/python/*.py[co]
