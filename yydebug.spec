%{?_javapackages_macros:%_javapackages_macros}
Name:     yydebug
Version:  1.1.0
Release:  10.0%{?dist}
Summary:  Supports tracing and animation for a Java-based parser generated by jay

License:  BSD
URL:      http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/package-summary.html
Source0:  http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/doc-files/src.jar
Patch0:   clean-up-broken-makefile.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=561452
Patch1:   add-javadocs-to-makefile.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: java-devel
BuildRequires:  jpackage-utils
Requires: java
Requires:  jpackage-utils

BuildArch:      noarch

%description
jay/yydebug supports tracing and animation for a Java-based parser generated 
by jay. An implementation of yyDebug is passed as an additional argument to 
yyparse() to trace a Java-based parser generated by jay with option -t set.
yyDebugAdapter produces one-line messages, by default to standard output. 
The messages are designed to be filtered by a program such as grep. yyAnim 
provides an animation of the parsing process

%package javadoc
Summary:        Javadocs for %{name}

Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jay/yydebug
%patch0
%patch1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}

cp yydebug.jar $RPM_BUILD_ROOT%{_javadir}/yydebug-%{version}.jar
ln -s %{_javadir}/yydebug-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/yydebug.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/yydebug-%{version}.jar
%{_javadir}/yydebug.jar
%doc package.html

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}


%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May  06 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-5
- added my name which was missing in this changelog

* Wed May  05 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-4
- added Alexander Kurtakov's patch to generate javadocs
- added javadoc bits to the spec

* Tue May  04 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-3
- BSD license retrieved from 'jay' superproject
- http://svn.codehaus.org/jruby/trunk/jay/jay.1

* Tue Apr  27 2010  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-2
- removed gcj bits

* Thu Jan  21 2009  Mohammed Morsi <mmorsi@redhat.com> - 1.1.0-1
- Initial build.
