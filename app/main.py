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


def check_dir(location, directory):
    for dir in directory:
        path = os.path.join(dir, location)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None


def exec(command, args, directory):
    path = check_dir(args, directory)
    if command == ALLOWED_COMMANDS[0]:
        sys.exit()
    elif command == ALLOWED_COMMANDS[1]:
        print(f"{args}")
    elif command == ALLOWED_COMMANDS[2]:
        if args in BUILT_IN_TYPES:
            print(f"{args} is a shell builtin")
        elif path is not None:
            print(f"{args} is {path}")
        else:
            print(f"{args}: not found")
    elif path:
        subprocess.Popen(path, stdout=subprocess.PIPE)
    else:
        validate_command(command)


def main():
    PATH = os.environ.get("PATH")
    directories = PATH.split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        entry = input()
        if entry != "":
            command = entry.split()[0]
            args = " ".join(entry.split()[1:])
            exec(command, args, directories)
        

if __name__ == "__main__":
    main()
