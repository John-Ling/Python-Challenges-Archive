from random import randint

def main():
    COMMENTS = [
        "This student should be teaching instead of me. Please help I am suffering from impostor syndrome.",
        "One of the best students I have ever taught.",
        "This student is above average",
        "This student IS average",
        "This student is not the brightest",
        "This student makes photography darkrooms look bright in comparison",
        "How did this student get put in my class I think there has been a mistake"
    ]
    _generate_comment = lambda COMMENTS : COMMENTS[randint(0, len(COMMENTS) - 1)]
    
    studentCount = int(input("How many students are in your class: "))
    for i in range(1, studentCount + 1):
        print(f"Student {i}: {_generate_comment(COMMENTS)}")

if __name__ == "__main__":
    main()