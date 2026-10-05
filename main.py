width = float(input("Enter the width of the wall in feet: "))
height = float(input("Enter the height of the wall in feet: "))
area = width * height
print(f"Wall area: {area} square feet")

coverage = 350
coats = int(input("How many coats of paint? "))
gallons_needed = area * coats / coverage
print(f"Paint needed for {coats} coats: {gallons_needed:.2f} gallons")