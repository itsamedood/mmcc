from cli import Cli
from mmcc import MMCC


if __name__ == "__main__":
    mmcc = MMCC(Cli.construct_flags().as_dict())
    mmcc.print_out_most_common_commands(mmcc.read_through_shell_history())
