#define _GNU_SOURCE
#include <fcntl.h>
#include <stdio.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <sched.h>
#include <sys/mman.h>
#include <sys/syscall.h>

static inline uint64_t now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);   /* VDSO, no syscall */
    return (uint64_t)ts.tv_sec * 1000000000ull + ts.tv_nsec;
}

int main(int argc, char **argv) {
    const char *path = argv[1];
    uint64_t n      = strtoull(argv[2], NULL, 10);
    uint64_t warm   = n / 10;

    /* preallocate + prefault + lock: no page faults in the loop */
    uint32_t *d = mmap(NULL, n * sizeof(uint32_t), PROT_READ|PROT_WRITE,
                       MAP_PRIVATE|MAP_ANONYMOUS|MAP_POPULATE, -1, 0);
    mlock(d, n * sizeof(uint32_t));
    for (uint64_t i = 0; i < n; i++) d[i] = 0;   /* fault everything in */

    for (uint64_t i = 0; i < n; i++) {
        uint64_t t0 = now_ns();
        long fd = syscall(SYS_openat, AT_FDCWD, path, O_RDONLY);   /* raw, no libc wrapper */
        uint64_t t1 = now_ns();
        if (fd >= 0) close(fd);
        d[i] = (uint32_t)(t1 - t0);
    }

    /* dump after the loop only */
    for (uint64_t i = warm; i < n; i++) printf("%u\n", d[i]);
    return 0;
}
