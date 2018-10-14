#
# spec file for package rdepends
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           rdepends
Version:        0.1 
Release:        1%{?dist}
Summary:        Reverse dependency listing tool
BuildArch:      noarch
License:        LGPL-2.1-or-later
Url:            https://github.com/bzoltan1/rdepends.git
Source:         rdepends-0.1.tar.gz
Requires:       python2

%description
This tool is to list all packages what depend on a given package.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 rdepends %{buildroot}/usr/bin/rdepends

%post
%postun

%files
%doc README.md
%license LICENSE
%{_bindir}/rdepends


%changelog
* Sun Oct 14 2018 Zoltán Balogh  0.1
  - Initial rpm release
