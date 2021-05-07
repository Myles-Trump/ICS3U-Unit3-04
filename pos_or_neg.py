#!/usr/bin/env python3
# Created by: Myles Trump
# Created on: May 2021
# This program lets the user know if their integer is poitive or negative


def main():
    # this function lets the user enter an integer
    #   and tells the user if their integer is positive or negative

    # input
    selected_integer = int(input("Enter an integer: "))
    print("")
    # process & output
    if selected_integer > 0:
        print("Your integer, {0}, is positive".format(selected_integer))

    elif selected_integer < 0:
        print("Your integer, {0}, is negative".format(selected_integer))

    elif selected_integer == 0:
        print("Your integer, {0}, is zero".format(selected_integer))

    print("\nDone.")


if __name__ == "__main__":
    main()
