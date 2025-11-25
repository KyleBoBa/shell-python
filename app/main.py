import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        if command == "exit":
            break
        sys.stdout.write(f"{command}: command not found\n")
        

if __name__ == "__main__":
    main()
