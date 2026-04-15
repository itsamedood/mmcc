from cli import Cli
from sys import argv


if __name__ == "__main__":
  cli = Cli(argv)
  cli.read_args()
