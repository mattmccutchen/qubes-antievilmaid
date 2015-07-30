%define name anti-evil-maid
%define subdir %{?qubes_builder:%{name}/}
%define _builddir %(pwd)/%{subdir}
%{!?version: %define version %(cat %{subdir}version)}

Name:		%{name}
Version:	%{version}
Release:	1%{?dist}
Summary:    	Anti Evil Maid for initramfs-based systems.
Requires:	anti-evil-maid-dracut parted tboot trousers-changer tpm-tools
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

%description
Anti Evil Maid for initramfs-based systems.

%install

mkdir -p $RPM_BUILD_ROOT/usr/sbin
cp antievilmaid_install $RPM_BUILD_ROOT/usr/sbin
cp antievilmaid_seal $RPM_BUILD_ROOT/usr/sbin

mkdir -p $RPM_BUILD_ROOT/usr/share/doc/antievilmaid
cp README $RPM_BUILD_ROOT/usr/share/doc/antievilmaid

mkdir -p $RPM_BUILD_ROOT/etc
cp antievilmaid.conf $RPM_BUILD_ROOT/etc

mkdir -p $RPM_BUILD_ROOT/etc/grub.d/
cp 19_linux_xen_tboot $RPM_BUILD_ROOT/etc/grub.d/

mkdir -p $RPM_BUILD_ROOT/mnt/antievilmaid
mkdir -p $RPM_BUILD_ROOT/var/lib/antievilmaid

%files
/usr/sbin/antievilmaid_install
/usr/sbin/antievilmaid_seal
/usr/share/doc/antievilmaid/README
/etc/antievilmaid.conf
/etc/grub.d/19_linux_xen_tboot
%dir /mnt/antievilmaid
%dir /var/lib/antievilmaid