import random
version_file = open('VERSION')
version = version_file.read().strip()

logo = """  /$$$$$$$  /$$      /$$       /$$$$$$$  /$$             /$$
 | $$__  $$| $$$    /$$$      | $$__  $$| $$            | $$
 | $$  \ $$| $$$$  /$$$$      | $$  \ $$| $$  /$$$$$$  /$$$$$$   /$$$$$$$
 | $$  | $$| $$ $$/$$ $$      | $$$$$$$/| $$ /$$__  $$|_  $$_/  /$$_____/
 | $$  | $$| $$  $$$| $$      | $$____/ | $$| $$  \ $$  | $$   |  $$$$$$
 | $$  | $$| $$\  $ | $$      | $$      | $$| $$  | $$  | $$ /$$\____  $$
 | $$$$$$$/| $$ \/  | $$      | $$      | $$|  $$$$$$/  |  $$$$//$$$$$$$/
 |_______/ |__/     |__/      |__/      |__/ \______/    \___/ |_______/"""


tagLine = "Make some plots already..."

toolsVersion = version

def main():
    print ""
    printLogo(version)
    print "\n\t\t\t", tagLine, "\n"

    print "    DMPlots version          :", toolsVersion
    print "\n"



def printLogo(version):
    lightDark = version.split(".")[0]
    lightDark = int(lightDark) + 1 % 2
    if lightDark == 0:
        lightDark ="3"
    else:
        lightDark ="9"

    colour = version.split(".")[1]
    colour = str(int(colour) % 7+1)

    CSI="\x1B[49m\x1B["

    print CSI+lightDark+colour+"m" + logo + CSI + "0m"


if __name__ == "__main__":
    main()
