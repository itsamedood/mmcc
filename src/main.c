#include <stdlib.h>
#include <stdio.h>
#include "cli.h"
#include "mmcc.h"

int main(int argc, char **argv)
{
  clflags_t flags = get_flags(argc, argv);
  char shelltype = get_shelltype();
  char *rc = determine_shell_rc(&flags);
  count_commands(rc, &flags, shelltype);

  printf("%s\n", rc);
  free(rc);
  return 0;
}
