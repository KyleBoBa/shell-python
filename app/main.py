import sys
import os
import subprocess
import shlex
import readline


def check_dir(location):
    executables = {}
    for dir in directory:
        path = os.path.join(dir, location)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            if location == "":
                executables[dir] = path
            else:
                return path
    if location == "":
        return executables
    else:
        return None


def validate_type(args):
    path = check_dir(args)
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


def completer(text: str, state: int) -> str | None:
    builtin_matches = [cmd + " " for cmd in BUILT_IN if cmd.startswith(text)]
    exe_matches = [cmd + " " for cmd in EXECUTABLES if cmd.startswith(text)]
    if exe_matches:
        return exe_matches[state] if state < len(exe_matches) else None
    elif builtin_matches:
        return builtin_matches[state] if state < len(builtin_matches) else None
    else:
        print("\x07")
        return None


def execute_command(entry):
    command = entry[0]
    args = entry[1:]
    if command in BUILT_IN:
        BUILT_IN[command](*args)
    elif check_dir(command):
        subprocess.run(entry)
    else:
        print(f"{command}: command not found")


def main():
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

    while True:
        sys.stdout.write("$ ")
        entry = input().strip()
        if ">" in entry or "1>" in entry:
            os.system(entry)
        elif entry != "":
            entry = shlex.split(entry)
            execute_command(entry)

BUILT_IN = {
    "exit": lambda: sys.exit(),
    "echo": lambda *args: print(" ".join(args)),
    "type": lambda args: validate_type(args),
    "pwd": lambda: print(os.getcwd()),
    "cd": lambda args: change(args),
}

PATH = os.getenv("PATH")
directory = PATH.split(os.pathsep)

EXECUTABLES = check_dir("")


if __name__ == "__main__":
    main()
