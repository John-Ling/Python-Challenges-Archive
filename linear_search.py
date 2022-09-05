def main():
    arr = [1,2,3,4,5,6,2]

    search = int(input("What value are you looking for: "))

    totalFound = linear_search(arr, search)
    if totalFound != 0:
        print(f"Found value {totalFound} times")
    else:
        print("Nothing found")

def linear_search(arr, searchValue):
    totalFound = 0

    for value in arr:
        if value == searchValue:
            totalFound += 1
    
    return totalFound


if __name__ == "__main__":
    main()