# Generated from moneta-0.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name moneta

Summary: A unified interface to key/value stores
Name: rubygem-%{gem_name}
Version: 0.8.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/minad/moneta
Source0: http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
BuildRequires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

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
%gem_install -n %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/.[a-z]*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/script
%doc %{gem_instdir}/Gemfile
%dir %{gem_instdir}

%files doc
%defattr(-,root,root,-)
%doc %{gem_docdir}
%doc %{gem_instdir}/SPEC.md
%doc %{gem_instdir}/CONTRIBUTORS
%doc %{gem_instdir}/CHANGES
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sun Jun 07 2015 mh <mh@immerda.ch> - 0.8.0-1
- Update

* Tue Mar 16 2010 Matthew Kent <mkent@magoazul.com> - 0.6.0-1
- Initial package
