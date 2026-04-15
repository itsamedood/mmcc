from os import getenv
from sys import exit


class MMCC:
  """ Handles the actual work of opening your shell history file and reading through it. """

  def __init__(self, verbose: bool, lst: int) -> None:
    self.verbose = verbose
    self.lst = lst

    if verbose:
      print("List:", lst)  # Just to know.

    # Determine shell.
    shell = getenv("SHELL")

    if shell is None:
      print("$SHELL returned None.")
      exit(1)

    self.shell = shell.split('/')[-1]

    if self.verbose:
      print(self.shell)
