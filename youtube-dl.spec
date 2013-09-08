Name:           youtube-dl
Version:        2013.09.07
Release:        1%{?dist}
Summary:        A small command-line program to download online videos
License:        Public Domain
URL:            https://yt-dl.org
Source0:        https://yt-dl.org/downloads/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
# Used to generate manpage
BuildRequires:  pandoc
BuildRequires:  python
# Tests failed because of no connection in Koji.
#BuildRequires:  python-nose
Requires:       python
BuildArch:      noarch

%description
Small command-line program to download videos from YouTube and other sites.

%prep
%setup -qn %{name}

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} \
             PREFIX=%{_prefix} \
             MANDIR=%{_mandir} \
             PYTHON=%{_bindir}/python
mkdir -p %{buildroot}%{_sysconfdir}
install -pm644 %{S:1} %{buildroot}%{_sysconfdir}

%check
#make test

%files
%doc LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/bash_completion.d/%{name}

%changelog
* Mon Sep 09 2013 Christopher Meng <rpm@cicku.me> - 2013.09.07-1
- Update to new release.

* Thu Sep 05 2013 Christopher Meng <rpm@cicku.me> - 2013.09.04-1
- Update to new release.

* Mon Sep 02 2013 Christopher Meng <rpm@cicku.me> - 2013.08.30-1
- Update to new release.

* Fri Aug 30 2013 Christopher Meng <rpm@cicku.me> - 2013.08.29-1
- Update to new release.

* Tue Aug 27 2013 Christopher Meng <rpm@cicku.me> - 2013.08.27-1
- Update to new release.

* Sat Aug 24 2013 Christopher Meng <rpm@cicku.me> - 2013.08.23-1
- Update to new release.

* Sun Aug 18 2013 Christopher Meng <rpm@cicku.me> - 2013.08.17-1
- Update to new release.

* Tue Aug 13 2013 Christopher Meng <rpm@cicku.me> - 2013.08.09-1
- Update to new release.

* Sat Aug 03 2013 Christopher Meng <rpm@cicku.me> - 2013.08.02-1
- Update to new release.

* Mon Jul 22 2013 Christopher Meng <rpm@cicku.me> - 2013.07.25.2-1
- Update to new release.

* Mon Jul 22 2013 Christopher Meng <rpm@cicku.me> - 2013.07.19-1
- Update to new release.

* Thu Jul 18 2013 Christopher Meng <rpm@cicku.me> - 2013.07.17.1-1
- Update to new release.

* Tue Jul 16 2013 Christopher Meng <rpm@cicku.me> - 2013.07.12-1
- Update to new release.

* Thu Jul 11 2013 Christopher Meng <rpm@cicku.me> - 2013.07.10-1
- Update to new release.

* Tue Jul 02 2013 Christopher Meng <rpm@cicku.me> - 2013.07.02-1
- Update to new release.
- SPEC cleanup.

* Wed Jun 26 2013 Christopher Meng <rpm@cicku.me> - 2013.06.31-1
- Update to new release.

* Mon Jun 17 2013 Christopher Meng <rpm@cicku.me> - 2013.05.23-1
- Update to new release and cleanup the spec.

* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 2013.05.14-1
- Update to new release.

* Wed May 08 2013 Christopher Meng <rpm@cicku.me> - 2013.05.07-1
- Update to new release.

* Thu Apr 18 2013 Till Maas <opensource@till.name> - 2013.04.18-1
- Update to new release.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.01.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Till Maas <opensource@till.name> - 2013.01.13-1
- Update to new release.

* Sun Jan 06 2013 Matěj Cepl <mcepl@redhat.com> - 2013.01.02-1
- Update to new release (fix #880270).

* Tue Oct 23 2012 Till Maas <opensource@till.name> - 2012.10.09-1
- Update to new release.
- Update BR: add pandoc.
- install make target.

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2012.09.27-3
- Add BR: python >= 2.6.

* Tue Oct 02 2012 Till Maas <opensource@till.name> - 2012.09.27-2
- Use noreplace for config file.
- Add BR: zip.

* Tue Oct  2 2012 Tim Landscheidt <tim@tim-landscheidt.de> - 2012.09.27-1
- Bump Python requirement to 2.6.
- Update to new release and GitHub tarballs.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.02.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 21 2012 Till Maas <opensource@till.name> - 2012.02.27-1
- Update to new release.

* Thu Jan 26 2012 Till Maas <opensource@till.name> - 2011.12.08-3
- Provide --prefer-free-formats in %%{_sysconfdir}/%%{name}.conf (RH #757577)
  (Patch by Jan Kratochvil)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.12.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Till Maas <opensource@till.name> - 2011.12.08-1
- Update to new release.

* Thu Dec 08 2011 Till Maas <opensource@till.name> - 2011.11.23-1
- Update to new release (fixed Red Hat Bug #758679).

* Fri Oct 21 2011 Till Maas <opensource@till.name> - 2011.10.19-1
- Update to latest release.

* Thu Aug 04 2011 Till Maas <opensource@till.name> - 2011.08.04-1
- Update to latest release to adjust to backend changes (Red Hat Bug
  #728378).

* Fri May 13 2011 Till Maas <opensource@till.name> - 2011.03.29-1
- Update to latest release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.01.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Till Maas <opensource@till.name> - 2010.01.30-1
- Update to latest release.

* Sun Dec 12 2010 Till Maas <opensource@till.name> - 2010.12.09-1
- Update to latest release to adjust with youtube changes.

* Sat Nov 06 2010 Till Maas <opensource@till.name> - 2010.10.24-1
- Update to latest release.
- Adjust to new upstream location at github instead of bitbucket.
- add -p to install.
- remove index.html

* Thu Oct 07 2010 Till Maas <opensource@till.name> - 2010.10.03-1
- Update to latest release.

* Thu Aug 05 2010 Till Maas <opensource@till.name> - 2010.08.04-1
- Update to latest release.

* Fri Jul 23 2010 Till Maas <opensource@till.name> - 2010.07.22-1
- Update to latest release.

* Thu Jul 15 2010 Till Maas <opensource@till.name> - 2010.07.14-1
- Update to latest release.

* Mon Jun 07 2010 Till Maas <opensource@till.name> - 2010.06.06-1
- Update to latest release.

* Thu Apr 29 2010 Till Maas <opensource@till.name> - 2010.04.04-1
- Update to latest release to fix some download issues RH #582372.

* Fri Oct 09 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-2
- Small fix in %%prep.

* Sun Sep 27 2009 Rafał Psota <rafalzaq@gmail.com> - 2009.09.13-1
- Update to 2009.09.13.
- License change to Public Domain.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.01.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 26 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2008.01.24-1
- Update to v2008.01.24
- Add polish summary and description.

* Wed Jan 02 2008 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-5
- Correct install.
- Correct documentation.

* Sat Dec 29 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-4
- Correct requires.
- Add documentation.

* Sun Dec 23 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 2007.10.12-3
- Correct version tag.

* Fri Dec 14 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-2
- Update to v2007.10.12, correct license and update summary.

* Sun Dec 9 2007 Krzysztof Kurzawski <kurzawax at gmail.com> 1-1
- First release.
