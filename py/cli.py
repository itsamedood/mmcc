from flags import Flags
from sys import argv


class Cli:
    @staticmethod
    def construct_flags() -> Flags: return Flags(argv[1:])
