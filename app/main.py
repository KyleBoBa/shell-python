import sys
from allowed_commands import ALLOWED_COMMANDS as AC


def validate_command(command):
    if not (command in AC):
        sys.stdout.write(f"{command}: command not found\n")
        return False
    return True

def exec(command, args):
    if not validate_command(command):
        return True
    if command == AC[0]:
        return False
    elif command == AC[1]:
        print(f"{" ".join(args)}")
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
