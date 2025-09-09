import sys

def main():
    if len(sys.argv) != 4:  
        print("Usage: python add.py num1 num2 num3")
        return

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])

    total = num1 + num2 + num3
    print("Sum =", total)

if __name__ == "__main__":
    main()
