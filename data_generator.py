import random
import datetime

def main():
    print(generate_date())

def generate_bool():
    randNum = random.randint(0,1)
    if randNum == 0:
        return False
    else: 
        return True
    
def generate_date():
    year = random.randint(2000, 2999)
    print(year)
    month = random.randint(1, 12)
    print(month)
    day = random.randint(1, 30)
    print(day)
    date = datetime.date(year, month, day)

    return date

def generate_string():
    strings =  [
        "Hello",
        "Wagwan",
        "Harambe",
        "Tide Pods",
        "Afghanistan"
    ]

    return strings[random.randint(0, len(strings) - 1)]
    
if __name__ == "__main__":
    main()