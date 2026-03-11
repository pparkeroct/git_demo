import sys

def greet(name):
    return f"Hello, {name}!"

def easter_egg():
    print("You found the Easter Egg! 🐰")

def main():
    message = "Hello, World!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    if message.lower() == "easter egg":
        easter_egg()
    else:
        print(greet(message))

if __name__ == "__main__":
    main()