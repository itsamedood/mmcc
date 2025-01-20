#ifndef MMCC_H
#define MMCC_H
#include "cli.h"

char *determine_shell_rc(clflags_t *flags);
void count_commands(char *rcpath, clflags_t *flags);
#endif /* MMCC_H */
