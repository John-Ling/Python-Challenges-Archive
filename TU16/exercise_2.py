import string


def main():
    numbers = [45, 12, 76, 23, 86, 21, 97, 45, 4, 67]

    for num in numbers:
        print(f"Binary: {int_to_binary(num)}\nHexadecimal: {num:x}\nDecimal: {num:d}")

def int_to_binary(number):
    return (f"{number:b}")

if __name__ == "__main__":
    main()