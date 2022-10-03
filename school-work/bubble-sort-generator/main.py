from random import randint

QUESTION_COUNT = 0

def main():
    global QUESTION_COUNT
    questionCount = 0
    with open("bubble_sort_questions.txt", "r") as file:
        for line in file:
            questionCount += 1
        
    QUESTION_COUNT = questionCount
    while True:
        print("Welcome to the bubble sort generaor")
        print("""
        1: Attempt question
        2: Create question
        3: Quit
        """)
        selection = str(input("Enter your choice: "))
        if selection == "1":
            attempt_question()
        elif selection == "2":
            create_question()
        elif selection == "3":
            break

def attempt_question():
    global QUESTION_COUNT
    questionNumber = randint(1, QUESTION_COUNT)

    print(f"Generated {questionNumber}")
    count = 0
    numbers = ""
    with open("bubble_sort_questions.txt", 'r') as file:
        questionFound = False
        while not questionFound:
            print(count)
            if count == questionNumber:
                break
            else:
                numbers = file.readline()
                count += 1
    numbers = numbers.strip()
    numbers = numbers.split(',')

    # check order code
    orderCode = numbers[0]
    numbers.pop(0)
    
    order = "any"
    if orderCode == "asc":
        order = "ascending"
    elif orderCode == "desc":
        order = "descending"
    
    print(f"Order the array {numbers} in {order} order")
    solution = solve_question(numbers, orderCode)
    submission = str(input("Enter your answer separated with commas without spaces: "))
    print(compare_answer(submission, solution))

def solve_question(question, orderCode):
    global QUESTION_COUNT
    ascending = True
    if orderCode == "desc": # order code decides whether answer should be ascending or descending
        ascending = False
    swaps = False
    limit = len(question)
    while swaps or limit != 0:
        for i in range(limit - 1):
            value1 = int(question[i])   
            value2 = int(question[i + 1])
            if value1 > value2 and ascending:
                temp = question[i + 1]
                question[i + 1] = question[i]
                question[i] = temp 
                swaps = True
            elif value1 < value2 and not ascending:
                temp = question[i]
                question[i] = question[i + 1]
                question[i + 1] = temp
                swaps = True
        limit -= 1
        swaps = False
    return question

def compare_answer(submission, solution):
    submission = submission.split(',')
    if len(submission) != len(solution):
        return "Incorrect Length"
    for i in range(len(submission)):
        if submission[i] != solution[i]:
            return "Incorrect answer"
    return "Correct answer"

def create_question():
    global QUESTION_COUNT
    
    with open("bubble_sort_questions.txt", 'a') as file:
        question = ""
        value = None
        print("Enter your values enter -1 to quit")
        while True:
            value = str(input("Enter your value: "))
            if value == "-1":
                break
            
            question += value
            question += ','
        question = question.strip(',')
        
        orderCode = "asc"
        order = str(input("Enter the order of your question ascending or descending? "))
        if order == "ascending":
            orderCode = "asc"
        elif order == "descending":
            orderCode = "desc"
        
        question = orderCode + ',' + question
        print(question)
        file.write('\n')
        file.write(question)
    QUESTION_COUNT += 1

if __name__ == "__main__":
    main()