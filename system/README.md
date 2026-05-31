Create labels for disk devices

During startup, device nodes are created as new devices are discovered. This can mean that device names can change when new devices are added.


If you receive a ROOT MOUNT ERROR during startup, you should create labels for each discrete (such as a SATA or IDE drive or a removable USB) partition to avoid conflicts and changes. To learn how, see Labeling Disk Devices. Below are examples.


    Reboot the system into single user mode. This can be accomplished by selecting boot menu option 2 for FreeBSD 10.3+ (option 4 for FreeBSD 8.x), or performing a 'boot -s' from the boot prompt.

    In Single user mode, create GEOM labels for each of the IDE disk partitions listed in your fstab (both root and swap). Below is an example of FreeBSD 10.3.
```
    # cat  /etc/fstab
    # Device           Mountpoint      FStype  Options   Dump   Pass#
    /dev/da0p2         /               ufs     rw        1       1
    /dev/da0p3         none            swap    sw        0       0

    # glabel  label rootfs  /dev/da0p2
    # glabel  label swap   /dev/da0p3
    # exit
```
    Additional information on GEOM labels can be found at: Labeling Disk Devices.

    The system will continue with multi-user boot. After the boot completes, edit /etc/fstab and replace the conventional device names, with their respective labels. The final /etc/fstab will look like this:
```
    # Device                Mountpoint      FStype  Options         Dump    Pass#
    /dev/label/rootfs       /               ufs     rw              1       1
    /dev/label/swap         none            swap    sw              0       0
```


    The system can now be rebooted. If everything went well, it will come up normally and mount will show:
```
    # mount
    /dev/label/rootfs on / (ufs, local, journaled soft-updates)
    devfs on /dev (devfs, local, mutilabel)
```


Use a wireless network adapter as the virtual switch

If the virtual switch on the host is based on wireless network adapter, reduce the ARP expiration time to 60 seconds by the following command. Otherwise the networking of the VM may stop working after a while.
```
   # sysctl net.link.ether.inet.max_age=60
```
