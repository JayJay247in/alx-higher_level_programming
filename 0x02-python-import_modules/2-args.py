#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    print("{} argument{}".format(argc, "s" if argc != 1 else ""))
    if argc > 1:
        print(":.")
        for arg in range(1, argc):
            print("{}: {}".format(arg, sys.argv[arg]))
