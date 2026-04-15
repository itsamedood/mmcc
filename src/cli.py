class Cli:
  HELP = """Usage: mmcc [-help|-h | -verbose|-v | -list=<int>]
Flags:
  -help       | -h      Get help.
  -verbose    | -v      Neeeeerd.
  -list=<int> | -l      List as many commands as you want.
  """

  def __init__(self, argv: list[str]):
    self.argv = argv

  def read_args(self) -> None:
    if len(self.argv) < 2:
      print(self.HELP)
      return

    for arg in self.argv:
      if arg[0] == '-' and len(arg) > 1:
        match arg[1:]:
          case "help" | 'h':
            print(self.HELP)

          case "verbose" | 'v':
            print("Neeeerd")

          case "list" | 'l':
            print("Proper syntax is `-list=<int> OR -l=<int>`!")

          case _:
            if '=' in arg:
              name, i = arg.split('=')

              if name == 'list' or name == 'l':
                try:
                  i = int(i)
                except ValueError:
                  print("Argument must be a number!")

            else:
              print("`%s` is not a valid flag. Run `mmcc -help` for valid flags." %arg)
