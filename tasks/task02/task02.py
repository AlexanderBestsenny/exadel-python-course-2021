import math

num = 0
while num != 3:
    print('\nMenu:\n'
          '1. Calculate triangle area by base and height\n'
          '2. Calculate triangle area by 2 sides and angle between them\n'
          '3. Exit\n')
    num = input("Enter menu item number: ")
    if not num.isdecimal():
        continue
    num = int(num)
    if num == 1:
        listInput = input("Enter base and height: ").split()
        if len(listInput) != 2:
            continue
        base, height = map(int, listInput)
        print(f"Area is: {base * height / 2:.2f}")
    elif num == 2:
        listInput = input("Enter 2 sides and angle(degrees) between them: ").split()
        if len(listInput) != 3:
            continue
        sideA, sideB, angle = map(int, listInput)
        result = sideA * sideB * math.sin(math.radians(angle)) / 2
        print(f"Area is: {result:.2f}")

print("\nGoodbye!")