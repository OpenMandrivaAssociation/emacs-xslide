Summary: A GNU Emacs major mode for editing XSL documents
name: emacs-xslide
%define version 0.2.2
Version: %{version}
Release: %mkrel 5
BuildRequires: emacs-bin
Requires: emacs
Obsoletes: xslide
Provides: xslide
License: GPL
Source: http://www.menteith.com/xslide/data/xslide-%{version}.tar.bz2
URL:	http://www.menteith.com/xslide/index.html
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


