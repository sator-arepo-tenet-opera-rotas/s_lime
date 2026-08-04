X11 and Intel Graphics

Xorg requires the Intel video drivers from the package drm-fbsd12.0-kmod (metapackage: drm-kmod). I’ve found building them from ports to work more reliably than installing from packages. After installation, load them at boot by adding kld_list="/boot/modules/i915kms.ko" to /etc/rc.conf.
