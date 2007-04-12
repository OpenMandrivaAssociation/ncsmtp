
Name:		ncsmtp
Summary:	Null Client SMTP daemon with aliases support
Version:	0.2
Release: 	%mkrel 3
URL:		http://voxel.jouy.inra.fr/darcs/ncsmtp/
Source0:	http://voxel.jouy.inra.fr/darcs/ncsmtp//ncsmtp-%{version}.tar.bz2
License:	GPL
Group:		System/Servers
Requires:	python
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch
PreReq:          rpm-helper

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
%setup


%build


%install
DESTDIR=%buildroot sh install.sh

%clean
/bin/rm -Rf %buildroot


%files
%defattr(-, root, root, 0755)
%doc COPYING README version
%dir %{_sysconfdir}/ncsmtp
%config(noreplace)  %{_sysconfdir}/ncsmtp/*
%config(noreplace) %{_sysconfdir}/rc.d/init.d/ncsmtp
%{_sbindir}/*


%post
# Install service:
%_post_service ncsmtp


%preun
# Remove service:
%_preun_service ncsmtp


