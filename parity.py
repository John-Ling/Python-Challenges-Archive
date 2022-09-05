def main():
    byte = str(input('Enter your byte: '))
    validate(byte)

def validate(byte):
    totalOnes = 0
    for bit in byte:
        if bit == '1':
            totalOnes += 1

    if totalOnes % 2 == 0:
        print("Nothing Wrong!")  
    else:
        print("An error has occurred")


if __name__ == "__main__":
    main()