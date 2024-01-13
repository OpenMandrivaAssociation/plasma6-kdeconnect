%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define oname kdeconnect-kde

Summary:	Connect KDE with your smartphone
Name:		plasma6-kdeconnect
Version:	24.01.90
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://albertvaka.wordpress.com/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{oname}-%{version}.tar.xz
# (tpg) add firewalld rule
# https://issues.openmandriva.org/show_bug.cgi?id=1491
Source1:	kde-connect.xml
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6PulseAudioQt)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(libfakekey)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	cmake(WaylandProtocols)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	cmake(KF6ModemManagerQt)
BuildRequires:	kirigami-addons
Requires:   kirigami
Requires:	kirigami-addons
Requires:   kirigami-addons-kde6
Requires:   qt6-qtquickcontrols
Requires:   qt6-qtquickcontrols2
Requires:   qt6-qtdeclarative
Requires:	sshfs
Requires:	%{_lib}qca2-plugin-openssl
Requires(post):	/bin/sh
# There is no point in separate libpackages for internal libraries.
# They can't be used outside of kdeconnect (no shipped headers or
# *.so files).
# Get rid of them.
Obsoletes:	%{mklibname kdeconnectcore 0} < 23.04.0
Obsoletes:	%{mklibname kdeconnectcore 1} < 23.04.0
Obsoletes:	%{mklibname kdeconnectcore 20} < 23.04.0
Obsoletes:	%{mklibname kdeconnectcore 21} < 23.04.0
Obsoletes:	%{mklibname kdeconnectinterfaces 0} < 23.04.0
Obsoletes:	%{mklibname kdeconnectinterfaces 1} < 23.04.0
Obsoletes:	%{mklibname kdeconnectinterfaces 20} < 23.04.0
Obsoletes:	%{mklibname kdeconnectinterfaces 21} < 23.04.0
Obsoletes:	%{mklibname kdeconnectpluginkcm 0} < 23.04.0
Obsoletes:	%{mklibname kdeconnectpluginkcm 1} < 23.04.0
Obsoletes:	%{mklibname kdeconnectpluginkcm 20} < 23.04.0
Obsoletes:	%{mklibname kdeconnectpluginkcm 21} < 23.04.0

%description
KDE Connect is a module to connect KDE with your smartphone.
You need to install KdeConnect.apk on your smartphone to make it work.

%package nautilus
Summary:	KDE Connect integration for Nautilus
Recommends:	nautilus
Requires:	%{name} = %{EVRD}

%description nautilus
KDE Connect integration for Nautilus

%package thunar
Summary:	KDE Connect integration for Thunar
Recommends:	thunar
Requires:	%{name} = %{EVRD}

%description thunar
KDE Connect integration for Thunar

%package deepin
Summary:	KDE Connect integration for the deepin file manager
Requires:	%{name} = %{EVRD}

%description deepin
KDE Connect integration for the deepin file manager

%files -f %{name}.lang
%{_bindir}/kdeconnect-app
%{_bindir}/kdeconnect-cli
%{_bindir}/kdeconnect-handler
%{_bindir}/kdeconnect-indicator
%{_bindir}/kdeconnect-settings
%{_bindir}/kdeconnect-sms
%{_libdir}/libkdeconnectcore.so.*
%{_libdir}/libkdeconnectpluginkcm.so.*
%{_datadir}/metainfo/org.kde.kdeconnect.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/knotifications6/kdeconnect.notifyrc
%{_libdir}/libexec/kdeconnectd
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kdeconnect.so
%{_qtdir}/plugins/kdeconnect
%{_qtdir}/plugins/kf6/kio/*.so
%{_qtdir}/plugins/kf6/kfileitemaction/*.so
%dir %{_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_datadir}/plasma/plasmoids/org.kde.kdeconnect/*
%dir %{_qtdir}/qml/org/kde/kdeconnect
%{_qtdir}/qml/org/kde/kdeconnect/*
%{_prefix}/lib/firewalld/services/kde-connect.xml
%{_datadir}/kdeconnect
%{_datadir}/qlogging-categories6/kdeconnect-kde.categories
%{_datadir}/contractor/kdeconnect.contract
%{_datadir}/icons/*/*/*/*
%{_datadir}/zsh/site-functions/_kdeconnect
%{_datadir}/metainfo/org.kde.kdeconnect.metainfo.xml

%files nautilus -f kdeconnect-nautilus-extension.lang
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py

%files thunar
%{_datadir}/Thunar/sendto/kdeconnect-thunar.desktop

%files deepin
%{_datadir}/deepin/dde-file-manager/oem-menuextensions/kdeconnect-dde.desktop

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -DEXPERIMENTALAPP_ENABLED=ON

%build
%ninja -C build

%install
%ninja_install -C build

install -m644 -p -D %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/kde-connect.xml

# No need to package a static helper lib
rm %{buildroot}%{_libdir}/*.a

%find_lang kdeconnect kdeconnect-cli kdeconnect-core kdeconnect-fileitemaction kdeconnect-kcm kdeconnect-kde kdeconnect-kded kdeconnect-plugins kdeconnect-kio kdeconnect-urlhandler plasma_applet_org.kde.kdeconnect kdeconnect-sms kdeconnect-app kdeconnect-indicator kdeconnect-interfaces kdeconnect-settings %{name}.lang --with-html
%find_lang kdeconnect-nautilus-extension --with-html

%post
# (tpg) reload firewalld
if [ -x /usr/bin/firewall-cmd ]; then
    /usr/bin/firewall-cmd --permanent --add-service kde-connect 2&>1 ||:
    /usr/bin/firewall-cmd --reload 2&>1 ||:
fi