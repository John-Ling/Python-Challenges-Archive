def main():
    SAMPLE_STRING = "Computer Science"
    print(f"Regular String: {SAMPLE_STRING}")
    print(f"Reverse String: {SAMPLE_STRING[::-1]}")
    print(f"Characters from Index 9 Onwards: {SAMPLE_STRING[9::]}")
    print(f"First Character of String: {SAMPLE_STRING[0]}")
    print(f"Last Character of String {SAMPLE_STRING[-1]}")
    print(f"Substring Starting from Index 1: {SAMPLE_STRING[1:]}")
    print(f"Substring Starting from Index 0 to 8: {SAMPLE_STRING[0:8]}")

if __name__ == "__main__":
    main()