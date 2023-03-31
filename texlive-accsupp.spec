Name:		texlive-accsupp
Version:	53052
Release:	2
Summary:	Better accessibility support for PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/accsupp
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accsupp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accsupp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accsupp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Since PDF 1.5 portions of a page can be marked for better
accessibility support. For example, replacement texts or
expansions of abbreviations can be provided. This package
starts with providing a minimal low-level interface for
programmers; its status is experimental. Support necessary for
the package was added to the "distill" capabilities of
Ghostscript with version 9.15 of Ghostscript; the dvips is only
available with that version (or later).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/accsupp
%{_texmfdistdir}/tex/latex/accsupp
%doc %{_texmfdistdir}/doc/latex/accsupp

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
