from mmcc import *


if __name__ == "__main__":
    mmcc = MMCC()
    mmcc.print_out_most_common_commands(mmcc.read_through_shell_history())
