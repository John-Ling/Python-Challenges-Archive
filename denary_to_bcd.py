def main():
    denary = str(input("enter a denary value: "))
    print(convert(denary))

def convert(denaryValue):
    binary = ""
    binaryValues = [8,4,2,1]

    for digit in denaryValue:
        digit = int(digit)

        for value in binaryValues:
            if digit - value < 0:
                binary += '0'
            else:
                binary += '1'
                digit -= value
    
    return binary

if __name__ == "__main__":
    main()