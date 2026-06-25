#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Fetch all attributes defined in the module
    names = dir(hidden_4)

    # Sort the names alphabetically
    names.sort()

    # Loop through and print names that do NOT start with '__'
    for name in names:
        if not name.startswith("__"):
            print("{}".format(name))
