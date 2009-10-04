%define rel	1
%define pre	0

%if %pre
%define release		%mkrel 0.%pre.%rel
%define distname	%name-%pre-%version.tar.gz
%define dirname		%name-%pre-%version
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif

Name:		touchfreeze
Version:	0.2.3
Release:	%mkrel 1
Summary:	Utility to disable touchpad tap-clicking while typing
License:	GPL+
Group:		System/Configuration/Hardware
Source0:	http://qsynaptics.sourceforge.net/%{distname}
BuildRoot:	%{_tmppath}/%{name}-root
URL:		http://qsynaptics.sourceforge.net/
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
%setup -q -n %{dirname}

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_sysconfdir}/xdg/autostart/mandriva-%{name}.desktop
%{_datadir}/autostart/mandriva-%{name}.desktop

