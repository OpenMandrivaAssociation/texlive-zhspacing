# revision 19473
# category Package
# catalog-ctan /macros/xetex/generic/zhspacing
# catalog-date 2009-11-10 09:00:49 +0100
# catalog-license lppl
# catalog-version 3.5
Name:		texlive-zhspacing
Version:	3.5
Release:	1
Summary:	A simple solution for typesetting CJK documents in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/zhspacing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package may be used by any document format under XeTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/zhspacing/context/t-zhspacing.tex
%{_texmfdistdir}/tex/xetex/zhspacing/latex/zhfont.sty
%{_texmfdistdir}/tex/xetex/zhspacing/latex/zhulem.sty
%{_texmfdistdir}/tex/xetex/zhspacing/plain/zhmath.sty
%{_texmfdistdir}/tex/xetex/zhspacing/plain/zhsmyclass.sty
%{_texmfdistdir}/tex/xetex/zhspacing/plain/zhspacing.sty
%{_texmfdistdir}/tex/xetex/zhspacing/plain/zhsusefulmacros.sty
%doc %{_texmfdistdir}/doc/xetex/zhspacing/README
%doc %{_texmfdistdir}/doc/xetex/zhspacing/zhs-man.pdf
%doc %{_texmfdistdir}/doc/xetex/zhspacing/zhs-man.tex
%doc %{_texmfdistdir}/doc/xetex/zhspacing/zhspacing-context-test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
