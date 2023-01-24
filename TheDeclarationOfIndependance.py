# programmer: Roman Cleary
# date:1.20.2023
# Program: Infotech center upgrades
"""
Our welcome screen will start our program letting
drivers know that the InfoTech Center 4.0 OS is loading
"""
import time
import sys
x=2
a=0

print("\n\nWelcome - Infotech Center 4.0")
time.sleep(x)


while x != 20:
    x += 1
    b = ("\033[1;33;40m InfoTech Center OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.5)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[1;32;40m Done!')