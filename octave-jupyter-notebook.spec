%global octpkg jupyter-notebook

Summary:	Run and fill Jupyter Notebooks within GNU Octave
Name:		octave-jupyter-notebook
Version:	1.2.0
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/jupyter-notebook/
Url:		https://github.com/gnu-octave/pkg-jupyter-notebook/
Source0:	https://github.com/gnu-octave/pkg-jupyter-notebook/archive/v%{version}/%{octpkg}-%{version}.tar.gz
# (upstream) https://github.com/gnu-octave/pkg-jupyter-notebook/issues/8
Patch0:		jupyter-notebook-1.2.0-remove_uneeded_deps.patch

BuildRequires:	octave-devel >= 7.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Run and fill Jupyter Notebooks within GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n pkg-%{octpkg}-%{version}

%build
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

