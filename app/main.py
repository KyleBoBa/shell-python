import sys
import os

BUILT_IN = ["exit","echo","type","pwd","cd"]


def check_dir(location, directory):
    for dir in directory:
        path = os.path.join(dir, location)
        if (os.path.isfile(path) and os.access(path, os.X_OK)):
            return path
    return None


def exec(entry, command, args, directory):
    if command == BUILT_IN[0]:
        sys.exit()
    elif command == BUILT_IN[1]:
        print(f"{args}")
    elif command == BUILT_IN[2]:
        path = check_dir(args, directory)
        if args in BUILT_IN:
            print(f"{args} is a shell builtin")
        elif path:
            print(f"{args} is {path}")
        else:
            print(f"{args}: not found")
    elif command == BUILT_IN[3]:
        print(os.getcwd())
    elif command == BUILT_IN[4]:
        path = args.strip() or os.getenv("HOME", "")
        try:
            os.chdir(path)
        except FileNotFoundError:
            print(f"cd: {path}: No such file or directory")
    elif check_dir(command, directory):
        os.system(entry)
    else:
        print(f"{command}: command not found")


def main():
    PATH = os.getenv("PATH")
    directories = PATH.split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        entry = input()
        if entry != "":
            command = entry.split()[0]
            args = " ".join(entry.split()[1:])
            exec(entry, command, args, directories)
        

if __name__ == "__main__":
    main()
