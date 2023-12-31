from os import getenv
from os.path import expanduser
from out import throw
from platform import system
from sys import exit


class MMCC:
    def __init__(self, _flags: dict[str, int | bool | list[str]]) -> None:
        self.FLAGS = _flags
        OS = system()
        shell: str | None

        match OS:
            case "Windows":
                shell = getenv("SHELL")
                if shell is None: throw(1, "SHELL variable not set. Are you using bash?")
                else: shell = shell.split('\\')[-1].removesuffix(".exe")

            case "Darwin" | "Linux": shell = getenv("SHELL")
            case _: shell = None

        if shell is None: throw(1, "OS not supported.")
        else:
            match shell.split('/')[-1]:
                case "zsh": self.SHELL, self.HISTFILE = "zsh", expanduser("~/.zsh_history")
                case "bash": self.SHELL, self.HISTFILE = "bash", expanduser("~/.bash_history")
                case _: throw(1, "unknown shell.")


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

        if "debug" in self.FLAGS: print(sorted_occurrences)

        llen = 3
        if "find" in self.FLAGS:
            filtered_dict: dict[str, int] = {}

            for o in sorted_occurrences:
               if o in self.FLAGS["find"]: filtered_dict[o] = sorted_occurrences[o]

            if "debug" in self.FLAGS: print(filtered_dict)

            print("Most common commands according to .%s_history, based off your query:" %self.SHELL)
            for i, f in enumerate(filtered_dict): print(f"{i+1}) {f} - {filtered_dict[f]}")
            exit(0)

        elif "list" in self.FLAGS:
            llen = self.FLAGS["list"]
            if not (llen > 0 and llen <= len(_occurrence_dict)): throw(1, "invalid length, you only have %s commands run." %len(_occurrence_dict))

        print("Most common commands according to .%s_history:" %self.SHELL)
        for i in range(0, llen):
            cmd, count = keys[i], sorted_occurrences[keys[i]]
            print(f"{i+1}) {cmd} - {count}")
