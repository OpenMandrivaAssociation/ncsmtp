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
