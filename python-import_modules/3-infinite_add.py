#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # Start iterating from index 1 to skip the script name
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
