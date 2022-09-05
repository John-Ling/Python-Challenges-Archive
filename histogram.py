def main():
    histogram([4,9,7])

def histogram(nums):
    for num in nums:
        for i in range(num):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()