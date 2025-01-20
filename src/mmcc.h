#ifndef MMCC_H
#define MMCC_H
#define MAX_LINE_LENGTH 1000
#define BASH 'b'
#define ZSH 'z'
#define FISH 'f'
#include "cli.h"

char get_shelltype(void);
char *determine_shell_rc(clflags_t *flags);
void count_commands(char *rcpath, clflags_t *flags, char shelltype);
#endif /* MMCC_H */
