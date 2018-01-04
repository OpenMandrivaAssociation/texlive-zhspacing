# revision 25644
# category Package
# catalog-ctan /macros/xetex/generic/zhspacing
# catalog-date 2012-03-14 18:58:06 +0100
# catalog-license lppl
# catalog-version 2012/03/14
Name:		texlive-zhspacing
Version:	20120314
Release:	9
Summary:	Spacing for mixed CJK-English documents in XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/generic/zhspacing
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package manages spacing in a CJK document; between
consecutive Chinese letters, spaces are ignored, but a
consistent space is inserted between Chinese text and English
(or mathematics). The package may be used by any document
format under XeTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xetex/zhspacing
%doc %{_texmfdistdir}/doc/xetex/zhspacing

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
