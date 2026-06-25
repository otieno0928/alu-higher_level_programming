#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # sys.argv[0] is the script name, subtract 1 for actual count
    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i in range(1, count + 1):
        print("{}: {}".format(i, sys.argv[i]))
