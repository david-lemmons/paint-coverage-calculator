def calculate_area(width,height):
    return width * height

def calculate_paint(area,coats,coverage):
    return area * coats / coverage

def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                print("Please enter a number greater than zero.")
            else:
                return number
        except ValueError:
            print("Please enter a valid number.")

width = get_positive_number("Enter the wall width in feet: ")
height = get_positive_number("Enter the wall height in feet: ")

area = calculate_area(width, height)
print(f"Wall area: {area} square feet")

coverage = 350

while True:
    try:
        coats = int(input("How many coats of paint? "))

        if coats <= 0:
            print("Number of coats must be greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a whole number for coats.")

gallons_needed = calculate_paint(area, coats, coverage)
print(f"Paint needed for {coats} coats: {gallons_needed:.2f} gallons")