from cli import Cli
from mmcc import MMCC
from sys import argv


if __name__ == "__main__":
  cli = Cli(argv)
  verbose, lst = cli.read_args()
  mmcc = MMCC(verbose, lst)
