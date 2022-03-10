%global octpkg jupyter-notebook

Summary:	Run and fill Jupyter Notebooks within GNU Octave
Name:		octave-%{octpkg}
Version:	1.2.0
Release:	1
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/gnu-octave/pkg-%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 5.1.0
BuildRequires:	octave-json >= 1.5.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-json > 1.5.0

Requires(post): octave
Requires(postun): octave

%description
Run and fill Jupyter Notebooks within GNU Octave..

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pkg-%{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

