##
# UNICAL, 2023
# main.py
# File description:
# This is the main for the project
##

#!/usr/bin/env python

def UserInterface():
    print("------------------------------------------------------------------")
    print("Hi ! /h or /help if you need the list of the commands")
    print("------------------------------------------------------------------")
    return True


def UserHelper():
    print("-------------------------------------------------------------------------")
    print("/h or /help : Get command list")
    print("/exit : Exit the program")
    print("/addfiles PathFile1.txt PathFile2.txt ... PathFileN.txt: Add List of txt")
    print("-------------------------------------------------------------------------")
    return True


def UserInputCatch():
    UserCommand = ''
    while UserCommand != '/exit':
        UserCommand = input("> ")
        if (UserCommand == '/h' or UserCommand == '/help'):
            print('help')
        if (UserCommand == '/exit'):
            print('Thanks you, Ciao ! \n')
            break
        if (UserCommand == '/addfiles'):
            print("Add Files")
    return True


def main():
    UserInterface()
    UserInputCatch()


if __name__ == '__main__':
    main()
