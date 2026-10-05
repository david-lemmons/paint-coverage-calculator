try:
    
    width = float(input("Enter the width of the wall in feet: "))
    height = float(input("Enter the height of the wall in feet: "))

    if width <= 0 or height <= 0:
        print("Width and height must be greater than zero.")
    else:
        area = width * height
        print(f"Wall area: {area} square feet")

        coverage = 350
        coats = int(input("How many coats of paint? "))

        if coats <= 0:
            print("Number of coats must be greater than zero.")
        else:
            gallons_needed = area * coats / coverage
            print(f"Paint needed for {coats} coats: {gallons_needed:.2f} gallons")

except ValueError:
    print("Enter numbers for width and height, and a whole number for coats.")