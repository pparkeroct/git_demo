import sys

def easter_egg():
    print("You found the Easter Egg! 🐰")

def main():
    message = "Hello, World!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    if message.lower() == "easter_egg":
        easter_egg()
    else:
        print(message)

if __name__ == "__main__":
    main()