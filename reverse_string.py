def main():
    string = str(input("Enter string to be reversed: "))
    print(reverse_string(string))

def reverse_string(string):
    answer = ""
    for c in reversed(string):
        answer += c
    return answer

if __name__ == "__main__":
    main()