#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mmcc.h"

char get_shelltype(void)
{
  char *shell = getenv("SHELL");
  char shelltype;

  if (strcmp(shell, "/bin/bash")==0)
  {
    shelltype = 'b';
  }
  else if (strcmp(shell, "/bin/zsh")==0)
  {
    shelltype = 'z';
  }
  else if (strcmp(shell, "/usr/bin/fish")==0)
  {
    shelltype = 'f';
  }
}

/* Determines the shell startup script according to `$SHELL`. */
char *determine_shell_rc(clflags_t *flags)
{
  size_t max_length = 500 * sizeof(char);
  char *hspath = (char*)malloc(max_length);
  char *shell = getenv("SHELL");
  char *home = getenv("HOME");
  int shelltype;

  if (shell == NULL)
  {
    printf("$SHELL is NULL.");
    exit(1);
  }

  /* Determining the startup script location. */
  if (strcmp(shell, "/bin/bash") == 0)
  {
    if (snprintf(hspath, max_length, "%s/.bash_history", home) >= max_length)
    {
      fputs("Buffer exceeded, string truncated.", stderr);
    }

    shelltype = 0; /* 0 = BASH. */
  }
  else if (strcmp(shell, "/bin/zsh") == 0)
  {
    if (snprintf(hspath, max_length, "%s/.zsh_history", home) >= max_length)
    {
      fputs("Buffer exceeded, string truncated.", stderr);
    }

    shelltype = 1; /* 1 = ZSH. */
  }
  else if (strcmp(shell, "/usr/bin/fish") == 0)
  {
    if (snprintf(hspath, max_length, "%s/.local/share/fish/fish_history", home) >= max_length)
    {
      fputs("Buffer exceeded, string truncated.", stderr);
    }

    shelltype = 2;  /* 2 = FISH. */
  }
  else
  {
    fputs("$SHELL not supported.", stderr);
    exit(1);
  }

  if (flags->verbose)
  {
    printf("$SHELL: %s\n$HOME: %s\n", shell, home);
    printf("Final 'history (hs)' path: %s\n", hspath);
  }

  return hspath;
}

void count_commands(char *hspath, clflags_t *flags, char shelltype)
{
  FILE *hsfile = fopen(hspath, "r");
  char line[MAX_LINE_LENGTH];

  if (hsfile == NULL)
  {
    fputs("Could not open history file for reading.", stderr);
    exit(1);
  }

  /* Read lines. */
  while (fgets(line, MAX_LINE_LENGTH, hsfile) != NULL)
  {
    switch (shelltype)
    {
      case 'b': /* BASH. */
        /* ... */
        break;

      case 'z': /* ZSH. */
        /* ... */
        break;

      case 'f': /* FISH. */
        /* ... */
        break;
    }
  }

  fclose(hsfile);
}
