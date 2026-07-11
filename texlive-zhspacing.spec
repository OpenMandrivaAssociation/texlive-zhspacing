%global tl_name zhspacing
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Spacing for mixed CJK-English documents in XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/generic/zhspacing
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zhspacing.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package manages spacing in a CJK document; between consecutive
Chinese letters, spaces are ignored, but a consistent space is inserted
between Chinese text and English (or mathematics). The package may be
used by any document format under XeTeX.

