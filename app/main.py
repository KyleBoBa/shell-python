import sys

ALLOWED_COMMANDS = ["exit","echo","type"]
BUILT_IN_TYPES = ["exit","echo","type"]


def validate_command(command):
    if not (command in ALLOWED_COMMANDS):
        sys.stdout.write(f"{command}: command not found\n")
        return False
    return True


def validate_type(args):
    if not (args in BUILT_IN_TYPES):
        sys.stdout.write(f"{args}: not found\n")
        return False
    return True


def exec(command, args):
    if not validate_command(command):
        return True
    if command == ALLOWED_COMMANDS[0]:
        return False
    elif command == ALLOWED_COMMANDS[1]:
        print(f"{" ".join(args)}")
    elif command == ALLOWED_COMMANDS[2]:
        if not validate_type(args[0]):
            return True
        print(f"{args[0]} is a shell builtin")
    else:
        print(command)
    return True


def main():
    while True:
        sys.stdout.write("$ ")
        entry = input()
        command = entry.split()[0]
        args = entry.split()[1:]

        if not exec(command, args):
            break


if __name__ == "__main__":
    main()
