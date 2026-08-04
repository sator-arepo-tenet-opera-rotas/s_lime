#include <stdio.h>
#include <unistd.h>

int setpgid(pid_t pid, pid_t pgid);

typedef struct {
    void (*function)(int);
    int value;
} anonFunction;

void execute(anonFunction af) {
    af.function(af.value);
}
void printNumber(int n) {
    printf("The number is %d\n", n);
}
int main() {
    anonFunction af = { printNumber, 5 };
    execute(af);
    return 0;
}
