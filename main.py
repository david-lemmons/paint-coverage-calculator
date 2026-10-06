while True:
    try:
        width = float(input("Enter the width of the wall in feet: "))

        if width <= 0:
            print("Width must be greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a valid number for the width.")

while True:
    try:
        height = float(input("Enter the height of the wall in feet: "))

        if height <= 0:
            print("Height must be greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a valid number for the height.")

area = width * height
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

gallons_needed = area * coats / coverage
print(f"Paint needed for {coats} coats: {gallons_needed:.2f} gallons")