import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.write(f"{input()}: command not found\n")

if __name__ == "__main__":
    main()
