# Assignment week 3-2

current_max = None
current_min = None

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        n = int(sval)
    except:
        print("Invalid input")
        continue

    if current_max is None or n > current_max:

        current_max = n
    if current_min is None or n < current_min:
        current_min = n

print("Maximum:", current_max)
print("Minimum:", current_min)
