from platform import system
from os import getenv
from os.path import expanduser
from sys import exit


class MMCC:
    def __init__(self) -> None:
        OS = system()
        shell: str | None

        match OS:
            case "Windows": shell = None  # Can't be bothered lol
            case "Darwin" | "Linux": shell = getenv("SHELL")
            case _: shell = None

        if shell is None: print("OS not supported."); exit(1)

        match shell.split('/')[-1]:
            case "zsh": self.SHELL, self.HISTFILE = "zsh", expanduser("~/.zsh_history")
            case "bash": self.SHELL, self.HISTFILE = "bash", expanduser("~/.bash_history")
            case _: print("Shell not supported."); exit(1)


    def read_through_shell_history(self) -> dict[str, int]:
        occurrence_dict: dict[str, int] = {}

        match self.SHELL:
            case "zsh":
                file = expanduser("~/.zsh_history")

                with open(file, 'r+b') as histfile:
                    lines = histfile.readlines()

                    for bline in lines:
                        line = bline.decode("latin-1")
                        line = line[:-1]  # Removes the trailing newline character.
                        if not len(line) > 0: continue

                        try: global actual_cmd; actual_cmd = line.split(';', 1)[1]
                        except: actual_cmd = line

                        if any(char.isspace() for char in actual_cmd): actual_cmd = actual_cmd.split(' ')[0]

                        if actual_cmd not in occurrence_dict: occurrence_dict[actual_cmd] = 1
                        else: occurrence_dict[actual_cmd] += 1

                    histfile.close()

            case "bash":
                file = expanduser("~/.bash_history")

                with open(file, 'r+b') as histfile:
                    lines = histfile.readlines()

                    for bline in lines:
                        line = bline.decode("latin-1")
                        line = line[:-1]  # Removes the trailing newline character.
                        if not len(line) > 0: continue

                        if any(char.isspace() for char in line): line = line.split(' ')[0]

                        if line not in occurrence_dict: occurrence_dict[line] = 1
                        else: occurrence_dict[line] += 1

                histfile.close()

        return occurrence_dict


    def print_out_most_common_commands(self, _occurrence_dict: dict[str, int]) -> None:
        most_common = ''

        for command in _occurrence_dict:
            if not len(most_common) > 0: most_common = command
            if _occurrence_dict[command] > _occurrence_dict[most_common]: most_common = command

        sorted_occurrences = dict(sorted(_occurrence_dict.items(), key=lambda item: item[1], reverse=True))  # Sorts keys by their values in numerical order.
        keys = list(sorted_occurrences.keys())

        print("Most common commands according to .%s_history:" %self.SHELL)
        for i in range(0, 3):
            cmd, count = keys[i], sorted_occurrences[keys[i]]
            print(f"{i+1}) {cmd} - {count}")
