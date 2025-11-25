import sys
import os
import subprocess

ALLOWED_COMMANDS = ["exit","echo","type"]
BUILT_IN_TYPES = ["exit","echo","type"]


def validate_command(command):
    if not (command in ALLOWED_COMMANDS):
        print(f"{command}: command not found")
        return False
    return True


def check_dir(location, directory, bol):
    for dir in directory:
        path = os.path.join(dir, location)
        if os.path.isfile(path):
            if (bol and os.access(path, os.X_OK)):
                return path
            return path
    return None


def exec(entry, command, args, directory):
    path = check_dir(command, directory, 0)
    if command == ALLOWED_COMMANDS[0]:
        sys.exit()
    elif command == ALLOWED_COMMANDS[1]:
        print(f"{args}")
    elif command == ALLOWED_COMMANDS[2]:
        path = check_dir(args, directory, 1)
        if args in BUILT_IN_TYPES:
            print(f"{args} is a shell builtin")
        elif path:
            print(f"{args} is {path}")
        else:
            print(f"{args}: not found")
    elif path:
        subprocess.run(entry)
    else:
        validate_command(command)


def main():
    PATH = os.environ.get("PATH")
    directories = PATH.split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        entry = input().split()
        if entry != "":
            command = entry[0]
            args = " ".join(entry[1:])
            exec(entry, command, args, directories)
        

if __name__ == "__main__":
    main()
