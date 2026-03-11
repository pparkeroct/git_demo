import sys

def easter_egg():
    print("You found the Easter Egg! 🐰")

def christmas_tree():
    tree = [
        "   *   ",
        "  ***  ",
        " ***** ",
        "*******",
        "  ***  ",
        "  ***  "
    ]
    for line in tree:
        print(line)

def main():
    message = "Hello, World!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    if message.lower() == "easter_egg":
        easter_egg()
    elif message.lower() == "christmas_tree":
        christmas_tree()
    else:
        print(message)

if __name__ == "__main__":
    main()