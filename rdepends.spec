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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           rdepends
Version:        0.2
Release:        1%{?dist}
Summary:        Reverse dependency listing tool
License:        LGPL-2.1-or-later
URL:            https://github.com/bzoltan1/rdepends.git
Source:         rdepends-0.2.tar.gz
Requires:       python3
BuildArch:      noarch

%description
This tool is to list all packages what depend on a given package.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}/
install -m 755 rdepends %{buildroot}%{_bindir}/rdepends

%files
%doc README.md
%license LICENSE
%{_bindir}/rdepends

%changelog
