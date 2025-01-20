from cli import Cli
from mmcc import MMCC
from out import throw


if __name__ == "__main__":
    try:
        mmcc = MMCC(Cli.construct_flags().as_dict())
        mmcc.print_out_most_common_commands(mmcc.read_through_shell_history())
    except FileNotFoundError: throw(1, "history file doesn't exist.")
