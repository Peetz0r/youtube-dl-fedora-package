Name:           youtube-dl
Version:        2008.01.24
Release:        1%{?dist}
Summary:        Small command-line program to download videos from YouTube
Summary(pl):    Tekstowy program do pobierania filmów z youtube.com
Group:          Applications/Multimedia
License:        MIT
URL:            http://www.arrakis.es/~rggi3/youtube-dl/
Source0:        http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl
Source1:        http://www.arrakis.es/~rggi3/youtube-dl/index.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       python >= 2.4

%description
Small command-line program to download videos from YouTube.

%description -l pl
youtube-dl to mały tekstowy program służący do pobierania filmów z
youtube.com.

%prep
cp %{SOURCE1} .

%build
#nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%doc index.html

%changelog
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
- First release
