Name:		texlive-feupphdteses
Version:	30962
Release:	2
Summary:	Typeset Engineering PhD theses at the University of Porto
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/feupphdteses
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feupphdteses.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/feupphdteses.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A complete template for thesis/works of Faculdade de Engenharia
da Universidade do Porto (FEUP) Faculty of Engineering
University of Porto.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/feupphdteses/feupphdteses.sty
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Abbs.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Abstract.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Acknow.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Appendix.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Chapter2.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Chapter3.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Conclusions.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Dedicatory.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Figures/uporto-feup.pdf
%doc %{_texmfdistdir}/doc/latex/feupphdteses/IEEEtranN.bst
%doc %{_texmfdistdir}/doc/latex/feupphdteses/IEEEtranSN.bst
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Intro.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Publications.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Quote.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/README
%doc %{_texmfdistdir}/doc/latex/feupphdteses/References.bib
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Resumo.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Template_EN.pdf
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Template_EN.tcp
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Template_EN.tex
%doc %{_texmfdistdir}/doc/latex/feupphdteses/Template_EN.tps
%doc %{_texmfdistdir}/doc/latex/feupphdteses/mymacros.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
