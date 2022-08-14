%global debug_package %{nil}

# macro to filter unwanted provides from Node.js binary native modules
%nodejs_default_filter

Name: eslint
Epoch: 100
Version: 8.22.0
Release: 1%{?dist}
BuildArch: noarch
Summary: An AST-based pattern checker for JavaScript
License: MIT
URL: https://github.com/eslint/eslint/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: nodejs-packaging
Requires: nodejs >= 12.22.0

%description
ESLint is a tool for identifying and reporting on patterns found in
ECMAScript/JavaScript code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{nodejs_sitelib}
cp -rfT node_modules %{buildroot}%{nodejs_sitelib}
pushd %{buildroot}%{_bindir} && \
    ln -fs %{nodejs_sitelib}/eslint/bin/eslint.js eslint && \
    popd
chmod a+x %{buildroot}%{nodejs_sitelib}/eslint/bin/eslint.js
fdupes -qnrps %{buildroot}%{nodejs_sitelib}

%check

%files
%license LICENSE
%dir %{nodejs_sitelib}
%{_bindir}/*
%{nodejs_sitelib}/*

%changelog
