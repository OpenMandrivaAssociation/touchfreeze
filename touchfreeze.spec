%define rel	2
%define pre	0

%if %pre
%define distname	%name-%pre-%version.tar.gz
%else
%define distname	%name-%version.tar.gz
%endif

Name:		touchfreeze
Version:	0.2.5
Release:	11
Summary:	Utility to disable touchpad tap-clicking while typing
License:	GPL+
Group:		System/Configuration/Hardware
Source0:	http://qsynaptics.sourceforge.net/%{distname}
URL:		http://qsynaptics.sourceforge.net/
Patch0:		touchfreeze-0.2.5-compile.patch
Obsoletes:	qsynaptics <= 0.22.0-4
Obsoletes:	ksynaptics <= 0.3.3-1
Provides:	qsynaptics
Provides:	ksynaptics
BuildRequires:	qt4-devel
Requires:	synaptics

%description
TouchFreeze is a simple utility that disables the tap-click function
of Synaptics touchpads while you are typing. As long as you are typing,
tapping the touchpad will not count as a mouse click. It replaces
the previous QSynaptics and KSynaptics tools.

%prep
%setup -q
%apply_patches

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %name %{buildroot}%{_bindir}/%{name}

# XDG autostart
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
cat > %{buildroot}%{_sysconfdir}/xdg/autostart/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Exec=%{_bindir}/%{name}
Name=TouchFreeze - touchpad tap-click inhibitor
Terminal=false
Type=Application
StartupNotify=false
X-KDE-autostart-phase=2
X-KDE-autostart-after=panel
EOF

# KDE autostart
mkdir -p %{buildroot}%{_datadir}/autostart
cp %{buildroot}%{_sysconfdir}/xdg/autostart/mandriva-%{name}.desktop %{buildroot}%{_datadir}/autostart/mandriva-%{name}.desktop

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/mandriva-%{name}.desktop
%{_datadir}/autostart/mandriva-%{name}.desktop
