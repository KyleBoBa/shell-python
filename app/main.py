import sys
import os

ALLOWED_COMMANDS = ["exit","echo","type"]
BUILT_IN_TYPES = ["exit","echo","type"]


def validate_command(command):
    if not (command in ALLOWED_COMMANDS):
        print(f"{command}: command not found")
        return False
    return True


def validate_type(args, directory):
    #1
    if args in BUILT_IN_TYPES:
        print(f"{args} is a shell builtin")
        return
    #2
    path = check_dir(args, directory)
    if path is not None:
        print(f"{args} is {path}")
        return
    #3
    print(f"{args}: not found")


def check_dir(location, directory):
    for dir in directory:
        path = os.path.join(dir, location)
        print(path)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None


def exec(command, args, directory):
    if not validate_command(command):
        return True
    if command == ALLOWED_COMMANDS[0]:
        return False
    elif command == ALLOWED_COMMANDS[1]:
        print(f"{args}")
    elif command == ALLOWED_COMMANDS[2]:
        validate_type(args, directory)
    else:
        print(command)
    return True


def main():
    PATH = os.environ.get("PATH")
    directories = PATH.split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        entry = input()
        command = entry.split()[0]
        args = " ".join(entry.split()[1:])

        if not exec(command, args, directories):
            break


if __name__ == "__main__":
    main()
