#ifndef CLI_H
#define CLI_H
#define MMCC_VERSION "0.0.01a"
#include <stdbool.h>

typedef struct ClFlags {
  bool verbose;
  // bool help;
  // bool version;
} clflags_t;

clflags_t get_flags(int argc, char **argv);
#endif /* CLI_H */
