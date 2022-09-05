def main():
    word = str(input("Enter a word: "))
    print(make_it_laugh(word))

def make_it_laugh(word):
    vowels = "aeiou"
    answer = ""
    for c in word:
        if c in vowels:
            answer += "haha"
        else:
            answer += c
    return answer

if __name__ == "__main__":
    main()