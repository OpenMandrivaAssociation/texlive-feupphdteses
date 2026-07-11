%global tl_name feupphdteses
%global tl_revision 30962

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.0
Release:	%{tl_revision}.1
Summary:	Typeset Engineering PhD theses at the University of Porto
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/feupphdteses
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feupphdteses.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/feupphdteses.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A complete template for thesis/works of Faculdade de Engenharia da
Universidade do Porto (FEUP) Faculty of Engineering University of Porto.

