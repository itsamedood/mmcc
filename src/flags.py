from out import throw
from sys import exit


class Flags:
    def __init__(self, _args: list[str]) -> None:
        self.flags_dict: dict[str, int | bool | list[str]] = {}

        for a in _args:
            if not a[0] == '-': throw(1, "unexpected '%s'." %a)

            eqsplit = a.split('=', 1)
            if len(eqsplit) > 1:
                global flag; flag, value = eqsplit[0][1:], eqsplit[1]
                if len(value) < 1: throw(1, "expected a value for flag '%s'." %flag)

                match flag:
                    case "list":
                        if value.isnumeric(): self.flags_dict[flag] = int(value)
                        else: throw(1, "value for flag '%s' must be an integer." %flag)

                    case "find":
                        queries = value.split(",")
                        self.flags_dict[flag] = queries

                    case _: throw(1, "unknown flag: '%s'" %flag)

            else:
                match a[1:]:
                    case "help":
                        print(*[
                            "Usage: mmcc [flags]\n",
                            "Flags:\n",
                            "  -list=<int>   ~ Change the length of the list of top commands used. Default is 3.\n",
                            "  -find=<query> ~ Shows list of commands used in query string in order of usage. Seperate commands by a `,`; `make,clear,...`.\n",
                            "  -help         ~ Displays this help menu.\n",
                            "  -debug        ~ Shows some boring debug stuff.\n",
                        ])
                        exit(0)

                    case "debug": self.flags_dict[a[1:]] = True

        if "debug" in self.flags_dict: print(self.flags_dict)

    def as_dict(self) -> dict[str, int | bool]: return self.flags_dict
