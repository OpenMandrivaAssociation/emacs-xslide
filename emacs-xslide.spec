Summary: A GNU Emacs major mode for editing XSL documents
name: emacs-xslide
%define version 0.2.2
Version: %{version}
Release: 10
BuildRequires: emacs-bin
Requires: emacs
Obsoletes: xslide
Provides: xslide
License: GPL
Source: http://www.menteith.com/xslide/data/xslide-%{version}.tar.bz2
URL:	https://www.menteith.com/xslide/index.html
Group: Publishing
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
%define xslidedir /%{_prefix}/share/emacs/site-lisp/xslide/

%description
Emacs is an advanced and extensible editor. An Emacs major mode
customizes Emacs for editing particular types of text documents.
The xslide package is an Emacs major mode for editing XSL.

%prep

%setup -q -n xslide-%version

%build

%make 

cat >> dot_emacs << __ELISP__
(setq load-path (append load-path '("/usr/share/emacs/site-lisp/xslide")))

;; "Used for prefix and colon portion of formatting object elements and attributes"
(make-face 'xsl-fo-alternate-face)
(set-face-foreground 'xsl-fo-alternate-face "Midnight Blue")

;; "Used for literal result element tags"
(make-face 'xsl-other-element-face)
(set-face-foreground 'xsl-other-element-face "Midnight Blue")

(make-face 'xsl-fo-main-face)
(set-face-foreground 'xsl-other-element-face "Midnight Blue")

__ELISP__

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{xslidedir}
mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d/

make
cp *.elc $RPM_BUILD_ROOT/%{xslidedir}
cp dot_emacs $RPM_BUILD_ROOT/etc/emacs/site-start.d/xslide-init.el

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.TXT ChangeLog TODO NEWS
%dir %{xslidedir}
%{xslidedir}/*.elc
/etc/emacs/site-start.d/xslide-init.el




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-9mdv2011.0
+ Revision: 618055
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-8mdv2010.0
+ Revision: 428590
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.2-7mdv2009.0
+ Revision: 244825
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.2-5mdv2008.1
+ Revision: 136403
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 Camille Bégnis <camille@mandriva.com> 0.2.2-5mdv2007.0
+ Revision: 120924
- Fix invalid carriage return in specfile (bug #28732)
- Import emacs-xslide

* Tue May 23 2006 Camille Begnis <camille@mandriva.com> 0.2.2-4mdk
- rebuild

* Sat Apr 30 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2-3mdk
- rebuild for new emacs

* Fri Dec 03 2004 Camille Begnis <camille@mandrakesoft.com> 0.2.2-2mdk
- rebuild

