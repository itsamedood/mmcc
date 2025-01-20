#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mmcc.h"

/* Determines the shell startup script according to `$SHELL`. */
char *determine_shell_rc(clflags_t *flags)
{
  size_t max_length = 100 * sizeof(char);
  char *rcpath = (char*)malloc(max_length);
  char *shell = getenv("SHELL");
  char *home = getenv("HOME");

  if (shell == NULL)
  {
    printf("$SHELL is NULL.");
    exit(1);
  }

  /* Determining the startup script location. */
  if (strcmp(shell, "/bin/bash") == 0)
  {
    if (snprintf(rcpath, max_length, "%s/.bashrc", home) >= max_length)
    {
      fputs("Buffer exceeded, string truncated.", stderr);
    }
  }
  else if (strcmp(shell, "/bin/zsh") == 0)
  {
    snprintf(rcpath, max_length, "%s/.zshrc", home);
  }
  else if (strcmp(shell, "/usr/bin/fish") == 0)
  {
    snprintf(rcpath, max_length, "%s/.config/fish/config.fish", home);
  }
  else
  {
    printf("$SHELL not supported.");
    exit(1);
  }

  if (flags->verbose)
  {
    printf("$SHELL: %s\n$HOME: %s\n", shell, home);
    printf("Final 'rc' path: %s\n", rcpath);
  }

  return rcpath;
}

void count_commands(char *rcpath, clflags_t *flags)
{
  //
}
