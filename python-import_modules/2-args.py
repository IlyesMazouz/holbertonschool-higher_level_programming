#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_arguments = len(argv) - 1
    print(
        "{} argument{}{}".format(
            num_arguments,
            "" if num_arguments == 1 else "s",
            "." if num_arguments == 0 else ":",
        )
    )

    if num_arguments > 0:
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
