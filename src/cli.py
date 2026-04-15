from sys import exit


class Cli:
  """ Handles arguments from the CLI. """

  HELP = """Usage: mmcc [-help|-h | -verbose|-v | -list=<int>]
Flags:
  -help       | -h      Get help.
  -verbose    | -v      Neeeeerd.
  -list=<int> | -l      List as many commands as you want.
  """

  def __init__(self, argv: list[str]):
    self.argv = argv

  def read_args(self) -> tuple[bool, int]:
    """ Reads through `self.argv` and returns (`bool` for verbose flag, and `int` for list flag). """

    verbose, lst = False, None

    if len(self.argv) < 2:
      print(self.HELP)
      exit(0)

    for arg in self.argv:
      if arg[0] == '-' and len(arg) > 1:
        match arg[1:]:
          case "help" | 'h':
            print(self.HELP)
            exit(0)

          case "verbose" | 'v':
            verbose = True

          case "list" | 'l':
            print("Proper syntax is `-list=<int> OR -l=<int>`!")

          case _:
            if '=' in arg:
              name, i = arg.split('=')
              name = name[1:]

              if name == 'list' or name == 'l':
                try:
                  i = int(i)
                  lst = i
                except ValueError:
                  print("Argument must be a number!")

            else:
              print("`%s` is not a valid flag. Run `mmcc -help` for valid flags." %arg)

    return (verbose, lst if lst is not None else 10)  # 10 is the default value.
