qemu-system-x86_64 -accel nvmm \
        -cpu max -smp cpus=2 -m 1G \
        -display sdl,gl=on \
        -cdrom NetBSD-9.1-amd64.iso


$ nvmmctl list
# Machine ID VCPUs RAM  Owner PID Creation Time
# ---------- ----- ---- --------- ------------------------
# 0          2     147M 10982     Sat May  8 10:09:59 2021
