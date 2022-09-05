from math import pi

def main():
    radius = int(input("Enter radius of your circle: "))
    circumference = calcCircumference(radius)
    area = calcArea(radius)
    print(f"Circumference is {round(circumference,3)} rounded")
    print(f"Area is {round(area,3)} rounded")


def calcArea(radius):
    area = pi * (radius**2)
    return area

def calcCircumference(radius):
    circumference = pi * (radius * 2)
    return circumference

if __name__ == "__main__":
    main()