import sys

def main():
    message = "Hello, World!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    print(message)

if __name__ == "__main__":
    main()