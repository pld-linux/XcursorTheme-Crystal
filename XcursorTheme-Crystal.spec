# TODO: more descriptive descriptions.
Summary:	X11 mouse theme with the crystal look&feel
Summary(pl):	Motyw kursorów X11 podobny do ikon Crystal
Name:		XcursorTheme-Crystal
Version:	1.0
Release:	1
License:	GPL
Group:		Themes
Source0:	http://digilander.libero.it/m4rt/files/Crystalcursors.tar.bz2
# Source0-md5:	7ba346d9f5b5d94054f2eb07373cd75e
URL:		http://www.kde-look.org/content/show.php?content=6240
BuildRequires:	XFree86 >= 4.3
Requires:	XFree86 >= 4.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 mouse theme with the crystal look&feel.

%description -l pl
Motyw kursorów X11 podobny do ikon Crystal.

%prep
%setup -q -n Crystalcursors

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
colors="blue \
gray \
green \
white"
Z="`/bin/pwd`"
for i in $colors;
do
install -d $RPM_BUILD_ROOT%{_iconsdir}/Crystal${i}/cursors
cp -df ${i}_cursors/* $RPM_BUILD_ROOT%{_iconsdir}/Crystal${i}/cursors
echo "[Icon Theme]" > $RPM_BUILD_ROOT%{_iconsdir}/Crystal${i}/index.theme
echo "Name = Crystal${i}" >> $RPM_BUILD_ROOT%{_iconsdir}/Crystal${i}/index.theme
echo "Comment = X11 mouse theme with the crystal look&feel - ${i} version" >> $RPM_BUILD_ROOT%{_iconsdir}/Crystal${i}/index.theme
done
cd "$Z"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/Crystal*
