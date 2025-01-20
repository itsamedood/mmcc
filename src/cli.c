#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cli.h"

/* Returns flags from the command line as `clflags_t` struct. */
clflags_t get_flags(int argc, char **argv)
{
  clflags_t flags = {
    .verbose = false,
    // .help = false,
    // .version = false
  };

  for (int i = 0; i < argc; i++)
  {
    char *arg = argv[i];

    /* Verbose flag. */
    if (strcmp(arg, "--verbose") == 0 || strcmp(arg, "-vb") == 0)
    {
      flags.verbose = true;
    }

    /* Help flag. */
    else if (strcmp(arg, "--help") == 0 || strcmp(arg, "-h") == 0)
    {
      printf("Usage: mmcc [flags] [leaderboard]\n");
      printf("Flags:\n");
      printf("  --help    | -h   | Displays this menu.\n");
      printf("  --version | -v   | Displays version and exits.\n");
      printf("  --verbose | -vb  | Prints debugging stuff.\n");
      printf("\n");

      exit(0);
    }

    /* Version flag. */
    else if (strcmp(arg, "--version") == 0 || strcmp(arg, "-v") == 0)
    {
      printf("mmcc v%s\n", MMCC_VERSION);
      exit(0);
    }
  }

  return flags;
}
