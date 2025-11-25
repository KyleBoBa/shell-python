import sys
import os
import subprocess
import shlex

BUILT_IN = {
    "exit": lambda: sys.exit(),
    "echo": lambda *args: print(" ".join(args)),
    "type": lambda args: validate_type(args),
    "pwd": lambda: print(os.getcwd()),
    "cd": lambda args: change(args),
}


def check_dir(location, directory):
    PATH = os.getenv("PATH")
    directory = PATH.split(os.pathsep)
    for dir in directory:
        path = os.path.join(dir, location)
        if (os.path.isfile(path) and os.access(path, os.X_OK)):
            return path
    return None


def validate_type(args):
    PATH = os.getenv("PATH")
    directory = PATH.split(os.pathsep)
    path = check_dir(args, directory)
    if args in BUILT_IN:
        print(f"{args} is a shell builtin")
    elif path:
        print(f"{args} is {path}")
    else:
        print(f"{args}: not found")


def change(args):
    path = args.strip()
    if path != "~":
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"cd: {path}: No such file or directory")
    else:
        os.chdir(os.getenv("HOME", ""))

def exec(entry, directory):
    command = entry[0]
    args = entry[1:]
    if command in BUILT_IN:
        BUILT_IN[command](*args)
    elif check_dir(command, directory):
        subprocess.run(entry)
    else:
        print(f"{command}: command not found")


def main():
    PATH = os.getenv("PATH")
    directories = PATH.split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        entry = input().strip()
        if entry != "":
            entry = shlex.split(entry)
            if ">" in entry or "1>" in entry:
                subprocess.run(entry)
            exec(entry, directories)


if __name__ == "__main__":
    main()
