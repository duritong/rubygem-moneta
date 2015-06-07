# Generated from moneta-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname moneta
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A unified interface to key/value stores
Name: rubygem-%{gemname}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/minad/moneta
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Requires: ruby(rubygems)
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Moneta provides a standard interface for interacting with various kinds of
key/value stores including Memcache, Redis, CouchDB, Berkeley DB and many more.

%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

mkdir -p .%{gemdir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gemdir} \
  --force --rdoc \
  %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/
rm -rf %{buildroot}/%{geminstdir}/.[a-z]*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{geminstdir}/README.md
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/spec
%doc %{geminstdir}/script
%doc %{geminstdir}/Gemfile
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/%{gemname}.gemspec
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-,root,root,-)
%doc %{geminstdir}/SPEC.md
%doc %{geminstdir}/CONTRIBUTORS
%doc %{geminstdir}/CHANGES
%{gemdir}/doc/%{gemname}-%{version}

%changelog
* Sun Jun 07 2015 mh <mh@immerda.ch> - 0.8.0-1
- Update

* Tue Mar 16 2010 Matthew Kent <mkent@magoazul.com> - 0.6.0-1
- Initial package
