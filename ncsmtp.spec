Summary:	Null Client SMTP daemon with aliases support
Name:		ncsmtp
Version:	0.2
Release: 	%mkrel 8
License:	GPL
Group:		System/Servers
URL:		http://voxel.jouy.inra.fr/darcs/ncsmtp/
Source0:	http://voxel.jouy.inra.fr/darcs/ncsmtp//ncsmtp-%{version}.tar.bz2
Requires:	python
BuildArch:	noarch
Requires(preun):  rpm-helper
Requires(post):  rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A null client is a machine that can only send mail. It receives no
mail from the network, and it does not deliver any mail locally.

This program accepts mail and sends it to the mail hub. It can manage
aliases, feature which is useful if mail hub administrator and local host
administrator are not the same person, or if accounts are different on
local host and on mail hub.

Null Client SMTP daemon :
 + manage aliases
 + is easy to configure
 + stores login and password in a file with restricted access
 + logs mail transfers on local host
 + lets you keep the default smtp configuration (localhost:smtp) of
   lots of softs
 + runs with low privileges

You should install a small package providing sendmail command (like
mini_sendmail or msmtp) to use this daemon.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

DESTDIR=%{buildroot} sh install.sh

%post
# Install service:
%_post_service ncsmtp


%preun
# Remove service:
%_preun_service ncsmtp

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README version
%{_initrddir}/ncsmtp
%dir %{_sysconfdir}/ncsmtp
%config(noreplace)  %{_sysconfdir}/ncsmtp/*
%{_sbindir}/*


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-8mdv2011.0
+ Revision: 620481
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2010.0
+ Revision: 430161
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-6mdv2009.0
+ Revision: 239080
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.2-5mdv2008.0
+ Revision: 71884
- the right PreReq fix (thanks to Thierry Vignaud)

* Sun Aug 26 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.2-4mdv2008.0
+ Revision: 71509
- fix PreReq
- rebuild


* Thu May 25 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-3mdv2007.0
- yearly rebuild

* Thu May 19 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-2mdk
- drop provides smtpdaemon
- drop mini_sendmail requirement

* Wed May 18 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-1mdk
- New release 0.2
- update url

* Wed Mar 23 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.1-2mdk
- remove sendmail update-alternatives (done in mini_sendmail)
- use mkrel

* Thu Mar 17 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.1-1mdk
- initial contrib

