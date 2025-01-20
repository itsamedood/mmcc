#include <stdlib.h>
#include <stdio.h>
#include "cli.h"
#include "mmcc.h"

int main(int argc, char **argv)
{
  clflags_t flags = get_flags(argc, argv);
  char *rc = determine_shell_rc(&flags);
  count_commands(rc, &flags);

  printf("%s\n", rc);
  free(rc);
  return 0;
}
